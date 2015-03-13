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

def graphDataFat(request):

    if request.is_ajax():

        response_list = []
        pigs_list = PigData.objects.all()

        for pig in pigs_list:

            response_data = {}
            response_data['label'] = pig.Name
            response_data['fillColor'] = colorGraph(pig.Name)[0]
            response_data['strokeColor'] = colorGraph(pig.Name)[1]
            response_data['pointColor'] = colorGraph(pig.Name)[0]
            response_data['pointStrokeColor'] = '#fff'
            response_data['pointHighlightFill'] = '#fff'
            response_data['pointHighlightStroke'] = colorGraph(pig.Name)[0]

            fat = []
            pig_status = pig.pigstatus_set.all()
            for ps in pig_status:
                fat.append(ps.fat_percentage)

            response_data['data'] = fat

            response_list.append(response_data)

        return HttpResponse(json.dumps(response_list),
            content_type='application/json')

    return render(request, 'index.html', {'user': ''})

def graphDataWeight(request):

    if request.is_ajax():

        response_list = []
        pigs_list = PigData.objects.all()

        for pig in pigs_list:

            response_data = {}
            response_data['label'] = pig.Name
            response_data['fillColor'] = colorGraph(pig.Name)[0]
            response_data['strokeColor'] = colorGraph(pig.Name)[1]
            response_data['pointColor'] = colorGraph(pig.Name)[0]
            response_data['pointStrokeColor'] = '#fff'
            response_data['pointHighlightFill'] = '#fff'
            response_data['pointHighlightStroke'] = colorGraph(pig.Name)[0]

            wght = []
            pig_status = pig.pigstatus_set.all()
            for ps in pig_status:
                wght.append(ps.weight)

            response_data['data'] = wght

            response_list.append(response_data)

        return HttpResponse(json.dumps(response_list),
            content_type='application/json')

    return render(request, 'index.html', {'user': ''})

def graphDataMuscle(request):

    if request.is_ajax():

        response_list = []
        pigs_list = PigData.objects.all()

        for pig in pigs_list:

            response_data = {}
            response_data['label'] = pig.Name
            response_data['fillColor'] = colorGraph(pig.Name)[0]
            response_data['strokeColor'] = colorGraph(pig.Name)[1]
            response_data['pointColor'] = colorGraph(pig.Name)[0]
            response_data['pointStrokeColor'] = '#fff'
            response_data['pointHighlightFill'] = '#fff'
            response_data['pointHighlightStroke'] = colorGraph(pig.Name)[0]

            mscl = []
            pig_status = pig.pigstatus_set.all()
            for ps in pig_status:
                mscl.append(ps.body_mass_index)

            response_data['data'] = mscl

            response_list.append(response_data)

        return HttpResponse(json.dumps(response_list),
            content_type='application/json')

    return render(request, 'index.html', {'user': ''})


def colorGraph(name):
    if name == 'Emma':
        return ['rgba(255, 102, 187, 0.9)', 'rgba(255, 102, 187, 1)']
    elif name == 'Miguel':
        return ['rgba(231, 193, 137, 0.8)', 'rgba(231, 193, 137, 1)']
    elif name == 'Abraham':
        return ['rgba(35, 76, 141, 0.8)', 'rgba(35, 76, 141, 1)']
    elif name == 'Israel':
        return ['rgba(0, 117, 0, 0.9)', 'rgba(0, 117, 0, 1)']
    elif name == 'Mario':
        return ['rgba(243, 202, 7, 0.9)', 'rgba(243, 202, 7, 1)']
    elif name == 'Guillermo':
        return ['rgba(0, 70, 255, 0.9)', 'rgba(0, 70, 255, 1)']
    elif name == 'David':
        return ['rgba(70, 225, 39, 0.9)', 'rgba(70, 225, 39, 1)']
    elif name == 'Alejandra':
        return ['rgba(235, 103, 41, 0.9)', 'rgba(235, 103, 41, 1)']
    elif name == 'Yosadara':
        return ['rgba(139, 20, 76, 0.9)', 'rgba(139, 20, 76, 1)']
    elif name == 'Erick':
        return ['rgba(251, 36, 11, 0.9)', 'rgba(251, 36, 11, 1)']

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

        scores = getScores(pig)
        master_pig.thumbs_up += scores[0]
        master_pig.thumbs_down += scores[1]

        if cnt > 0:
            master_pig.ideal = pig_status[0].ideal_weight
            master_pig.weight = pig_status[cnt-1].weight
            master_pig.fat_percentage = pig_status[cnt-1].fat_percentage
            master_pig.total_body_water = pig_status[cnt-1].total_body_water
            master_pig.body_mass_index = pig_status[cnt-1].body_mass_index
            master_pig.bone_percentage = pig_status[cnt-1].bone_percentage
            master_pig.muscle_percentage = pig_status[cnt-1].muscle_percentage
            master_pig.kilocalories = pig_status[cnt-1].kilocalories
            master_pig.week = pig_status[cnt-1].week

        if cnt > 1:
            stst1 = pig_status[cnt-2]
            stst2 = pig_status[cnt-1]
            master_pig.weight_diff = diffStatus(stst2.weight, stst1.weight)
            master_pig.fat_percentage_diff = diffStatus(stst2.fat_percentage, stst1.fat_percentage)
            master_pig.total_body_water_diff = diffStatus(stst2.total_body_water, stst1.total_body_water)
            master_pig.body_mass_index_diff = diffStatus(stst2.body_mass_index, stst1.body_mass_index)
            master_pig.bone_percentage_diff = diffStatus(stst2.bone_percentage, stst1.bone_percentage)
            master_pig.muscle_percentage_diff = diffStatus(stst2.muscle_percentage, stst1.muscle_percentage)
            master_pig.kilocalories_diff = diffStatus(stst2.kilocalories, stst1.kilocalories)

        result.append(master_pig)

    return sorted(result, key=getKey)

def getKey(master_pig):
    return master_pig.name

def getThumbsUp(master_pig):
    return master_pig.thumbs_up

def getThumbsDown(master_pig):
    return master_pig.thumbs_down

def score(request):
    if request.is_ajax():

        response_list = []
        sort_me = []
        pigs_list = PigData.objects.all()

        for pig in pigs_list:
            master_pig = MasterPig()
            master_pig.name = pig.Name

            scores = getScores(pig)
            master_pig.thumbs_up += scores[0]
            master_pig.thumbs_down += scores[1]

            sort_me.append(master_pig)

        sortedThumbsUp = sorted(sort_me, key=getThumbsUp, reverse=True)
        for i in xrange(0,3):
            response_data = {}
            response_data['name'] = sortedThumbsUp[i].name
            response_data['up'] = sortedThumbsUp[i].thumbs_up
            response_list.append(response_data)

        sortedThumbsDown = sorted(sort_me, key=getThumbsDown, reverse=True)
        for i in xrange(0,3):
            response_data_down = {}
            response_data_down['name'] = sortedThumbsDown[i].name
            response_data_down['down'] = sortedThumbsDown[i].thumbs_down
            response_list.append(response_data_down)

        return HttpResponse(json.dumps(response_list),
            content_type='application/json')

    return render(request, 'index.html', {'user': ''})

def getScores(pig):
    pig_scores = pig.pigscore_set.all()
    thumbs_up = 0
    thumbs_down = 0

    for score in pig_scores:
        thumbs_up += score.thumbs_up
        thumbs_down += score.thumbs_down

    return [thumbs_up-thumbs_down, thumbs_down]
