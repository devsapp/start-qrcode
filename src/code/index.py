# -*- coding: utf-8 -*-

import logging
import qrcode
import base64
import io
import json

TEMPLATE = open("/code/index.html").read()


def handler(event, context):
    evt = json.loads(event)
    q = evt.get("queryParameters", {})
    if "data" not in q:
        return {
            "body": "querystring must be like this data=mydata",
            "headers": {"Content-type": "text/plain"},
            "statusCode": 200,
        }
    data = q["data"][0]
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
    img.save(img_byte_arr, format="PNG")
    img_byte_arr = img_byte_arr.getvalue()
    img_enc = base64.b64encode(img_byte_arr).decode("utf-8")
    return {
        "body": TEMPLATE.replace("{fc-py}", img_enc),
        "headers": {"Content-type": "text/html"},
        "statusCode": 200,
    }
