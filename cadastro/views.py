#from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import *
from .forms import UsuarioForm
from django.core.paginator import Paginator

def home(request):
    data = {}  
    search = request.GET.get('search')
    if search:
        data['db'] = Usuario.objects.filter(descricao__icontains=search)
    else:
        data['db'] = Usuario.objects.all()        
    lista =  Usuario.objects.all()
    paginator = Paginator(lista, 8)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    #return render(request, 'list.html', {'page_obj': page_obj}
    return render(request, 'home.html', data)
    
def form(request):
    data = {}
    data['form'] = UsuarioForm()
    return render(request, 'form.html', data)

def create(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    data['form'] = UsuarioForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    form = UsuarioForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def delete(request, pk):
    db = Usuario.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def profile(request):
    data = {}  
    search = request.GET.get('search')
    if search:
        data['db'] = Usuario.objects.filter(descricao__icontains=search)
    else:
        data['db'] = Usuario.objects.all()        
    lista =  Usuario.objects.all()
    paginator = Paginator(lista, 8)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    #return render(request, 'list.html', {'page_obj': page_obj}
    return render(request, 'index.html', data)

    


