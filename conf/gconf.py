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
    },
    'fund_data_portfolio': {
        'url': 'http://fund.eastmoney.com/Data/FundDataPortfolio_Interface.aspx',
        'dt' : 14,
        'mc' :'returnjson',
        'ft' :'all',
        'pn' :5000,
        'pi' :1,
        'sc' :'abbname',
        'st' :'asc',
    }
}

pg_conf = {
    'database': 'fund',
    'user': 'pgadmin',
    'host': '127.0.0.1',
    'port': '5432',
    'password':'',
}

if '__main__' == __name__:
    print fund_data_day
