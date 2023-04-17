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
    return render(request, 'users/list.html')
    


# Old Item Pages (We should delete the commented out section)

#def facts(request):
 #   return HttpResponse(loader.get_template('users/facts.html').render())

#def reasons(request):
    #return HttpResponse(loader.get_template('users/reasons.html').render())

#def benefits(request):
 #   return HttpResponse(loader.get_template('users/benefits.html').render())

#def solutions(request):
 #   return HttpResponse(loader.get_template('users/solutions.html').render())

#def resources(request):
 #   return HttpResponse(loader.get_template('users/resources.html').render())

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
    Waste.append(str(Info("Perth",3000,"2000 People")))
    Waste.append(str(Info("Melbourne",54000,"100000 People")))
    Waste.append(str(Info("Sydney",58000,"120000 People")))
    Waste.append(str(Info("Darwin",2322,"1200 People")))
    
    return Waste
    
# class Info:
#     def __init__(self,city,wastage,impact):
#         self.city = city
#         self.wastage = wastage
#         self.impact =impact
#     def __str__(self):

#         return str(self.city) + ", " + str(self.wastage) + ", " + str(self.impact)
    
def wastage(request):
    context={
        'var':create_wastage()
    }
    return render(request,'users/data_model.html',context)