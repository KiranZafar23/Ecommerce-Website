from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View


class UserLogin(View):
    def post(self, request):
        login_user_name = request.POST['loginusername']
        login_password = request.POST['loginpassword']
        user = authenticate(username=login_user_name, password=login_password)

        if user:
            login(request, user)
            messages.success(request, "Successfully Logged In")

            return redirect("home")

        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    def get(self):
        return HttpResponse("404- Not found")
