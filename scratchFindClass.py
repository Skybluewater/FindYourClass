import os
import time
import json
import pyautogui
import pyperclip
import requests
import threading
import OCRVerify

# import winsound


header_output = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": "117",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "wengine_vpn_ticketwebvpn_bit_edu_cn=88533de683843fdd; show_vpn=0; show_faq=0; refresh=0",
    "Host": "webvpn.bit.edu.cn",
    "Origin": "https://webvpn.bit.edu.cn",
    "Referer": "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/course.html",
    "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

headers_choose_class = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": "85",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "wengine_vpn_ticketwebvpn_bit_edu_cn=88533de683843fdd; show_vpn=0; show_faq=0; refresh=0",
    "Host": "webvpn.bit.edu.cn",
    "Origin": "https://webvpn.bit.edu.cn",
    "Referer": "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/course.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS"
}

headers_button = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": "44",
    "Content-Type": "text/plain; charset=UTF-8",
    "Cookie": "wengine_vpn_ticketwebvpn_bit_edu_cn=88533de683843fdd; show_vpn=0; show_faq=0; refresh=0",
    "Host": "webvpn.bit.edu.cn",
    "Origin": "https://webvpn.bit.edu.cn",
    "Referer": "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/course.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS"
}

headers_sea_class = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": "133",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "wengine_vpn_ticketwebvpn_bit_edu_cn=88533de683843fdd; show_vpn=0; show_faq=0; refresh=0",
    "Host": "webvpn.bit.edu.cn",
    "Origin": "https://webvpn.bit.edu.cn",
    "Referer": "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/course.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS"
}

headers_get_public = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "Connection": "keep-alive",
    "Cookie": "wengine_vpn_ticketwebvpn_bit_edu_cn=88533de683843fdd; show_vpn=0; show_faq=0; refresh=0",
    "Host": "webvpn.bit.edu.cn",
    "Referer": "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/course.html",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS"
}

headers_search_class = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": "123",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "show_vpn=0; show_faq=0; wengine_vpn_ticketwebvpn_bit_edu_cn=88533de683843fdd; refresh=0",
    "Host": "webvpn.bit.edu.cn",
    "Origin": "https://webvpn.bit.edu.cn",
    "Referer": "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/course.html",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

data = {
    "query_keyword": "",
    "query_sfct": "0",
    "query_sfym": "",
    "fixedAutoSubmitBug": "",
    "query_kclb": "",
    "pageIndex": "1",
    "pageSize": "10",
    "sortField": "",
    "sortOrder": ""
}

data_nature = {
    "query_keyword": "2700002",
    "query_kkyx": "",
    "fixedAutoSubmitBug": "",
    "query_jxsjhnkc": "0",
    "query_jxsfankc": "0",
    "pageIndex": "1",
    "pageSize": "10",
    "sortField": "",
    "sortOrder": ""
}

data_choose_class = {
    "bjdm": "",
    "lx": "0",
    "csrfToken": "25689518a51840baba14b90a2f8c31a3"
}

data_search_class = {
    "query_keyword": "{class_id}",
    "query_kkyx": "",
    "query_sfct": "",
    "query_sfym": "",
    "fixedAutoSubmitBug": "",
    "pageIndex": "1",
    "pageSize": "10",
    "sortField": "",
    "sortOrder": ""
}

data_search_class_fetch = {
    "query_keyword": "",
    "query_kkyx": "",
    "query_sfct": "",
    "query_sfym": "",
    "fixedAutoSubmitBug": "",
    "pageIndex": "1",
    "pageSize": "10",
    "sortField": "",
    "sortOrder": ""
}

data_button = {"name": "", "type": "button", "value": "查询"}
site = "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/xsxkCourse/loadJhnCourseInfo.do?vpn-12-o1-xk.bit.edu.cn&_={time}"
site_choose = "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/xsxkCourse/choiceCourse.do?vpn-12-o1-xk.bit.edu.cn&_={time}"
site_get_public = "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/xsxkHome/loadPublicInfo_course.do?vpn-12-o1-xk.bit.edu.cn"
site_sea = "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/xsxkCourse/loadAllCourseInfo.do?vpn-12-o1-xk.bit.edu.cn&_={time}"
site_choose_others = "https://webvpn.bit.edu.cn/http/77726476706e69737468656265737421e8fc0f9e2e2426557a1dc7af96/yjsxkapp/sys/xsxkappbit/xsxkCourse/loadGxkCourseInfo.do?vpn-12-o1-xk.bit.edu.cn&_={time}"
site_button = "https://webvpn.bit.edu.cn/wengine-vpn/input"
friend = "亿锦前程 方震 刘翔"


def get_msg(msg):
    time.sleep(0.5)
    pyautogui.click(x=-906, y=888, duration=2)
    pyperclip.copy(msg)
    pyautogui.hotkey('command', 'v', interval=0.2)
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)


def send_to_file_transfer_helper(msg, is_first=True, name=friend):
    if not is_first:
        time.sleep(12)
    pyautogui.hotkey('command', 'ctrl', 'w', interval=0.2)
    time.sleep(0.5)
    pyautogui.hotkey('command', 'f', interval=0.2)
    time.sleep(0.5)
    pyperclip.copy(name)
    pyautogui.hotkey('command', 'v', interval=0.2)
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    get_msg(msg)
    pyautogui.hotkey('ctrl', 'right', interval=0.2)


if __name__ == '__main__':
    cnt = 0
    class_id = ["0700046", "1200019"]
    cur_lesson = 0
    # while True:
    #     try:
    #         response = requests.post(site.format(time=str(time.time()).replace(".", "")[:-4]), headers=header_output,
    #                                  data=data, timeout=60)
    #         ''''
    #         response = requests.post(site_sea.format(time=str(time.time()).replace(".", "")[:-4]),
    #                                  headers=headers_sea_class, data=data_nature)
    #         '''
    #     except (TimeoutError, OSError):
    #         os.system('say failed to connect')
    #         print("Trying to reconnect")
    #         continue
    #     print("times: " + str(cnt))
    #     cnt += 1
    #     try:
    #         to_dic = json.loads(response.text)
    #         class_list = to_dic["datas"]
    #         first_in_list = True
    #         for lesson in class_list:
    #             if lesson['DQRS'] < lesson['KXRS'] and lesson['KCMC'] != "核磁共振成像及其应用":
    #                 requests.post(site_button, headers=headers_button, data=data_button)
    #                 public_get = requests.get(site_get_public, headers=headers_get_public)
    #                 csrf_token = json.loads(public_get.text)["csrfToken"]
    #                 data_choose_class['bjdm'] = lesson['BJDM']
    #                 data_choose_class['csrfToken'] = csrf_token
    #                 response = requests.post(site_choose.format(time=str(time.time()).replace(".", "")[:-4]),
    #                                          headers=headers_choose_class,
    #                                          data=data_choose_class)
    #                 print("Lesson Available " + lesson["BJMC"])
    #                 os.system('say ' + lesson["BJMC"])
    #                 os.system(
    #                     'say "your program has finished" "your program has finished" "your program has finished" "your program has finished"')
    #                 thread = threading.Thread(target=send_to_file_transfer_helper,
    #                                           args=(lesson['KCMC'], first_in_list))
    #                 thread.start()
    #                 first_in_list = False
    #         time.sleep(4)
    #     except json.decoder.JSONDecodeError:
    #         print("Trying to login")
    #         os.system('say Trying to login')
    #         try:
    #             thread = threading.Thread(target=send_to_file_transfer_helper, args=("Tryin'tologin"))
    #             thread.start()
    #             OCRVerify.ocr_handle()
    #         except ValueError:
    #             os.system(
    #                 'say -v \'bad news\' "Login Failed" "Login Failed" "Login Failed" "Login Failed" "Login Failed"')
    #         print("Login Success")
    while True:
        try:
            cur_lesson = class_id[cnt % len(class_id)]
            data_search_class["query_keyword"] = cur_lesson
            response = requests.post(site_choose_others.format(time=str(time.time()).replace(".", "")[:-4]), headers=headers_search_class,
                                     data=data_search_class, timeout=60)
            ''''
            response = requests.post(site_sea.format(time=str(time.time()).replace(".", "")[:-4]),
                                     headers=headers_sea_class, data=data_nature)
            '''
        except (TimeoutError, OSError):
            os.system('say failed to connect')
            print("Trying to reconnect")
            continue
        print("times: " + str(cnt) + " " + cur_lesson)
        cnt += 1
        try:
            to_dic = json.loads(response.text)
            class_list = to_dic["datas"]
            # first_in_list = True
            # for lesson in class_list:
            #     if lesson['DQRS'] < lesson['KXRS'] and lesson['KCMC'] != "核磁共振成像及其应用":
            #         requests.post(site_button, headers=headers_button, data=data_button)
            #         public_get = requests.get(site_get_public, headers=headers_get_public)
            #         csrf_token = json.loads(public_get.text)["csrfToken"]
            #         data_choose_class['bjdm'] = lesson['BJDM']
            #         data_choose_class['csrfToken'] = csrf_token
            #         response = requests.post(site_choose.format(time=str(time.time()).replace(".", "")[:-4]),
            #                                  headers=headers_choose_class,
            #                                  data=data_choose_class)
            #         print("Lesson Available " + lesson["BJMC"])
            #         os.system('say ' + lesson["BJMC"])
            #         os.system(
            #             'say "your program has finished" "your program has finished" "your program has finished" "your program has finished"')
            #         thread = threading.Thread(target=send_to_file_transfer_helper,
            #                                   args=(lesson['KCMC'], first_in_list))
            #         thread.start()
            #         first_in_list = False

            for lesson in class_list:
                if lesson['DQRS'] < lesson['KXRS']:
                    # requests.post(site_button, headers=headers_button, data=data_button)
                    # public_get = requests.get(site_get_public, headers=headers_get_public)
                    # csrf_token = json.loads(public_get.text)["csrfToken"]
                    # data_choose_class['bjdm'] = lesson['BJDM']
                    # data_choose_class['csrfToken'] = csrf_token
                    # response = requests.post(site_choose.format(time=str(time.time()).replace(".", "")[:-4]),
                    #                          headers=headers_choose_class,
                    #                          data=data_choose_class)
                    print("Lesson Available " + lesson["BJMC"])
                    os.system('say ' + lesson["BJMC"])
                    os.system('say "your program has finished" "your program has finished" "your program has finished" "your program has finished"')
            time.sleep(1)
        except json.decoder.JSONDecodeError:
            print("Trying to login")
            os.system('say Trying to login')
            try:
                thread = threading.Thread(target=send_to_file_transfer_helper, args=("Tryin'tologin"))
                thread.start()
                OCRVerify.ocr_handle()
            except ValueError:
                os.system(
                    'say -v \'bad news\' "Login Failed" "Login Failed" "Login Failed" "Login Failed" "Login Failed"')
            print("Login Success")
