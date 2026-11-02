from django.db import models


# One row in the SQLite table todos_todo.
# Django creates that table from this class when you run migrate.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    # False until the checkbox on the page is clicked.
    completed = models.BooleanField(default=False)
    # Filled in automatically the first time the row is saved.
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Open tasks first, then newest first within each group.
        ordering = ["completed", "-created_at"]

    def __str__(self):
        # What the admin site shows for this row.
        return self.title
