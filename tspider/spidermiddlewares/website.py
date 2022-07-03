'''
@Time    : 2021/1/26 10:25
@Author  : 19045845
'''
import json
from tspider.utils import Registry

WEBSITEDICT = Registry("websitedict")


@WEBSITEDICT.register_module
def qiantu(sp):
    data_url = sp.xpath("//div[@class='pic-box clearfix ']/div/a/div/img/@data-original") # //*[@id='qt-app']/div/div/div[5]/div[2]/div[1]/a/div[1]/img/@data-original
    data_title = sp.xpath("//div[@class='pic-box clearfix ']/div/a/div/img/@title")
    return data_url, data_title


@WEBSITEDICT.register_module
def shetu(sp):
    data_url = sp.xpath("//img[@class='lazy']/@data-original")
    data_title = sp.xpath("//img[@class='lazy']/@alt")
    return data_url, data_title


@WEBSITEDICT.register_module
def mizhi(sp):
    data_urls = sp.xpath("/html/body/div[3]/div[2]/div[4]/*//@href")
    data_title = sp.xpath('/html/body/div[3]/div[2]/div[4]/*//@title')
    data_url = []
    for url in data_urls:
        if '.html' not in url:
            data_url.append(url)

    return data_url, data_title


@WEBSITEDICT.register_module
def burst(sp):
    data_url = sp.xpath("//*[@id='Main']/section[1]/div[3]/div//img[@data-srcset]/@src")
    data_title = sp.xpath("//*[@id='Main']/section[1]/div[3]//a[@class='photo-tile__image-wrapper']/@href")
    return data_url, data_title


@WEBSITEDICT.register_module
def kaboompics(sp):
    data_url = sp.xpath("//*[@id='work-grid']/li//a[@title='QUICK DOWNLOAD']/@href")
    data_title = sp.xpath("//*[@id='work-grid']/li//a[@title='QUICK DOWNLOAD']/@data-popup-href")
    return data_url, data_title


@WEBSITEDICT.register_module
def negativespace(sp):
    data_url = sp.xpath("//*[@id='content']//a/img/@src")
    data_title = sp.xpath("//*[@id='content']//a/img/@alt")
    return data_url, data_title


@WEBSITEDICT.register_module
def freestocks(sp):
    data_url = sp.xpath("//*[@id='gallery']//div/a[@class='download-link']/@href")
    data_title = sp.xpath("//*[@id='gallery']//div/a[@class='download-link']/@title")
    return data_url, data_title


@WEBSITEDICT.register_module
def pexels(sp):
    data_title = sp.xpath("//a[@class='js-photo-link photo-item__link']/@title")
    data_url = sp.xpath("//a[@class='js-photo-link photo-item__link']/@href")
    return data_url, data_title


@WEBSITEDICT.register_module
def gaoding_product_main_image(sp):
    data_url = sp.xpath("//*[@id='app']/div/div[2]/div[1]/div/div[3]/div/span/div[1]/*/div/div/div[1]/div/div/div/img/@src")
    data_title = sp.xpath("//*[@id='app']/div/div[2]/div[1]/div/div[3]/div/span/div[1]/*/div/div/div[1]/div/div/div/img/@title")
    return data_url, data_title


@WEBSITEDICT.register_module
def tusiji_main_image(sp):
    data_url = sp.xpath("//*[@id='masonry']//dt/div/img/@src")
    data_title = sp.xpath("//*[@id='masonry']//dt/div/img/@alt")
    return data_url, data_title


@WEBSITEDICT.register_module
def tusiji_detail_image(sp):
    data_url = sp.xpath("//*[@id='masonry']/*/dt/div/img/@src")
    data_title = sp.xpath("//*[@id='masonry']/*/dt/div/img/@alt")
    return data_url, data_title


@WEBSITEDICT.register_module
def tuguaishou_poster(sp):
    data_url = sp.xpath("//*[@id='masonry']//p/a/@href")
    data_title = sp.xpath("//*[@id='masonry']//p/a/strong")
    return data_url, data_title


@WEBSITEDICT.register_module
def qiantu_banner(sp):
    data_url = sp.xpath("/html/body/div[4]/div[3]/div[2]//a/@href")
    data_title = sp.xpath("/html/body/div[4]/div[3]/div[2]//a/div[1]/img/@alt")
    return data_url, data_title


@WEBSITEDICT.register_module
def ace_promoteMarketing():
    pass


@WEBSITEDICT.register_module
def smzdm(sp):
    data_url = sp.xpath("//*[@id='feed-main']/div//a[@class='shaiwu-card-title']/@href")
    return data_url
