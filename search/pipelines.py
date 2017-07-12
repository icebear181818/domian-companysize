# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from search.items import SearchItem


class SearchPipeline(object):
    # def __init__(self):
    #     self.tem = []

    def process_item(self, item, spider):


        self.text = open('output1', 'a+')

        item['result']=item['result'].replace(",", "")
        if item['result']=='':
            item['result']='0'
        #self.text.write(item['keyword'] + ' ' + item['result']  + '\n')
        self.text.write(item['keyword'] + ' ' + item['result'] +' ' + item['link']+'\n')
        self.text.close()

        return item
