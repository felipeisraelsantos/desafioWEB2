from collections import defaultdict

from django.shortcuts import render

def form(request):
    return render(request, 'mysite/form.html')

''' aqui sera passado o parametro para o tratamento do texto'''
def result(request):
    txt = request.GET['input']
    lista = txt.split()

    lst_u = Remove(lista)

    return render(request, 'mysite/result.html', {'key': txt, 'key2': len(lst_u), 'key3': txt})


def Remove(lst):
    I = []
    for i in lst:
        if i not in I:
            I.append(i)
        I.sort()

    return I