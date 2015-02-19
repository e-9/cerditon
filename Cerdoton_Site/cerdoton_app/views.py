import json

from django.shortcuts import render
from django.http import HttpResponse

from cerdoton_app.models import PigData, PigStatus, MasterPig

def index(request):
    pigs_list = PigData.objects.all()
    context = {'pigs_list': masterPigList(pigs_list)}
    return render(request, 'cerdoton_app/index.html', context)

def generalData(request, pig_id):
    return HttpResponse("You're looking at pig %s." % pig_id)

def status(request, pig_id):
    return HttpResponse("Details from pig %s." % pig_id)

def graphData(request):

    if request.is_ajax():
        # do whatever processing you need
        # user.some_property = whatever

        # send back whatever properties you have updated
        json_response = {'user': {'some_property': 'Abraham :)'}}

        return HttpResponse(json.dumps(json_response),
            content_type='application/json')

    return render(request, 'index.html', {'user': ''})



def diffStatus(a, b):
    return a - b

def masterPigList(pigs_list):
    result = []

    for pig in pigs_list:
        master_pig = MasterPig()
        pig_status = pig.pigstatus_set.all()
        cnt = pig_status.count()

        master_pig.name = pig.Name
        master_pig.age = pig.Age
        master_pig.height = pig.Height

        if cnt > 0:
            master_pig.weight = pig_status[cnt-1].weight
            master_pig.fat_percentage = pig_status[cnt-1].fat_percentage
            master_pig.total_body_water = pig_status[cnt-1].total_body_water
            master_pig.body_mass_index = pig_status[cnt-1].body_mass_index
            master_pig.bone_percentage = pig_status[cnt-1].bone_percentage
            master_pig.muscle_percentage = pig_status[cnt-1].muscle_percentage
            master_pig.kilocalories = pig_status[cnt-1].kilocalories
            master_pig.week = pig_status[cnt-1].week

        if cnt > 1:
            stst2 = pig_status[cnt-2]
            stst1 = pig_status[cnt-1]
            master_pig.weight_diff = diffStatus(stst2.weight, stst1.weight)
            master_pig.fat_percentage_diff = diffStatus(stst2.fat_percentage, stst1.fat_percentage)
            master_pig.total_body_water_diff = diffStatus(stst2.total_body_water, stst1.total_body_water)
            master_pig.body_mass_index_diff = diffStatus(stst2.body_mass_index, stst1.body_mass_index)
            master_pig.bone_percentage_diff = diffStatus(stst2.bone_percentage, stst1.bone_percentage)
            master_pig.muscle_percentage_diff = diffStatus(stst2.muscle_percentage, stst1.muscle_percentage)
            master_pig.kilocalories_diff = diffStatus(stst2.kilocalories, stst1.kilocalories)

        result.append(master_pig)

    return result
