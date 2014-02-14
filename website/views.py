from django.db.models import Count
from django.shortcuts import render_to_response
from django.template import RequestContext
from website.models import FoodTruck

def foodtrucks(request):
  foodtrucks = FoodTruck.objects. \
    values_list('name'). \
    annotate(truck_count=Count('name')). \
    order_by('-truck_count')
  context = {
    'foodtrucks': foodtrucks,
  }
  return render_to_response(
    'website/foodtruck.html',
    context,
    context_instance = RequestContext(request),
  )
