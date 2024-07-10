from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Person
from .forms import UserForm
from django.urls import reverse

def index(request):
    users = Person.objects.all()
    return render(request, 'users/index.html', {'users': users})

def view_user(request, id):
    user = Person.objects.get(pk=id)
    return redirect('index')

def add(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'users/add.html', {'form': UserForm(), 'success': True})
    return render(request, 'users/add.html', {'form': form})

def edit(request,id):
    if request.method == "POST":
        user = Person.objects.get(pk=id)
        form = UserForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            return render(request, 'users/edit.html',{'form':form,'success':True})
        
    else:
        user = Person.objects.get(pk=id)
        form = UserForm(instance=user)
        return render(request, 'users/edit.html',{'form':form})
    
    
    
    
def delete(request,id):
    if request.method == "POST":
        user = Person.objects.get(pk=id)
        user.delete()
    return HttpResponseRedirect(reverse('index'))
        
          
          
             
        
        
        
    