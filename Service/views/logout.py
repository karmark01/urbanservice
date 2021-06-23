from django.views import View
from django.shortcuts import render
from ..models import service,Uuser,category
from django.contrib import messages
from . import home


class logout(View):

    def get(self,request):
        if 'customerid' in request.session:
            del request.session['customerid']
            return home.Home.as_view()(self.request)

        elif 'senderid' in request.session:
            del request.session['senderid']
            return home.Home.as_view()(self.request)
