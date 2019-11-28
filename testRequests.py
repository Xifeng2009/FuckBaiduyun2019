#! /usr/bin/python3
#! coding:  utf-8
#! Author:  Zy
#! Date:    2019-11-28

import requests


def main():
    try:
        r = requests.get("https://pan.baidu.com/s/1Vi2g_l0A4UJFnuAaeZh7fg")
    except Exception as e:
        print(f"[Exception] {e}")
    
    
if __name__ == '__main__':
    main()