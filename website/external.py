import re, requests
from itertools import ifilter
from website.models import FoodTruck

class FacebookAPI():

  def __init__(self):
    # make these configurable variables
    self.base_fb_url = "https://graph.facebook.com/"
    self.access_token = "1402112503380749|mBrN1URv2GedZPmlOOFpf2-dciQ"
    self.base_hc_url = 'https://api.hipchat.com/v1/rooms/message'
    self.hc_token = '4c1f7738d7462393c8f628e7ed17a6'
    self.hc_room_id = '425050'
    self.default_from_addr = 'New Intern'
    

  def get_facebook_json(self, id = None):
    if not id:
      id = "OffTheGridSF/events/"
    url = self.base_fb_url + id
    params = {'access_token': self.access_token}
    result = requests.get(url, params=params)
    if result.status_code == 200:
      results = result.json().get('data', [])
      if results:
        for ids in results:
          self.get_facebook_json(ids['id'])
      else:
        vendors = _parse_description_string(
                        result.json(). \
                        get('description', []))
        location = result.json().get('location')
        temp = result.json().get('start_time').split("T")
        start_date = temp[0]
        start_time = temp[1][:8]
        if vendors:
            for ven in vendors:
                if ven.strip() != '':
                    foodtruck = FoodTruck(name = ven.strip(),
                                          location = location, 
                                          start_date = start_date, 
                                          start_time = start_time)
                    foodtruck.save()

  def post_to_hipchat(self, msg, from_addr = None):
      if not from_addr:
          from_addr = self.default_from_addr
      pass

def _parse_description_string(desc = None):
  if desc:
    desc_match = re.search(r'''(?sx)
         Vendors:(?P<vendors>.+?)(?:\n\r?){2}''', desc)
    if desc_match:
        temp = desc_match.group('vendors')
        return list(ifilter(None, 
                            re.split(r'(\s*\n|\r)+', 
                                     temp.strip())))

