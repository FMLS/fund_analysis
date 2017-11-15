import psycopg2

from conf import gconf

class BaseStore(object):
    def __init__(self):
       self._create_conn() 

    def _create_conn(self):
        self.conn = psycopg2.connect(database=kwargs['database'], user=kwargs['user'],
                                     host=kwargs['host'], port=kwargs['port'],
                                     password=kwargs['password'])
        except BaseException, err:
            logger.error(str(err))
            sys.exit(0)
