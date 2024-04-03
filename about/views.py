from django.shortcuts import render, get_object_or_404
from .models import About
from django.contrib import messages
from .forms import CollaborateForm

# Create your views here.
def about_detail(request):
    """
    Renders the About page
    """

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collab = collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, 
            "Collaboration request recieved! I endeavor to respond within 2 working days.")

    about = About.objects.all().order_by('-updated_on').first()

    collaborate_form = CollaborateForm()
    
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )