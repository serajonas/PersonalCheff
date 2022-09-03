from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
def sucodelaranja(request):
    return render(request,'sucodelaranja.html')    
        
# Create your views here.
