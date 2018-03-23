# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy import signals
import json
import codecs
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
num = 0
class WenmanPipeline(object):
    def process_item(self, item, spider):
        '''
        this_item['url'] = this_url
        this_item['from_url'] = from_url
        this_item['title'] = title
        this_item['gender_age'] = sex_age_time
        this_item['answers'] = answers
        this_item['path'] = path
        this_item['detail'] = c
        :param item:
        :param spider:
        :return:
        '''


        test_dict = {'hospital_phone': item['hospital_phone'],
                     'hospital_address': item['hospital_address'],
                     'hospital_intro': item['hospital_intro'],
                     'hospital_level': item['hospital_level'],
                     'hospital_name': item['hospital_name'],
                     'hospital_type': item['hospital_type']

                     }
        test_txt = '|+|'.join([item['hospital_name'] , item['hospital_type'] ,
         item['hospital_level'],item['hospital_address'], item['hospital_phone']  \
            ,item['hospital_intro']])


        file_path = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'file'),
                                 'hospital.txt')

        fp = open(file_path, 'a')
        # fp.write(json.dumps(test_dict) + '\n')
        fp.write(str(test_dict)+'\n')
        fp.close()
        global  num
        num += 1
        print('writed {} content!!!!'.format(num))
        return item
