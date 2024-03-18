from django.shortcuts import redirect,render
from django.views import View
from .models import Student
from .forms import AddStudenForm
# Create your views here.

class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()
        return render(request, 'core/home.html',{'studata':stu_data})
    
class Add_Student(View):
    def get(self, request):
        fm = AddStudenForm()
        return render(request, 'core/add-student.html', {'form':fm})
    def post(self, request):
        fm = AddStudenForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'core/add-student.html', {'form':fm})

class Delete_Student(View):
    def post(self, request):    
        data = request.POST
        id = data.get('id')
        student=Student.objects.get(id=id)
        student.delete()
        return redirect('/')
class Edit_Student(View):
    def get(self, request, id):
        stu = Student.objects.get(id=id)
        fm= AddStudenForm(instance=stu)
        return render(request, 'core/edit-student.html',{'form':fm})
    def post(self, request, id ):
        stu = Student.objects.get(id=id)
        fm = AddStudenForm(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')

    
