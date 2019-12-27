# I've created this file
from django.http import HttpResponse
from django.shortcuts import render

# def freqLinks(request):
    # return HttpResponse('''<h2><a href="http://www.prajjwalmishra.com" target="blank">PrajjwalMishra's Website</a></h2>''')


# def about(request):
#     return HttpResponse("Hello, Prajjwal! This is your about view!")

def index(request):
    return render(request, 'index.html')

# def firstTemplate(request):
#     pyaaraVariable = {'name':'Prajjwal', 'nation':'Indian'}
#     return render(request, 'first.html', pyaaraVariable)
    # return HttpResponse("Hello, Prajjwal! This is your first view!")

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')
    analyzed = ""

    #checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    params = {}
    count = 0
    #remove punctuation starts
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    #remove punctuation ends

    #full caps starts
    if fullcaps == "on":
        analyzed = ""
        for char in djtext :
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed To Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
    #full caps ends

    #new line remover starts
    if newlineremover == "on":
        analyzed = ""
        for char in djtext :
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed
    #new line remover ends

    #extra space remover starts
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}
        djtext = analyzed
    #extra space remover ends

    # char counter starts
    if charcount == "on":
        count = 0
        for char in djtext:
            count += 1
        params = {'purpose': 'Character Count', 'analyzed_text': djtext, 'counter': count, 'renHTML': "No Of Characters:"}
        djtext = analyzed
    #char counter ends

    if (removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on"):
        return HttpResponse("Please select a valid option")
    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("New Line Remove")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>Back</a>")
#
# def charcount(request):
#     return HttpResponse("charcount ")