from django import forms 

from .models import Product, Order


class OrderForm(forms.ModelForm): 
    class Meta: 
        model = Order 
        fields = ('first_name', 'last_name', 'address', 'zipcode', 'city',)

class ProductForm(forms.ModelForm):
    class Meta: 
        model = Product 
        fields = ('category', 'title', 'description', 'price','image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full py-4 px-3 border rounded border-grey-200',}),
            'title': forms.TextInput(attrs={
                'class': 'w-full py-4 px-3 border rounded border-grey-200 ',}),
            'description': forms.Textarea(attrs={
                'class': 'w-full py-4 px-3 border rounded border-grey-200',}),
            'price': forms.NumberInput(attrs={
                'class': 'w-full py-4 px-3 border rounded border-grey-200',}),
        }