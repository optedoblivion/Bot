from sa_utils import insert_select
from sqlalchemy import literal_column, union
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import and_, select
from sqlalchemy.sql.functions import count

class BaseTable(object):
    
    """
        Table base class
    """
    
    __table__ = None
    __tablename__ = None
    
    @property
    def session(self):
        """
            Returns instance of object session.
        """
        return Session.object_session(self)
    
    def __iter__(self):
        """
            This makes a table instance iterable by its columns.
            Can be case as a dictionary.
        """
        class_table = self.__table__
        for col in class_table.c:
            col_name = col.name
            yield(col_name.encode("utf8", "replace"), getattr(self, col_name))
        