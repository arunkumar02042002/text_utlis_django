from django.shortcuts import HttpResponse, render
from django.http import HttpRequest, HttpResponse, JsonResponse
import re
from collections import Counter
import string

# Create your views here.
def home(request):
    return render(request, 'index.html')


def analyzeText(request):
    text = request.GET['text']
    task = request.GET['task']

    if task == 'analyze':
        char_list = [*text]
        word_dict = {}
        for i in char_list:
            if i.isalpha():
                i = i.lower()
                word_dict[i] = word_dict.get(i, 0) + 1
        context = {
            'task' : task,
            'text' : word_dict,
        }
        return render(request, 'analyzed.html', context)

    elif task == 'removepunctuations':
        text = re.sub(r"[^a-zA-Z0-9\s]", '', text)
        context = {
            'task' : task,
            'text' : text,
        }
        return render(request, 'analyzed.html', context)

    elif task == 'removespace':
        text = re.sub(r"\s", '', text)
        context = {
            'task' : task,
            'text' : text,
        }
        return render(request, 'analyzed.html', context)

    else:
        return render(request, 'analyzed.html')
        