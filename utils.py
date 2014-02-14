from django.conf import settings
import simplejson as json
import re, requests

class FacebookAPI():

  def __init__(self):
    self.base_url = "https://graph.facebook.com/"
    self.access_token = "1402112503380749|mBrN1URv2GedZPmlOOFpf2-dciQ"

  def get_facebook_json(self, id = None):
    if not id:
      id = "OffTheGridSF/events/"

    url = self.base_url + id 
    params = {'access_token': self.access_token}
    result = requests.get(url, params=params)
    if result.status_code == 200:
      results = result.json().get('data', [])
      if results:
        for ids in results:
          self.get_facebook_json(ids['id'])
      else:
        parse_description_string(result.json().get('description', []))

def parse_description_string(desc = None):
  if desc:
    desc_match = re.search(r'''(?sx) 
          (?P<loc>Location:.+?)[\n\r]
          (?P<time>Time:.+?)[\n\r]
          (?P<vendors>Vendors:.+?)(?:\n\r?){2}''', desc)
    if desc_match:
      for gname in ['loc', 'time', 'vendors']:
        temp = desc_match.group(gname).splitlines()
        for val in temp[0].split(":", 1)[1:]:
          print val

if __name__ == '__main__':
    fb = FacebookAPI()
    fb.get_facebook_json()
