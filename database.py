from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1, 1, database="exercises",
                                            user="postgres", password="password", host="localhost")


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.connection

    def __exit__(self, exception_type, exception_value, excepition_traceback):
        if exception_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        connection_pool.putconn(self.connection)
