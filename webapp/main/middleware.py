# importing functions to logout, for redirection and to use time
from django.contrib.auth import logout
from django.shortcuts import redirect
from datetime import datetime, timedelta

# this class is the middleware that automatically logs out inactive uses


class AutoLogout:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if 'last_request' in request.session:
                elapsed_time = datetime.now(
                ) - datetime.strptime(request.session['last_request'], "%Y-%m-%d %H:%M:%S.%f")
                # 600 seconds = 10 minutes
                if elapsed_time > timedelta(seconds=600):
                    logout(request)
                    return redirect('login')
            request.session['last_request'] = str(datetime.now())
        response = self.get_response(request)
        return response
