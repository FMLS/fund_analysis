#encoding=utf-8

from funds.Fund import Fund
from store.FundDailyData import FundDailyData

class FundOrgData(object):
    
    def __init__(self, fund_obj):
        self.__fund_obj = fund_obj

    def save_daily_data(self):
        for item in self.__fund_obj.get_daily_data():
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
    fund_obj = Fund('001986')
    db_obj = FundOrgData(fund_obj)
    db_obj.save_daily_data()
