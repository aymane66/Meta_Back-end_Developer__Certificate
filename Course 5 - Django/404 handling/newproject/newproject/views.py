from django.http import HttpResponse


def handler404(request, exception):
    return HttpResponse("This page does not exist")