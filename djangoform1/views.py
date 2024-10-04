from django.shortcuts import render
from . import forms
from djangoform1.models import Employee

# Create your views here.
def userRegistrationView(request):
    form = forms.UserRegistrationForm()
    data = {'form':form}
    return render(request, 'userRegistration.html', data)

def employeeData(request):
    empleados = Employee.objects.all()
    data = {'empleados':empleados}
    return render(request, 'DjangoModel1/empleados.html', data)
