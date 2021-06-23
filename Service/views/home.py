from django.views import View
from django.shortcuts import render
from ..models import category,service
from json import dumps

class Home(View):

    def post(self,request,id1=None):

        if id1:                                                                                 # When you click on card
            print("id1")
            category = id1
            type = service.objects.filter(type= category)
        else:                                                                                   # When you search on search bar
            print("fsdsfsdfsd")
            category = request.POST['category']
            type = service.objects.filter(type=category)

        # if request.session['customerid'] or request.session['senderid']:
        return render(request, 'Service/showservices.html',{'type':type,'category':category})


    def get(self,request):
        categorys = category.objects.all()

        dictCat=[]

        for cat in categorys:
            dictCat.append(cat.cname)

        CatJSON = dumps(dictCat)
        return  render(request, 'Service/Home.html',{'categorys':categorys,'CatJson': CatJSON})
