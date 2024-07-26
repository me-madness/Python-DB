from django import forms
from fruits.models import Category

class CategoryBaseForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Category name'})
    )
    class Meta:
        model = Category
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''    
        
class CategoryAddForm(CategoryBaseForm):
    pass        