from django.shortcuts import render
from django.http      import HttpResponse

# Create your views here.

def home_page(request):
  return render(request, 'tstapp/home_page.html')
  #return HttpResponse("------ Home Page ----1---")
