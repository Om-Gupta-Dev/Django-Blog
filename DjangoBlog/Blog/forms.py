from django import forms 

from Blog.models import *

class EmailSendForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows':1,'class':'ml-2 text-danger rounded font-weight-bold width-100'}))
    email = forms.EmailField(widget=forms.Textarea(attrs={'rows':1,'class':'ml-2 text-danger rounded font-weight-bold width-100'}))
    to = forms.CharField(widget=forms.Textarea(attrs={'rows':1,'class':'ml-2 text-danger rounded font-weight-bold width-100'}))
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':6,'class':'ml-2 text-danger rounded font-weight-bold width-100'}))
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
        widgets = {
            'body':forms.Textarea(attrs={'rows':6,'class':'ml-2 text-danger rounded font-weight-bold width-100'}),
            'name':forms.Textarea(attrs={'rows':1,'class':'ml-2 text-danger rounded font-weight-bold width-100'}),
            'email':forms.Textarea(attrs={'rows':1,'class':'ml-2 text-danger rounded font-weight-bold width-100'}),
        }