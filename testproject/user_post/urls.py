
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import index, UsersPostDetailView, UsersPostDeleteView, UsersPostCreateView
from django.urls import path, include
from.views import UsersPostListView

app_name = "user_post"


urlpatterns = [
    path("", UsersPostListView.as_view(), name="list"),
    path('<int:pk>/', UsersPostDetailView.as_view(), name="details"),
    path("<int:pk>/confirm-delete/", UsersPostDeleteView.as_view(), name="delete"),
    path("create/", UsersPostCreateView.as_view(), name="create"),
    path("test/", index, name="index"),
    #path("nousers", name="nousers"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
