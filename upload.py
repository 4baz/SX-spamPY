import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

import globals

def user_upload(file):



    imgdata = MultipartEncoder(

        fields={
            'password':globals.passwd,
            'image': (file, open(file, 'rb'), globals.mime)

            }


    )

    p = requests.post(globals.url, data=imgdata,
                  headers={'Content-Type': imgdata.content_type})
    print(p.status_code)

    p.raise_for_status()

  #  print(p.content.decode())

    return p.content.decode()
