from django.shortcuts import render
from crud_application.models import *
from crud_application.models.ViewModels.ViewModels import *
from crud_application.models.Resturant import *
from django.shortcuts import redirect


def index(request):
    data = Branches.objects.all()

    context = {
        'title': 'اطلاعات کامل از موجودیت ها',
        'data': data,
        'statusCode': 200
    }

    return render(request, 'Views/index.html', context)


def addPage(request):
    return render(request, 'Views/addPage.html')


def addPagePost(request):
    restur = Resturant()
    restur.resturantName = request.POST['resturantName']
    restur.startCount = request.POST['starCount']
    restur.managerFullName = request.POST['managerFullName']
    restur.save()

    # branch = Branches()
    # branch.cityName = request.POST['cityName']
    # branch.countryName = request.POST['countryName']
    # branch.fullAddress = request.POST['fullAddress']
    # branch.streetName = request.POST['streetName']
    # branch.resturantId = restur
    # branch.save()
    return redirect(index)


def addBranches(request):
    resturants = Resturant.objects.all()

    context = {
        'title': 'اضافه کردن شعبه',
        'allResturant': resturants,
        'statusTest': 'success'
    }
    return render(request, 'Views/addBranch.html', context)


def insertBranch(request):
    branch = Branches()
    branch.streetName = request.POST['streetName']
    branch.cityName = request.POST['cityName']
    branch.countryName = request.POST['countryName']
    branch.fullAddress = request.POST['fullAddress']
    rest =Resturant.objects.get(pk=request.POST['resturantID'])
    branch.resturantId = rest
    branch.resturantId_id = rest.id
    branch.save()
    return redirect(index)


def updatePage(request, id):
    data = Branches.objects.select_related('resturantId').get(pk=id)
    branchList = Branches.objects.all()

    context = {
        'data': data,
        'branchList': branchList,
        'title': 'ویرایش',
        'statusTest': 'success'
    }
    return render(request, 'Views/updatePage.html', context)


def updatePagePost(request):
    res = Resturant.objects.get(pk=request.POST['restId'])
    brch = Branches.objects.get(pk=request.POST['branchId'])

    res.resturantName = request.POST['resturantName']
    res.startCount = request.POST['starCount']
    res.managerFullName = request.POST['managerFullName']
    res.save()

    brch.streetName = request.POST['streetName']
    brch.countryName = request.POST['countryName']
    brch.fullAddress = request.POST['fullAddress']
    brch.cityName = request.POST['cityName']
    brch.save()

    return redirect(index)


def delete(request, id):
    data = Branches.objects.get(pk=id).delete()
    return redirect(index)