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
        new_blog.save(commit=False)
        new_blog.instance.author = request.user
        new_blog.save()
        blog_result = 'Блог создан'
        return render(request=request, template_name='blog_app/blog_creation.html',
                      context={'blog_result': blog_result})


class BlogRedactionView(View):

    def get(self, request, pk, *args, **kwargs):
        blog_db = Blog.objects.get(id=pk)
        blog_form = BlogForm(initial={'title': blog_db.title, 'body': blog_db.body})
        return render(request=request, template_name='blog_app/blog_redaction.html',
                      context={'blog_form': blog_form})

    def post(self, request, pk, *args, **kwargs):
        blog_db = Blog.objects.get(id=pk)
        blog = BlogForm(data=request.POST, instance=blog_db)
        blog.save()
        blog_result = 'Блог отредактирован'
        return render(request=request, template_name='blog_app/blog_redaction.html',
                      context={'blog_result': blog_result})

class MainView(generic.TemplateView):
    template_name = 'blog_app/main.html'
