#encoding=utf-8

from threading import Timer

from funds.Fund import Fund
from store.FundDailyData import FundDailyData
from store.FundEstiData  import FundEstiData

class FundOrgData(object):
    
    def __init__(self, fund_obj):
        self.__fund_obj = fund_obj

    def update_daily_data(self):
        for item in self.__fund_obj.get_daily_data():
            record = FundDailyData()
            record.code = item['code']
            record.date = item['date']
            record.nav  = item['nav']
            record.jj_lggz     = item['jj_lggz']
            record.growth_rate = item['growth_rate']
            record.subscription_status = item['subscription_status']
            record.redemption_status   = item['redemption_status']
            if not record.exists():
                record.insert()
            else:
                print 'skip'

    def get_daily_data(self):
        pass

    def do_update_estimation_data(self):
        res = self.__fund_obj.get_real_time_estimation()
        record = FundEstiData()
        print res
        record.code = res['fundcode']
        record.gsz  = res['gsz']
        record.gszzl = res['gszzl']
        record.gztime = res['gztime']
        record.insert()

    def update_estimation_data(self):
        timer = Timer(30, self.do_update_estimation_data())
        timer.start()

if '__main__' == __name__:
    fund_obj = Fund('001986')
    db_obj = FundOrgData(fund_obj)
    db_obj.update_estimation_data()
