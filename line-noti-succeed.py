#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# const critical_StickerPkg = 2;
# const critical_StickerId = 39;
# const information_StickerPkg = 2;
# const information_StickerId = 34;

import requests
import time

url = 'https://notify-api.line.me/api/notify'
token = '5yAHpkG0sZXhtN7sFSlMJ8SZX1zyaF8VlOeO81ZUhNN'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

time = time.strftime("%c") 
msg = 'Successfully Build https://www.dohome.co.th/ '+ time
# msg = 'Error Build, Please re-checking again!'

mydata = {
#   'stickerPackageId': 1,
#   'stickerId': 403,
  'message': msg,
  }

r = requests.post(url, headers=headers , data =mydata )
print r.text
