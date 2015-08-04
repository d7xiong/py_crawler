# -*- coding:utf-8 -*-

import urllib2
import json
from extractors.weather_json_extractor import WeatherJsonExtractor
from etl.weather_etl import WeatherETL

class WeatherCrawler:

    def __init__(self):
        pass

    def run(self):

        url = 'http://apis.baidu.com/apistore/weatherservice/recentweathers?cityid=101010100'

        weather_data = self.download(url)
        
        extractor = WeatherJsonExtractor()
        etl = WeatherETL()

        res_ext = extractor.extract(weather_data)
        res_etl = etl.process(res_ext)

        print json.dumps(res_etl)

    def download(self, url):
        req = urllib2.Request(url)
        apikey = ''
        req.add_header('apikey', apikey)
        resp = urllib2.urlopen(req)
        content = resp.read()
        return content


if __name__ == '__main__':
    weather_crawler = WeatherCrawler()
    weather_crawler.run()
