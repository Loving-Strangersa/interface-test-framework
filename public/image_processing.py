# -*- coding: utf-8 -*-
import base64
import io

import ddddocr
import jsonpath
import requests
from PIL import Image


def get_code(url, selector):
    """
    获取验证码，识别验证码内容
    :param url: 验证码地址
    :param selector: xpath解析
    :return: dict["code"]
    """
    try:
        s = requests.get(url).json()
        base64_data = jsonpath.jsonpath(s, selector)[0].split(',')[1]
        image_bytes = base64.b64decode(base64_data)
        image = Image.open(io.BytesIO(image_bytes))
        ocr = ddddocr.DdddOcr()
        s["code"] = ocr.classification(image)
        return s
    except (requests.RequestException, KeyError, base64.binascii.Error, ddddocr.OCRError) as e:
        print(f"An error occurred: {e}")
