import datetime

from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
# ^^ asking if the statment is true so it can go to newyear/index.html and run the function 
    })