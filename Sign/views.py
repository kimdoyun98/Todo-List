from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User_Info
from .serializers import UserinfoSerializer


class login(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        user_pw = request.POST.get("user_pw")
        user =User_Info.objects.filter(user_id=user_id).first()

        error_template = "login/error.html"
        if user is None:
            return render(request, error_template, {"msg": "아이디를 잘못 입력하셨습니다."})
        if check_password(user_pw, user.user_pw):
            user.is_active = True
            user.save()

            response = redirect('/')
            response.set_cookie('user_id', user.user_id)
            return response
        else:
            return render(request, error_template, {"msg": "비밀번호가 틀렸습니다."})

    def get(self, request):
        template_name = 'login/login.html'
        return render(request, template_name)


class logout(APIView):
    def get(self, request):
        user_id = request.COOKIES.get('user_id')
        user = User_Info.objects.filter(user_id=user_id).first()
        user.is_active = False
        user.save()

        response = redirect('/')
        response.delete_cookie('user_id')

        return response

class signup(APIView):
    def post(self, request):
        serializer = UserinfoSerializer(request.data)
        error_template = "login/error.html"
        if User_Info.objects.filter(user_id=serializer.data['user_id']).exists():
            return render(request, error_template, {"msg": "사용할 수 없는 아이디입니다."})

        serializer.create(serializer.data)
        return redirect('/sign/login')

    def get(self, request):
        template_name = 'signup/signup.html'
        return render(request, template_name)


