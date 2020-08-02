# I anurag mukherjee has created this file

from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>HELLO WORLD</h1><a href = "https://www.coursera.org/programs/academy-of-technology-on-coursera-kd3zh">My coursera website</a><br>
#     <a href = "https://mail.google.com/mail/u/0/#inbox">My gmail account<a><br>
#     <a href = "https://swayam.gov.in/">My Swyam account</a>
#     ''')
    
#     return HttpResponse('''<a href = "https://mail.google.com/mail/u/0/#inbox">My gmail account</a>''')

# def about(request):
#     return HttpResponse("About Anurag mukherjee")


def index(request):
    return render(request,'index.html')


def analyze(request):

    #Get the text
    djtext = request.GET.get('text','default')

    #Check checkbox values
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    spaceremover = request.GET.get('spaceremover','off')
    charcount = request.GET.get('charcount','off')

        
    # analysed = djtext

    #check which check box is on
    if (removepunc == "on"):
        punctuations = '''!()"'{}[]?#$:*;.,~-_/'''

        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed puntuations', 'analysed_text': analyzed}
        djtext = analyzed


    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'changed into Uppercase', 'analysed_text': analyzed}
        
        djtext = analyzed
          

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose':'removed all the new lines', 'analysed_text': analyzed}
        
        djtext = analyzed
        

    elif(spaceremover == "on"): 
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'removed all the extra spaces', 'analysed_text': analyzed}
        #analyse the text
        return render(request,'analyze.html', params)    

    if(charcount == "on"):
        analyzed = ""
        for char in djtext:
           analyzed = analyzed+char
        x = len(analyzed)   
        params = {'purpose':'counting all the characters', 'analysed_text': analyzed,'len_of_the_text': x-1}
       
    if(removepunc !="on" and fullcaps !="on" and newlineremover !="on" and charcount !="on"):
        return HttpResponse("Please select any operation")

    
    return render(request,'analyze.html', params)    

def about(request):
    return render(request, 'about.html')

def contact(request):
    return  render(request, 'contact.html')
       
    

# def capfirst(request):
#     return HttpResponse("Capitalize first")  

# def newlineremove(request):
#     return HttpResponse("New line is removed")

# def charcount(request):
#     return HttpResponse("Character is counted")

# def spaceremove(request):
#     return HttpResponse("Space is removed")
