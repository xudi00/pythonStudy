import requests
import logging
import re

BASIC_MP3 = 'http://k6.kekenet.com/'
BASIC_LRC = 'http://www.kekenet.com/'
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


def find_page(pattern):
    # 读取html文件,这里open必须三个参数写全
    file = open('kekeindex.html', 'r', encoding='utf-8')
    content = file.read()
    file.close()
    # 检索网页
    results = re.findall(pattern, content)
    return results


def url():
    pattern_url = re.compile('<a.*?href="(http.*?)".*?title="人教版')
    return pattern_url


def name():
    pattern_title = re.compile('<a.*?href="http.*?".*?title="(人教版.*?)"')
    return pattern_title


def find_mp3():
    # 读取html文件
    file = open("kekeunit4.html", "r", encoding="utf-8")
    content = file.read()
    file.close()
    # 检索网页
    pattern = re.compile('thunder_url.*?(Sound.*?)"')
    result = re.search(pattern, content)
    mp3_url = BASIC_MP3 + result.group(1)
    return mp3_url

    # if result:
    #     # group()是对象的内容；group(1)是第一个括号里面的内容
    #     mp3_url = result.group(1)
    #     logging.info('Found the url of mp3...')
    # else:
    #     logging.warning('Can not find the mp3 url')


def find_lrc():
    # 读取html文件
    file = open("kekeunit4.html", "r", encoding="utf-8")
    content = file.read()
    file.close()
    # 检索网页
    pattern = re.compile('jmlrc.*?(Sound.*?.lrc)"')
    result = re.search(pattern, content)

    if result:
        # group()是对象的内容；group(1)是第一个括号里面的内容
        lrc_url = BASIC_LRC + result.group(1)
        logging.info('Found the url of lrc...')
        print(lrc_url)
    else:
        logging.warning('Can not find the lrc url')


# url_list = find_page(url())
# print(url_list)
# print('=' * 50)
# name_list = find_page(name())
# print(name_list)
# for i in range(len(name_list)):
#     name_list[i] = 'Book' + re.sub('[\u4e00-\u9fa5]|\W','',name_list[i])
# print(name_list)
# print('=' * 50)

# find_mp3()
find_lrc()
print('this is a point')