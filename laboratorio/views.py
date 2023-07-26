from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateNewLab
from .models import Laboratorio
# Create your views here.

def mostrarLab(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'mostrar.html', {'laboratorios': laboratorios})


def insertarLab(request):
    context = {
        # Agrega los datos que deseas pasar a la plantilla 'index.html'
    }
    if request.method == 'POST':
        form = CreateNewLab(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_laboratorios')
    else:
        form = CreateNewLab()

    context['form'] = form  # Agrega el formulario al contexto
    
    return render(request, 'insertar.html', context)

def editarLab(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)

    if request.method == 'POST':
        form = CreateNewLab(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('mostrar_laboratorios')  # Redirecciona a la página que muestra todos los laboratorios

    else:
        form = CreateNewLab(instance=laboratorio)

    return render(request, 'editar.html', {'form': form})

def eliminar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)

    if request.method == 'POST':
        laboratorio.delete()
        return redirect('mostrar_laboratorios')

    return render(request, 'eliminar_laboratorio.html', {'laboratorio': laboratorio})