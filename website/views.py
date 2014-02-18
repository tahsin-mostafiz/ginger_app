from django.db.models import Count
from django.shortcuts import render_to_response
from django.template import RequestContext
from website.models import FoodTruck
from website.external import FacebookAPI

def get_foodtrucks(request):
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

def update_foodtrucks(request):
  fb = FacebookAPI()
  fb_json = fb.get_facebook_json()
  
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

def post_message():
  fb = FacebookAPI()
  foodtrucks = FoodTruck.objects.filter(
    location = '410 Minna St, San Francisco')
  for ft in foodtrucks:
    context = {
      'name': ft.name,
      'location':ft.location,
      'start_date': ft.start_date, 
      'start_time': ft.start_time,
      }
    fb.post_to_hipchat(context)




