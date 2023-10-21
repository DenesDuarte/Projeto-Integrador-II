from django.shortcuts import render,redirect, get_object_or_404
from portal.models import Autor,Editora,Formato
from portal.forms import AutorForm,EditoraForm,FormatoForm

# Create your views here.
def home(request):
    return render(request,'portal/home.html')

def autor(request):
    autores = Autor.objects.all()
    context = {
        'autores':autores

    }
    return render(request,'portal/autor.html', context)

def autor_add(request):
    form = AutorForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('autor')
         
    context = {
        'form': form,
    }

    return render(request,'portal/autor_add.html', context)

def autor_edit(request,id):
    autor = get_object_or_404(Autor, id=id)

    form = AutorForm(request.POST or None, instance=autor)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('autor')
    
    context = {
        'form': form,
        'autor': autor,
    }

    return render(request,'portal/autor_edit.html', context)

def autor_delete(request, id):
    autor = Autor.objects.get(id=id)
    autor.delete()

    return redirect('autor')

def editora(request):
    editoras = Editora.objects.all()
    context = {
        'editoras':editoras

    }
    return render(request,'portal/editora.html', context)

def editora_add(request):
    form = EditoraForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('editora')
         
    context = {
        'form': form,
    }

    return render(request,'portal/editora_add.html', context)

def editora_edit(request,id):
    editora = get_object_or_404(Editora, id=id)

    form = EditoraForm(request.POST or None, instance=editora)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('editora')
    
    context = {
        'form': form,
        'editora': editora,
    }

    return render(request,'portal/editora_edit.html', context)

def editora_delete(request, id):
    editora = Editora.objects.get(id=id)
    editora.delete()

    return redirect('editora')

def formato(request):
    formatos = Formato.objects.all()
    context = {
        'formatos':formatos

    }
    return render(request,'portal/formato.html', context)

def formato_add(request):
    form = FormatoForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('formato')
         
    context = {
        'form': form,
    }

    return render(request,'portal/formato_add.html', context)

def formato_edit(request,id):
    formato = get_object_or_404(Formato, id=id)

    form = FormatoForm(request.POST or None, instance=formato)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('formato')
    
    context = {
        'form': form,
        'formato': formato,
    }

    return render(request,'portal/formato_edit.html', context)

def formato_delete(request, id):
    formato = Formato.objects.get(id=id)
    formato.delete()

    return redirect('formato')