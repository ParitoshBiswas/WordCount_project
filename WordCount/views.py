from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def count(request):
    worddictionary = {}
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    for word in wordlist:
        if word in worddictionary:
            #increment
            worddictionary[word] += 1

        else:
            #add to the dictionary
            worddictionary[word] = 1

    sortedWords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedWords': sortedWords})

def about(request):
    return render(request, 'about.html')