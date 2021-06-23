from django.views import View
from django.shortcuts import render
from ..models import service,Uuser,category
from django.contrib import messages

class register(View):
    def post(self,request,id=None):
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # Address = request.POST['Address']
        # phoneno = request.POST['phone_number']
        # categorys = request.POST['dropdown']
        #
        # email = request.POST['email']
        # Pass = request.POST['Pass']


        # if choice == "Receiver":
        #     choice = "receiver"
        # else:
        #     choice = "sender"
        if id == 1:                                           # if id = 1 Mense Customer are trying to register
            user = Uuser()
            user.name = request.POST['first_name']
            user.lname = request.POST['last_name']
            user.address = request.POST['Address']
            user.phonenumber = request.POST['phone_number']
            user.email = request.POST['email']
            user.password = request.POST['Pass']
            user.phonenumber = request.POST['phone_number']
            user.save()
            return render(request, 'Service/Login.html')
        else:
            user = Uuser()
            user.name = request.POST['first_name']
            user.lname = request.POST['last_name']
            user.address = request.POST['Address']
            user.phonenumber = request.POST['phone_number']
            user.role = request.POST['dropdown']
            user.email =request.POST['email']
            user.password = request.POST['Pass']
            user.save()
            messages.success(request,"Thankyou for Being a Member")
            return render(request, 'Service/Login.html')

    def get(self,request):

        cat = category.objects.all()
        return render(request, 'Service/register.html',{'cat':cat})