from django.shortcuts import render
from django.http import HttpResponse

from cerdoton_app.models import PigData, PigStatus

def index(request):
    pigs_list = PigData.objects.all()
    context = {'pigs_list': pigs_list}
    return render(request, 'cerdoton_app/index.html', context)

def generalData(request, pig_id):
    return HttpResponse("You're looking at pig %s." % pig_id)

def status(request, pig_id):
    return HttpResponse("Details from pig %s." % pig_id)
