#encoding=utf-8
import random

urls = {
    'fund_data_day' : {
        'url': 'http://fund.eastmoney.com/f10/F10DataApi.aspx',
        'url_args': {
            'type': 'lsjz',
            'code': None,
            'page': None,
            'per' : None,
            'sdate': '',
            'edate': '',
            'rt'   : random.random()
        }
    }
}

if '__main__' == __name__:
    print fund_data_day
