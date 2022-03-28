from django.shortcuts import render
from . import forms, models
from .profitability_calculator.gpu import GPU


def calculator_view(request):
    if request.method == "POST":
        form = forms.CalculateGpu(request.POST, request.FILES)  # might not need request.FILES. Check later.
        if form.is_valid():
            instance = form.save(commit=False)
            # calculator = models.Calculator  # create Calculator model object
            gpu = GPU(mhs=instance.mhs, name=instance.name, power=instance.power,
                      price=instance.price, kwh_price_gbp=instance.kwh_price)
            calculator = models.Calculator(name="test",
                            mhs=gpu.mhs, power=gpu.power, price=gpu.price,
                            kwh_price=instance.kwh_price, efficiency=gpu.efficiency,
                            epp=gpu.epp, roi=gpu.roi)
            return render(request, 'calculator/calculator_form.html', {'calculator':calculator})
    return render(request, 'calculator/calculator_form.html')
