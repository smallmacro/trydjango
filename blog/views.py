
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from .forms import ArticleModelForm

#implemented by generic View
from django.views.generic import(
    DeleteView,
    UpdateView,
    CreateView,
    DetailView,
    ListView

    )

# Create your views here.
# The default object in context is object_list

#self.object_list 将包含该视图正在操作的对象列表
class ArticleListView(ListView):
    template_name = "blog/article_list.html"
    queryset = Article.objects.all()
    #model = Article
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        print(context['object_list'])
        return context

   

#self.object 将包含该视图正在操作的对象
class ArticleDetailView(DetailView):
    """docstring for ArticleDetailView"""
    template_name = "blog/article_detail.html"
    model = Article   # 相当于queryset = Article.objects.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

# self.object，也就是正在创建的对象
class ArticleCreateView(CreateView):
    template_name = "blog/article_create.html"
    model = Article
    form_class = ArticleModelForm
    
    #Save the POSTed data and redirect to url of the specific article 
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

   
# self.object in UpdateView is different with the one in CreateView
class ArticleUpdateView(UpdateView):
    template_name = "blog/article_create.html"
    model = Article
    form_class = ArticleModelForm

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())




    # The DeleteView will delete the specific obejct 
    # So need to explictly indicate the redirect path
class ArticleDeleteView(DeleteView):
    """docstring for ArticleDeleteView"""
    
    template_name = "blog/article_delete.html"
    model = Article
    success_url = reverse_lazy('blog:article-list')

    #Alternative way  is to overide the get_success_url to indicate the redirect url path.
    # def get_success_url(self):
    #     return reverse('blog:article-list')
        
