from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, reverse
from . import items
from django.contrib.auth import authenticate, login, logout
from .info import Info
from audit.models import WasteItems

def index(request):
    return render(request, 'users/index.html')

def invalid(request, invalid):
    return render(request, 'users/notfound.html')

def data_model(request):
    return render(request, 'users/data_model.html')


    

def header(request):
    return render(request, 'header.html',{})

def footer(request):
    return render(request, 'footer.html',{})
    


# Old Item Pages (We should delete the commented out section)

def impacts(request):
   return HttpResponse(loader.get_template('users/facts.html').render())

def Calindex(request):
    return render(request, 'users/CalculateForm.html')
def calculator(request):
    try:
        number_of_people=int(request.GET.get('number_of_people'))
        kilos=int(request.GET.get('kilos'))
        frequency_of_buying=int(request.GET.get('frequency_of_buying'))
        age=int(request.GET.get('age'))
        

        food_Waste= (kilos*frequency_of_buying)/(number_of_people)
        if food_Waste<5:


            params = {'purpose': 'calculated food waste', 'analyzed_text': int(food_Waste)}

            return render(request,'users/CalculatorAnalyse.html',params)
        else:
            params = {'purpose': 'calculated food waste', 'analyzed_text': int(food_Waste)}
            return render(request,'users/CalculatorAnalyse1.html',params)
            
    except: 
        return render(render, "users/notfound.html")

# New function to handle item url lookup
# Details
def detail(request, id):
    page = 'users/details.html'
    try:
        context = {'item':items.Item_Class.find(id)}
        #page = "users/{}.html".format(id)
    except:
        context = {}
        page = "users/notfound.html"
    return render(request, page, context)



def create_wastage():
    Waste=[]
    Waste.append((Info("Perth",3000,"2000 People")))
    Waste.append((Info("Melbourne",54000,"100000 People")))
    Waste.append((Info("Sydney",58000,"120000 People")))
    Waste.append((Info("Darwin",2322,"1200 People")))
    
    return Waste
    

    
def wastage(request):
    context={
        'var':create_wastage()
    }
    return render(request,'users/data_model.html',context)

def wastelist(request):
    wastelist= WasteCollection.objects.all()

    return render(request, 'users/wastelist.html', {'wastelist': wastelist})


def LoginView(request):
    login = reverse("audit:login")
    return redirect(login)
    
def LogoutView(request):
    logout = reverse("audit:logout")
    return redirect(logout)

def Signup(request):
    return render(request, 'users/signup.html',{})

def welcome(request):
    users = Users.objects.all()
    
    context = {
        'users': users,
    }

    return render(request, 'users/welcome.html', context)
