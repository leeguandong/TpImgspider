'''
@Time    : 2021/1/27 10:55
@Author  : 19045845
'''
from tspider.core import TRequest
from tspider.downloadermiddlewares import proxies


class Download:
    def __init__(self, html_url, headers, proxies, dirname, html_title):
        self.html_title = html_title
        self.html_url = html_url
        self.headers = headers
        self.proxies = proxies
        self.dirname = dirname

    def images(self):
        if self.proxies:
            response = TRequest(self.html_url, headers=self.headers, proxies=proxies).request_get()
        else:
            response = TRequest(self.html_url, headers=self.headers).request_get()

        with open(self.dirname, 'wb') as f:
            f.write(response.content)

            print("正在下载" + self.html_title)
            print("已完成" + self.html_title + "下载")
