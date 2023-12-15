from django import forms
from .models import Item, User, FAQ
from phonenumber_field.formfields import PhoneNumberField

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['usernum' ,'username','password', 'phone',  'usertype' ,'gender' , 'address','age','birthdate']
         
