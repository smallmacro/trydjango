from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from .models import Course
from .forms import CourseForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


##
# Listview can not reflect on the current object in database 
##
#implemented by raw View
# Create your views here.

"""CourseDeleteView"""
class CourseDeleteView(View):
    
    template_name = "courses/course_delete.html"
    def get_object(self):
        id =  self.kwargs.get('id')

        if not id == None:
            obj = get_object_or_404(Course,id=id)
            return obj
        else:
            return None

    def get(self,request,id=None, *arg, **kwargs):
        obj = self.get_object()
        context = {}
        if obj is not None:
            context = {
                'object': obj
            }
       
        return render(request, self.template_name, context)
    def post(self,request, id=None,*arg, **kwargs):
        obj = self.get_object()
        context = {}
        if obj is not None:
            obj.delete()
            context = {'object':None} 
            
        return redirect("courses:course-list")



"""CourseUpdateView"""
class CourseUpdateView(View):
    
    template_name = "courses/course_create.html"
    def get_object(self):
        id =  self.kwargs.get('id')

        if not id == None:
            obj = get_object_or_404(Course,id=id)
            return obj
        else:
            return None
    def get(self,request,id=None, *arg, **kwargs):
        obj = self.get_object()
        context = {}
        if obj is not None:
            form = CourseForm(instance=obj)
            context = {
                'form': form,
                'object': obj
            }
        return render(request, self.template_name, context)
    def post(self,request,id=None, *arg, **kwargs):
        
        obj = self.get_object()
        context = {}
        if obj is not None:
            form = CourseForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                form = CourseForm()
            context = {
                    'form': form,
                    'object': obj
                }
        print(self.kwargs)
        return render(request, self.template_name, context)



"""CourseCreateView"""
class CourseCreateView(View):
    
    template_name = "courses/course_create.html"
    def get(self,request, *arg, **kwargs):
        form = CourseForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    def post(self,request, *arg, **kwargs):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseForm()
        context = {
            'form': form
        }
        

        return render(request, self.template_name, context)
        # return HttpResponseRedirect(self.get_success_url())
    # def get_success_url(self):
    #     return reverse_lazy("courses:course_detail", kwargs={'id':self.object.pk})


"""CourseDetailView"""
class CourseDetailView(View):
    
    template_name = "courses/course_detail.html"
    def get_object(self):
        id =  self.kwargs.get('id')
        if not id == None:
            obj = get_object_or_404(Course,id=id)
            return obj
        else:
            return None
    def get(self,request, *arg, **kwargs):
        context = {
            'object':self.get_object()
        }
        return render(request, self.template_name, context)

"""CourseListView"""
class CourseListView(View):
    
    template_name = "courses/course_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset 

    def get(self,request, *arg, **kwargs):
        context = {
            'object_list':self.get_queryset().all()
        }
        return render(request, self.template_name, context)



