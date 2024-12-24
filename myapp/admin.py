# myapp/admin.py
from django.contrib import admin
from .models import Book, NewBookRequest

admin.site.register(Book)


@admin.register(NewBookRequest)
class NewBookRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'request_date', 'status')
    list_filter = ('status', 'request_date')
    search_fields = ('title', 'user__username')

    actions = ['approve_requests', 'decline_requests', 'mark_as_present']

    def approve_requests(self, request, queryset):
        queryset.update(status='APPROVED')
        self.message_user(request, "Selected requests have been approved.")

    def decline_requests(self, request, queryset):
        queryset.update(status='DECLINED')
        self.message_user(request, "Selected requests have been declined.")

    def mark_as_present(self, request, queryset):
        queryset.update(status='ALREADY_PRESENT')
        self.message_user(request, "Selected requests have been marked as already present.")