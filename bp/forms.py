from django import forms
from .models import Post


class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('title', 'text',)


""" No creé un formulario para usuarios porque no le encontré sentido si Django ya tiene uno.
En reemplazo hice el de post """
