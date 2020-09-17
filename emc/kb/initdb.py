#-*- coding: UTF-8 -*-
from emc.kb import log_session as Session
from emc.kb import ora_engine as engine
from  emc.kb import ORMBase as Base
from  emc.kb.tests.base import TABLES


class DbTools(object):

    def drop_tables(self,tbls=None):
        """drop all db tables
        """

        for tb in tbls:
            import_str = "from %(p)s import %(t)s" % dict(p='emc.kb.mapping_db',t=tb) 
            exec import_str
        Base.metadata.drop_all(engine)                                

    def empty_tables(self,tbls=None):
        """clear all db tables
        """
        if not bool(tbls):
            tbls = TABLES       
        items = []
        for tb in tbls:
            import_str = "from %(p)s import %(t)s as tablecls" % dict(p='emc.kb.mapping_db',t=tb) 
            exec import_str
            items.extend(Session.query(tablecls).all())
        for m in items:
            Session.delete(m)                    
        Session.commit()

    def create_tables(self,tbls=None):
        """create all db tables
        """
        if not bool(tbls):
            tbls = TABLES  
        for tb in tbls:
            import_str = "from %(p)s import %(t)s as tablecls" % dict(p='emc.kb.mapping_db',t=tb) 
            exec import_str
        Base.metadata.create_all(engine)

def main():
    print("haha")
    pass

if __name__ == '__main__':
    main()
        
