from django.contrib import admin
from second_app.models import AccessRecord, Topic, Webpage
# Register your models here.


admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)