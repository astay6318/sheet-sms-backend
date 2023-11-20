from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Response,Question,Answer,Form
from .serializers import Response_Serializer,Form_Serializer,Answer_Serializer,Question_Serializer
from django.http.response import JsonResponse
from rest_framework import status
#using ModelViewSet we have to create a router to use it with the api
class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = Response_Serializer


#using the APIViewSet we can define the HTTP method

class ResponseViewSet2(APIView):
    queryset = Response.objects.all()
    serializer_class = Response_Serializer
    def post(self, request):
        data = request.data
        serializer = Response_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

class FormViewSet(APIView):
    def post(self,request):
        data = request.data
        serializer = Form_Serializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class QuestionViewSet(APIView):
    def post(self,request):
        print(request.data)
        form_id = request.data.get('form')
        print(form_id)
        form_instance = Form.objects.get(form_id=form_id)
        serializer = Question_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class AnswerViewSet(APIView):
    def post(self,request):
        data = request.data
        form_id = request.data.get('form_id')
        question_id = request.data.get('question_id')
        form_instance = Form.objects.get(pk=form_id)
        question_instance = Question.objects.get(pk=question_id)
        request.data['form'] = form_instance.id
        request.data['question'] = question_instance.id
        serializer = Answer_Serializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

