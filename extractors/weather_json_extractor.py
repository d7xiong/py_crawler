# -*- coding:utf-8 -*-

import sys
import json
import urllib2

class WeatherJsonExtractor:

    def __init__(self):
        pass

    def extract(self, data_str):
        result = {}
        if not data_str:
            return result

        data = json.loads(data_str) 

        status = data.get('errNum', -1)
        if 0 != status:
            return result

        ret_data = data.get('retData')


        result['city'] = ret_data.get('city')
        result['city_id'] = ret_data.get('cityid')
        today = ret_data.get('today')
        forecast = ret_data.get('forecast')
        history = ret_data.get('history')

        result['today'] = self._extractor_today(today)
        result['forecast'] = self._extractor_forecast(forecast)
        result['history'] = self._extractor_history(history)
        return result


    def _extractor_history(self, history):
        res_list = []
        if not history:
            return res_list
        for data in history:
            res = {}
            res['date'] = data.get('date','0000-00-00')
            res['week'] = data.get('week', '0')
            res['fengxiang'] = data.get('fengxiang', '无')
            res['fengli'] = data.get('fengli', '无')
            res['hightemp'] = data.get('hightemp', '100')
            res['lowtemp'] = data.get('lowtemp', '-100')
            res['type'] = data.get('type', '无')
            res_list.append(res)
        return res_list
            

    def _extractor_forecast(self, forecast):
        res_list = []
        if not forecast:
            return res_list
        for data in forecast:
            res = {}
            res['date'] = data.get('date','0000-00-00')
            res['week'] = data.get('week', '0')
            res['fengxiang'] = data.get('fengxiang', '无')
            res['fengli'] = data.get('fengli', '无')
            res['hightemp'] = data.get('hightemp', '100')
            res['lowtemp'] = data.get('lowtemp', '-100')
            res['type'] = data.get('type', '无')
            res_list.append(res)
        return res_list

    def _extractor_today(self,data):
        res = {}
        if not data:
            return res
        res['date'] = data.get('date','0000-00-00')
        res['week'] = data.get('week', '0')
        res['cur_temp'] = data.get('curTemp', '-100')
        res['aqi'] = data.get('aqi', '0')
        res['fengxiang'] = data.get('fengxiang', '无')
        res['fengli'] = data.get('fengli', '无')
        res['hightemp'] = data.get('hightemp', '100')
        res['lowtemp'] = data.get('lowtemp', '-100')
        res['type'] = data.get('type', '无')
        res['index'] = data.get('index', [''])
        return res
            
        
if __name__ == '__main__':
    
    url = 'http://apis.baidu.com/apistore/weatherservice/recentweathers?cityid=101010100'
    apikey = 'your_api_key'

    req = urllib2.Request(url)
    req.add_header('apikey', apikey)

    resp = urllib2.urlopen(req)
    content = resp.read()
    
    weather_extractor = WeatherJsonExtractor()
    res = weather_extractor.extract(content)
    print(json.dumps(res))



