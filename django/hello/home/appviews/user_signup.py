from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View


class UserSignup(View):
    def post(self, request):
        user_name = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        password = request.POST['pass1']
        again_password = request.POST['pass2']

        if not user_name.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')

        if (password != again_password):
            messages.error(request, " Passwords do not match")
            return redirect('home')

        my_user = User.objects.create_user(user_name, email, password)
        my_user.first_name = first_name
        my_user.last_name = last_name
        my_user.save()
        messages.success(request, "Registered Successfully. Now Logged In")

        return redirect('home')

    def get(self):
        return HttpResponse("404 - Not found")
