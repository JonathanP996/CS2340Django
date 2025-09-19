from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .models import Petition, PetitionVote
from .forms import PetitionForm


def index(request):
    petitions = Petition.objects.all()
    template_data = {
        "title": "Petitions",
        "petitions": petitions,
    }
    return render(request, "petitions/index.html", {"template_data": template_data})


@login_required
def create(request):
    if request.method == "POST":
        form = PetitionForm(request.POST)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.created_by = request.user
            petition.save()
            messages.success(request, "Petition created!")
            return redirect("petitions:detail", id=petition.id)
    else:
        form = PetitionForm()

    template_data = {
        "title": "Create Petition",
        "form": form,
    }
    return render(request, "petitions/create.html", {"template_data": template_data})


def detail(request, id: int):
    petition = get_object_or_404(Petition, id=id)
    has_voted = request.user.is_authenticated and PetitionVote.objects.filter(petition=petition, user=request.user).exists()
    template_data = {
        "title": petition.title,
        "petition": petition,
        "has_voted": has_voted,
    }
    return render(request, "petitions/detail.html", {"template_data": template_data})


@login_required
def vote_yes(request, id: int):
    petition = get_object_or_404(Petition, id=id)
    PetitionVote.objects.get_or_create(petition=petition, user=request.user)
    messages.success(request, "Your vote has been recorded.")
    return redirect("petitions:detail", id=petition.id)
