from django.shortcuts import render, redirect

def clima(request):
    return render(
        request,
        'base/clima.html'
    )