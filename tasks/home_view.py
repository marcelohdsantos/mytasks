from django.http import HttpResponse


def home(requests):
    return HttpResponse('Olá Projeto de tarefas')
