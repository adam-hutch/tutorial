from django import forms

class CreateBlogPostForm(forms.Form):
    title = forms.CharField()
    quick_description = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    image_url = forms.URLField()