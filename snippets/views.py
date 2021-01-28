from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from snippets.models import Language, Snippet
from .form import FormSnippet
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'No te has identificado correctamente')

    return render(request, 'login.html', {
        'title': 'Identificate'
    })
    
def logout_user(request):
    logout(request)

    return redirect('index')


def index(request):
    snippets = Snippet.objects.all()
    snippets = Snippet.objects.filter(public=True)
   
    
    return render(request, 'index.html', {
        'snippets': snippets        
    })


def CategoryPython(request):
    snippets = Snippet.objects.all()
    snippets = Snippet.objects.filter(public=True, languages=1)   
    
    return render(request, 'snippets/category_python.html', {
        'snippets': snippets   
    }) 

def CategoryJava(request):
    snippets = Snippet.objects.all()
    snippets = Snippet.objects.filter(public=True, languages=2)   
    
    return render(request, 'snippets/category_java.html', {
        'snippets': snippets   
    })

def CategoryC(request):
    snippets = Snippet.objects.all()
    snippets = Snippet.objects.filter(public=True, languages=3)   
    
    return render(request, 'snippets/category_c.html', {
        'snippets': snippets   
    })

def CategoryHTML(request):
    snippets = Snippet.objects.all()
    snippets = Snippet.objects.filter(public=True, languages=4)   
    
    return render(request, 'snippets/category_html.html', {
        'snippets': snippets   
    })  

def snippets_user(request):

    #snippets = Snippet.objects.all()
    snippets = Snippet.objects.filter(user= request.user)

    return render(request, 'snippets/snippets_user.html', {
        'snippets': snippets
    })



def detail(request,snippet_id):

    snippets = get_object_or_404(Snippet, id=snippet_id)   
    return render(request, 'snippets/detail_snippet.html', {
        'snippets': snippets        
    })



def añadir_snippets(request):
    if request.method == 'POST':
        formulario = FormSnippet(request.POST)
        
        if formulario.is_valid():
            data_form = formulario.cleaned_data

            user= data_form['user']
            name = data_form['name']
            description = data_form['description']
            languages = data_form['languages']
            public = data_form['public']
            snippet = data_form['snippet']

            snippets = Snippet(
                user= user,
                name = name,
                description = description,
                languages = languages,
                public = public,
                snippet = snippet
            )

            snippets.save()
            formulario = FormSnippet()

            #return HttpResponse()
        
    else:
        formulario = FormSnippet()
    return render(request, 'snippets/añadir_snippets.html', {
            'form': formulario
        })


def snippet_edit(request,snippet_id):
    snippets = Snippet.objects.get(id=snippet_id)
    form = FormSnippet(instance=snippets)

    if request.method == "POST":
        form = FormSnippet(request.POST, instance=snippets)
        if form.is_valid():
            snippets = form.save(commit=False)
            snippets.save()
    return render(request, 'snippets/snippet_edit.html', {'form': form})        
    

def snippet_delete(request, snippet_id):
    snippets = Snippet.objects.get(pk=snippet_id)
    snippets.delete()

    return redirect('snippets_user')
