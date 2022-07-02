from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView

from .forms import UsersPostCreateForm
from .models import UsersPosts, Usersjson, Postsjson
from .apiload import init


def index(request: HttpRequest):
    init()
    q1 = UsersPosts.objects.values('name', 'email')
    q2 = Usersjson.objects.values('name', 'email')
    users = q1.union(q2, all=True).order_by("id")
    print(users)
    context = {
        "name": users,
    }
    return render(request, "user_post/index.html", context=context)

def details(request: HttpRequest, pk: int):
    users = UsersPosts.objects.filter_by(pk)
    context = {
        "users": users,
        "pk": pk,
    }
    print(users)
    return render(request, "user_post/usersposts_detail.html", context=context)

def nousers(request: HttpRequest):
    return render(request, "user_post/nousers.html")
class UsersPostListView(ListView):
    #queryset = UsersPosts.objects.all()
   # if UsersPosts.objects.all().exists():
   #     print("no users")
    model = UsersPosts

class UsersPostDetailView(DetailView):
    model = UsersPosts

class UsersPostDeleteView(DeleteView):
    model = UsersPosts
    success_url = reverse_lazy("user_post:list")

class UsersPostCreateView(CreateView):
    model = UsersPosts
    form_class = UsersPostCreateForm

    def get_success_url(self):
        return reverse("user_post:details", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        self.object: UsersPosts = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)