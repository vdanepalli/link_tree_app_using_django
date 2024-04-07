from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Profile, Link

# INTERNAL
# list out the links 
# create a new link

# EXTERNAL
# see a profile (and it's links)

class LinkListView(ListView):
    
    
    model = Link
    #def template model_list.html

class LinkCreateView(CreateView):
    # if we used functional views, we would have to 
    # create forms.py file and form 
    # check if this was a post or get request
    # return an empty form or save the form data
    
    model = Link
    # template - model_form.html
    # figure out what fields - could pass a list
    fields = "__all__"
    #success_url
    success_url = reverse_lazy('link-list')
    
    # uses template modelName_form.html -> link_form.html

class LinkUpdateView(UpdateView):
    # create a form 
    # check if get or a put request # put is similar to post but we are updating
    # either render form or update and save in our db
    
    # Shares same template as create view
    model = Link
    fields = ["text", "url"] # only these can be updated
    success_url = reverse_lazy('link-list') # after successfully updating, where should we send the user
    
    # uses template modelName_form.html -> link_form.html


class LinkDeleteView(DeleteView):
    # with functioonal views, we would need to 
    # take in a id/pk of an object, query db
    # check if exists -> delete object
    # return some template or forward user to some url
    
    #send a form with a single 'confirm delete btn'
    # template - model_confirm_delete.html
    model = Link
    success_url = reverse_lazy('link-list')
    # expects a template named modelName_confirm_delete.html
    # link_confirm_delete.html

## external profile view - could be a ListView or a function view
def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        "profile": profile,
        "links": links
    }
    return render(request, 'link_plant/profile.html', context)