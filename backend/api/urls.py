from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),

    path('api/add-item/', views.AddItemView.as_view(), name='add_item'),
    path('api/user-items/', views.UserItemsView.as_view(), name='get_user_items'),
]