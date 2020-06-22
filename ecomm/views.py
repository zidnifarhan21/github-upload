from django.shortcuts import render

def index(request):
    context = {
        'judul' : 'Bunakit',
        'subJudul' : 'Selamat datang di Toko Bunakit'
    }
    return render(request, 'index.html', context)

def login(request):
    context = {
        'judul' : "Login Page"
    }
    return render(request, "login.html", context)
