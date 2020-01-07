from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .forms import PostForm
from .models import Post,Profile
from django.contrib.auth.models import User
from django.views.generic import (ListView,CreateView,DetailView)
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here.
class PostListView(ListView):
    template_name = "post_list.html"
    queryset = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    context_object_name = "posts"
    success_url = '/'

class PostCreateView(CreateView):
    template_name = "post_create.html"
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '/'

    def form_valid(self,form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    template_name ="post_details.html"
    queryset = Post.objects.all().filter(created_date__lte=timezone.now()) 
     
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Post,id=id_)
      

def signUp(request):
    return render(request,'registration/registration_form.html')

@login_required(login_url='/accounts/login/')
def login(request):
    return render(request,'registration/login.html')


@login_required(login_url='/profile')
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = User.objects.filter(username = search_term)
        message = f"{search_term}"
        profile_pic = User.objects.all()
        return render(request, 'search.html', {'message':message, 'results':searched_users, 'profile_pic':profile_pic})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message':message})
            
def profile(request):
    # image = request.user.profile.posts.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
            return render(request, 'profile.html', {})

    return render(request, 'profile.html', {})

def timeline(request):
    posts = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if edit_form.is_valid():
            form.save()
            return render(request, 'post_list.html', {'form': form, 'posts': posts})

    return render(request, 'post_list.html', {'posts': posts})

    