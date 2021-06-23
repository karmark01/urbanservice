from django.views import View
from django.shortcuts import render
from ..models import Uuser,service
from django.db.models import Q
from . import home
class Login(View):

    def get(self,request):
        return render(request, 'Service/Login.html')


    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('pass')
        print("sdfsf",request)
        print(password,username)
        All_user = Uuser.objects.all()

        temp = 0
        for user in All_user:
            if user.password == password and user.email == username:
                temp = 1
                s = Uuser
                if user.role == '':
                    # show_service = service.objects.all()
                    # t =service.objects.all().select_related('uid_id')
                    # print('uuuuuuuuuuu', t.values())
                    # post = []
                    # ser = Uuser.objects.filter( role__isnull=True)
                    # ser = service.objects.filter(receveri__isnull = True)
                    #
                    # for s in ser:
                    #     users = Uuser.objects.get(uid = s.uid_id,)
                    #
                    #     if users:
                    #         tem = {}
                    #         tem['uid'] = users.uid
                    #         tem['sid'] = s.sid
                    #         tem['name']=users.name
                    #         tem['phonenumber']=users.phonenumber
                    #         tem['work']=s.type
                    #         tem['duration']=s.duration
                    #         tem['address']=s.address
                    #         post.append(tem)

                    # print(post)
                    # for s in post:
                    #     print(s['name'],s['phonenumber'])

                    request.session['customerid'] = user.uid
                    print(user.uid)
                    request.method = "GET"
                    return home.Home.as_view()(self.request)
                else:
                    # sender = { 'email':user.email , 'password':user.password }
                    request.session['senderid'] = user.uid
                    request.method = "GET"
                    return home.Home.as_view()(self.request)

        return render(request, 'Service/Login.html')





#         if data == "Recever":
#             return render(request, 'Service/profile.html')
#         else:
#             return render(request, 'Service/postservice.html')
#