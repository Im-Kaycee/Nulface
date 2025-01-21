from django import forms
from .models import Posts,Category
from ckeditor.widgets import CKEditorWidget
#choices=[('Cyber Security','Cyber Security'),('Graphics Design','Graphics Design'),('UI/UX Design','UI/UX Design'),('Networking','Networking'),('Experience','Experience'),]
choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Posts
        fields = ('title', 'category',  'content', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs= {'class':'inputbox'}),
            'category':forms.Select(choices=choice_list,attrs= {'class':'inputbox'}),
            'content': CKEditorWidget(),
            }