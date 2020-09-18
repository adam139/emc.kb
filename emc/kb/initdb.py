#-*- coding: UTF-8 -*-
from emc.kb import log_session as Session
from emc.kb import ora_engine as engine
from  emc.kb import ORMBase as Base
from  emc.kb.tests.base import TABLES
from  emc.kb.tests.base import LOGTABLES

actions = ["create","drop","empty"]

class DbTools(object):


    def drop_tables(self,tbls=None):
        """drop all db tables
        """
        if not bool(tbls):
            tbls = TABLES       
        for tb in tbls:
            import_str = "from %(p)s import %(t)s as tablecls" % dict(p='emc.kb.mapping_db',t=tb) 
            exec import_str
            tablecls.__table__.drop(engine)
        for tb in LOGTABLES:
            import_str = "from %(p)s import %(t)s as tablecls" % dict(p='emc.kb.mapping_log_db',t=tb) 
            exec import_str
            tablecls.__table__.drop(engine)
#         Base.metadata.drop_all(engine)                                

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
        for tb in LOGTABLES:
            import_str = "from %(p)s import %(t)s as tablecls" % dict(p='emc.kb.mapping_log_db',t=tb) 
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
            tablecls.__table__.create(engine)
        for tb in LOGTABLES:
            import_str = "from %(p)s import %(t)s as tablecls" % dict(p='emc.kb.mapping_log_db',t=tb) 
            exec import_str
            tablecls.__table__.create(engine)
#         Base.metadata.create_all(engine)

def main(action=None):  
   
    import sys
    args = sys.argv
    if len(args)  >1:
        action = args[1]
    else:
        action = action or "create"
    if action not in actions:
        print("command line parameters is invalid!")
        return 1
    tool = DbTools()
    if action =="create":
        sure = raw_input("warning:This operation will create all database tables in oracle,are you sure?(yes/no):")
        if sure.upper() == "YES" or  sure.upper()=="Y":
            try:
                tool.create_tables()
                print("Oracle tables have been created successfully!")
                return 0
            except:
                print("raise some errors")
        print("None table has been created!")
        return 1
    elif action =="drop":
        sure = raw_input("dangerous!!!:This operation will drop all database tables,are you sure?(yes/no):")
        if sure.upper() == "YES" or  sure.upper()=="Y":
            try:
                tool.drop_tables()
                print("All Oracle tables have been dropped successfully!")
                return 0
            except:
                print("raise some errors")
        print("None table has been dropped!")
        return 1
    else:
        sure = raw_input("dangerous!!!:This operation will remove all database tables data,are you sure?(yes/no):")
        if sure.upper() == "YES" or  sure.upper()=="Y":
            try:
                tool.empty_tables()
                print("Oracle tables have been emptied successfully!")
                return 0
            except:
                print("raise some errors")
        print("None table has been emptied!")
        return 1
        
if __name__ == '__main__':
    main()
        
