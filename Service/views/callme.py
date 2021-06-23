from django.views import View
from django.shortcuts import render
from ..models import Uuser,service
from django.db.models import  Q

class callme(View):
    def post(self,request):
        return render(request, 'Service/callme.html')

    def get(self,request):
        print(request.session['senderid'])
        senderid = request.session['senderid']
        post = service.objects.filter(Q(uid =senderid) & Q(receveri__isnull = False))
        print()
               #


        return render(request, 'Service/callme.html',)