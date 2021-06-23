from django.views import View
from django.shortcuts import render
from ..models import category,service,Uuser,Requestss,requests
from django.db.models import Q

class Bookmyservice(View):

    def post(self,request,id=None):
        customerid = request.session['customerid']
        print(customerid)
        if id:
           i = requests(uid_id=customerid,sid_id=id)
           i.save()
        customer_requests = requests.objects.filter(uid_id = customerid)
        all_service = []

        for c1 in customer_requests:
            if service.objects.filter(sid = c1.sid_id):
                s = service.objects.filter(sid = c1.sid_id)
                s=list(s)
                s.append(c1.req)
                print(s)
                all_service.append(s)

        for i in all_service:
            print(i[0].heading,i[1])
        return render(request, 'Service/bookmyservice.html',{'myservice':all_service})


    def get(self,request,id=None):
        customerid = request.session['customerid']

        if id:
            requests.objects.get(req=id).delete()

        customer_requests = requests.objects.filter(uid_id=customerid)
        all_service = []

        for c1 in customer_requests:
            if service.objects.filter(sid=c1.sid_id):
                s = service.objects.filter(sid=c1.sid_id)
                s = list(s)
                s.append(c1.req)
                print(s)
                all_service.append(s)

        for i in all_service:
            print(i[0].heading, i[1])

        return render(request, 'Service/bookmyservice.html', {'myservice': all_service})