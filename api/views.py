from django.http import JsonResponse


def health_check(request, *args, **kwargs):
    return JsonResponse({"message": "health check OK!"})
