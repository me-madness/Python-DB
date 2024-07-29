from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from fruits.models import Fruit
from fruits.forms import AddFruitForm, CategoryAddForm, EditFruitForm, DeleteFruitForm
from django.views.generic.edit import CreateView, DeleteView


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
    fruit = Fruit.objects.get(pk=pk)
    
    if request.method == "GET":
        form = EditFruitForm(instance=fruit)
    else:
        form = EditFruitForm(request.POST, instance=fruit)
        
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context = {
        "fruit": fruit,
        "form": form,
    }
        
    return render(request, 'fruits/edit-fruit.html', context)


def details_view(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    
    context = {
        "fruit": fruit
    }
    
    return render(request, 'fruits/details-fruit.html', context)


# def delete_view(request, pk):
#     return render(request, 'fruits/delete-fruit.html')


class DeleteFruitView(DeleteView):
    model = Fruit
    form_class = DeleteFruitForm
    template_name = 'fruits/delete-fruit.html'
    success_url = reverse_lazy('dashboard')
    
    


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