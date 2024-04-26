# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, PatientForm
from django.contrib.auth import login, logout, authenticate
from .models import Patients, PatientMedications, PatientCondition, Medications, Conditions
# from .forms import PatientSearchForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView

# This class is to manage patients data to create a new patient
#  it uses the model Patients and redirects the user to a form and
#  whatever infomation entered will be in the table managed by Patients model


class PatientCreateView(CreateView):
    model = Patients
    form_class = PatientForm
    template_name = 'main/patient_form.html'
    success_url = 'main/patients.html'

# Same as the previous class but this is used to modify existing data in Patients


class PatientUpdateView(UpdateView):
    model = Patients
    form_class = PatientForm
    template_name = 'main/patient_form.html'
    success_url = 'main/patients.html'


# a function to search patients by their last name on the patients list
def search_patient(request):
    if request.method == "POST":
        searched = request.POST.get('searched', None)
        try:

            # searching by the patients last name
            patient = Patients.objects.filter(patient_lname=searched)
            return render(request, 'main/search_patient.html', {'searched': searched, 'patient': patient})
        except ValueError:
            # Handling the case where the input is not a valid integer
            return render(request, 'main/search_patient.html', {'error': 'Invalid Patient ID'})
    else:
        return render(request, 'main/search_patient.html', {})


# logging in with the right credentials is required to be redirected to the home page
@login_required(login_url='/login/')
def home(request):
    return render(request, 'main/home.html')

# sign_up finction handles form submission
# uses Django's built in package to check for input validation
# after signing up user is redirected to the home page


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

# login required to view patients detail
# uses model class Patients to get patients data


@login_required(login_url='/login/')
def patients_list(request):
    patients = Patients.objects.all()
    return render(request, 'main/patients.html', {'patients': patients})

# login required to view patients detail
#  the function processes data from the model classes
# Patients, PatientCondition,... to get data from the database to display on the front end


@login_required(login_url='/login/')
def patient_detail(request, pk):
    patient = Patients.objects.get(pk=pk)
    conditions = PatientCondition.objects.filter(patient=patient)
    medications = PatientMedications.objects.filter(patient=patient)
    return render(request, 'main/patient_detail.html', {'patient': patient, 'conditions': conditions, 'medications': medications})
