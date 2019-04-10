# -*- coding: utf-8 -*-
#!/usr/bin/env python
import argparse
import requests
import ctypes
import sys

#config
timeout = 5

class ColorPrinter:
    def print_red_text(self, content):
        print("\033[1;31;40m %s \033[0m" % (content),end='')
    def print_green_text(self, content):
        print("\033[1;32;40m %s \033[0m" % (content),end='')
    def print_blue_text(self, content):
        print("\033[1;34;40m %s \033[0m" % (content),end='')

def urlFormater(url):
    if (not url.startswith("http://")) and (not url.startswith("https://")):
        url = "http://" + url
    if not url.endswith("/"):
        url += "/"
    return url


def main():
    parse = argparse.ArgumentParser(description="Sensitive information file")
    parse.add_argument('--file','-f',help='url file')
    parse.add_argument('--url','-u',help='may be you only want to test one url')
    parse.add_argument('--save','-s',action='store_true',help='save scan infos')
    args = parse.parse_args()

    try:
        sys.argv[1]
    except:
        parse.print_help()
        exit()

    colorPrinter = ColorPrinter()
    if not colorPrinter :
        exit()

    targets = [] #target url
    urls = [] #test url
    logs = []#scan info
    if args.file:
        try:
            with open(args.file,'r') as f:
                for i in f.readlines():
                    targets.append(urlFormater(i.strip()))
        except:
            colorPrinter.print_red_text("[-]File not found!")
            exit()
    if args.url:
        targets.append(urlFormater(url))

    #Get Test Url
    if targets:
        for website in targets:
            listFile = open('list.txt', 'r')
            for i in listFile:
                i = i.replace("\n","")
                i = i.replace("\r","")
                if "?" in i:
                    fileFile = open('file.txt', 'r')
                    for j in fileFile:
                        j = j.replace("\n","")
                        j = j.replace("\r","")
                        temp = i.replace("?",j)
                        urls.append(website + temp)
                else:
                    urls.append(website + i)
    #Check The url is or not
    for url in urls:
        try:
            response = requests.head(url,timeout = timeout)
            code = response.status_code
            logs.append(str(code)+','+url)
            if code == 200:
                colorPrinter.print_green_text("[ " + str(code) + " ]")
                print("Checking : " + url)
                if "404" in response.text:
                    colorPrinter.print_blue_text(url + "\tMaybe every page same!")
            elif code == 404 or code == 405:
                pass
            else:
                colorPrinter.print_red_text("[ " + str(code) + " ]")
                print("Checking : " + url)
        except Exception as e:
            print(e)

    #write info into scaninfo.csv
    if args.file:
        with open('scaninfo.csv','w') as wf:
            wf.write('\n'.join(logs))


if __name__ == '__main__':
    main()
