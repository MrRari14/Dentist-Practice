from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    return render(request, 'main/index.html')

# send mail code.


def contact(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

# actually send mail.
        send_mail(
            message_name,
            message,
            message_email,
            ['bernardoferraricarp@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'main/index.html')

    else:
        return render(request, 'main/index.html', {})
