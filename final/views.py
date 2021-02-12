from datetime import datetime,timedelta


from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.views.generic import View
from django.utils.crypto import get_random_string
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q,F
from django.contrib.auth import logout
from django.utils.crypto import get_random_string
from django.core.paginator import Paginator
from django.http import JsonResponse


from .models import single_sweet, weight_sweet



class IndexPage(View):
    def get(self, request,  **kwargs):        
        return render(request, 'index.html')

def single_sweets(request):
    all_single_product = single_sweet.objects.all()
    context = {}
    context['all_single'] = all_single_product
    return render(request, 'single.html', context)

def single_sweets_detail(request, single_product_slug):
    selected_product = single_sweet.objects.get(single_product_slug = single_product_slug)
    context = {}
    context['single_product'] = selected_product
    return render(request, 'single-detail.html', context)


def weight_sweets(request):
	all_weight_product = weight_sweet.objects.all()
	context = {}
	context['all_weight'] = all_weight_product
	return render(request,'weight.html', context)

def weight_sweets_detail(request, product_slug):
    selected_weight = weight_sweet.objects.get(product_slug = product_slug)
    context = {}
    context['selected_weight'] = selected_weight
    return render(request,'weight-detail.html', context)

def about(request):
    return render(request,'about.html')