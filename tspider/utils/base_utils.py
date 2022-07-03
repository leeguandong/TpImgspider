'''
@Time    : 2021/1/26 9:44
@Author  : 19045845
'''
import json
import os
import timeit

import numpy as np

from tspider.settings.config import TXTPATH


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)


def geturls(path):
    urls = []
    with open(path, 'r') as f:
        for line in f:
            urls.append(line.strip('\n'))
    return urls


def clock(func):
    """
    修饰器函数，对函数计时
    :param func:
    :return:
    """

    def clocked(*args):
        t0 = timeit.default_timer()
        result = func(*args)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s)' % (elapsed, name, arg_str))
        return result

    return clocked


def record_url(html_url, html_title, page, index):
    with open(os.path.join(TXTPATH, "url.txt"), "a", encoding="utf-8") as burl:
        burl.write(html_url)
        burl.write("\t //")
        burl.write(html_title)
        burl.write("\t //")
        burl.write(str(page) + "_" + str(index))
        burl.write("\n")
        burl.flush()


def record_txt(html_text, html_title, index, ):
    with open(os.path.join(TXTPATH, str(index) + ".txt"), 'a', encoding='utf-8') as burl:
        burl.write('---')
        burl.write('\n')
        burl.write(f'标题：{html_title[0].strip()}')
        burl.write('\n---\n')
        burl.write(html_text)
        burl.write('\n')
