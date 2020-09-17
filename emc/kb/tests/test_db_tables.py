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
from emc.kb.interfaces import IDbapi
from zope.component import queryUtility
from emc.kb import log_session as Session
from emc.kb import ora_engine as engine
from  emc.kb import ORMBase as Base
from  emc.kb.tests.base import TABLES


class TestDatabase(unittest.TestCase):
    layer = INTEGRATION_TESTING

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

        for tb in tbls:
            import_str = "from %(p)s import %(t)s as tablecls" % dict(p='emc.kb.mapping_db',t=tb) 
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


    def test_dbapi_fashej(self):
# ('333333002','发射机01','asd2w23sds212211111','m',2.4,0,2.8,10,0,2.8,20,1.1,'AM-V',2,1,' 常用发射机1')
        values = dict(sbdm="333333003",sbmc=u"发射机02",pcdm="asd2w23sds212211111",location=u"m",
                      freq=2.4,pd_upper=0,pd_lower=2.8,num=10,
                      freq_upper=0,freq_lower=2.8,bw=20,base_power=1.1,
                      tzlx="AM-V",bzf=2,mid_freq=1,comment1=u"常用发射机1")        
        dbapi = queryUtility(IDbapi, name='fashej')
        dbapi.add(values)
        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})
        if bool(nums):
            id = nums[0][0]
            rt = dbapi.getByCode(id)
            self.assertTrue(nums is not None)
            self.assertEqual(len(nums),1)
        else:
            print("add data failed!")



    def test_dbapi_jieshouj(self):

        
#('sb-1234','接收机1','sb-1234-1','m',1800,900,300,1500,1000,50000,-90,'1',300,1500)
        values = dict(sbdm="sb-1234",sbmc=u"接收机1",pcdm="sb-1234-1",location=u"m",
                      fb_upper=1800,fb_lower=900,freq=300,f_upper=1500,
                      f_lower=1000,bw_receiver=50000,sen_receiver=-90,mf_freq_sign='1',
                      mf_freq=300,lo_freq=1500)        
        dbapi = queryUtility(IDbapi, name='jieshouj')
        dbapi.add(values)

        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})

        id = nums[0][0]
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        self.assertTrue(rt)

 
    def test_dbapi_fashetx(self):

# ('sb-1234','接收天线1','pc-1-pass','m',10.2,'Ver',30,20,10)
        values = dict(cssbdm="sb-1234",cssbmc=u"接收天线1",pcdm="pc-1-pass",location=u"m",
                      gain=10.2,polarization='Ver',fwbskd=30,fybskd=20,txzxj=10)        
        dbapi = queryUtility(IDbapi, name='fashetx')
        dbapi.add(values)

        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})

        id = nums[0][0]       
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)
 
    def test_dbapi_jieshoutx(self):
        
# ('sb-1234','接收天线1','pc-1-pass','m',10.2,'Ver',30,20,10)
        values = dict(cssbdm="sb-1234",cssbmc=u"接收天线1",pcdm="pc-1-pass",location=u"m",
                      gain=10.2,polarization='Ver',fwbskd=30,fybskd=20,txzxj=10)        
        dbapi = queryUtility(IDbapi, name='jieshoutx')
        dbapi.add(values)

        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})

        id = nums[0][0]       
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)

    def test_dbapi_lvboq(self):
        
# ('sb-1234','滤波器1','pc-1-pass','m',1500,1600,1400,5,1.5)
        values = dict(cssbdm="sb-1234",cssbmc=u"滤波器1",pcdm="pc-1-pass",location=u"m",
                      freq=1500,f_upper=1600,f_lower=1400,order1=5,s21=1.5)        
        dbapi = queryUtility(IDbapi, name='lvboq')
        dbapi.add(values)

        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})

        id = nums[0][0]       
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)

    def test_dbapi_dianxingtxzyzk(self):
        
# ('喇叭天线1',10)
        values = dict(type_antennas=u"喇叭天线1",gain=10)        
        dbapi = queryUtility(IDbapi, name='dianxingtxzyzk')
        dbapi.add(values)

        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})

        id = nums[0][0]       
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)
 
    def test_dbapi_tianxianzk(self):
        
# ('TX-sbdm1','天线库1')
        values = dict(lib_name=u"TX-sbdm1",lib_code='天线库1')        
        dbapi = queryUtility(IDbapi, name='tianxianzk')
        dbapi.add(values)

        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})

        id = nums[0][0]       
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)

    def test_dbapi_tianxianzk(self):
        
# ('RE-sbdm1','接收机库1')
        values = dict(lib_name=u"RE-sbdm1",lib_code='接收机库1')        
        dbapi = queryUtility(IDbapi, name='jieshoujzk')
        dbapi.add(values)

        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})

        id = nums[0][0]       
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)

### enviroment lib
    def test_dbapi_bachang(self):
       
# ('RE-sbdm1','接收机库1')
        values = dict(name=u"靶场01",bcdm='bc-001',location='m',length=19.2,width=20.3,
                      wk=1,ti=2,landform='测试',xh='test')        
        dbapi = queryUtility(IDbapi, name='bachang')
        dbapi.add(values)

        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})

        id = nums[0][0]       
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)

    def test_dbapi_bachangzhdw(self):
       
# ('RE-sbdm1','接收机库1')
        values = dict(bcdm='bc-002',shelter_name=u"靶场01",zdno=10,lt_x=19.2,
                      lt_y=20.3,lt_z=10.3,ld_x=4.24,ld_y=0.3,ld_z=0.69,rt_x=2.02,rt_y=3.38,rt_z=1.1,
                      rd_x=2.1,rd_y=3.2,rd_z=1.1)        
        dbapi = queryUtility(IDbapi, name='bachangzhdw')
        dbapi.add(values)

        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})

        id = nums[0][0]       
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)

    def test_dbapi_bachangfshj(self):

#''sbmc','x','y','z','ft','pt_u','pt_l','num','fu','fl','bt','pt','tzlx','bzf','zp','bz',
#          'rt_x','rt_y','rt_z'        
# ('RE-sbdm1','接收机库1')
        values = dict(bcdm='bc-002',sbmc=u"靶场01",fsno=10,x=19.2,
                      y=20.3,z=10.3,ft=4,pt_u=0.69,pt_l=2,num=3,fu=1.1,fl=1.3,
                      bt=1,pt=2,bzf=12.5678,zp=12.09,tzlx='测试',bz='test')        
        dbapi = queryUtility(IDbapi, name='bachangfshj')
        dbapi.add(values)

        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})

        id = nums[0][0]       
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)
                                          

    def test_dbapi_ceshixm(self):

#''sbmc','x','y','z','ft','pt_u','pt_l','num','fu','fl','bt','pt','tzlx','bzf','zp','bz',
#          'rt_x','rt_y','rt_z'        
# ('RE-sbdm1','接收机库1')
        values = dict(device='bc-002',name=u"项目01",t_remark='马人口',
                      t_strument='示波器',t_value='work',t_result='pass')        
        dbapi = queryUtility(IDbapi, name='ceshixm')
        dbapi.add(values)

        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})

        id = nums[0][0]       
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)

    def test_dbapi_ceshibg(self):

#''sbmc','x','y','z','ft','pt_u','pt_l','num','fu','fl','bt','pt','tzlx','bzf','zp','bz',
#          'rt_x','rt_y','rt_z'        
# ('RE-sbdm1','接收机库1')
        dt=datetime.datetime.now()
        values = dict(t_id='bc-002',bailor=u"项目01",address='马人口',
                      device='示波器',eut_id='work',eut_type='pass',
                      manufacturor='示波器',t_date=dt,t_address='pass',
                      t_device='示波器',t_device_type='work',t_device_id='pass',
                      reference='示波器',temp=12.5,huminitily=0.95,
                      t_man='示波器',signer='work',assessor='pass',t_result='通过')        
        dbapi = queryUtility(IDbapi, name='ceshibg')
        dbapi.add(values)

        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})

        id = nums[0][0]       
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)

    def test_dbapi_ceshiff(self):

#''sbmc','x','y','z','ft','pt_u','pt_l','num','fu','fl','bt','pt','tzlx','bzf','zp','bz',
#          'rt_x','rt_y','rt_z'        
# ('RE-sbdm1','接收机库1')
        values = dict(m_id='bc-002',m_title=u"项目01",range1='马人口',
                      device='示波器',step='work',annotation='pass')        
        dbapi = queryUtility(IDbapi, name='ceshiff')
        dbapi.add(values)

        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})

        id = nums[0][0]       
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)

    def test_dbapi_ceshishysh(self):

#''sbmc','x','y','z','ft','pt_u','pt_l','num','fu','fl','bt','pt','tzlx','bzf','zp','bz',
#          'rt_x','rt_y','rt_z'        
# ('RE-sbdm1','接收机库1')
        values = dict(name='bc-002',unit=u"项目01",level1='马人口',survey='示波器')        
        dbapi = queryUtility(IDbapi, name='ceshishysh')
        dbapi.add(values)

        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})

        id = nums[0][0]       
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)

    def test_dbapi_ceshiry(self):

        values = dict(name='bc-002',sex=u"男",age=18,edu_level='示波器',post='教授',
                      certificate_code='bc-002',unit=u"男")        
        dbapi = queryUtility(IDbapi, name='ceshiry')
        dbapi.add(values)

        nums = dbapi.query({'start':0,'size':1,'SearchableText':'','sort_order':'reverse'})

        id = nums[0][0]       
        rt = dbapi.getByCode(id)
        self.assertTrue(nums is not None)
        self.assertEqual(len(nums),1)
        rt = dbapi.DeleteByCode(id)
        self.assertTrue(rt)
                                                                   
