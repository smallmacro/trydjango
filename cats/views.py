from django.shortcuts import render, get_object_or_404 ,redirect
from django.http import Http404
from .models import Cat

from .forms import CatForm, RawCatForm
# Create your views here.
def cat_list_view(request, *arg, **kwargs):
    obj = Cat.objects.all()
    num = Cat.objects.count()
    context = {
        'obj':obj,
        'num':num
    }
    return render(request, "cats/cat_list_detail.html", context)


def cat_create_view(request,*arg, **kwargs):
    form = CatForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form = CatForm()
    context = {
        'form':form
    }
    return render(request, "cats/cat_create.html", context)

# def cat_create_view(request,*arg, **kwargs):

#     my_form = RawCatForm()
#     if request.method == "POST":
#         my_form = RawCatForm(request.POST)  #django do the validation here and the csrf_token in form tag.
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Cat.objects.create(** my_form.cleaned_data)
#         else:
#             print(my_form.errors)
    

#     context = {
#         'form':my_form
#     }
#     return render(request, "cats/cat_create.html", context)

def cat_update_view(request, id):
    obj = get_object_or_404(Cat, id=id)
    form = CatForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        
    context = {
        'form':form
    }
    
    return render(request, "cats/cat_create.html", context)




def dynamic_lookup_view(request, id):
    # obj = Cat.objects.get(id=id)
    # obj = get_object_or_404(Cat, id=id)
    try:
        obj = Cat.objects.get(id=id)
    except Cat.DoesNotExist:
        raise Http404
    print(obj.name)
    context = {
        "obj": obj
    }
    return render(request, "cats/cat_detail.html",context)


def cat_delete_view(request, id):
    try:
        obj = Cat.objects.get(id=id)
    except Cat.DoesNotExist:
        raise Http404
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    print(obj.name)
    context = {
        "obj" : obj
    }
    return render(request, "cats/cat_delete.html", context)
