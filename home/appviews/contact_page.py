from django.contrib import messages
from django.shortcuts import render
from django.views import View

from home.models.contact import Contact


class Contact(View):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        description = request.POST.get('description')

        try:
            contact = Contact(name=name, email=email, contact=contact, description=description)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
        except Exception:
            messages.warning(request, "Please Enter correct Information")

        return render(request, 'contact.html')

    def get(self, request):
        return render(request, 'contact.html')
