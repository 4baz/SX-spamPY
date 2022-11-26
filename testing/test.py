import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

fname = "test.png"

imgdata = MultipartEncoder(

        fields={
            'password':'',
            'image': (fname, open(fname, 'rb'), 'application/octet-stream')

            }


)
r = requests.post('urlhere', data=imgdata,
                  headers={'Content-Type': imgdata.content_type})

print(r)
