from django.shortcuts import render
from fruits.models import Fruit


# Create your views here.
def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()
    
    context = {
        "fruits": fruits,
    }
    return render(request, 'common/dashboard.html', context)


def create_view(request):
    return render(request, 'fruits/create-fruit.html')


def edit_view(request, pk):
    return render(request, 'fruits/edit-fruit.html')


def details_view(request, pk):
    return render(request, 'fruits/details-fruit.html')


def delete_view(request, pk):
    return render(request, 'fruits/delete-fruit.html')


def create_category(request):
    return render(request, 'categories/create-category.html')