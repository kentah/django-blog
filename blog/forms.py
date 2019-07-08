from django import forms

from blog.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')
        
        widgets = {     # these widgets will add styling to the post
                'title': forms.TextInput(attrs={'class': 'textinputclass'}),
                'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
                }
    


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {     # these widgets will add styling to the comment
                'author': forms.TextInput(attrs={'class': 'textinputclass'}),
                'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
                } 
