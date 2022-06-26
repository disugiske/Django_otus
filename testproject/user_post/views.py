from django.shortcuts import render
from django.http import HttpRequest
from .models import UsersPosts


def index(request: HttpRequest):
    users = UsersPosts.objects.order_by("id").all()
    # return HttpResponse(f"<h1>Hello page {request.path}</h1>")
    context = {
        "name": users,
    }
    return render(request, "/index.html", context=context)
