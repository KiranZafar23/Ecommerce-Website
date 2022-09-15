from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class UserLogout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Successfully logged out")

        return redirect('home')
