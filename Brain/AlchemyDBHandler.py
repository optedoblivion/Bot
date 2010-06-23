import sys
import sqlalchemy as sa
from sqlalchemy.orm import mapper, sessionmaker, scoped_session, clear_mappers

class AlchemyDBHandler:

    engine = None
    metadata = None
    Session = None
    model = None

    def __init__(self, engine_path=None, echo=True):
        """
            You must specify an engine path!
        """

        if not engine_path:
            print "You must specify an engine path!"
            sys.exit(1)

        self.engine = sa.create_engine(engine_path,echo=echo,pool_recycle=3600)
        self.metadata = sa.MetaData()

    def importModel(self, modelName=None):
        if not modelName:
            print "Model name not provided!"
            sys.exit(1)
        exec'import %s as model'%modelName
        for object in dir(model):

            tableoverride = None
            foreignkeys = None

            if object == "__tableoverride__":
                tableoverride = object.__tableoverride__
            if object == "__foreignkeys__":
                foreignkeys = object.__foreignkeys__

            if object[0] != "_":
                exec'global t_%s'%object
                if tableoverride:
                    exec"%s"%(model.tableoverride%(object, object))
                else:
                    if foreignkeys:
                        pass
                    else:
                        exe = """t_%s=sa.Table('%s', self.metadata, """
                        exe += """autoload=True, autoload_with=self.engine)"""
                        exe = exe%(object, object)
                        exec'%s'%exe
                exec'mapper(model.%s, t_%s)'%(object, object)

        self.model = model
        sm = sessionmaker(bind=self.engine)
        self.model._Session = scoped_session(sm)

    def close(self):
        self.Session.close()
        clear_mappers()