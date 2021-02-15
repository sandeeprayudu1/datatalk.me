from django import forms
from .models import Post,Category,Comment,Project,Contact

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippet','image','header_image')


        widgets= {
            'title':forms.TextInput(attrs = {'class': 'form-control','placeholder':'name of the post'}),
            'title_tag':forms.TextInput(attrs = {'class': 'form-control'}),
            'author':forms.TextInput(attrs = {'class': 'form-control','Value': '','id':'elder','type':'hidden'}),
            #'author':forms.Select(attrs = {'class': 'form-control','placeholder': 'select author'}),
            'category':forms.Select(choices = choice_list, attrs = {'class': 'form-control'}),
            'body':forms.Textarea(attrs = {'class': 'form-control'}),
            'snippet':forms.Textarea(attrs = {'class': 'form-control'}),
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','category','body','snippet','image','header_image')

        widgets = {
            'title':forms.TextInput(attrs = {'class':'form-control'}),
            'title_tag':forms.TextInput(attrs = {'class':'form-control'}),
            'category':forms.Select(choices = choice_list, attrs = {'class': 'form-control','placeholder': 'select category'}),
            'body':forms.Textarea(attrs = {'class':'form-control'}),
            'snippet':forms.Textarea(attrs = {'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name':forms.TextInput(attrs = {'class': 'form-control','Value': '','id':'elder','type':'hidden'}),
            'body':forms.Textarea(attrs = {'class':'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name':forms.TextInput(attrs = {'class':'form-control'}),

        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title','author','github_link','image',)


        widgets= {
            'title':forms.TextInput(attrs = {'class': 'form-control','placeholder':'name of the post'}),
            'author':forms.TextInput(attrs = {'class': 'form-control','Value': '','id':'elder','type':'hidden'}),
            'github_link':forms.TextInput(attrs = {'class': 'form-control'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','email','message')

        widgets = {
            'name':forms.TextInput(attrs = {'class': 'form-control',}),
            'email':forms.TextInput(attrs = {'class': 'form-control',}),
            'message':forms.Textarea(attrs = {'class': 'form-control',}),

        }
