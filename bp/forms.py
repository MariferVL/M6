from django import forms
# from M6.bp.views import search
from .models import Post


class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('title', 'text',)


""" class SearchForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('title', 'text',)
            search = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)
            """

