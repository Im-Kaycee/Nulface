from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Posts
from .forms import PostForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
def all_posts(request):
    all_posts = Posts.objects.all().order_by('-date_posted')
    context = {
        'all_posts': all_posts,
    }
    return render(request, 'All_posts.html',context)
def cyber_posts(request):
    cyber_posts = Posts.objects.all().order_by('-date_posted')
    context = {
        'cyber_posts': cyber_posts,
    }
    return render(request, 'cyber.html',context)
#def blog(request):
    #return render(request, 'blog.html', {})
#def upload(request):
    #return render(request, 'upload.html', {})

class blogs(ListView):
    model = Posts
    template_name = 'blog.html'
    context_object_name = 'post'  
    ordering = ['-id']

    def get_queryset(self):
        return Posts.objects.all().order_by('-date_posted')[:10]  # Limit to first 10 entries for the main list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve a different amount of data for the first section
        context['top_posts'] = Posts.objects.all().order_by('-date_posted')[:5]  # First 5 posts

        # Retrieve a different amount of data for the second section
        context['recent_posts'] = Posts.objects.all().order_by('-date_posted')[:2]  # first 2 posts
        # Retrieve a different amount of data for the third section
        context['newest_post'] = Posts.objects.all().order_by('-date_posted')[:1]  # first post
          # Retrieve a different amount of data for the third section
        context['all_posts'] = Posts.objects.all().order_by('-date_posted')

        
        return context
class post_details(DetailView):
    model = Posts
    template_name = 'post.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_details'] = get_object_or_404(Posts, id=self.kwargs.get('pk'))
        return context

class upload(CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'upload.html'
    context_object_name = 'upload'
    #fields = ['title', 'content', 'date_posted', 'category', 'author']
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set author to logged-in user
        return super().form_valid(form)   

class add_category(CreateView):
    model = Posts
    #form_class = PostForm
    template_name = 'add_category.html'
    context_object_name = 'add_category'
    #fields = ['title', 'content', 'date_posted', 'category', 'author']
    
class edit_post(UpdateView):
    model = Posts
    form_class = PostForm
    template_name = 'edit_post.html'
    #fields =['title','category','content']
    context_object_name = 'update'
    def get_context_data(self, **kwargs):
        # Get the default context data
        context = super().get_context_data(**kwargs)

        # Add 'post_details' to the context using the current post being edited
        context['post_details'] = get_object_or_404(Posts, pk=self.kwargs['pk'])

        return context

class delete_post(DeleteView):
    model = Posts
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')
    def get_context_data(self, **kwargs):
        # Get the default context data
        context = super().get_context_data(**kwargs)

        # Add 'post_details' to the context using the current post being edited
        context['post_details'] = get_object_or_404(Posts, pk=self.kwargs['pk'])

        return context