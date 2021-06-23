from django.views import View
from django.shortcuts import render
from ..models import Uuser,service


class services(View):
    def post(self, request):
        return render(request, 'Service/service.html')

    def get(self, request):
        if request.session['senderid']:
           sid= request.session['senderid']
           query = service.objects.filter(uid = sid)
           return render(request, 'Service/service.html', {'post':query})



