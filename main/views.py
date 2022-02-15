from django.shortcuts import render
# Create your views here.
from datetime import datetime, date
from django.http import HttpResponse

def getAge(request):


    date_ = request.GET.get('date', None)
    print(date_)
    date_ = date_[1:len(date_)-1]
    month = request.GET.get('month', None)
    month = month[1:len(month)-1]
    year = request.GET.get('year', None)
    year = year[1:len(year)-1]

   
    if int(date_) < 1 or int(date_) > 31:
        return HttpResponse("Incorrect Date")
        
    elif int(month)==2 and int(date_)>29:
        return HttpResponse("Incorrect Date")
        
    if len(str(year))!=4 or len(str(date_))!=2 or len(str(month))!=2:
        return HttpResponse("Incorrect Date Format")
        
    if int(month)<1 or int(month)>12: 
        return HttpResponse("Incorrect Month")

    

    try:    
        input_date = datetime(int(year), int(month), int(date_))
    except:
        return HttpResponse("Incorret Date Entered, If the entered month is February then maybe the problem is with Date")

    age = date.today().year - input_date.year - ((date.today().month, date.today().day) < (input_date.month, input_date.day))

    return HttpResponse("Your Age: "+str(age))



    