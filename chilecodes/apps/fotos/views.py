from django.shortcuts import render,redirect
from .forms import FormFotos
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def agregarFoto(request):
    formulario = FormFotos()
    if request.method == 'POST':
        formulario = FormFotos(request.POST, request.FILES)
        if formulario.is_valid():
            nuevoFormulario = formulario.save(commit=False)
            nuevoFormulario.usuario = request.user
            nuevoFormulario.save()
            return redirect('/usuario/perfil/')
    context = {
        'formulario':formulario
    }
    return render(
        request,
        'fotos/agregarFoto.html',
        context
    )