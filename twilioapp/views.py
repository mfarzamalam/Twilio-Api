from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from twilioapp.twilioHelper import TwilioHelper


def register(request):
    if request.user.is_authenticated:
        return redirect('twilioapp:checkout')
    elif request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            list(messages.get_messages(request))
            messages.success(request, 'You\'ve been registered successfully. A confirmation SMS has been sent to your phone number <strong>' +
                             TwilioHelper.MY_MOBILE_NUMBER+'</strong>.')
            TwilioHelper.send_sms()
            return redirect('twilioapp:login')
        else:
            context = {'form': form}
            return render(request, 'registration/register.html', context)
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)
