'''
@Time    : 2021/1/25 21:07
@Author  : 19045845
'''
import os
import math
from tspider.core import TRequest
from tspider.downloadermiddlewares import proxies
from tspider.utils import Registry

SPIDERDICT = Registry("spiderdict")


@SPIDERDICT.register_module
def universal(banner_url, banner_title):
    html_url = "http:" + banner_url
    html_title = banner_title
    return html_url, html_title


@SPIDERDICT.register_module
def burst(banner_url, banner_title):
    html_title = os.path.basename(banner_title).split("?")[0]
    html_url = banner_url.split("?")[0] + "?width=4460&height=4460&exif=1&iptc=1&attachment=" + html_title + ".jpg"
    return html_url, html_title


@SPIDERDICT.register_module
def mizhi(banner_url, banner_title):
    html_url = banner_url.split('&id')[0] + '&a=download&' + banner_url.split('m=download&')[-1]
    html_title = banner_title
    return html_url, html_title


@SPIDERDICT.register_module
def kaboompics(banner_url, banner_title):
    html_title = os.path.basename(banner_title).split("/")[-1]
    html_url = "https://kaboompics.com" + banner_url
    return html_url, html_title


@SPIDERDICT.register_module
def negativespace(banner_url, banner_title):
    html_title = banner_title
    html_url = banner_url.split("-1062x708.jpg")[0] + ".jpg"
    return html_url, html_title


@SPIDERDICT.register_module
def freestocks(banner_url, banner_title):
    html_title = banner_title.split("-")[0]
    html_url = banner_url
    return html_url, html_title


@SPIDERDICT.register_module
def pexels(banner_url, banner_title):
    html_title = banner_title
    html_url = "https://www.pexels.com/photo/{}/download/".format(banner_url.split("-")[-1].split("/")[0])
    return html_url, html_title


@SPIDERDICT.register_module
def tuguaishou_poster(banner_url, banner_title, headers, downloadjson):
    html_urls = "https://818ps.com{}".format(banner_url)
    sp = TRequest(html_urls, headers, downloadjson, proxies).request_get_text_sp()
    html_url = "http:" + sp.xpath("//*[@id='template_type1']/div[1]/div[1]/img[1]/@src")[0]
    html_title = banner_title.text
    return html_url, html_title


@SPIDERDICT.register_module
def qiantu_banner(banner_url, banner_title, headers, downloadjson):
    html_urls = "https:" + banner_url
    return TRequest(html_urls, headers, downloadjson, proxies).request_get_text_sp()


@SPIDERDICT.register_module
def ace_promoteMarketing(args, IMGWEB1, header, responsejson, market_dict):
    def subquery(id, subpage):
        subresponse = TRequest(IMGWEB1.format(id, subpage), headers=header, proxies=args.proxies).request_get()
        if subresponse.status_code == 200:
            subresponsejson = subresponse.json()
        return subresponsejson

    for index, act in enumerate(responsejson["data"]["datas"]):
        id = act["id"]
        submarkertingjson = subquery(id, 1)
        market_dict["data"].append(submarkertingjson["data"])

        if math.ceil(submarkertingjson["data"]["totalDataCount"] / submarkertingjson["data"]["pageSize"]) > 1:
            for subpage in range(2, math.ceil(
                                    submarkertingjson["data"]["totalDataCount"] / submarkertingjson["data"]["pageSize"] + 1)):
                submarkertingjson1 = subquery(id, subpage)
                market_dict["data"][index]["datas"].extend(submarkertingjson1["data"]["datas"])
    return market_dict
