from django.views import View
from django.shortcuts import render
from ..models import service,Uuser,requests
from itertools import chain

class Aheadservice(View):

    def post(self,request,id=None):
        return render(request, 'Service/Aheadservice.html')

    def get(self,request,id=None):
        uid = request.session['senderid']
        # uuid =uid
        All_service = service.objects.filter(uid=uid)

        print(All_service)
        All_sid = []
        for all in All_service:
            All_sid.append(all.sid)

        request_uid_sid = []
        for a in All_sid:
            print("a is",a)
            if requests.objects.filter(sid=a):
                result = requests.objects.filter(sid=a)
                request_uid_sid.append(result.values('uid_id','sid_id'))



        print(len(request_uid_sid))

        Detail = []
        for result in request_uid_sid:
            for r in result:
                user_id=r['uid_id']
                service_id=r['sid_id']
                tem = []
                user_detail = Uuser.objects.get(uid=user_id)
                service_detail = service.objects.get(sid=service_id)
                tem.append(user_detail)
                tem.append(service_detail)
                Detail.append(tem)


        for d in Detail:
            print(d[0].uid)


        # if uid:
        #     service.objects.filter(sid=id).update(receveri_id=None)
        # resultsm = service.objects.filter(receveri_id = uid)
        #
        # tem = 0
        # for i in resultsm:
        #     tem = i.uid_id
        #
        # user = Uuser.objects.filter(uid= tem)
        return render(request, 'Service/Aheadservice.html',{'detail':Detail})
