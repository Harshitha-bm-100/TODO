from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Todo


# GET /  — the page you see in the browser.
def index(request):
    # QuerySet of every Todo. The template loops over this.
    # It does not hit the database until the template uses it.
    todos = Todo.objects.all()
    return render(
        request,
        "todos/index.html",
        {
            "todos": todos,
            # A second query: how many tasks are still open.
            "open_count": todos.filter(completed=False).count(),
        },
    )


# Only POST is allowed. A normal page load (GET) is rejected.
@require_POST
def add_todo(request):
    # The form field is <input name="title">. strip() drops extra spaces.
    title = request.POST.get("title", "").strip()
    if title:
        # INSERT into todos_todo. completed and created_at use their defaults.
        Todo.objects.create(title=title)
    # Send the browser back to /. The name "index" is defined in urls.py.
    return redirect("index")


@require_POST
def toggle_todo(request, pk):
    # pk comes from the URL, for example /4/toggle/. 404 if that id is gone.
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    # Write only the completed column, not the whole row.
    todo.save(update_fields=["completed"])
    return redirect("index")


@require_POST
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect("index")
