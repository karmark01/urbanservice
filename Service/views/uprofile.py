from django.views import View
from django.shortcuts import render

class userprofile(View):
    def post(self,request):
        return render(request, 'Service/profile.html')

    def get(self,request):
        print("hello")
        return render(request, 'Service/profile.html')