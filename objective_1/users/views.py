from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from . import items
from .info import Info
def index(request):
    return render(request, 'users/index.html')

def data_model(request):
    return render(request, 'users/data_model.html')

def list(request):    
    context = {'item_list':items.Item_Class.getItems()}
    return render(request, 'users/list.html', context)

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
    number_of_people=int(request.GET.get('number_of_people'))
    kilos=int(request.GET.get('kilos'))
    frequency_of_buying=int(request.GET.get('frequency_of_buying'))
    age=int(request.GET.get('age'))
    

    food_Waste= (kilos*frequency_of_buying)/(number_of_people)
    

    params = {'purpose': 'calculated food waste', 'analyzed_text': int(food_Waste)}

    return render(request,'users/CalculatorAnalyse.html',params)

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
