from django.shortcuts import render
from django.http import HttpResponse

from cerdoton_app.models import PigData, PigStatus

def index(request):
    pigs_list = PigData.objects.all()
    context = {'pigs_list': pigs_list}

    print ('Prueba' + str(PigData.objects.all()[0].pigstatus_set.all().count()))
    tst = PigData.objects.all()
    tststat = tst[0].pigstatus_set.all()
    print (str(tststat[0].weight))
    print (str(tststat[0].fat_percentage))
    print (str(tststat[0].total_body_water))
    print (str(tststat[0].kilocalories))

    return render(request, 'cerdoton_app/index.html', context)

def generalData(request, pig_id):
    return HttpResponse("You're looking at pig %s." % pig_id)

def status(request, pig_id):
    return HttpResponse("Details from pig %s." % pig_id)
