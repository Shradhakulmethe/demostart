from django.shortcuts import render, HttpResponse
from .models import Student

# Create your views here.
def demo(request):
    print("demo")
    stu = Student.objects.all
    template_name = "demo.html"
    context = {"stu":stu}
    return render(request, template_name, context)
