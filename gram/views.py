from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .forms import PostForm
from .models import Post
from django.views.generic import (ListView,CreateView,DetailView)
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here.
class PostListView(ListView):
    template_name = "post_list.html"
    queryset = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
    context_object_name = "posts"

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
        return get_object_or_404(post,id=id_)
      

def signUp(request):
    return render(request,'.html')

def login(request):
    return render(request,'registration/login.html')


@login_required(login_url='/profile')
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = User.objects.filter(username__icontains = search_term)
        message = f"{search_term}"
        profile_pic = User.objects.all()
        return render(request, 'registration/search.html', {'message':message, 'results':searched_users, 'profile_pic':profile_pic})
    else:
        message = "You haven't searched for any term"
        return render(request, 'registration/search.html', {'message':message})
            
def profile(request):
    images = request.user.profile.posts.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        'images': images,

    }
    return render(request, 'registration/profile.html', params)

