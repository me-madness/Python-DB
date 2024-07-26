from django import forms
from fruits.models import Category

class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        
        
        
class CategoryAddForm(CategoryBaseForm):
    pass        