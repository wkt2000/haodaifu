# -*- coding: utf-8 -*-
import sys

__author__ = 'rujia'
import scrapy

from ..items import WenmanItem
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
class Ask39Spider(scrapy.Spider):
    name = 'haodaifu'
    start_urls = [
        'http://www.haodf.com/yiyuan/all/list.htm',
    ]
    def parse(self, response):

        diqu_url = response.xpath("//div[@class='kstl']//a/@href").extract()
        print 'diqu_url:',diqu_url
        beijin =response.xpath("//div[@class='kstl2']//a/@href").extract()
        diqu_url_all =diqu_url.extend(beijin)
        print diqu_url_all
        for each_zore in diqu_url_all:
            req = scrapy.Request(each_zore, callback=self.parse_question)
            yield req



    def parse_question(self, response):
        hospital_url = response.xpath("//div[@class='m_ctt_green']//li//a/@href").extract()
        for each in hospital_url:
            req = scrapy.Request(each, callback=self.parse_next)
            yield req

    def parse_next(self,response):
        hospital_name = response.xpath("//div[@class='hospital-detail']//h1/text()").extract()[0]
        leval_type = response.xpath("//div[@class='hospital-detail']//span[@class='hospital-label-item']//text()").extract()
        if len(leval_type) <2:
            hospital_level = ''
            hospital_type = leval_type[0]
        else:
            hospital_level = leval_type[0]
            hospital_type = \
                leval_type[1]

        hospital_site = response.xpath("//div[@class='h-d-content']//a/@href").extract()
        hospital_detail = {'hospital_name':hospital_name,'hospital_level':hospital_level,'hospital_type':hospital_type,'hospital_site':hospital_site}
        req = scrapy.Request(hospital_site[0], callback=self.parse_nex)
        req.meta['hospital_detail'] = hospital_detail
        yield req

    def parse_nex(self,response):
        hospital_intro = ''.join(response.xpath("//table[@class='czsj']//tr//text()").extract())
        hospital_detail = response.meta['hospital_detail']
        hospital_detail['hospital_intro'] = hospital_intro
        req = scrapy.Request(hospital_detail['hospital_site'][1], callback=self.parse_ne)
        req.meta['hospital_detail'] = hospital_detail
        yield req

    def parse_ne(self,response):
        hospital_phone = response.xpath('//*[@id="gray"]/div[5]/table[2]/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[2]').extract()
        hospital_address = response.xpath('//*[@id="gray"]/div[5]/table[2]/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[2]').extract()
        hospital_detail = response.meta['hospital_detail']
        hospital_intro = hospital_detail['hospital_intro']
        hospital_level = hospital_detail['hospital_level']
        hospital_name = hospital_detail['hospital_name']
        hospital_type = hospital_detail['hospital_type']
        this_item = WenmanItem()
        this_item['hospital_phone'] = hospital_phone
        this_item['hospital_address'] = hospital_address
        this_item['hospital_intro'] = hospital_intro
        this_item['hospital_level'] = hospital_level
        this_item['hospital_name'] = hospital_name
        this_item['hospital_type'] = hospital_type
        yield this_item

