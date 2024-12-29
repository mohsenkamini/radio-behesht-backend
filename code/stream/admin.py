from django.contrib import admin
from .models import StreamRequest

# Register your models here.


@admin.register(StreamRequest)
class StreamRequestAdmin(admin.ModelAdmin):
    list_display= ("program_name", "schedule", "start_date", "episodes", "contact", "status", "submitted_at")
    search_fields = ("program_name", "schedule", "contact")
    list_filter = ("start_date", "status")
    ordering = ("-submitted_at",)
    actions = ["mark_as_pending", "mark_as_in_review", "mark_as_rejected", "mark_as_accepted"]
    
    @admin.action(description="Mark selected requests as Pending")
    def mark_as_pending(self, request, queryset):
        queryset.update(status='pending')
    
    @admin.action(description="Mark selected requests as In Review")
    def mark_as_in_review(self, request, queryset):
        queryset.update(status='in_review')
    
    @admin.action(description="Mark selected requests as Rejected")
    def mark_as_rejected(self, request, queryset):
        queryset.update(status='rejected')
    
    @admin.action(description="Mark selected requests as Accepted")
    def mark_as_accepted(self, request, queryset):
        queryset.update(status='accepted')
