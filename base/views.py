from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, User, Profile, Logs, CrudUser, FAQ
from django.core.paginator import Paginator
from .form import  UserForm, ItemForm, FAQForm
from django.http import JsonResponse
import qrcode
from io import BytesIO
from django.urls import reverse_lazy
from .models import CrudUser
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from django.db import connection
from django.core import serializers
from django.http import JsonResponse

from django.views.generic import TemplateView, View, DeleteView



# functions
def login(request):

    return render(request, 'index.html')

def log(request, user,password):

    try:
        condition = User.objects.get(username = user, password = password,status=1, usertype='Security Guard')
        return redirect('SG') 
    
    except User.DoesNotExist:
    
        if user == 'admin' and password == 'admin':
            return redirect('dashboard') 
        else:
            return redirect('login') 
        
def updateUserInfo(request, id,uid, user,password,phone,usertype,gender,address,age,birthdate):

    item = get_object_or_404(User,id=id)
    
    item.usernum = uid
    item.username = user
    item.password = password
    item.phone = phone
    item.usertype = usertype
    item.gender = gender
    item.address = address
    item.age = age  
    item.birthdate = birthdate  
    item.save()
    return redirect('home')
         
def SG(request):
    profile = Profile.objects.get(id=1)
    cursor.execute('CALL storedProcLogs')
    result = cursor.fetchall()
   
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    item = Logs.objects.filter(remarks__icontains=q) 
    page = Paginator(result, 14)
    page_list = request.GET.get('page','')
    page = page.get_page(page_list)

    totalStudent = User.objects.filter(status=1,usertype = 'Student').count()
    totalPersonnel = User.objects.filter(status=1,usertype = 'School Personnel').count()

    context = {
        'profile' : profile,
        'items' : page,
        'totalStudent': totalStudent,
        'totalPersonnel': totalPersonnel,
    }
    return render(request, 'SGdashboard.html', context)

def filter_stored_proc(request):
    if request.is_ajax() and request.method == 'POST':
        filter_value = request.POST.get('filter_value')

        with connection.cursor() as cursor:
            cursor.execute('CALL storedProc', ["Student"])
            result = cursor.fetchall()

        data = {'result': result}
        return JsonResponse(data)

    return JsonResponse({'error': 'Invalid request'})     
def profile(request):
    profile = Profile.objects.get(id=1)
    totalStudent = User.objects.filter(status=1,usertype = 'Student').count()
    totalPersonnel = User.objects.filter(status=1,usertype = 'School Personnel').count()
    item = FAQ.objects.all()
   
    context = {
        'profile' : profile,
        'totalStudent': totalStudent,
        'totalPersonnel': totalPersonnel,
        'item': item
    }
    return render(request, 'dashboard.html', context)

def updateProfile(request, schoolName,address):
    item = get_object_or_404(Profile,pk=1)
    item.schoolName = schoolName
    item.address = address
    item.save()
    return redirect('dashboard')

def updateMission(request, mission):
    item = get_object_or_404(Profile,pk=1)
    item.mission = mission
    item.save()
    return redirect('dashboard')

def updateVission(request, vission):
    item = get_object_or_404(Profile,pk=1)
    item.vission = vission
    item.save()
    return redirect('dashboard')

def addFAQ(request):
    forms = FAQForm()
    if request.method == 'POST':
        forms = FAQForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard')  
    else:
        forms = FAQForm()
    return render(request, 'dashboard.html', {'form': forms})

def updateFAQ(request, id,question, answer):

    item = get_object_or_404(FAQ,pk=id)
    
    item.question = question
    item.answer = answer
    item.save()
    return redirect('dashboard')

def delete_faq(request, id):
    item = get_object_or_404(FAQ,pk=id)
    item.delete()
    return redirect('dashboard')

def generate_qrcode(request):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=3,
    )
    data = 1
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white") 
    img = img.convert('RGBA')
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response

def addUser(request):
    forms = UserForm()
    if request.method == 'POST':
        forms = UserForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('home')  
    else:
        forms = UserForm()
    return render(request, 'home.html', {'form': forms})

def updateUser(request,pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        forms = UserForm(request.POST, instance=user)
        if forms.is_valid():
            forms.save()
            return redirect('home')  
  
    return render(request, 'home.html', {'form': forms})

def home(request):

    i = request.GET.get('i') if request.GET.get('i') != None else 42
    item = User.objects.filter(status=1, school_id = 1).order_by('-id')
    females = User.objects.filter(status=1, gender='female').count()
    male = User.objects.filter(status=1, gender='male').count()
    totalStudent = User.objects.filter(status=1,usertype = 'Student').count()
    totalPersonnel = User.objects.filter(status=1,usertype = 'School Personnel').count()
    page = Paginator(item, 6)
    page_list = request.GET.get('page','')
    page = page.get_page(page_list)

    context = {
        'item' : page,
        'female': females,
        'male': male,
        'totalStudent': totalStudent,
        'totalPersonnel': totalPersonnel
    }
    return render(request, 'home.html', context)

def delete_item(request, id):
    item = get_object_or_404(User,pk=id)
    item.status = 0
    item.save()
    return redirect('home')
  
def add_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = ItemForm()
    return render(request, 'home.html', {'form': form})

cursor = connection.cursor()
def userLogs(request):

    cursor.execute('CALL storedProcLogs')
    result = cursor.fetchall()
    profile = Profile.objects.get(id=1)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    item = Logs.objects.filter(remarks__icontains=q) 
    page = Paginator(result, 8)
    page_list = request.GET.get('page','')
    page = page.get_page(page_list)

    context = {
        'profile': profile,
        'result' : page,
        'items' : result
    }
    return render(request, 'userLogs.html', context)

def viewPage(request,userid,schoolid,logsid, hostid):

    userProfile = User.objects.get(id=userid)
    schoolProfile = Profile.objects.get(id=schoolid)
    logsProfile = Logs.objects.get(id=logsid)
    hostProfile = Profile.objects.get(id=hostid)

    context = {
        'userProfile' : userProfile,
        'schoolProfile' : schoolProfile,
        'logsProfile' : logsProfile,
        'hostProfile' : hostProfile
    }
    return render(request,'viewPage.html', context )

def modal(request ,id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'userLogs.html', {'item': item})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'myapp/item_detail.html', {'item': item})

# Add views for create, update, and delete operations
def generate_pdf(request):
    response = FileResponse(generate_pdf_file(), 
                            as_attachment=True, 
                            filename='book_catalog.pdf')
    return response
 
def generate_pdf_file():
   
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
 
    # Create a PDF document
    books = Logs.objects.all()
    p.drawString(100, 750, "Book Catalog")
 
    y = 700
    for book in books:
        p.drawString(100, y, f"Title: {book.date}")
        p.drawString(100, y - 20, f"Author: {book.time}")
        p.drawString(100, y - 40, f"Author: {book.id}")
        y -= 60
 
    p.showPage()
    p.save()
 
    buffer.seek(0)
    return buffer

class CrudView(TemplateView):
    template_name = 'crud.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = CrudUser.objects.all()
        return context

class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)