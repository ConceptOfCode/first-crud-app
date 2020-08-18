from django.shortcuts import redirect
from django.shortcuts import render
from crud_application.models.Equipments import *
from django.http import JsonResponse


def index(request):
    data = Equip.objects.select_related('Factory')
    context = {
        'data': data,
        'title': 'لیست تجهیزات'
    }
    return render(request, 'Views/indexView.html', context)


def renderEquAdd(request):
    factories = Factories.objects.all()
    context = {
        'data': factories,
        'title': 'اضافه کردن قطعه'
    }
    return render(request, 'Views/addEquView.html', context)


def addEqu(request):
    equ = Equip()
    postData = request.POST
    equ.equipName = postData['equipName']
    equ.equipVolt = postData['equipVolt']
    equ.equipNo = postData['equipNo']
    if 'equipStatus' in postData:
        equ.equipStatus = 2
    else:
        equ.equipStatus = 1
    currentFactory = Factories.objects.get(pk=postData['factoryId'])
    equ.Factory = currentFactory

    equ.save()
    return redirect(index)


def renderUpdate(request, equID):
    data = Equip.objects.get(pk=equID)
    factoryList = Factories.objects.all()
    context = {
        'data': data,
        'factories': factoryList,
        'title': 'ویرایش محصئل'
    }
    return render(request, 'Views/updateEquView.html', context)


def update(request):
    equ = Equip.objects.get(pk=request.POST['equID'])
    postData = request.POST
    equ.equipName = postData['equipName']
    equ.equipVolt = postData['equipVolt']
    equ.equipNo = postData['equipNo']
    if 'equipStatus' in postData:
        equ.equipStatus = 2
    else:
        equ.equipStatus = 1
    currentFactory = Factories.objects.get(pk=postData['factoryId'])
    equ.Factory = currentFactory

    equ.save()
    return redirect(index)


def delete(request, equID):
    data = Equip.objects.get(pk=equID)
    data.delete()
    return redirect(index)


def retriveDataTest(request):
    # for javaScript you must convert Query to list for own Django you don`t need to convert to list
    data = list(Equip.objects.all().select_related('Factory')
                .values_list('equipName', 'equipNo', 'equipVolt',
                             'Factory__factoryName', 'Factory__factoryAddress',
                             'Factory__factoryManagerFullName'))

    response = {'statusCode': 200, 'data': data}
    return JsonResponse(response)
