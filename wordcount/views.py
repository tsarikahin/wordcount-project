from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    text_len = len(fulltext.split())
    words_text = fulltext.split()

    word_dict = {}

    for word in words_text:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'full_text': fulltext, 'count_words': text_len, 'sorted_words': sorted_words})


def thispart(request):
    return HttpResponse('<h1>HEY WELCOME TO THISPART<h1>')


def about(request):
    return render(request, 'about.html')
