from django import forms
class FormName(forms.Form):
    itemName = forms.CharField()
    shortDescription=forms.CharField()
    longDescription=forms.CharField(widget=forms.Textarea)
    featured=forms.BooleanField()
    publish=forms.BooleanField()