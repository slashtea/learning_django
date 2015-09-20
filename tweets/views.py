from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


# Create your views here.

class Index(View):

    def get(self, request):
        return render(request, "hello.html")

    def post(self, request):
        if request.method == 'POST':
            return HttpResponse('I am called from a POST request')