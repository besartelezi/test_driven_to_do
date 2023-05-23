from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages
from accounts.models import Token
from django.core.urlresolvers import reverse
import sys
from django.contrib import auth

def send_login_email(request):
    send_mail('subject', 'body', 'from_email', ['to_email'])
    return redirect('/')


def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    # build_absolute_uri is a way to build absolute url, https://domain-name included
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        'noreply@superlists',
        [email]
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')


def login(request):
    user = auth.authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')