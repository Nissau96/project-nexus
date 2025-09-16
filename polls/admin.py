# polls/admin.py

from django.contrib import admin
from .models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['questions']}),
        ('Date information', {'fields': ['pub_date', 'expiry_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInline]
    list_display = ('questions', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['questions']



admin.site.register(Poll, PollAdmin)