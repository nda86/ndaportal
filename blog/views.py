from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse(str(request.user))
