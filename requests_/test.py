import requests
import json

url='http://oa.oppein.com'
my_headers={
    "user-agent":"requests",
    "imooc_uid":"321"
}
res=requests.post(url,data=json.dumps(my_headers))
print(res.headers)
print(res.status_code)