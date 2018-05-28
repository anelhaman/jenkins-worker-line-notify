#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# const critical_StickerPkg = 2;
# const critical_StickerId = 39;
# const information_StickerPkg = 2;
# const information_StickerId = 34;

import requests

url = 'https://notify-api.line.me/api/notify'
token = 'Lb3PxUO8qc5olGmWSCoBagq1W5ZATViiX5fyotZ0nWh'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

#msg = 'Successfully Build http://www.prachindaily.com'
msg = 'Error Build, Please re-checking again!'

mydata = {
  'stickerPackageId': 2,
  'stickerId': 39,
  'message': msg,
  }

r = requests.post(url, headers=headers , data =mydata )
print r.text
