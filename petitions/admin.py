from django.contrib import admin
from .models import Petition, PetitionVote


@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created_at", "yes_count")
    search_fields = ("title", "description", "created_by__username")
    list_filter = ("created_at",)


@admin.register(PetitionVote)
class PetitionVoteAdmin(admin.ModelAdmin):
    list_display = ("petition", "user", "created_at")
    search_fields = ("petition__title", "user__username")
    list_filter = ("created_at",)
