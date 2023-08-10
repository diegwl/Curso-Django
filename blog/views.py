from django.shortcuts import render

def blog(request):
    context = {
        'text':'Olá Blog',
        'title':'Blog -'
    }

    return render(request, 'blog/index.html', context)

def exemplo(request):
    context = {
        'text':'Olá Exemplo',
        'title': 'Exemplo -'
    }
        
    return render(request, 'blog/exemplo.html', context)
