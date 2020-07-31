from django import forms 

from Blog.models import *

class EmailSendForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    to = forms.CharField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
        widgets = {
            'body':forms.Textarea(attrs={'rows':4,'cols':111,'class':'ml-2 text-danger font-weight-bold'}),
            'name':forms.Textarea(attrs={'rows':1,'cols':50,'class':'ml-2 text-danger font-weight-bold'}),
            'email':forms.Textarea(attrs={'rows':1,'cols':50,'class':'ml-2 text-danger font-weight-bold'}),
        }