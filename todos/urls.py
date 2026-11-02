from django.urls import path

from . import views

# These paths are mounted at the site root from config/urls.py,
# so "" really is http://127.0.0.1:8000/.
# name= is what {% url 'add' %} and redirect("index") look up.
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_todo, name="add"),
    # <int:pk> is the row id, passed into the view as the argument pk.
    path("<int:pk>/toggle/", views.toggle_todo, name="toggle"),
    path("<int:pk>/delete/", views.delete_todo, name="delete"),
]
