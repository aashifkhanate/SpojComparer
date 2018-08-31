from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from compare import parsing

def foo(request):
    userA = request.POST['userA']
    userB = request.POST['userB']
    listAB = parsing.foo(userA, userB)
    listBA = parsing.foo(userB, userA)
    return {'userA': userA, 'userB': userB, 'listAB': listAB, 'listBA': listBA}

class IndexView(View):
    template_name = 'compare/index.html'
    def get(self, request):
        return render(request, self.template_name)

class ComparisonList(View):
    template_name = 'compare/lister.html'
    def post(self, request):
        return render(request, self.template_name, foo(request))

class ComparisonListAPI(APIView):
    def post(self, request):
        return Response(foo(request))