import sys

import psycopg2

from conf import gconf

pg_conf = gconf.pg_conf

class BaseStore(object):
    def __init__(self):
       self.__conn = self._create_conn() 
       self.__cursor = self.__conn.cursor()

    def _create_conn(self):
        try:
            conn = psycopg2.connect(database=pg_conf['database'], user=pg_conf['user'],
                                    host=pg_conf['host'], port=pg_conf['port'],
                                    password=pg_conf['password'])
            return conn
        except BaseException, err:
            print 'error: ', type(err)
            sys.exit(0)
    

    def _get_pub_attribute(self):
        return [
                attr for attr in dir(self)
                if not attr.startswith('_') and
                   not callable(getattr(self, attr))
            ]

    def _gen_insert_sql(self):
        sql = 'INSERT INTO %s ' % self.table_name().strip()
        sql += '('
        attrs = self._get_pub_attribute()
        for attr in attrs:
            sql += attr
            sql += ','
        sql = sql[:-1]
        sql += ') VALUES ('
        for attr in attrs:
            sql += '%%(%s)s,' % attr
        sql = sql[:-1]
        sql += ')'

        return sql

    def table_name(self):
        raise AttributeError('you must inherit this method')

    def get_attr_map(self):
        attrs_map = {}
        attrs = self._get_pub_attribute()
        for attr in attrs:
            attrs_map[attr] = getattr(self, attr)
        return attrs_map

    def insert(self):
        attrs_map = self.get_attr_map()
        sql = self._gen_insert_sql()
        self.__cursor.execute(sql, attrs_map)
        self.__conn.commit()

    def execute(self, sql, attrs=None):
        self.__cursor.execute(sql, attrs)
        return self.__cursor.fetchall()

if '__main__' == __name__:
    obj = BaseStore()
