import time
import ddddocr
import json
import requests
from PIL import Image
from io import BytesIO

# get_v_code
headers_get_vcode = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "Connection": "keep-alive",
    "Cookie": "wengine_vpn_ticketwebvpn_bit_edu_cn=1441fe4ae8073bc8; show_vpn=0; show_faq=0; refresh=0",
    "Host": "webvpn.bit.edu.cn",
    "Referer": "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/index.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
}

# ocr_image
header_get_ocr = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "Connection": "keep-alive",
    "Cookie": "wengine_vpn_ticketwebvpn_bit_edu_cn=1441fe4ae8073bc8; show_vpn=0; show_faq=0; refresh=0",
    "Host": "webvpn.bit.edu.cn",
    "Referer": "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/index.html",
    "Sec-Fetch-Dest": "image",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
}

# send_verify_number
header_send_ocr = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": "138",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "wengine_vpn_ticketwebvpn_bit_edu_cn=1441fe4ae8073bc8; show_vpn=0; show_faq=0; refresh=0",
    "Host": "webvpn.bit.edu.cn",
    "Origin": "https://webvpn.bit.edu.cn",
    "Referer": "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/index.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS"
}

data_login = {
    "loginName": "3220220891",
    "loginPwd": "787CDCB10A5F0F15BA0E68B599921C9464DC9BD5CEC5A44F",
    "verifyCode": "",
    "vtoken": ""
}

site_get_vcode = "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/login/4/vcode.do?vpn-12-o1-xk.bit.edu.cn&timestamp={time}"
site_get_ocr = "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/login/vcode/image.do?vtoken={token}"
site_send_ocr = "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/login/check/login.do?vpn-12-o1-xk.bit.edu.cn&timestrap={time}"
image_cnt = 0


def get_vcode():
    response = requests.get(site_get_vcode.format(time=str(time.time()).replace(".", "")[:-4]),
                            headers=headers_get_vcode)
    text_dic = json.loads(response.text)
    v_code = text_dic["data"]["token"]
    return v_code


def get_ocr(v_code):
    response = requests.get(site_get_ocr.format(token=v_code), headers=header_get_ocr)
    ocr = ddddocr.DdddOcr()
    res = ocr.classification(response.content)
    image = Image.open(BytesIO(response.content))
    global image_cnt
    image.save("ocr_{cnt}.jpg".format(cnt=image_cnt))
    image_cnt += 1
    return res


def send_ocr(v_code, v_code_res):
    data_login["verifyCode"] = v_code_res
    data_login['vtoken'] = v_code
    response = requests.post(site_send_ocr.format(time=str(time.time()).replace(".", "")[:-4]),
                             headers=header_send_ocr, data=data_login)
    data_msg = json.loads(response.text)
    return data_msg["code"] == "1"


# get process & handle
def ocr_handle():
    has_succeed = False
    cnt = 0
    while not has_succeed and cnt < 10:
        v_code = get_vcode()
        v_code_res = get_ocr(v_code)
        has_succeed = send_ocr(v_code, v_code_res)
        cnt += 1
        time.sleep(6)
    if not has_succeed:
        raise ValueError("not successful login")
