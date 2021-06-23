from django.views import View
from django.shortcuts import render
from ..models import Uuser,service
from django.db.models import Q
class showservices(View):
    def get(self,request,t1=None):
        return render(request,'showservices.html')

    def post(self,request):
        return render(request, 'showservices.html')