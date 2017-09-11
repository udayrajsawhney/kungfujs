from django.http import HttpResponse
from django.template import loader
from .models import MacroSensor,addPlant
from django.views.decorators.csrf import csrf_exempt

def index(request):
    all_plants = addPlant.objects.all()
    template = loader.get_template('sensors/index.html')
    context ={
        'all_plants':all_plants,
    }
    return HttpResponse(template.render(context,request))

def detailMacro(request):
    macrosensors=MacroSensor.objects.all()
    template = loader.get_template('sensors/macro.html')
    context={
        'macrosensors':macrosensors,
    }
    return HttpResponse(template.render(context,request))

def detailMacrosingle(request):
    macrosensors= MacroSensor.objects.latest('id')
    a = list()
    a.append(macrosensors)
    print (a)
    template = loader.get_template('sensors/macro.html')
    context={
        'macrosensors':a,
    }
    return HttpResponse(template.render(context,request))

def detailMicro(request):
    microsensors=addPlant.objects.all()
    template = loader.get_template('sensors/micro.html')
    context = {
        'microsensors': microsensors,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def add_reading(request):
    if request.POST.get('watL'):
        new_reading = MacroSensor()
        new_reading.Temperature = request.POST.get('temp')
        new_reading.Humidity = request.POST.get('hum')
        new_reading.WaterLevel = request.POST.get('watL')
        new_reading.save()

        return HttpResponse(status=200)

    return  HttpResponse(status=400)