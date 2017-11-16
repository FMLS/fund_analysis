#encoding=utf-8

import re
import requests

from conf import gconf
from store.FundDailyData import FundDailyData

pattern_data = r'''
<tr>
<td>(?P<date>\d{4}-\d{1,2}-\d{1,2})</td>
<td\sclass='.*?'>(?P<nav>[\d\.]*)</td>
<td\sclass='.*?'>(?P<jj_lggz>[\d\.]*)</td>
<td\sclass='.*?'>(?P<growth_rate>[-\d\.]*)%</td>
<td>(?P<subscription_status>.*?)</td>
<td>(?P<redemption_status>.*?)</td>
<td\sclass='.*?'>(?P<dividends>.*?)</td>
</tr>
'''

pattern_params = r'''
records:(?P<records>\d+).*
pages:(?P<pages>\d+).*
'''

fund_day_addr_info = gconf.urls['fund_data_day']
fund_day_url = fund_day_addr_info['url']

class Fund(object):
    def __init__(self, code):
        self.code = code
        self.per = 10
    
    def get_day_data_total_pages(self):
        pages   = 0
        records = 0

        url_args = fund_day_addr_info['url_args']
        url_args['code'] = self.code
        url_args['page'] = 1
        url_args['per'] = self.per
        
        result = requests.get(fund_day_url, url_args)
        m = re.search(pattern_params, result.text, re.VERBOSE)
        if m:
            records = int(m.group('records'))
            pages   = int(m.group('pages'))
        
        return {'records':records, 'pages': pages}

    def collect_data_per_day(self):
        res = self.get_day_data_total_pages()

        url_args = fund_day_addr_info['url_args']
        url_args['code'] = self.code
        url_args['per'] = self.per

        record = {}
        for i in range(1, res['pages'] + 1):
            url_args['page'] = i
            result = requests.get(fund_day_url, url_args)
            m = re.finditer(pattern_data, result.text, re.VERBOSE)
            for item in m:
                record['code'] = self.code
                record['date'] = item.group('date')
                record['nav']  = item.group('nav')
                record['jj_lggz']     = item.group('jj_lggz')
                record['growth_rate'] = item.group('growth_rate')
                record['subscription_status'] = item.group('subscription_status')
                record['redemption_status']   = item.group('dividends')
                
                yield record

    def save_data_per_day(self):
        for item in obj.collect_data_per_day():
            record = FundDailyData()
            record.code = item['code']
            record.date = item['date']
            record.nav  = item['nav']
            record.jj_lggz     = item['jj_lggz']
            record.growth_rate = item['growth_rate']
            record.subscription_status = item['subscription_status']
            record.redemption_status   = item['redemption_status']
            record.insert()

if '__main__' == __name__:
    obj = Fund('001986')
    obj.save_data_per_day()
