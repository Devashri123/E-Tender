from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import requires_csrf_token
from django.utils.timezone import datetime 


from django_ajax.decorators import ajax


from .models import CurrentUser
from .models import Vendor
from .models import Buyer
from .models import TenderInfo

# Create your views here.






def index(request):
    return HttpResponse("Welcome , You're at tenderApp.")
def demo(request):
    tenderList = TenderInfo.objects.filter(tender_deadline__gte = datetime.today())
    tenderList1 = TenderInfo.objects.filter(tender_deadline__lt = datetime.today())
    return render(request,'tenderApp/homepagedemo.html',{ 'tenderList':tenderList, 'tenderList1':tenderList1})
    
    


    
    
def homepage(request):
    return render(request, 'tenderApp/homepage.html',{})
def about(request):
    return render(request, 'tenderApp/about.html',{})
def contact(request):
    return render(request, 'tenderApp/contact.html',{})
def help(request):
    return render(request, 'tenderApp/help.html',{})
def services(request):
    return render(request, 'tenderApp/services.html',{})

def openTenders(request):
    tenderList = TenderInfo.objects.filter(tender_deadline__gte = datetime.today())
    return render(request,'tenderApp/homepagedemo.html',{ 'tenderList':tenderList})
    
def closedTenders(request):
    tenderList = TenderInfo.objects.filter(tender_deadline__lt = datetime.today())
    return render(request,'tenderApp/opentenders.html',{ 'tenderList':tenderList})
    
    

def login(request):     
     return render(request,'tenderApp/login.html',{})

def validate_login(request):
     user=CurrentUser.objects.get(user_email=request.POST['username'])
     if user.user_password == request.POST['password']:
        request.session['username']=request.POST['username']
        return render(request,'tenderApp/dashboard.html',{'full_name':user.user_email})
     else:
        return HttpResponse("Your credentials did not match...")
    

def logout(request):
    try:
       del request.session['username']
    except KeyError:
              pass
    return render(request,'tenderApp/homepage.html',{})




   

def create_buyer(request):
    if request.method == 'POST':
            name = request.POST['name'] 
            address = request.POST['address'] 
            regNo = request.POST['regNo']  
            contactNo= request.POST['contactNo']  
            email = request.POST['email']        
            password = request.POST['password']
            CurrentUser.objects.create(user_email=email,user_password=password)         
            Buyer.objects.create( buyer_name=name,buyer_address=address,buyer_regNo=regNo,buyer_contactNo=contactNo,buyer_email=email,buyer_password=password)
            
    #Get goes here
           
    return HttpResponseRedirect('/tenderApp/login')


def create_vendor(request):
    if request.method == 'POST':
            name = request.POST['name'] 
            address = request.POST['address'] 
            contactNo= request.POST['contactNo']  
            email = request.POST['email']        
            password = request.POST['password']
            CurrentUser.objects.create(user_email=email,user_password=password)         
            Vendor.objects.create( vendor_name=name,vendor_address=address,vendor_contactNo=contactNo,vendor_email=email,vendor_password=password)
            
    #Get goes here
           
    return HttpResponseRedirect('/tenderApp/login')

def vendorSignup(request):
     return render(request, 'tenderApp/vendorSignUp.html',{})
def buyerSignup(request):
     return render(request, 'tenderApp/buyerSignUp.html',{})


def vendorDashboard(request):
    return HttpResponse("vendorDashboard")
def allocatedTenders(request):
    return HttpResponse("allocatedTenders")

def appliedTenders(request):
    return HttpResponse("appliedTenders")




def buyerDashboard(request):
    return HttpResponse("buyerDashboard")
def createTender(request):
    return HttpResponse("createTender")
def trackTender(request):
    return HttpResponse("trackTender")


def hello(request):
    text="""<h1>HELLO!!!</h1>"""
    return HttpResponse(text)

def sample(request):
    return render(request, 'tenderApp/sample.html', {})

def display_details(request,vendor_id):
    return HttpResponse("<h2>Details for id :" + str(vendor_id) + "</h2>")

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'tenderApp/vendor_list.html', {'vendors': vendors})

def buyer_list(request):
    buyers = Buyer.objects.all()
    return render(request, 'tenderApp/buyer_list.html', {'buyers': buyers})

def add(request):
   #Creating an entry
   
   v = Vendor(
      vendor_name="Syntel",vendor_email="syntel@gmail.com",vendor_password="syntel@123",
      vendor_address="Hydrabad",vendor_contactNo=678
   )
   
   v.save()
   b = Buyer(
      buyer_name="Toshiba",buyer_email="toshiba@gmail.com",buyer_password="toshiba@123",
      buyer_address="Japan",buyer_contactNo=125
   )
   
   b.save()
    

   return HttpResponse("New Vendor and buyer created successfully ")



def read_vendor(request):
   #Read ALL entries
   objects = Vendor.objects.all()
   result ='Printing all Vendor entries in the DB : <br>'
   
   for vendor in objects:
      result += vendor.vendor_name+" "+vendor.vendor_email+" "+vendor.vendor_address+"<br>"

   return HttpResponse(result)

def read_buyer(request):
   #Read ALL entries
   objects = Buyer.objects.all()
   result ='Printing all Buyer entries in the DB : <br>'
   
   for buyer in objects:
      result += buyer.buyer_name+" "+buyer.buyer_email+" "+buyer.buyer_address+"<br>"

   return HttpResponse(result)

def delete(request):
   read_vendor = Vendor.objects.get(vendor_name="Syntel")
   result = 'Printing the  vendor entry to be deleted <br>'
   result += read_vendor.vendor_name

   #Delete an entry
   result += '<br> Deleting entry... <br>'
   read_vendor.delete()

   read_buyer = Buyer.objects.get(buyer_name="Toshiba")
   result += 'Printing the  buyer entry to be deleted <br>'
   result += read_buyer.buyer_name

   #Delete an entry
   result += '<br> Deleting entry... <br>'
   read_buyer.delete()
   return HttpResponse(result)

def update(request):
   
   #Update
   v = Vendor(
      vendor_name="Syntel",vendor_email="syntel@gmail.com",vendor_password="syntel@123",
      vendor_address="Hydrabad",vendor_contactNo=678
   )
   v.save()
   result = 'Updating entry<br>'
   
   v= Vendor.objects.get(vendor_address = 'Hydrabad')
   v.vendor_address= 'Pune'
   v.save()
   objects = Vendor.objects.all()
   result +='Updated Vendor details : <br>'
   
   for vendor in objects:
      result += vendor.vendor_name+" "+vendor.vendor_email+" "+vendor.vendor_address+"<br>"

   return HttpResponse(result)
   

  
   
  

    
   

 




