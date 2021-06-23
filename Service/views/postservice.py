from django.views import View
from django.shortcuts import render
from ..models import service,Uuser

class postservice(View):
    def post(self, request,obj=None):
        service_providerid= request.session['senderid']
        user = Uuser.objects.get(uid = service_providerid)
        sname = request.POST['sname']
        description = request.POST['SerDescription']
        Fees = request.POST['Fees']
        address = request.POST['address']
        date = request.POST['date']
        i = service(uid_id=user.uid,  heading=sname,  description= description,fees=Fees,address=address,date=date , type =user.role)
        i.save()
        return render(request, 'Service/postservice.html')

    def get(self, request,obj=None):
        return render(request,'Service/postservice.html')

