
# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category,Profile,Comment,Project,Contact
from .forms import PostForm,UpdatePostForm,CommentForm,CategoryForm,ProjectForm,ContactForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.
# def home(request):
#     return render(request,'home.html',{})

def LikeView(request,pk):
    post = Post.objects.get(id = pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('artical-detail', args = [str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-pub_date']
    
    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

    

    
def CategoryView(request,cats):
    category_posts = Post.objects.filter(category = cats.replace('-',' '))
    category_posts = Post.objects.order_by('-pub_date')
    return render(request,'categories.html',{'cats':cats.title().replace('-',' '),'category_posts':category_posts})

def get_context_data(self,*args,**kwargs):
    cat_menu = Category.objects.all()
    context = super(CategoryView,self).get_context_data(*args,**kwargs)
    context["cat_menu"] = cat_menu
    return context

class ArticalDetailView(DetailView):
    model = Post
    template_name = 'artical_details.html'

    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticalDetailView,self).get_context_data(*args,**kwargs)
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True


        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
    


class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'
    #fields = '__all__'

class UpdatePost(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'
    #fields = ['title','title_tag','body']

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class ProjectView(ListView):
    model = Project
    template_name = 'projects.html'
    ordering = ['-pub_date']


class AddProject(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'add_project.html'
    success_url = reverse_lazy('projects')


def Aboutus(request):
    return render(request,'aboutus.html')


class Contactus(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contactus.html'
    success_url = reverse_lazy('home')


def Customers(request):
    return render(request,'customers.html')


def Privacy(request):
    return render(request,'privacy.html')


def Terms(request):
    return render(request,'terms.html')


  