from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

# Create your views here.
user_profile ={
    "name" : "Grace Oliver",
    "email" : "grace.oliver@meltwater.org",
    "phone_number" : "08084629437"

}

def say_hello(req):
    return HttpResponse("<h1>Hello Fleur</h1>")

def get_profile(req):
    return JsonResponse(user_profile)
   


def filter_queries(req, query_id):
    return JsonResponse({
        "id": query_id,
        "title": "Financial Secretary",
        "description": "Handle Money",
        "status": "Active",
        "submited_by": "David"
    })

class QueryView(View):
    queries = [
        {"id": 1, "title": "Adama declined Val shots"},
        {"id": 2, "title": "Samson declined Val shots"}
     ]
    def get(self, request):
        
        return JsonResponse({"result":self.queries})
    def post(self, response):
        return JsonResponse({"status": "ok"})
