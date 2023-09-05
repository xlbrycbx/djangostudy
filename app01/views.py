from django.shortcuts import render, redirect
from app01 import models
from django import forms


# Create your views here.
def dept_list(request):
    dept_list = models.Department.objects.all()

    return render(request, 'dept_list.html', {'dept_list': dept_list})


def dept_add(request):
    if request.method == 'GET':
        return render(request, 'dept_add.html')
    title = request.POST.get('title')
    models.Department.objects.create(title=title)
    return redirect('/dept/list/')


def dept_delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect('/dept/list/')


def dept_edit(request, nid):
    if request.method == 'GET':
        edit_data = models.Department.objects.filter(id=nid).first()
        return render(request, 'dept_edit.html', {'edit_data': edit_data})
    title = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect('/dept/list')


def user_list(request):
    user_list = models.UserInfo.objects.all()
    return render(request, 'user_list.html', {'userlist': user_list})


def user_add(request):
    if request.method == 'GET':
        context = {
            'gender_choices': models.UserInfo.gender_choices,
            'dept_list': models.Department.objects.all()
        }
        return render(request, 'user_add.html', context)
    name = request.POST.get('name')
    password = request.POST.get('password')
    account = request.POST.get('account')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    dept_id = request.POST.get('dept_id')
    cdate = request.POST.get('cdate')

    models.UserInfo.objects.create(name=name,password=password,age=age,account=account,gender=gender,
                                   depart_id=dept_id,create_time=cdate)
    return redirect('/user/list')


class UserModelForm(forms.ModelForm):
    name=forms.CharField(min_length=3,label='用户名')
    password=forms.CharField(min_length=8,label='秘钥')
    class Meta:
        model = models.UserInfo
        fields = ['name','password','age','account','create_time','gender','depart']
        # widgets = {
        #     'name' : forms.TextInput(attrs={'class':'form-control'}),
        #     'password': forms.TextInput(attrs={'class': 'form-control'}),
        #     'age': forms.TextInput(attrs={'class': 'form-control'}),
        #     'account': forms.TextInput(attrs={'class': 'form-control'}),
        #     'create_time': forms.DateInput(attrs={'class': 'form-control'}),
        #     'gender': forms.TextInput(attrs={'class': 'form-control'}),
        # }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs = {'class':'form-control','placeholder':field.label}




def user_add_model_form(request):
    if request.method == 'GET':
        form = UserModelForm()

        return render(request,'user_add_model_form.html',{'form':form})

    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list')

    return render(request,'user_add_model_form.html',{'form':form})



def user_edit(request,nid):
    thisdata = models.UserInfo.objects.filter(id=nid).first()

    if request.method == 'GET':
        form = UserModelForm(instance=thisdata)

        return render(request,'user_edit.html',{'form':form})
    form = UserModelForm(data=request.POST,instance=thisdata)
    if form.is_valid():
        form.save()
        return redirect('/user/list')

    return render(request,'user_edit.html',{'form':form})

def user_delete(request):
    nid = request.GET.get('nid')
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list')


