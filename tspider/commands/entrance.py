import json
import os

from tqdm import tqdm

from tspider.core import TRequest
from tspider.downloadermiddlewares import header, proxies
from tspider.pipelines import Download
from tspider.settings.config import TEXTWEB, IMGPATH, IMGWEB, TXTPATH, CATEGORY_LIBRARY, WEBNAME  # IMGWEB1,
from tspider.spidermiddlewares import WEBSITEDICT
from tspider.spiders import SPIDERDICT
from tspider.utils import Registry
from tspider.utils import geturls, record_url, MyEncoder, record_txt

ENTRANCEDICT = Registry("entrancedict")


@ENTRANCEDICT.register_module
def DPA(args):
    txtpath = IMGWEB
    urls = geturls(txtpath)
    print(f"链接行数: {len(urls)}")

    for index, url in tqdm(enumerate(urls)):
        url = url.split('"motherSetUrl":')[-1].replace('"', "")

        # download
        response = TRequest(url, headers=header).request_get()
        with open(os.path.join(IMGPATH, os.path.basename(url)), "wb") as f:
            f.write(response.content)
            response.close()


@ENTRANCEDICT.register_module
def burst(args):
    sp = TRequest(IMGWEB, headers=header, proxies=args.proxies).request_get_text_sp()
    categories = sp.xpath("//a[@class='tile__link-overlay']/@href")
    newurls = [IMGWEB + category for category in categories]

    for index in tqdm(range(0, len(newurls))):
        try:
            url = newurls[index]
            savefolder = os.listdir(os.getcwd().split("tspider")[0] + "saved/" + WEBNAME + "/img_download")
            if os.path.basename(url) in savefolder:
                continue
            elif "in_" + os.path.basename(url) in savefolder:
                continue

            # 页面有的话，直接写，有些网站页面所在位置会频繁更换
            # sp = etree.HTML(TRequest(url, headers=header, proxies=args.proxies).request_get().text)
            # try:
            #     num = int(sp.xpath("//*[@id='Main']/section[1]/section/nav/span[8]/a[@href]")[0].attrib["href"].split("page=")[-1])
            # except:
            #     num = int(sp.xpath("//*[@id='Main']//span[@class='last']/a/@href")[0].split("?page=")[-1])
            num = 10

            for page in tqdm(range(1, num + 1)):
                if os.path.basename(url) in CATEGORY_LIBRARY:
                    name = "in_" + os.path.basename(url)
                else:
                    name = os.path.basename(url)
                urls = url + "?page={}".format(page)
                sp = TRequest(urls, headers=header, proxies=args.proxies).request_get_text_sp()
                data_url, data_title = WEBSITEDICT.get(args.name)(sp)

                for index, (banner_url, banner_title) in tqdm(enumerate(zip(data_url, data_title))):
                    try:
                        html_url, html_title = SPIDERDICT.get(args.name)(banner_url, banner_title)

                        record_url(html_url, html_title, page, index)

                        dirname = os.path.join(IMGPATH, name)
                        if not os.path.exists(dirname): os.mkdir(dirname)
                        Download(html_url, header, proxies, dirname, html_title).images()

                    except:
                        continue
        except:
            print("Bizarre problem generation completed")


@ENTRANCEDICT.register_module
def ace_promoteMarketing(args):
    jsonflag = True
    market_dict = {"api": "getActivityList", "code": "1", "data": [], "msg": "", "v": "1.0"}
    if jsonflag:
        for page in range(1, 4):
            urls = IMGWEB.format(page)

            response = TRequest(urls, headers=header, proxies=args.proxies).request_get()
            if response.status_code == 200:
                responsejson = response.json()
            market_dict = SPIDERDICT.get(args.name)(args, IMGWEB1, header, responsejson, market_dict)

            json.dump(market_dict, open(os.path.join(TXTPATH, "market.json"), "w", encoding="utf-8"), indent=4,
                      ensure_ascii=False,
                      cls=MyEncoder)
    else:
        f = open(os.path.join(TXTPATH, "market.json"), encoding="utf-8").read()
        market_dict = json.load(f)

        flag = False
        for data in tqdm(market_dict["data"]):
            for psdfile in data["datas"]:
                if "1586258684894.zip" in psdfile["designUrl"]:
                    flag = True
                if flag:
                    dirname = IMGPATH + '/{}'.format(os.path.basename(psdfile["designUrl"]))
                    Download(psdfile["designUrl"], header, proxies, dirname, psdfile["designName"]).images()


@ENTRANCEDICT.register_module
def smzdm(args):
    for index in tqdm(range(0, 100)):
        try:
            sp = TRequest(TEXTWEB.format(index), headers=header, proxies=args.proxies).request_get_text_sp()

            data_url = WEBSITEDICT.get(args.name)(sp)
            for index, url in tqdm(enumerate(data_url)):
                html_text, html_title = SPIDERDICT.get(args.name)(args, header, url)
                html_text_ = ''
                for text in html_text:
                    html_text_ += text
                record_txt(html_text_, html_title, index)
        except:
            print('什么值得买failed！！！')


@ENTRANCEDICT.register_module
def qiantu(args):
    for page in tqdm(range(1, 44)):
        sp = TRequest(IMGWEB.format(page), headers=header, proxies=args.proxies).request_get_text_sp()

        data_url, data_title = WEBSITEDICT.get(args.name)(sp)

        for index, (banner_url, banner_title) in tqdm(enumerate(zip(data_url, data_title))):
            try:
                html_url, html_title = SPIDERDICT.get(args.name)(banner_url, banner_title)
                record_url(html_url, html_title, page, index)

                dirname = os.path.join(IMGPATH, name='temp')
                if not os.path.exists(dirname): os.mkdir(dirname)
                Download(html_url, header, proxies, dirname, html_title).images()
            except:
                continue
