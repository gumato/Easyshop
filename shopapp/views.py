from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    date = dt.date.today()
    products = Product.objects.all()
    cat=Category.objects.all()
    return render(request,'index.html',{'cat':cat,'products':products})


def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
                user = form.save(commit=False)
                user.is_active = True
                user.save()
                to_email = form.cleaned_data.get('email')
                return HttpResponse('Confirm your email address to complete registration')
           
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'Form':form})


def search(request):
    if 'name' in request.GET and request.GET['name']:
        search_term = request.GET.get('name')
        search_category = Product.search_by_name(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'products':search_category})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})
@login_required(login_url='/accounts/login/')
def product(request):
    category = None
    category = Category.objects.all()
def categories(request,idi):
    title='Category'
    products = Product.objects.filter(category=idi)
    
    return render(request,'category.html',{'title':title,'products':products})