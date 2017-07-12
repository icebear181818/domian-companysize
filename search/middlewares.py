# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import scrapy
import logging
from user_agents  import agents
class proxMiddleware(object):

    proxy_list=[
        "http://44.217.207.178:80",
        "http://112.140.184.136:3128",
        "http://114.159.167.211:8080",
        "http://03.14.27.134:8080",
        "http://36.66.83.239:8080",
        "http://118.193.142.61:3128",
        "http://190.147.208.143:8080",
        "http://95.97.216.165:8090",
        "http://113.20.141.52:8080",
        "http://182.253.236.74:8080",
        "http://94.75.70.66:8080",
        "http://181.49.44.14   :8080"]
    def process_request(self,request,spider):
        # if not request.meta['proxies']:
        ip = random.choice(self.proxy_list)

        #print 'ip=' %ip
        request.meta['proxy'] = ip


class UserAgentMiddleware(object):


    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent