from django.contrib import admin

from .models import Todo


# Same todos_todo rows, edited at /admin/ after createsuperuser.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "completed", "created_at")
    list_filter = ("completed",)
    search_fields = ("title",)
