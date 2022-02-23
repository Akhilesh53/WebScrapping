import bs4
from django.contrib import admin
from .models import BsModel,SeleniumModel,ScrapModel
# Register your models here.

admin.site.register(BsModel)
admin.site.register(SeleniumModel)
# admin.site.register(CamelotModel)
admin.site.register(ScrapModel)



