from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
def home(request):
	return render(request, "base.html", {})
def polymerase(request):
	title = "Product details"
	form = PCR_Polymerase.objects.all()
	title_align_center = True
	context = {
		"title": title,
		"form": form,
		"title_align_center": title_align_center
	}
	return render(request, "product_result.html", context)

def benchtop(request):
	title = "Product details"
	form = BenchTop.objects.all()
	title_align_center = True
	context = {
		"title": title,
		"form": form,
		"title_align_center": title_align_center
	}
	return render(request, "product_result.html", context)
