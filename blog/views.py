from django.http import JsonResponse

# Create your views here.

def index(request):
    context = {"name":"mehedi hasan khan"}
    return JsonResponse(context)