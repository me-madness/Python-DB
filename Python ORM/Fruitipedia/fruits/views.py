from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from fruits.models import Fruit
from fruits.forms import AddFruitForm, CategoryAddForm
from django.views.generic.edit import CreateView


# Create your views here.
def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()
    
    context = {
        "fruits": fruits,
    }
    return render(request, 'common/dashboard.html', context)

class CreateFruitView(CreateView):
    model = Fruit
    form_class = AddFruitForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')
    
# def create_view(request):
#     return render(request, 'fruits/create-fruit.html')


def edit_view(request, pk):
    return render(request, 'fruits/edit-fruit.html')


def details_view(request, pk):
    return render(request, 'fruits/details-fruit.html')


def delete_view(request, pk):
    return render(request, 'fruits/delete-fruit.html')


def create_category(request):
    if request.method == "GET":
        form = CategoryAddForm()
    else:
        form = CategoryAddForm(request.POST)
    
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = {
        "form": form,
    }
        
    return render(request, 'categories/create-category.html', context)