from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Arslan'})



def add(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    result = num1 + num2
    return render(request, 'result.html', {'result':result})


def about(request):
    return render(request, 'about.html', )

