from django import forms
from .models import Component,Product,ProductOption,ProductOptionComponent
#DataFlair

class ComponentForm(forms.ModelForm):

    class Meta:
        model = Component
        fields = '__all__'

class ProducttForm(forms.ModelForm):
    options = forms.ModelChoiceField(queryset=None)
    ass = forms.CharField(max_length=64,empty_value="poop",label="Hey Now")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['options'].queryset = ProductOption.objects.filter(product_id=1)
    class Meta:
        model = Product
        fields = ['uid','ass','options']

class ProductOptionForm(forms.ModelForm):
    class Meta:
        model = ProductOption
        fields = '__all__'
class ProductOptionComponentForm(forms.ModelForm):
    class Meta:
        model = ProductOptionComponent
        fields = '__all__'
