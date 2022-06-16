# -*- coding: utf-8 -*-

import logging
import qrcode
import base64
import io
from urllib.parse import parse_qs

TEMPLATE = open('/code/index.html').read()


def handler(environ, start_response):
    # context = environ['fc.context']
    # request_uri = environ['fc.request_uri']
    # for k, v in environ.items():
    #     if k.startswith('HTTP_'):
    #         pass

    # get query_string
    try:
        query_string = environ['QUERY_STRING']
    except (KeyError):
        query_string = " "

    print(query_string)
    q = parse_qs(query_string)
    if 'data' not in q:
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return [b"querystring must be like this data=mydata"]

    data = q['data'][0]
    print(data)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    # img.save("/tmp/a.png")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    img_enc = base64.b64encode(img_byte_arr).decode("utf-8")

    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)

    return [TEMPLATE.replace('{fc-py}', img_enc).encode('utf-8')]
