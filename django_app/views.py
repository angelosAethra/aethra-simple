from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is a first try to reach out.")
