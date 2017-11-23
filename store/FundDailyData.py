#encoding=utf-8
import sys
from store.BaseStore import BaseStore
from psycopg2 import sql

class FundDailyData(BaseStore):
    
    def __init__(self):
        super(FundDailyData, self).__init__()

    def table_name(self):
        return 'fund_daily_data'

    def exists(self):
        where = self.get_attr_map()
        where['table_name'] = self.table_name()
        sql_obj = sql.SQL('select * from {} where code=%(code)s and date=%(date)s').format(sql.Identifier(self.table_name()))
        res = self.execute(sql_obj, where)
        return res

    def get_columns(self, order_field, order):
        cond = {}
        cond['order_field'] = order_field
        cond['order'] = order
        sql_obj = sql.SQL('select * from {} order by %(order_field)s %(order)s'%cond).format(sql.Identifier(self.table_name()))
        res = self.execute(sql_obj, cond)
        return res

if '__main__' == __name__:

    obj = FundDailyData()
    ls = obj.get_columns('date', 'desc')
    for i in ls:
        print i[2]
    #obj.nav = 12
    #obj.code = '0011'
    #obj.date = '2017-11-11'
    #obj.jj_lggz     = 0.012
    #obj.growth_rate = 0.012 
    #obj.subscription_status = '开放申购'
    #obj.redemption_status = '开放赎回'
    #obj.insert()
