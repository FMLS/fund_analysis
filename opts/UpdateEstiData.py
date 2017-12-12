#encoding=utf-8

import time
import threading

from funds.Fund import Fund
from store.FundEstiData  import FundEstiData

class UpdateEstiData(threading.Thread):

    def __init__(self, code):
        super(UpdateEstiData, self).__init__()
        self.__fund_obj = Fund(code)

    def do_update_estimation_data(self):
        while True:
            try:
                res = self.__fund_obj.get_real_time_estimation()
                record = FundEstiData()
                record.code = res['fundcode']
                record.gsz  = res['gsz']
                record.gszzl = res['gszzl']
                record.gztime = res['gztime']
                if not record.exists():
                    record.insert()
                else:
                    print (record, 'exists')
                time.sleep(5)
            except Exception as err:
                time.sleep(10)
                print(err)

    def run(self):
        self.do_update_estimation_data()

if '__main__' == __name__:
    obj1 = UpdateEstiData('001986')
    obj1.setDaemon(True)
    obj1.start()

    obj2 = UpdateEstiData('001878')
    obj2.setDaemon(True)
    obj2.start()

    obj3 = UpdateEstiData('004450')
    obj3.setDaemon(True)
    obj3.start()

    time.sleep(3600 * 8)
