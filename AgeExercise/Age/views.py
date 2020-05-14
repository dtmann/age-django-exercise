from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person
from datetime import date, datetime
from .forms import NewPersonForm
# Create your views here.

def main(request, action=None):
    #return HttpResponse(action)
    person_added = False
    if request.method == "POST":
        f = NewPersonForm(request.POST)
        if f.is_valid():
            f.save()
            person_added = True
    all_people = Person.objects.all()
    form = NewPersonForm()
    data = []
    deleted_data = []
    for person in all_people:
        formatted_date = datetime.strptime(str(person.dob), "%Y-%m-%d")
        age_years = int((datetime.now() - formatted_date).days)//365
        age_days = (datetime.now() - formatted_date).days
        age_hours = int(age_days) * 24
        person_data = {"id" : person.id,
                        "name": person.name,
                        "dob": person.dob,
                        "age_y": age_years,
                        "age_d": age_days,
                        "age_h": age_hours}
        if person.deleted == 0:
            data.append(person_data)
        else:
            deleted_data.append(person_data)
    return render(request = request, 
                    template_name = 'Age\main.html',
                    context = {"person" : data,
                                "person_d": deleted_data,
                                "form" : form,
                                "action" : person_added})

def delete(request):
    if request.method == "POST":
        delete_id = request.POST['did']
        if delete_id:
            d = Person.objects.get(id=delete_id)
            d.deleted = 1
            d.save()
    return HttpResponseRedirect("/", True)

def undelete(request):
    if request.method == "POST":
        delete_id = request.POST['did']
        if delete_id:
            d = Person.objects.get(id=delete_id)
            d.deleted = 0
            d.save()
    return HttpResponseRedirect("/")

def update(request):
    pass