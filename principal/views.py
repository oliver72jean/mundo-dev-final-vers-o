
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Question

from django.core.mail import send_mail


def index(request):
    questao = Question.objects.first()
    context = {
        'questao': questao
    }

    return render(request, "principal/index.html", context)


def sobre(request):
    context = {}

    return render(request, "principal/sobre.html", context)


def pub1(request):
    pub1 = Question.objects.first()
    context = {
        'pub1': pub1
    }
    if request.method == 'POST':
        mensagem = "Dados da mensagem:\n"
        mensagem += "Nome: "+request.POST['nome'] + "\n"
        mensagem += "Email: "+request.POST['email'] + "\n"
        mensagem += "Mensagem: "+request.POST['mensagem'] + "\n"
        send_mail(
            'Mundo Dev',
            mensagem,
            'testedjango123@gmail.com',
            ['mundodev2222@gmail.com'],
            fail_silently=False,
        )

    return render(request, "principal/pub1.html", context)


def pub2(request):
    pub2 = Question.objects.first()

    context = {
        'pub2': pub2

    }
    if request.method == 'POST':
        mensagem = "Dados da mensagem:\n"
        mensagem += "Nome: "+request.POST['nome'] + "\n"
        mensagem += "Email: "+request.POST['email'] + "\n"
        mensagem += "Mensagem: "+request.POST['mensagem'] + "\n"
        send_mail(
            'Mundo Dev',
            mensagem,
            'testedjango123@gmail.com',
            ['mundodev2222@gmail.com'],
            fail_silently=False,
        )

    return render(request, "principal/pub2.html", context)


def pub3(request):
    context = {}
    if request.method == 'POST':
        mensagem = "Dados da mensagem:\n"
        mensagem += "Nome: "+request.POST['nome'] + "\n"
        mensagem += "Email: "+request.POST['email'] + "\n"
        mensagem += "Mensagem: "+request.POST['mensagem'] + "\n"
        send_mail(
            'Mundo Dev',
            mensagem,
            'testedjango123@gmail.com',
            ['mundodev2222@gmail.com'],
            fail_silently=False,
        )

    return render(request, "principal/pub3.html", context)


def pub4(request):
    context = {}
    if request.method == 'POST':
        mensagem = "Dados da mensagem:\n"
        mensagem += "Nome: "+request.POST['nome'] + "\n"
        mensagem += "Email: "+request.POST['email'] + "\n"
        mensagem += "Mensagem: "+request.POST['mensagem'] + "\n"
        send_mail(
            'Mundo Dev',
            mensagem,
            'testedjango123@gmail.com',
            ['mundodev2222@gmail.com'],
            fail_silently=False,
        )

    return render(request, "principal/pub4.html", context)


def pub5(request):
    context = {}
    if request.method == 'POST':
        mensagem = "Dados da mensagem:\n"
        mensagem += "Nome: "+request.POST['nome'] + "\n"
        mensagem += "Email: "+request.POST['email'] + "\n"
        mensagem += "Mensagem: "+request.POST['mensagem'] + "\n"
        send_mail(
            'Mundo Dev',
            mensagem,
            'testedjango123@gmail.com',
            ['mundodev2222@gmail.com'],
            fail_silently=False,
        )

    return render(request, "principal/pub5.html", context)


def pub6(request):
    context = {}
    if request.method == 'POST':
        mensagem = "Dados da mensagem:\n"
        mensagem += "Nome: "+request.POST['nome'] + "\n"
        mensagem += "Email: "+request.POST['email'] + "\n"
        mensagem += "Mensagem: "+request.POST['mensagem'] + "\n"
        send_mail(
            'Mundo Dev',
            mensagem,
            'testedjango123@gmail.com',
            ['mundodev2222@gmail.com'],
            fail_silently=False,
        )

    return render(request, "principal/pub6.html", context)


def pub7(request):
    context = {}
    if request.method == 'POST':
        mensagem = "Dados da mensagem:\n"
        mensagem += "Nome: "+request.POST['nome'] + "\n"
        mensagem += "Email: "+request.POST['email'] + "\n"
        mensagem += "Mensagem: "+request.POST['mensagem'] + "\n"
        send_mail(
            'Mundo Dev',
            mensagem,
            'testedjango123@gmail.com',
            ['mundodev2222@gmail.com'],
            fail_silently=False,
        )

    return render(request, "principal/pub7.html", context)


def pub8(request):
    context = {}
    if request.method == 'POST':
        mensagem = "Dados da mensagem:\n"
        mensagem += "Nome: "+request.POST['nome'] + "\n"
        mensagem += "Email: "+request.POST['email'] + "\n"
        mensagem += "Mensagem: "+request.POST['mensagem'] + "\n"
        send_mail(
            'Mundo Dev',
            mensagem,
            'testedjango123@gmail.com',
            ['mundodev2222@gmail.com'],
            fail_silently=False,
        )

    return render(request, "principal/pub8.html", context)


def pub9(request):
    context = {}
    if request.method == 'POST':
        mensagem = "Dados da mensagem:\n"
        mensagem += "Nome: "+request.POST['nome'] + "\n"
        mensagem += "Email: "+request.POST['email'] + "\n"
        mensagem += "Mensagem: "+request.POST['mensagem'] + "\n"
        send_mail(
            'Mundo Dev',
            mensagem,
            'testedjango123@gmail.com',
            ['mundodev2222@gmail.com'],
            fail_silently=False,
        )

    return render(request, "principal/pub9.html", context)


def pub10(request):
    context = {}
    if request.method == 'POST':
        mensagem = "Dados da mensagem:\n"
        mensagem += "Nome: "+request.POST['nome'] + "\n"
        mensagem += "Email: "+request.POST['email'] + "\n"
        mensagem += "Mensagem: "+request.POST['mensagem'] + "\n"
        send_mail(
            'Mundo Dev',
            mensagem,
            'testedjango123@gmail.com',
            ['mundodev2222@gmail.com'],
            fail_silently=False,
        )

    return render(request, "principal/pub10.html", context)
