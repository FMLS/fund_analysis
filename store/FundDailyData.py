#encoding=utf-8

from store.BaseStore import BaseStore

class FundDailyData(BaseStore):
    
    def __init__(self):
        super(FundDailyData, self).__init__()

    def table_name(self):
            return 'fund_daily_data'

if '__main__' == __name__:

    obj = FundDailyData()
    obj.nav = 12
    obj.code = '0011'
    obj.date = '2017-11-11'
    obj.jj_lggz     = 0.012
    obj.growth_rate = 0.012 
    obj.subscription_status = '开放申购'
    obj.redemption_status = '开放赎回'
    obj.insert()
