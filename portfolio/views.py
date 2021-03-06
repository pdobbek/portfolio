from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def homepage(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = "from_email=" + from_email + "\n\n" + form.cleaned_data["message"]
            try:
                send_mail(subject, message, "contactform@patrykdobbek.com", ["p.dobbek@pm.me"], fail_silently=False)
                messages.success(request, "Email sent succesfully. Thank you!")
                return redirect("home")
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
        else:
            messages.error(request, "Invalid form submission.")
            messages.error(request, form.errors)
            return redirect("home")
    return render(request, "homepage.html")

def about(request):
    return render(request, "about.html")
