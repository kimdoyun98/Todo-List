from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import Main_Todo, Day_Todo, Sub_Todo


class main(APIView):
    def get(self, request):
        user_id = request.COOKIES.get('user_id')
        task_list = Main_Todo.objects.filter(user_id=user_id)

        template_name = "todo_main/main_list.html"
        return render(request, template_name, {'task_list': task_list})

    def post(self, request):# Delete
        id_list = request.POST.getlist("todo-check")
        for id in id_list:
            obj = Main_Todo.objects.get(id=id)
            obj.delete()
        return redirect('/board/main/')


class main_create(APIView):
    def post(self, request):
        try:
            database = Main_Todo()
            database.user_id = request.COOKIES.get('user_id')
            database.context = request.data["context"]
            database.save()
            return redirect('/board/main/')

        except:
            template_name = "todo_main/error.html"
            return render(request, template_name, {"msg": "로그인이 필요합니다."})


class day(APIView):
    def get(self, request):
        user_id = request.COOKIES.get('user_id')
        task_list = Day_Todo.objects.filter(user_id=user_id)

        template_name = "todo_day/day_list.html"
        return render(request, template_name, {'task_list': task_list})

    def post(self, request):# Delete
        id_list = request.POST.getlist("todo-check")
        for id in id_list:
            obj = Day_Todo.objects.get(id=id)
            obj.delete()
        return redirect('/board/day/')


class day_create(APIView):
    def post(self, request):
        try:
            database = Day_Todo()
            database.user_id = request.COOKIES.get('user_id')
            database.context = request.data["context"]
            database.save()
            return redirect('/board/day/')

        except:
            template_name = "todo_main/error.html"
            return render(request, template_name, {"msg": "로그인이 필요합니다."})


class sub(APIView):
    def get(self, request):
        user_id = request.COOKIES.get('user_id')
        task_list = Sub_Todo.objects.filter(user_id=user_id)

        template_name = "todo_sub/sub_list.html"
        return render(request, template_name, {'task_list': task_list})

    def post(self, request):# Delete
        id_list = request.POST.getlist("todo-check")
        for id in id_list:
            obj = Sub_Todo.objects.get(id=id)
            obj.delete()
        return redirect('/board/sub/')


class sub_create(APIView):
    def post(self, request):
        try:
            database = Sub_Todo()
            database.user_id = request.COOKIES.get('user_id')
            database.context = request.data["context"]
            database.save()
            return redirect('/board/sub/')

        except:
            template_name = "todo_main/error.html"
            return render(request, template_name, {"msg": "로그인이 필요합니다."})