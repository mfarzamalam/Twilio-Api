from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib import messages
from .forms import RegistrationForm, OTPForm
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


def checkout(request):
    if not request.user.is_authenticated:
        return redirect('twilioapp:login')
    if request.method == 'GET' or 'resend-otp' in request.POST:
        TwilioHelper.send_Otp()
        form = OTPForm()
        if 'resend-otp' in request.POST:
            messages.success(
            request, 'The OTP has been resent to your phone number <strong>' + TwilioHelper.MY_MOBILE_NUMBER+'</strong>.')
        else:
            messages.success(
            request, 'Your order of <strong>1 Unicorn</strong> has been processed. OTP has been sent to your phone number <strong>' +
                             TwilioHelper.MY_MOBILE_NUMBER+'</strong>.')
    else:
        form = OTPForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if TwilioHelper.check_Otp(instance.otp):
                TwilioHelper.send_whatsapp_message()
                return redirect('twilioapp:finish')
            else:
                messages.error(request, 'The OTP is incorrect. Please try again.')
                return redirect('twilioapp:checkout')
    context = {'form': form}
    return render(request, 'twilioapp/checkout.html', context)


def finish(request):
    if not request.user.is_authenticated:
        return redirect('twilioapp:login')
    if request.method == 'GET':
        messages.success(request, 'Thanks for using our service. The order confirmation has been sent to your WhatsApp number <strong>' +
                     TwilioHelper.MY_WHATSAPP_NUMBER+'</strong>.')
        return render(request, 'twilioapp/finish.html')
    else:
        logout(request)
        return redirect('twilioapp:register')


def log_out(request):
    logout(request)
    return redirect('twilioapp:login')