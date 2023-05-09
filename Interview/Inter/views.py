from django.views.generic import DetailView
from .models import File


class Post(DetailView):
    model = File
    ordering = 'file'
    template_name = 'default.html'
    context_object_name = 'file'


