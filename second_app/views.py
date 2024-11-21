from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import AccessRecord, Topic, Webpage

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    my_dict={'access_records':webpages_list}
    return render(request,'second_app/index.html',context=my_dict)
