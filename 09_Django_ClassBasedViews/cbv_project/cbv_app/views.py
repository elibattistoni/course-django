from django.shortcuts import render
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy

# Create your views here.
## FUNCTION BASED VIEW
def index(request):
    return render(request, "index.html")


# ==============================================================================
## Class-Based Views: View
# ==============================================================================


class CBView(View):
    def get(self, request):
        return HttpResponse("Class Based Views are cool!")


# ==============================================================================
## Class-Based Views: TemplateView
# ==============================================================================


class IndexView(TemplateView):
    template_name = "index_cbv.html"


class CBViewContext(TemplateView):
    template_name = "context_cbv.html"

    def get_context_data(self, **kwargs):
        # kwargs = keyword arguments
        # args = arguments
        # *args >> single asterisk: will give you all the function parameters as a tuple
        # **kwargs >> double asterisk will give you all keyword arguments except for those corresponding parameter as a dictionary: this allows you to define key value pairs
        # def foo(**kwargs): ...
        # bar(name="one", age=27)
        context = super().get_context_data(**kwargs)
        context["context"] = "BASIC CONTEXT"
        return context


# ==============================================================================
## Class-Based Views: ListView and DetailView
# ==============================================================================


class SchoolListView(ListView):

    ## OPTION 1:
    # model = models.School # uncomment this for option 1
    #! the ListView automatically creates a context dictionary:
    #! it takes the model (School), lowercases it, and then adds _list
    #! therefore at the end you automatically have the context dictionary:
    #! context = {"school_list":[School1,School2,...]}

    ## OPTION 2
    #! if you want to have a different name (e.g. schools) instead of school_list:
    context_object_name = "schools"
    model = models.School


class SchoolDetailView(DetailView):
    #! the DetailView atuomatically returns the name of the model in lowercase
    #! if you want to have a different name, e.g. school_detail, do:
    context_object_name = "school_detail"
    model = models.School
    template_name = "cbv_app/school_detail.html"


# ==============================================================================
## CreateView
# ==============================================================================


class SchoolCreateView(CreateView):
    #! fields >> used if you want to avoid that someone edits a field
    #! (e.g. location) that you do not want to be edited (it's like a security measure)
    # in fields you specify the fields that you want to show
    fields = ("name", "principal", "location")
    model = models.School
    #! if you run the code without specifying a template, you see that Django is looking for a specific template
    #! i.e. cbv_app/school_form.html
    #! it is usually best to choose a name for the template that matches the default that django is looking for


class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")
    #! leave out 'location' because it is unlikely that a school location changes
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    template_name = "cbv_app/school_confirm_delete.html"
    #! now you have to add a success url
    # reverse_lazy is called, because you want it to be run only when it has been actually deleted
    success_url = reverse_lazy("cbv_app:school_list")
    # success_url = "/"
