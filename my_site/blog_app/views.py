
from django.shortcuts import render
from django.views import generic, View
from .models import Blog
from .forms import BlogForm


class BlogDetailView(generic.DetailView):
    model = Blog
    context_object_name = 'blog_detail'


class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'blog_list'


class BlogCreationView(View):

    def get(self, request, *args, **kwargs):
        blog_form = BlogForm()

        return render(request=request, template_name='blog_app/blog_creation.html',
                      context={'blog_form': blog_form})

    def post(self, request, *args, **kwargs):
        new_blog = BlogForm(data=request.POST)
        new_blog.save()
        blog_result = 'Блог создан'
        return render(request=request, template_name='blog_app/blog_creation.html',
                      context={'blog_result': blog_result})

#  TODO: создать представление редактирования блога


class MainView(generic.TemplateView):
    template_name = 'blog_app/main.html'
