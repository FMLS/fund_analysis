#encoding=utf-8
import sys
from store.BaseStore import BaseStore
from psycopg2 import sql

class FundEstiData(BaseStore):

    def __init__(self, fund=None):
        super(FundEstiData, self).__init__()
        if fund:
            self.code = fund.code

    def table_name(self):
        return 'fund_estimation'

    def exists(self):
        where = self.get_attr_map()
        where['table_name'] = self.table_name()
        sql_obj = sql.SQL('select * from {} where code=%(code)s and gztime=%(gztime)s').format(sql.Identifier(self.table_name()))
        res = self.execute(sql_obj, where)
        return res

    def get_latest_record(self):
        sql_obj = sql.SQL('select * from {} where code=%(code)s order by gztime desc limit 1').format(sql.Identifier(self.table_name()))
        res = self.execute(sql_obj, {'code':self.code})
        return res

if '__main__' == __name__:
    obj = FundEstiData()
    print obj.get_latest_record()
