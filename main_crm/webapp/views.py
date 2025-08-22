from django.shortcuts import render
from .forms import CreateUserForm

# Create your views here.

def index (request):
    return render (request, 'web/index.html')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('login')

    else:
        form=CreateUserForm()        

    context ={'form':form}

    return render (request, 'web/register.html', context)   