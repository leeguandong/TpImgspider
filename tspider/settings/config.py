'''
@Time    : 2021/1/27 10:58
@Author  : 19045845
'''
import os
from pathlib import Path

# -------------------------------------------------- 爬取的网站 ------------------------------------------------------------
# IMGWEB = "https://www.58pic.com/piccate/"

# 外部网站 (大约有15个)
# 不稳定
# IMGWEB = "https://unsplash.com"

# 51个标签且较为稳定
# IMGWEB = "https://burst.shopify.com"

# 不稳定
# IMGWEB = "https://pixabay.com/photos/"

# 网站不错，但是图片没有标签
# IMGWEB = "https://kaboompics.com/gallery"

# 有标签,超高清，单图质量很高，爬取很慢
# IMGWEB = "https://negativespace.co/"

# 不稳定，gallery 有标签
# IMGWEB = "https://www.lifeofpix.com/"

# 摄影师网站，无标签
# IMGWEB = "https://freestocks.org/"

# 创意图库，画风ins，相当违和
# IMGWEB = "https://gratisography.com/"

# 插图，不太稳定
# IMGWEB = "https://mixkit.co/free-stock-art/relationships/"

# 优优教程网,不可下载原图，前端小图，质量低
# IMGWEB = "https://uiiiuiii.com/inspiration"

# pexels 风景图
# IMGWEB = "https://www.pexels.com/search/HD%20wallpaper/"
IMGWEB = "https://www.pexels.com/search/digital/"
# IMGWEB = "https://www.pexels.com/search/baby/"
# IMGWEB = "https://www.pexels.com/search/cars/"
# IMGWEB = "https://www.pexels.com/search/indoor/"
# IMGWEB = "https://www.pexels.com/search/beauty/"
# IMGWEB = "https://www.pexels.com/search/clothing/"

# 搞定设计商品主图
# IMGWEB = "https://www.gaoding.com/s/ecommerce/search?filter_id=1612839"

# 图司机商品主图
# IMGWEB = "https://www.tusij.com/pic/1-13-138-0-0-{}.html"

# 图司机详情图
# IMGWEB = "https://www.tusij.com/pic/1-13-195-0-0-{}.html"

# Canva 手机海报,和搞定一样，是动态页面，也是学习爬虫的好网站
# IMGWEB = "https://www.canva.cn/templates/search/5omL5py65rW35oqlX64/?continuation={}"

# 京东玲珑
# IMGWEB = ""

# 图怪兽
# IMGWEB = "https://818ps.com/search/0-0-0-0-0-null-34_800_0_0-0-0-0-0/{}.html"

# 千图网基础
# IMGWEB = ""

# 千图网精选
IMGWEB = "https://www.58pic.com/piccate/3-8-0-ty1-p{}.html"
# IMGWEB = "https://www.58pic.com/piccate/3-8-0-ty1-se1-p{}.html"

# URL
# IMGWEB = r"E:\comprehensive_library\TpImgspider\tspider\example\dpa.txt"
# IMGWEB = "./example/picurl2000_20200529.txt"

# ------------------------------------------------ download psd -----------------------------------------------
# IMGWEB = "http://spsadm.cnsuning.com/spsadm/search/goSencondPage.act"

# IMGWEB = "http://ace.cnsuning.com/ace-admin/index.htm#/designMaterial/socialPoster.htm"

# IMGWEB = "http://ace.cnsuning.com/ace-admin/index.htm#/designMaterial/atmosphere.htm"

# ACE-promoteMarketing
# IMGWEB = "http://ace.cnsuning.com/ace-admin/material/getActivityList.htm?pageSize=40&pageNumber={}&searchFieldName=&level=&startTime=&endTime="
# IMGWEB1 = "http://ace.cnsuning.com/ace-admin/material/getMarketMaterialList.htm?&activityId={}&syncSwitch=&pageSize=40&pageNumber={}&materialName=&terminalType=&siteCategoryDictKey=&venueTypeDictKey=&isMy=2&orderType="

# 什么值得买
TEXTWEB = 'https://post.smzdm.com/talk/p{}'


# ----------------------------------------------- download path ----------------------------------------------
SAVEPATH = os.getcwd().split("tspider")[0] + "saved"
# SAVEPATH = r"E:\统计\site_material"
Path(SAVEPATH).mkdir(parents=True, exist_ok=True)

WEBNAME = "smzdm"
SAVEPATH = os.path.join(SAVEPATH, WEBNAME)
Path(SAVEPATH).mkdir(parents=True, exist_ok=True)
IMGPATH = os.path.join(SAVEPATH, "img_download")
TXTPATH = os.path.join(SAVEPATH, "txt_download")
Path(IMGPATH).mkdir(parents=True, exist_ok=True)
Path(TXTPATH).mkdir(parents=True, exist_ok=True)

# 类别库
CATEGORY_LIBRARY = {"冰洗": ["household supplies", "cleaning", "refrigerator"], "厨卫": ["kitchen", "bathroom", "home dector"],
                    "通讯": ["sky", "night sky", "landscape"], "医药": ["medicine", "medicine"], "黑电": ["urban life", "smart home"],
                    "粮油休食": ["food", "cooking", "snacks"], "家装": ["home", "furniture", "home decoration"],
                    "冲调酒水": ["wine", "beer", "drink", "bar"], "百货": ["home"], "个护家清": ["cleaning", "washing"], "汽车": ["cars", "city"],
                    "电脑": ["office", "meeting"], "母婴": ["baby", "baby"], "小家电": ["home", "household applies"],
                    "空调": ["home", "nature", "countryside"], "美妆": ["make up", "makeup"],
                    "数码": ["technology", "sky", "night", "sky", "landscape"],
                    "进口保健生鲜": ["health", "fresh"], "体育": ["fitness", "gym"]}
