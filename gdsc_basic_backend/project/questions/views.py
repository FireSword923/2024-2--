from django.shortcuts import render

# Create your views here.
def index(request):
    name = 'kim'
    context = {'name' : name}
    return render(request, 'index.html', context)