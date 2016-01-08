from django.contrib import admin
from .models import PCR_Polymerase
from .forms import PCR_PolymeraseForm
# Register your models here.
class PCR_PolymeraseAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "name", "price", "unit", "category", "factory", "lifetime", "pro_date"]
	form = PCR_PolymeraseForm
admin.site.register(PCR_Polymerase, PCR_PolymeraseAdmin)