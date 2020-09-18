#-*- coding: UTF-8 -*-
import datetime
import unittest

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from emc.kb.testing import INTEGRATION_TESTING
#sqlarchemy
from sqlalchemy import text
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base

import datetime
from emc.policy import fmt
from emc.kb import ora_engine as engine
from  emc.kb import ORMBase as Base
from emc.kb.interfaces import IDbapi
from zope.component import queryUtility
from  emc.kb.tests.base import LOGTABLES as TABLES

class TestLogDatabase(unittest.TestCase):

    layer = INTEGRATION_TESTING
#          mapper single create or drop
#         UserLog.__table__.drop(engine)
#         UserLog.__table__.create(engine)

    def drop_tables(self,tbls=None):
        """drop all db tables
        """

        for tb in tbls:
            import_str = "from %(p)s import %(t)s" % dict(p='emc.kb.mapping_log_db',t=tb) 
            exec import_str
        Base.metadata.drop_all(engine)                                

    def empty_tables(self,tbls=None):
        """clear all db tables
        """
        if not bool(tbls):
            tbls = TABLES       
        items = []
        for tb in tbls:
            import_str = "from %(p)s import %(t)s as tablecls" % dict(p='emc.kb.mapping_log_db',t=tb) 
            exec import_str
            items.extend(Session.query(tablecls).all())
        for m in items:
            Session.delete(m)                    
        Session.commit()

    def create_tables(self,tbls=None):
        """create all db tables
        """

        for tb in tbls:
            import_str = "from %(p)s import %(t)s as tablecls" % dict(p='emc.kb.mapping_log_db',t=tb) 
            exec import_str
        Base.metadata.create_all(engine)

    def setUp(self):
        import os
        os.environ['NLS_LANG'] = '.AL32UTF8'
        self.create_tables(tbls=TABLES)

    def tearDown(self):
#         self.empty_tables(tbls=TABLES)
        self.drop_tables(tbls=TABLES)
        
    def batch_create_tables(self):
        tbls = TABLES
        self.create_tables(tbls)
#         self.drop_tables(tbls)

    def test_dbapi_fetch_rownum(self):
        self.add_adminlog()
        dbapi = queryUtility(IDbapi, name='adminlog')
        num = dbapi.get_rownumber()
        self.assertTrue(num is not None)
        
    def test_dbapi_fetch_oldest(self):        
        self.add_adminlog()
        dbapi = queryUtility(IDbapi, name='adminlog')
        num = dbapi.fetch_oldest()
        self.assertTrue(num is not None)        

    def test_dbapi_bulk_del(self):

        value = {'adminid':'adm','userid':'user5','datetime':datetime.datetime.now().strftime(fmt),
                  'ip':u"192.168.3.108",'type':0,'operlevel':4,'result':1,'description':u'adm create了用户user5'}
        value2 = {'adminid':'tyj','userid':'user9','datetime':datetime.datetime.now().strftime(fmt),
                  'ip':u"192.168.3.109",'type':0,'operlevel':4,'result':1,'description':u'adm modified用户user9'}
        self.add_adminlog()
        self.add_adminlog(values=value)
        self.add_adminlog(values=value2)
        dbapi = queryUtility(IDbapi, name='adminlog')
        num = dbapi.get_rownumber()
        dbapi.bulk_delete(2)
        num2 = dbapi.get_rownumber()
        self.assertEqual(num2 +2,num)

  
    def add_adminlog(self,values=None):
        dbapi = queryUtility(IDbapi, name='adminlog')
        if values==None:
            values = {'adminid':'admin','userid':'user3','datetime':datetime.datetime.now().strftime(fmt),
                  'ip':u"192.168.3.101",'type':0,'operlevel':4,'result':1,'description':u'admin删除了用户user3'}  
        dbapi.add(values)
        
    def query_adminlog_1st_id(self):
        dbapi = queryUtility(IDbapi, name='adminlog')
        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})
        if bool(nums):
            id = nums[0][0]
        return id
 
    def test_adminlog_locator(self):
        dbapi = queryUtility(IDbapi, name='adminlog')          
        self.add_adminlog()
        id = self.query_adminlog_1st_id()
        if bool(id):
            record = dbapi.getByCode(id)
            self.assertEqual(record.id,id)
            dbapi.DeleteByCode(id)
  
    def add_userlog(self,values=None):
        dbapi = queryUtility(IDbapi, name='userlog')
        if values==None:
            values = {'userid':'user3','datetime':datetime.datetime.now().strftime(fmt),
                  'ip':u"192.168.3.101",'type':0,'operlevel':4,'result':1,'description':u'admin删除了用户user3'} 
            dbapi.add(values)
            
    def query_userlog_1st_id(self):
        dbapi = queryUtility(IDbapi, name='userlog')        
        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})
        if bool(nums):
            id = nums[0][0]
        return id
 
    def test_userlog_locator(self):
        dbapi = queryUtility(IDbapi, name='userlog')          
        self.add_userlog()
        id = self.query_userlog_1st_id()
        if bool(id):
            record = dbapi.getByCode(id)
            self.assertEqual(record.id,id)
            dbapi.DeleteByCode(id)
 
 