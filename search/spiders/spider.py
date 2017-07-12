from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from search.items import SearchItem
import re
from scrapy.selector import HtmlXPathSelector

class Spider(CrawlSpider):
    name="search"

    # file=open(r'C:\Users\jessica_zhu1\Desktop\Book1.txt', 'r+')
    # read=file.readlines()
    # file.close()
    name = "search"
    with open(r'C:\Users\jessica_zhu1\Desktop\list', 'r') as r:
        f = r.readlines()
    kw = set(f)
    finished = set()



    def start_requests(self):
        while True:
            code=self.kw.pop()
            code=code.strip('\n')
            item=SearchItem()
            item['keyword']=code
            sic_url='http://www.alexa.com/siteinfo/%s'%code
            yield Request(url=sic_url,meta={"item":item['keyword']},callback=self.parse0)

    def parse0(self, response):
        item = SearchItem()
        selector = Selector(response)
        text0 = selector.xpath('//div/strong[@class="metrics-data align-vmiddle"]/text()').extract()[1].strip()
        text1 = selector.xpath('//span[@class="font-4 box1-r"]/text()').extract()[0]
        item['result'] = text0
        item['keyword'] = response.meta['item']
        item['link']=text1


        yield item

# class Spider(CrawlSpider):
#     name="search"
#     with open(r'input', 'r') as r:
#         f=r.readlines()
#     kw=set(f)
#     finished=set()
#     def start_requests(self):
#         while self.kw.__len__():
#             code=self.kw.pop()
#             self.finished.add(code)
#             code=code.strip('\n')
#             item=SearchItem()
#             item['keyword']=code
#             sic_url='https://www.google.com/search?q=%s'%code
#             yield Request(url=sic_url,meta={"item":item['keyword']},callback=self.parse0)
#
#     def parse0(self,response):
#         item = SearchItem()
#         selector = Selector(response)
#         text0 = selector.xpath('//div[@id="resultStats"]/text()').extract()
#         text0 = ''.join(text0)
#         num = re.findall(r'\d+', text0)
#         item['result'] = ''.join(num)
#         item['keyword'] = response.meta['item']
#         if item['keyword'] not in self.finished:
#             self.kw.add(item['keyword'])
#
#
#         yield item