import sys

import psycopg2

from conf import gconf

pg_conf = gconf.pg_conf

class BaseStore(object):
    def __init__(self):
       self._create_conn() 

    def _create_conn(self):
        try:
            self.conn = psycopg2.connect(database=pg_conf['database'], user=pg_conf['user'],
                                         host=pg_conf['host'], port=pg_conf['port'],
                                         password=pg_conf['password'])
        except BaseException, err:
            sys.exit(0)


if '__main__' == __name__:
    obj = BaseStore()
