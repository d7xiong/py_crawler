# -*- coding:utf-8 -*-


class WeatherETL:

    def __init__(self):
        pass

    
    def process(self,weather_dict):
        res_list = []
        if not weather_dict:
            return res_list

        res = {}

        res['city'] = weather_dict.get('city','无')
        res['city_id'] = weather_dict.get('city_id','无')
        history = weather_dict.get('history',[])

        index = len(history) - 1

        res['history'] = history[index] if index >= 0 else {}

        res_list.append(res)
        return res_list
