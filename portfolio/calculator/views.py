from django.shortcuts import render

def calculator_form(request):
    return render(request, 'calculator/calculator_form.html')
