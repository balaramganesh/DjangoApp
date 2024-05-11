from django import forms
from .models import orderTable

class OrdersForm(forms.ModelForm) :
    class Meta :
        model = orderTable
        fields = ['productName','productCount']