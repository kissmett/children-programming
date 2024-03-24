# -*- coding: utf-8 -*-
import urllib.request  # url request
import re  # regular expression
import os  # dirs
import time

from urllib.parse import urlparse
import datetime
 
'''
url 下载网址
pattern 正则化的匹配关键词
Directory 下载目录
NeedAutoFileName 是否需要自动生成文件名
defaultext 默认的文件扩展名
'''
# 拉动请求，模拟成浏览器去访问网站->跳过反爬虫机制
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
# headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [ 
    ('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'),
    ('Referer','www.doczj.com')
] 
# User-Agent：模拟真实浏览器请求；
# Referer: 前导页面，即本次请求是从哪里发起的，服务器可能会对请求头里的referer进行检测，并触发403 Access is denied错误；
 
def DownloadByURL(url, pattern, Directory,NeedAutoFileName:bool = False,defaultext='.jpg',protocol='',overwrite:bool = False):
    # 获取网页内容
    a = opener.open(url)
    content = a.read().decode('Utf-8')
    DownloadByContent(content,pattern,Directory,NeedAutoFileName,defaultext,protocol,overwrite)

def DownloadByContent(content,pattern,Directory,NeedAutoFileName:bool = False,defaultext='.jpg',protocol='',overwrite:bool = False): 
    if not os.path.exists(Directory):
        os.makedirs(Directory)
    # 构造正则表达式，从content中匹配关键词pattern
    raw_hrefs = re.findall(pattern, content, 0)
 
    # set函数消除重复元素
    hset = set(raw_hrefs)
 
    # 下载链接
    for href in hset:
        # 之所以if else 是为了区别只有一个链接的特别情况
        if False and (len(hset) > 1):
            link = url + href[0]
            filename = os.path.join(Directory, href[0])
            print("正在下载", filename)
            urllib.request.urlretrieve(link, filename)
            print("成功下载！")
        else:
            link = href
            if protocol != '':
                link = protocol + href

            a = urlparse(link)
            filename = os.path.basename(a.path)
            if NeedAutoFileName:
                prepart,ext=os.path.splitext(a.path)
                if ext == '':
                    ext = defaultext 
                filename = filename +  str(round( time.time() * 1000)) + ext

            filename = os.path.join(Directory, filename)
            if os.path.exists(filename):
                print('已存在，跳过')
            else:
                print("正在下载", filename)
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(link, filename)
                print("成功下载！")
    
        # 无sleep间隔，网站认定这种行为是攻击，反反爬虫
        time.sleep(1)

content = '''
<div class="preview-bd" style="cursor: grab;"><div class="webpreview-item" data-id="1" style="min-height: 1218px;"><img oncontextmenu="return false;" ondragstart="return false;" onload="WebPreview.Image.onLoad(this)" onerror="WebPreview.Image.onError(this)" src="//view-cache.book118.com/view21/M02/03/2A/wKh2DmGVlWKAX58SAACv21FlrNA960.png" style="display: block;"></div><div class="webpreview-split"></div><div class="webpreview-recommend re" data-re_id="1"><ul class="re-pic" id="re_pic_1"><li><a href="/user_center_v1/crm/home/index.html?from=view" target="_blank" title="文档crm管理系统" owa-href="had" owa-btn="had"><img class="lazy-success" src="//img.book118.com/sr1/M00/00/34/wKh2C2JWOQuIcSdHAAA3PuPlphMAA13iAGobrgAADdW807.png" data-src="//img.book118.com/sr1/M00/00/34/wKh2C2JWOQuIcSdHAAA3PuPlphMAA13iAGobrgAADdW807.png" alt="文档crm管理系统"></a></li></ul><i class="fix">文档crm管理系统</i></div><div class="webpreview-split">&nbsp;</div><div class="webpreview-item" data-id="2" style="min-height: 1218px;"><img oncontextmenu="return false;" ondragstart="return false;" onload="WebPreview.Image.onLoad(this)" onerror="WebPreview.Image.onError(this)" src="//view-cache.book118.com/view21/M01/03/29/wKh2EGGVlWKAIGCHAACwiZgvjQc684.png" style="display: block;"></div><div class="webpreview-split"></div><div class="webpreview-recommend re" data-re_id="2"><ul class="re-shop" id="re_shop_2"><li><a href="https://zhineng.book118.com/merchant.html?type=27&amp;from=pc-view" target="_blank" title="PPT定制" owa-href="had" owa-btn="had"><span class="cover"><img class="lazy" src="//static.book118.com/user_center_v1/static/home/images/lazy/load.png" data-src="//img.book118.com/sr1/M00/0A/01/wKh2C2MXDYiIfJJgAAAgRcuP5HAAA5dnwH6bU4AACBd530.png" alt="PPT定制"></span><span class="shop-title">PPT定制</span></a></li><li><a href="https://zhineng.book118.com/merchant.html?type=19&amp;from=pc-view" target="_blank" title="标书撰写" owa-href="had" owa-btn="had"><span class="cover"><img class="lazy-success" src="//img.book118.com/sr1/M00/0A/01/wKh2C2MXDYCIaHxTAAAg6zAsGaoAA5dnwHv1rUAACED949.png" data-src="//img.book118.com/sr1/M00/0A/01/wKh2C2MXDYCIaHxTAAAg6zAsGaoAA5dnwHv1rUAACED949.png" alt="标书撰写"></span><span class="shop-title">标书撰写</span></a></li><li><a href="https://zhineng.book118.com/merchant.html?type=74&amp;from=pc-view" target="_blank" title="法律咨询" owa-href="had" owa-btn="had"><span class="cover"><img class="lazy" src="//static.book118.com/user_center_v1/static/home/images/lazy/load.png" data-src="//img.book118.com/sr1/M00/0A/01/wKh2C2MXDXGIWNmmAAAijr6FmO4AA5dnwHlMGoAACKm302.png" alt="法律咨询"></span><span class="shop-title">法律咨询</span></a></li><li><a href="https://zhineng.book118.com/merchant.html?type=30&amp;from=pc-view" target="_blank" title="教案撰写" owa-href="had" owa-btn="had"><span class="cover"><img class="lazy-success" src="//img.book118.com/sr1/M00/0A/01/wKh2C2MXDWSIK_wsAAAcvjHaZ98AA5dnwHbkJ8AABzW431.png" data-src="//img.book118.com/sr1/M00/0A/01/wKh2C2MXDWSIK_wsAAAcvjHaZ98AA5dnwHbkJ8AABzW431.png" alt="教案撰写"></span><span class="shop-title">教案撰写</span></a></li><li><a href="https://zhineng.book118.com/merchant.html?type=13&amp;from=pc-view" target="_blank" title="论文写作辅导" owa-href="had" owa-btn="had"><span class="cover"><img class="lazy-success" src="//img.book118.com/sr1/M00/36/09/wKh2C2MXDVSICirqAAAcC5v_umEAAV0ggC1rtIAABwj994.png" data-src="//img.book118.com/sr1/M00/36/09/wKh2C2MXDVSICirqAAAcC5v_umEAAV0ggC1rtIAABwj994.png" alt="论文写作辅导"></span><span class="shop-title">论文写作辅导</span></a></li></ul><i class="fix">定制咨询</i></div><div class="webpreview-split">&nbsp;</div><div class="webpreview-item" data-id="3" style="min-height: 1218px;"><img oncontextmenu="return false;" ondragstart="return false;" onload="WebPreview.Image.onLoad(this)" onerror="WebPreview.Image.onError(this)" class="" data-src="//view-cache.book118.com/view21/M03/03/2A/wKh2DmGVlWKAWijoAACu1WNGtX8348.png" src="//view-cache.book118.com/view21/M03/03/2A/wKh2DmGVlWKAWijoAACu1WNGtX8348.png" style="display: block;"></div><div class="webpreview-split"></div><div class="webpreview-recommend re" data-re_id="3"><ul class="re-pic" id="re_pic_3"><li><a href="https://zhuanjia.book118.com" target="_blank" title="专家库" owa-href="had" owa-btn="had"><img class="lazy-success" src="//img.book118.com/sr1/M00/04/19/wKh2C2Km8RuIcpPaAACMFg73qiwAA3Q6AC7I5AAAIwu166.png" data-src="//img.book118.com/sr1/M00/04/19/wKh2C2Km8RuIcpPaAACMFg73qiwAA3Q6AC7I5AAAIwu166.png" alt="专家库"></a></li></ul><i class="fix">专家库</i></div><div class="webpreview-split">&nbsp;</div><div class="webpreview-item" data-id="4" style="min-height: 1218px;"><img oncontextmenu="return false;" ondragstart="return false;" onload="WebPreview.Image.onLoad(this)" onerror="WebPreview.Image.onError(this)" class="" data-src="//view-cache.book118.com/view21/M04/03/2A/view_1_2AE1kWj@OIIM6QFj_UR2VqetqW8EuNZ0r1YhmkaBr9o=.png" src="//view-cache.book118.com/view21/M04/03/2A/view_1_2AE1kWj@OIIM6QFj_UR2VqetqW8EuNZ0r1YhmkaBr9o=.png" style="display: block;"></div><div class="webpreview-split"></div><div class="webpreview-recommend re" data-re_id="4"><ul class="re-tag" id="re_tag_4"><li><a href="/search.html?q=优才4 岁计算小能手" target="_blank" title="优才4 岁计算小能手" owa-href="had" owa-btn="had">优才4 岁计算小能手</a></li><li><a href="/search.html?q=4岁小娃计算小能手" target="_blank" title="4岁小娃计算小能手" owa-href="had" owa-btn="had">4岁小娃计算小能手</a></li><li><a href="/search.html?q=4岁小娃优才计算" target="_blank" title="4岁小娃优才计算" owa-href="had" owa-btn="had">4岁小娃优才计算</a></li><li><a href="/search.html?q=优才计算小能手" target="_blank" title="优才计算小能手" owa-href="had" owa-btn="had">优才计算小能手</a></li><li><a href="/search.html?q=5岁小娃计算小能手" target="_blank" title="5岁小娃计算小能手" owa-href="had" owa-btn="had">5岁小娃计算小能手</a></li><li><a href="/search.html?q=4岁优才计算" target="_blank" title="4岁优才计算" owa-href="had" owa-btn="had">4岁优才计算</a></li><li><a href="/search.html?q=5岁计算小能手" target="_blank" title="5岁计算小能手" owa-href="had" owa-btn="had">5岁计算小能手</a></li><li><a href="/search.html?q=4岁小娃第二阶段计算" target="_blank" title="4岁小娃第二阶段计算" owa-href="had" owa-btn="had">4岁小娃第二阶段计算</a></li><li><a href="/search.html?q=4岁优才" target="_blank" title="4岁优才" owa-href="had" owa-btn="had">4岁优才</a></li></ul><i class="fix">他们都在搜索</i></div><div class="webpreview-split">&nbsp;</div><div class="webpreview-item" data-id="5" style="min-height: 1218px;"><img oncontextmenu="return false;" ondragstart="return false;" onload="WebPreview.Image.onLoad(this)" onerror="WebPreview.Image.onError(this)" class="" data-src="//view-cache.book118.com/view21/M00/03/29/wKh2EGGVlWGAcP9RAACx20PLQrI243.png" src="//view-cache.book118.com/view21/M00/03/29/wKh2EGGVlWGAcP9RAACx20PLQrI243.png" style="display: block;"></div><div class="webpreview-split"></div><div class="webpreview-recommend re" data-re_id="5"><ul class="re-pic" id="re_pic_5"><li><a href="/user_center_v1/upload/Upload/ordinary.html?from=view" target="_blank" title="上传文档" owa-href="had" owa-btn="had"><img class="lazy-success" src="//img.book118.com/sr1/M00/06/33/wKh2AmI0OrSIMIHtAABFLqYlVLEAA1UYgHcsoAAAEVG371.png" data-src="//img.book118.com/sr1/M00/06/33/wKh2AmI0OrSIMIHtAABFLqYlVLEAA1UYgHcsoAAAEVG371.png" alt="上传文档"></a></li></ul><i class="fix">上传文档</i></div><div class="webpreview-split">&nbsp;</div><div class="webpreview-grab"></div><div class="webpreview-item" data-id="6" style="min-height: 1218px;"><img oncontextmenu="return false;" ondragstart="return false;" onload="WebPreview.Image.onLoad(this)" onerror="WebPreview.Image.onError(this)" src="//view-cache.book118.com/view21/M03/03/2A/wKh2DmGVlWGAT_gjAAC1Ge4NI4A247.png" style="display: block;"></div><div class="webpreview-split"></div><div class="webpreview-recommend re" data-re_id="6"><ul class="re-shop" id="re_shop_6"><li><a href="https://zhineng.book118.com/merchant.html?type=27&amp;from=pc-view" target="_blank" title="PPT定制" owa-href="had" owa-btn="had"><span class="cover"><img class="lazy-success" src="//img.book118.com/sr1/M00/0A/01/wKh2C2MXDYiIfJJgAAAgRcuP5HAAA5dnwH6bU4AACBd530.png" data-src="//img.book118.com/sr1/M00/0A/01/wKh2C2MXDYiIfJJgAAAgRcuP5HAAA5dnwH6bU4AACBd530.png" alt="PPT定制"></span><span class="shop-title">PPT定制</span></a></li><li><a href="https://zhineng.book118.com/merchant.html?type=19&amp;from=pc-view" target="_blank" title="标书撰写" owa-href="had" owa-btn="had"><span class="cover"><img class="lazy-success" src="//img.book118.com/sr1/M00/0A/01/wKh2C2MXDYCIaHxTAAAg6zAsGaoAA5dnwHv1rUAACED949.png" data-src="//img.book118.com/sr1/M00/0A/01/wKh2C2MXDYCIaHxTAAAg6zAsGaoAA5dnwHv1rUAACED949.png" alt="标书撰写"></span><span class="shop-title">标书撰写</span></a></li><li><a href="https://zhineng.book118.com/merchant.html?type=74&amp;from=pc-view" target="_blank" title="法律咨询" owa-href="had" owa-btn="had"><span class="cover"><img class="lazy-success" src="//img.book118.com/sr1/M00/0A/01/wKh2C2MXDXGIWNmmAAAijr6FmO4AA5dnwHlMGoAACKm302.png" data-src="//img.book118.com/sr1/M00/0A/01/wKh2C2MXDXGIWNmmAAAijr6FmO4AA5dnwHlMGoAACKm302.png" alt="法律咨询"></span><span class="shop-title">法律咨询</span></a></li><li><a href="https://zhineng.book118.com/merchant.html?type=30&amp;from=pc-view" target="_blank" title="教案撰写" owa-href="had" owa-btn="had"><span class="cover"><img class="lazy-success" src="//img.book118.com/sr1/M00/0A/01/wKh2C2MXDWSIK_wsAAAcvjHaZ98AA5dnwHbkJ8AABzW431.png" data-src="//img.book118.com/sr1/M00/0A/01/wKh2C2MXDWSIK_wsAAAcvjHaZ98AA5dnwHbkJ8AABzW431.png" alt="教案撰写"></span><span class="shop-title">教案撰写</span></a></li><li><a href="https://zhineng.book118.com/merchant.html?type=13&amp;from=pc-view" target="_blank" title="论文写作辅导" owa-href="had" owa-btn="had"><span class="cover"><img class="lazy-success" src="//img.book118.com/sr1/M00/36/09/wKh2C2MXDVSICirqAAAcC5v_umEAAV0ggC1rtIAABwj994.png" data-src="//img.book118.com/sr1/M00/36/09/wKh2C2MXDVSICirqAAAcC5v_umEAAV0ggC1rtIAABwj994.png" alt="论文写作辅导"></span><span class="shop-title">论文写作辅导</span></a></li></ul><i class="fix">定制咨询</i></div><div class="webpreview-split">&nbsp;</div><div class="webpreview-item" data-id="7" style="min-height: 1218px;"><img oncontextmenu="return false;" ondragstart="return false;" onload="WebPreview.Image.onLoad(this)" onerror="WebPreview.Image.onError(this)" class="" data-src="//view-cache.book118.com/view21/M05/03/29/wKh2EGGVlWGALnN6AAC0wZeP-vo539.png" src="//view-cache.book118.com/view21/M05/03/29/wKh2EGGVlWGALnN6AAC0wZeP-vo539.png" style="display: block;"></div><div class="webpreview-split">&nbsp;</div></div>

'''
# pattern = '//view-cache\.book118\.com/view21/.*?\.png'
pattern = '//view-cache\.book118\.com/view21/.*?\.png'
# pattern = 'http://www\.doczj\.com/pic/view\?.*?sys_ver=2.3.7'
'''
http://appwk.baidu.com/naapi/doc/view?ih=521&rn=1&doc_id=f25f6ce9a517866fb84ae45c3b3567ec112ddc5f&o=jpg_6_0_______&pn=1&iw=737&ix=0&sign=425b9876cf168059040542fe935f88a8&type=1&iy=0&aimw=737&app_ver=2.9.8.2&ua=bd_800_800_IncredibleS_2.9.8.2_2.3.7&bid=1&app_ua=IncredibleS&uid=&cuid=&fr=3&Bdi_bear=WIFI&from=3_10000&bduss=&pid=1&screen=800_800&sys_ver=2.3.7
http://appwk.baidu.com/naapi/doc/view?ih=509&rn=1&doc_id=f25f6ce9a517866fb84ae45c3b3567ec112ddc5f&o=jpg_6_0_______&pn=2&iw=742&ix=0&sign=07aea1df774fb74434618bd6290b7f73&type=1&iy=0&aimw=742&app_ver=2.9.8.2&ua=bd_800_800_IncredibleS_2.9.8.2_2.3.7&bid=1&app_ua=IncredibleS&uid=&cuid=&fr=3&Bdi_bear=WIFI&from=3_10000&bduss=&pid=1&screen=800_800&sys_ver=2.3.7
http://appwk.baidu.com/naapi/doc/view?ih=430&rn=1&doc_id=f25f6ce9a517866fb84ae45c3b3567ec112ddc5f&o=jpg_6_0_______&pn=2&iw=748&ix=0&sign=07aea1df774fb74434618bd6290b7f73&type=1&iy=509&aimw=748&app_ver=2.9.8.2&ua=bd_800_800_IncredibleS_2.9.8.2_2.3.7&bid=1&app_ua=IncredibleS&uid=&cuid=&fr=3&Bdi_bear=WIFI&from=3_10000&bduss=&pid=1&screen=800_800&sys_ver=2.3.7

'''
Directory = 'd:\\test\\' 

DownloadByContent(content, pattern, Directory,protocol='https:') 

urls = [
    'http://www.doczj.com/doc/fc2877231.html',
    'http://www.doczj.com/doc/fc2877231-1.html',
    'http://www.doczj.com/doc/fc2877231-2.html',
    'http://www.doczj.com/doc/fc2877231-3.html',
    'http://www.doczj.com/doc/fc2877231-4.html',
    'http://www.doczj.com/doc/fc2877231-5.html',
    'http://www.doczj.com/doc/fc2877231-6.html',
    'http://www.doczj.com/doc/fc2877231-7.html'

]
# for url in urls:
#     DownloadByURL(url, pattern,Directory,NeedAutoFileName=True)

 