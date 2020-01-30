from django import forms
from .models import Author, Book, Friends  
  
class AuthorForm(forms.ModelForm): 

    full_name = forms.CharField(widget=forms.TextInput)  

    class Meta:
        model = Author  
        fields = '__all__'

class BookForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput)
    description = forms.CharField(widget=forms.TextInput)

    class Meta:  
        model = Book  
        fields = '__all__'

class FriendsForm(forms.ModelForm):

	class Meta:
		model = Friends
		fields = '__all__'


