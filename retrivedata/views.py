# My file -Eaglesoft
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
     

def about(request):
    data=request.POST.get('text','default')
    ch=request.POST.get('check','off')
    fullcap=request.POST.get('fullcap','off')
    removeline=request.POST.get('removeline','off')
    print(ch)
    print(data)
  
    if ch=='on':
        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed=" "
        for char in data:
            if char not in punctuations:
                analyzed = analyzed + char 
        params={'purpose':'Remove punctuations','analyze_text':analyzed}
        data=analyzed
    if fullcap=='on':
        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed=" "
        for char in data:
                analyzed = analyzed + char.upper() 
        params={'purpose':'change into uppercase','analyze_text':analyzed}
        data=analyzed

    if removeline=='on':
        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed=" "
        for char in data:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char 
        params={'purpose':'Remove Lines','analyze_text':analyzed}
        data=analyzed
  
    if(ch!="on" and fullcap!="on" and removeline!='on'):
        return HttpResponse("Please! Select any options")
             
    return render(request,'analyze.html',params)


    