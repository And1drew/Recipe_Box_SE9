from django import forms
from recipe_box_app.models import Recipe, Author

class add_recipe_form(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset = Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=40)
    instructions = forms.CharField(widget=forms.Textarea)

class add_author_form(forms.ModelForm):
    class Meta:
        model = Author
        fields =['name', 'bio', 'username', 'password']


class login_form(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)
