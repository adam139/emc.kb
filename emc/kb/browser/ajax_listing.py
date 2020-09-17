#-*- coding: UTF-8 -*-
from zope.interface import Interface
from zope.component import getMultiAdapter
from five import grok
import json
import datetime
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.CMFCore import permissions
from Products.CMFCore.interfaces import ISiteRoot
from plone.memoize.instance import memoize
from Products.Five.browser import BrowserView
# from collective.gtags.source import TagsSourceBinder
from zope.component import getUtility
# input data view
from plone.directives import form
from z3c.form import field, button
from Products.statusmessages.interfaces import IStatusMessage
from emc.kb.interfaces import InputError
from zope.component import queryUtility
from emc.kb.interfaces import IDbapi
from emc.kb.mapping_db import IModel,Model
from emc.kb.mapping_db import Fashej,IFashej
from emc.kb.mapping_db import Jieshouj,IJieshouj
from emc.kb.mapping_db import IFashetx,Fashetx
from emc.kb.mapping_db import IJieshoutx,Jieshoutx
from emc.kb.mapping_db import ILvboq,Lvboq
from emc.kb.mapping_db import IDianxingtxzyzk,Dianxingtxzyzk
from emc.kb.mapping_db import ITianxianzk,Tianxianzk
from emc.kb.mapping_db import IJieshoujzk,Jieshoujzk
from emc.kb.mapping_db import IBachang,Bachang
from emc.kb.mapping_db import IFashejzk,Fashejzk
from emc.kb.mapping_db import IBachangzhdw,Bachangzhdw
from emc.kb.mapping_db import IBachangfshj,Bachangfshj
from emc.kb.mapping_db import ICeshiry
from emc.kb.mapping_db import ICeshixm
from emc.kb.mapping_db import ICeshibg
from emc.kb.mapping_db import ICeshiff
from emc.kb.mapping_db import ICeshishysh
from emc.kb.contents.ormfolder import Iormfolder
# update data view
from zope.interface import implements
from zope.publisher.interfaces import IPublishTraverse
from zExceptions import NotFound
from emc.kb import InputDb
from emc.kb import _
grok.templatedir('templates')

class ModelView(BrowserView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    @memoize
    def pm(self):
        context = aq_inner(self.context)
        pm = getToolByName(context, "portal_membership")
        return pm

    def get_locator(self,name):
        "get db specify name table api"

        dbapi = queryUtility(IDbapi, name=name)
        return dbapi
    
    @property
    def canbeUpdate(self):
# checkPermission function must be use Title style permission
        canbe = self.pm().checkPermission("emc.kb:Update db",self.context)
        return canbe
    
    @property
    def canbeInput(self):
# checkPermission function must be use Title style permission
        canbe = self.pm().checkPermission("emc.kb:Input db",self.context)
        return canbe    
    
    def getPathQuery(self):

        """返回 db url
        """
        query = {}
        query['path'] = "/".join(self.context.getPhysicalPath())
        return query

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"

        locator = self.get_locator('model')
        recorders = locator.query(query)
        return recorders

### log lib start
#admin_logs table
class AdminLogView(ModelView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:admin_logs
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"

        locator = self.get_locator('adminlog')
        recorders = locator.query(query)
        return recorders


#user_logs table
class UserLogView(ModelView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:user_logs
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('userlog')
        recorders = locator.query(query)
        return recorders
### log lib end

### parameters lib start
# fashej table
class FashejView(ModelView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('fashej')
        recorders = locator.query(query)
        return recorders


class JieshoujView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('jieshouj')
        recorders = locator.query(query)
        return recorders
    
# fashetx table
class FashetxView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('fashetx')
        recorders = locator.query(query)
        return recorders

# jieshoutx table
class JieshoutxView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('jieshoutx')
        recorders = locator.query(query)
        return recorders


class LvboqView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('lvboq')
        recorders = locator.query(query)
        return recorders


class DianxingtxzyzkView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('dianxingtxzyzk')
        recorders = locator.query(query)
        return recorders


class TianxianzkView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('tianxianzk')
        recorders = locator.query(query)
        return recorders


class JieshoujzkView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('jieshoujzk')
        recorders = locator.query(query)
        return recorders


class FashejzkView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('fashejzk')
        recorders = locator.query(query)
        return recorders


class TianxianzyzkView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('tianxianzyzk')
        recorders = locator.query(query)
        return recorders
    
    
### parameters lib end
### enviroment lib start
# ceshixm table
class BachangView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('bachang')
        recorders = locator.query(query)
        return recorders

# bachangzhdw table
class BachangzhdwView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('bachangzhdw')
        recorders = locator.query(query)
        return recorders
    
# bachangfshj table
class BachangfshjView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('bachangfshj')
        recorders = locator.query(query)
        return recorders    

### enviroment lib end
### test lib start
# ceshixm table
class CeshixmView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('ceshixm')
        recorders = locator.query(query)
        return recorders 
# ceshibg table
class CeshibgView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('ceshibg')
        recorders = locator.query(query)
        return recorders 
# ceshiff table
class CeshiffView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('ceshiff')
        recorders = locator.query(query)
        return recorders 
# ceshishysh table
class CeshishyshView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('ceshishysh')
        recorders = locator.query(query)
        return recorders 
# Ceshiry table
class CeshiryView(FashejView):
    """
    DB AJAX 查询，返回分页结果,这个class 调用数据库表 功能集 utility,
    从ajaxsearch view 构造 查询条件（通常是一个参数字典），该utility 接受
    该参数，查询数据库，并返回结果。
    view name:db_listing
    """

    def search_multicondition(self,query):
        "query is dic,like :{'start':0,'size':10,'':}"
        locator = self.get_locator('ceshiry')
        recorders = locator.query(query)
        return recorders                 
### test lib end      
###### output class
 # ajax multi-condition search relation db
class ajaxsearch(grok.View):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """
    grok.context(Interface)
    grok.name('dbajaxsearch')
    grok.require('zope2.View')
#     grok.require('emc.project.view_projectsummary')
    def Datecondition(self,key):
        "构造日期搜索条件"
        end = datetime.datetime.today()
#最近一周
        if key == 1:
            start = end - datetime.timedelta(7)
#最近一月
        elif key == 2:
            start = end - datetime.timedelta(30)
#最近一年
        elif key == 3:
            start = end - datetime.timedelta(365)
#最近两年
        elif key == 4:
            start = end - datetime.timedelta(365*2)
#最近五年
        else:
            start = end - datetime.timedelta(365*5)
#            return    { "query": [start,],"range": "min" }
        datecondition = { "query": [start, end],"range": "minmax" }
        return datecondition

    def searchview(self,viewname="model_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def render(self):
#        self.portal_state = getMultiAdapter((self.context, self.request), name=u"plone_portal_state")
        searchview = self.searchview()
 # datadic receive front ajax post data
        datadic = self.request.form
        start = int(datadic['start']) # batch search start position
        size = int(datadic['size'])      # batch search size
        sortcolumn = datadic['sortcolumn']
        sortdirection = datadic['sortdirection']
        keyword = (datadic['searchabletext']).strip()
#         origquery = searchview.getPathQuery()
        origquery = {}
        # default reverse,as is desc
        origquery['sort_on'] = sortcolumn
        # sql db sortt_order:asc,desc
        origquery['sort_order'] = sortdirection
 #模糊搜索
        if keyword != "":
            origquery['SearchableText'] = '%'+keyword+'%'
        else:
            origquery['SearchableText'] = ""
#origquery provide  batch search
        origquery['size'] = size
        origquery['start'] = start
#totalquery  search all
        totalquery = origquery.copy()
        totalquery['size'] = 0
        # search all   size = 0 return numbers of recorders
        totalnum = searchview.search_multicondition(totalquery)
        resultDicLists = searchview.search_multicondition(origquery)
        del origquery
        del totalquery
#call output function
# resultDicLists like this:[(u'C7', u'\u4ed6\u7684\u624b\u673a')]
        data = self.output(start,size,totalnum, resultDicLists)
        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(data)

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
#         inputable= self.canbeInput()
        for i in resultDicLists:
            out = """<tr class="text-left">
                                <td class="col-md-1 text-center">%(num)s</td>
                                <td class="col-md-2 text-left"><a href="%(edit_url)s">%(title)s</a></td>
                                <td class="col-md-7">%(description)s</td>
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            num=str(k + 1),
                                            title=i[0],
                                            description= i[1],
                                            edit_url="%s/@@update_model/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_model/%s" % (contexturl,i[0]))
            outhtml = "%s%s" %(outhtml ,out)
            k = k + 1
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data

### log output class
class AdminLogajaxsearch(ajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """
    grok.name('admin_logs_ajaxsearch')

    def searchview(self,viewname="admin_logs"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        
        from emc.kb.utils import kind
        from emc.kb.utils import level as log_level
        from emc.kb.utils import result as log_result 
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        for i in resultDicLists:           
            out = """<tr class="text-left">                                
                                <td class="col-md-1 text-left">%(adminid)s</td>
                                <td class="col-md-1">%(userid)s</td>
                                <td class="col-md-2">%(datetime)s</td>
                                <td class="col-md-2">%(ip)s</td>
                                <td class="col-md-1">%(type)s</td>
                                <td class="col-md-1">%(level)s</td>
                                <td class="col-md-3">%(description)s</td>
                                <td class="col-md-1">%(result)s</td>
                                </tr> """% dict(
                                            adminid = i[1],
                                            userid = i[2],
                                            datetime = i[3],
                                            ip = i[4],
                                            type = kind[i[5]],
                                            level = log_level[i[6]],
                                            description = i[7],
                                            result = log_result[i[8]])
            outhtml = "%s%s" %(outhtml ,out)
            k = k + 1
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data


class UserLogajaxsearch(ajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """
    grok.name('user_logs_ajaxsearch')

    def searchview(self,viewname="user_logs"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        
        from emc.kb.utils import kind
        from emc.kb.utils import level as log_level
        from emc.kb.utils import result as log_result 
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()

        for i in resultDicLists:
            out = """<tr class="text-left">                                                               
                                <td class="col-md-1">%(userid)s</td>
                                <td class="col-md-2">%(datetime)s</td>
                                <td class="col-md-2">%(ip)s</td>
                                <td class="col-md-1">%(type)s</td>
                                <td class="col-md-1">%(level)s</td>
                                <td class="col-md-3">%(description)s</td>
                                <td class="col-md-1">%(result)s</td>
                                </tr> """% dict(
                                            userid = i[1],
                                            datetime = i[2],
                                            ip = i[3],
                                            type = kind[i[4]],
                                            level = log_level[i[5]],
                                            description = i[6],
                                            result = log_result[i[7]])
            outhtml = "%s%s" %(outhtml ,out)
            k = k + 1
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data


### parameters lib output class
class Fashejajaxsearch(ajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """

    grok.name('fashej_ajaxsearch')

    def searchview(self,viewname="fashej_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        if self.searchview().canbeInput:
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-1 text-center">%(sbdm)s</td>
                                <td class="col-md-1 text-left"><a href="%(edit_url)s">%(sbmc)s</a></td>
                                <td class="col-md-1">%(pcdm)s</td>
                                <td class="col-md-1">%(location)s</td>
                                <td class="col-md-1">%(freq)s</td>
                                <td class="col-md-1">%(pd_upper)s</td>
                                <td class="col-md-1">%(pd_lower)s</td>
                                <td class="col-md-1">%(num)s</td>
                                <td class="col-md-1">%(freq_upper)s</td>
                                <td class="col-md-1">%(freq_lower)s</td>
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            sbdm=i[1],
                                            sbmc= i[2],
                                            pcdm= i[3],
                                            location= i[4],
                                            freq= i[5],
                                            pd_upper= i[6],
                                            pd_lower= i[7],
                                            num= i[8],
                                            freq_upper= i[9],
                                            freq_lower= i[10],
                                            edit_url="%s/@@update_fashej/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_fashej/%s" % (contexturl,i[0]))
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1
        else:
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-2 text-center">%(sbdm)s</td>
                                <td class="col-md-2 text-left">%(sbmc)s</td>
                                <td class="col-md-1">%(pcdm)s</td>
                                <td class="col-md-1">%(location)s</td>
                                <td class="col-md-1">%(freq)s</td>
                                <td class="col-md-1">%(pd_upper)s</td>
                                <td class="col-md-1">%(pd_lower)s</td>
                                <td class="col-md-1">%(num)s</td>
                                <td class="col-md-1">%(freq_upper)s</td>
                                <td class="col-md-1">%(freq_lower)s</td>               
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            sbdm=i[1],
                                            sbmc= i[2],
                                            pcdm= i[3],
                                            location= i[4],
                                            freq= i[5],
                                            pd_upper= i[6],
                                            pd_lower= i[7],
                                            num= i[8],
                                            freq_upper= i[9],
                                            freq_lower= i[10])
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1                
                
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data
        
    
class Jieshoujajaxsearch(ajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """

    grok.name('jieshouj_ajaxsearch')

    def searchview(self,viewname="jieshouj_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        if self.searchview().canbeInput:        
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-1 text-center">%(sbdm)s</td>
                                <td class="col-md-1 text-left"><a href="%(edit_url)s">%(sbmc)s</a></td>
                                <td class="col-md-1">%(pcdm)s</td>
                                <td class="col-md-1">%(location)s</td>
                                <td class="col-md-1">%(fb_upper)s</td>
                                <td class="col-md-1">%(fb_lower)s</td>
                                <td class="col-md-1">%(freq)s</td>
                                <td class="col-md-1">%(f_upper)s</td>
                                <td class="col-md-1">%(f_lower)s</td>
                                <td class="col-md-1">%(bw_receiver)s</td>
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            sbdm=i[1],
                                            sbmc= i[2],
                                            pcdm= i[3],
                                            location= i[4],
                                            fb_upper= i[5],
                                            fb_lower= i[6],
                                            freq= i[7],
                                            f_upper= i[8],
                                            f_lower= i[9],
                                            bw_receiver= i[10],
                                            edit_url="%s/@@update_jieshouj/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_jieshouj/%s" % (contexturl,i[0]))
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1
        else:
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-2 text-center">%(sbdm)s</td>
                                <td class="col-md-2 text-left">%(sbmc)s</td>
                                <td class="col-md-1">%(pcdm)s</td>
                                <td class="col-md-1">%(location)s</td>
                                <td class="col-md-1">%(fb_upper)s</td>
                                <td class="col-md-1">%(fb_lower)s</td>
                                <td class="col-md-1">%(freq)s</td>
                                <td class="col-md-1">%(f_upper)s</td>
                                <td class="col-md-1">%(f_lower)s</td>
                                <td class="col-md-1">%(bw_receiver)s</td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            sbdm=i[1],
                                            sbmc= i[2],
                                            pcdm= i[3],
                                            location= i[4],
                                            fb_upper= i[5],
                                            fb_lower= i[6],
                                            freq= i[7],
                                            f_upper= i[8],
                                            f_lower= i[9],
                                            bw_receiver= i[10])
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1            
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data

class Fashetxajaxsearch(Fashejajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """

    grok.name('fashetx_ajaxsearch')

    def searchview(self,viewname="fashetx_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        if self.searchview().canbeInput:        
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-1 text-center">%(cssbdm)s</td>
                                <td class="col-md-1 text-left"><a href="%(edit_url)s">%(cssbmc)s</a></td>
                                <td class="col-md-1">%(pcdm)s</td>
                                <td class="col-md-1">%(location)s</td>
                                <td class="col-md-1">%(gain)s</td>
                                <td class="col-md-1">%(polarization)s</td>
                                <td class="col-md-1">%(fwbskd)s</td>
                                <td class="col-md-1">%(fybskd)s</td>
                                <td class="col-md-1">%(txzxj)s</td>
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            cssbdm=i[1],
                                            cssbmc= i[2],
                                            pcdm= i[3],
                                            location= i[4],
                                            gain= i[5],
                                            polarization= i[6],
                                            fwbskd= i[7],
                                            fybskd= i[8],
                                            txzxj= i[9],
                                            edit_url="%s/@@update_fashetx/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_fashetx/%s" % (contexturl,i[0]))
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1
        else:
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-2 text-center">%(cssbdm)s</td>
                                <td class="col-md-2 text-left">%(cssbmc)s</td>
                                <td class="col-md-1">%(pcdm)s</td>
                                <td class="col-md-1">%(location)s</td>
                                <td class="col-md-1">%(gain)s</td>
                                <td class="col-md-1">%(polarization)s</td>
                                <td class="col-md-1">%(fwbskd)s</td>
                                <td class="col-md-1">%(fybskd)s</td>
                                <td class="col-md-1">%(txzxj)s</td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            cssbdm=i[1],
                                            cssbmc= i[2],
                                            pcdm= i[3],
                                            location= i[4],
                                            gain= i[5],
                                            polarization= i[6],
                                            fwbskd= i[7],
                                            fybskd= i[8],
                                            txzxj= i[9])
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1            
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data

class Jieshoutxajaxsearch(Fashejajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """

    grok.name('jieshoutx_ajaxsearch')

    def searchview(self,viewname="jieshoutx_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        if self.searchview().canbeInput:        
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-1 text-center">%(cssbdm)s</td>
                                <td class="col-md-1 text-left"><a href="%(edit_url)s">%(cssbmc)s</a></td>
                                <td class="col-md-1">%(pcdm)s</td>
                                <td class="col-md-1">%(location)s</td>
                                <td class="col-md-1">%(gain)s</td>
                                <td class="col-md-1">%(polarization)s</td>
                                <td class="col-md-1">%(fwbskd)s</td>
                                <td class="col-md-1">%(fybskd)s</td>
                                <td class="col-md-1">%(txzxj)s</td>
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            cssbdm=i[1],
                                            cssbmc= i[2],
                                            pcdm= i[3],
                                            location= i[4],
                                            gain= i[5],
                                            polarization= i[6],
                                            fwbskd= i[7],
                                            fybskd= i[8],
                                            txzxj= i[9],
                                            edit_url="%s/@@update_jieshoutx/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_jieshoutx/%s" % (contexturl,i[0]))
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1
        else:
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-2 text-center">%(cssbdm)s</td>
                                <td class="col-md-2 text-left"><%(cssbmc)s</td>
                                <td class="col-md-1">%(pcdm)s</td>
                                <td class="col-md-1">%(location)s</td>
                                <td class="col-md-1">%(gain)s</td>
                                <td class="col-md-1">%(polarization)s</td>
                                <td class="col-md-1">%(fwbskd)s</td>
                                <td class="col-md-1">%(fybskd)s</td>
                                <td class="col-md-1">%(txzxj)s</td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            cssbdm=i[1],
                                            cssbmc= i[2],
                                            pcdm= i[3],
                                            location= i[4],
                                            gain= i[5],
                                            polarization= i[6],
                                            fwbskd= i[7],
                                            fybskd= i[8],
                                            txzxj= i[9])
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1                
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data

### enviroment lib output class
class Bachangajaxsearch(ajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """
    grok.name('bachang_ajaxsearch')

    def searchview(self,viewname="bachang_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        if self.searchview().canbeInput:
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-2 text-center"><a href="%(edit_url)s">%(name)s</a></td>
                                <td class="col-md-1 text-left">%(bcdm)s</td>
                                <td class="col-md-1">%(location)s</td>
                                <td class="col-md-1">%(length)s</td>
                                <td class="col-md-1">%(width)s</td>
                                <td class="col-md-1">%(wk)s</td>
                                <td class="col-md-1">%(ti)s</td>
                                <td class="col-md-1">%(landform)s</td>
                                <td class="col-md-1">%(xh)s</td>                               
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            name=i[1],
                                            bcdm= i[2],
                                            location= i[3],
                                            length= i[4],
                                            width= i[5],
                                            wk= i[6],
                                            ti= i[7],
                                            landform= i[8],
                                            xh= i[9],
                                            edit_url="%s/@@update_bachang/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_bachang/%s" % (contexturl,i[0]))
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1
        else:
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-2 text-center">%(name)s</td>
                                <td class="col-md-1 text-left">%(bcdm)s</td>
                                <td class="col-md-3">%(location)s</td>
                                <td class="col-md-1">%(length)s</td>
                                <td class="col-md-1">%(width)s</td>
                                <td class="col-md-1">%(wk)s</td>
                                <td class="col-md-1">%(ti)s</td>
                                <td class="col-md-1">%(landform)s</td>
                                <td class="col-md-1">%(xh)s</td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            name=i[1],
                                            bcdm= i[2],
                                            location= i[3],
                                            length= i[4],
                                            width= i[5],
                                            wk= i[6],
                                            ti= i[7],
                                            landform= i[8],
                                            xh= i[9])
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1            
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data


class Bachangzhdwajaxsearch(ajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """
    grok.name('bachangzhdw_ajaxsearch')

    def searchview(self,viewname="bachangzhdw_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        if self.searchview().canbeInput:
            for i in resultDicLists:
                out = """<tr class="text-left">                                
                                <td class="col-md-1 text-left"><a href="%(edit_url)s">%(shelter_name)s</a></td>
                                <td class="col-md-1">%(lt_x)s</td>
                                <td class="col-md-1">%(lt_y)s</td>
                                <td class="col-md-1">%(lt_z)s</td>
                                <td class="col-md-1">%(ld_x)s</td>
                                <td class="col-md-1">%(ld_y)s</td>
                                <td class="col-md-1">%(ld_z)s</td>
                                <td class="col-md-1">%(rt_x)s</td>
                                <td class="col-md-1">%(rt_x)s</td>
                                <td class="col-md-1">%(rt_z)s</td>                               
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            shelter_name=i[1],
                                            lt_x= i[2],
                                            lt_y= i[3],
                                            lt_z= i[4],
                                            ld_x= i[5],
                                            ld_y= i[6],
                                            ld_z= i[7],
                                            rt_x= i[8],
                                            rt_y= i[9],
                                            rt_z= i[10],
                                            edit_url="%s/@@update_bachangzhdw/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_bachangzhdw/%s" % (contexturl,i[0]))
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1
        else:
            for i in resultDicLists:
                out = """<tr class="text-left">                                
                                <td class="col-md-2 text-left">%(shelter_name)s</td>
                                <td class="col-md-2">%(lt_x)s</td>
                                <td class="col-md-1">%(lt_y)s</td>
                                <td class="col-md-1">%(lt_z)s</td>
                                <td class="col-md-1">%(ld_x)s</td>
                                <td class="col-md-1">%(ld_y)s</td>
                                <td class="col-md-1">%(ld_z)s</td>
                                <td class="col-md-1">%(rt_x)s</td>
                                <td class="col-md-1">%(rt_x)s</td>
                                <td class="col-md-1">%(rt_z)s</td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            shelter_name=i[1],
                                            lt_x= i[2],
                                            lt_y= i[3],
                                            lt_z= i[4],
                                            ld_x= i[5],
                                            ld_y= i[6],
                                            ld_z= i[7],
                                            rt_x= i[8],
                                            rt_y= i[9],
                                            rt_z= i[10])
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1            
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data        
 
class Bachangfshjajaxsearch(ajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """
    grok.name('bachangfshj_ajaxsearch')

    def searchview(self,viewname="bachangfshj_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        if self.searchview().canbeInput:        
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-1 text-left"><a href="%(edit_url)s">%(sbmc)s</a></td>
                                <td class="col-md-1">%(x)s</td>
                                <td class="col-md-1">%(y)s</td>
                                <td class="col-md-1">%(z)s</td>
                                <td class="col-md-1">%(ft)s</td>
                                <td class="col-md-1">%(pt_u)s</td>
                                <td class="col-md-1">%(pt_l)s</td>
                                <td class="col-md-1">%(num)s</td>
                                <td class="col-md-1">%(fu)s</td>
                                <td class="col-md-1">%(fl)s</td>                               
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            sbmc=i[1],
                                            x= i[2],
                                            y= i[3],
                                            z= i[4],
                                            ft= i[5],
                                            pt_u= i[6],
                                            pt_l= i[7],
                                            num= i[8],
                                            fu= i[9],
                                            fl= i[10],
                                            edit_url="%s/@@update_bachangfshj/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_bachangfshj/%s" % (contexturl,i[0]))
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1
        else:
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-2 text-left">%(sbmc)s</td>
                                <td class="col-md-2">%(x)s</td>
                                <td class="col-md-1">%(y)s</td>
                                <td class="col-md-1">%(z)s</td>
                                <td class="col-md-1">%(ft)s</td>
                                <td class="col-md-1">%(pt_u)s</td>
                                <td class="col-md-1">%(pt_l)s</td>
                                <td class="col-md-1">%(num)s</td>
                                <td class="col-md-1">%(fu)s</td>
                                <td class="col-md-1">%(fl)s</td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            sbmc=i[1],
                                            x= i[2],
                                            y= i[3],
                                            z= i[4],
                                            ft= i[5],
                                            pt_u= i[6],
                                            pt_l= i[7],
                                            num= i[8],
                                            fu= i[9],
                                            fl= i[10])
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1            
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data
    

### test lib output class
class Ceshishyshajaxsearch(ajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """
    grok.name('ceshishysh_ajaxsearch')

    def searchview(self,viewname="ceshishysh_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        if self.searchview().canbeInput:
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-3 text-center"><a href="%(edit_url)s">%(name)s</a></td>
                                <td class="col-md-3 text-left">%(unit)s</td>
                                <td class="col-md-1">%(level)s</td>
                                <td class="col-md-3">%(survey)s</td>                               
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            name=i[1],
                                            unit= i[2],
                                            level= i[3],
                                            survey= i[4],
                                            edit_url="%s/@@update_ceshishysh/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_ceshishysh/%s" % (contexturl,i[0]))
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1
        else:
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-3 text-center">%(name)s</td>
                                <td class="col-md-3 text-left">%(unit)s</td>
                                <td class="col-md-1">%(level)s</td>
                                <td class="col-md-3">%(survey)s</td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            name=i[1],
                                            unit= i[2],
                                            level= i[3],
                                            survey= i[4])
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1            
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data


class Ceshiffajaxsearch(ajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """
    grok.name('ceshiff_ajaxsearch')

    def searchview(self,viewname="ceshiff_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        if self.searchview().canbeInput:        
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-1 text-center">%(m_id)s</td>
                                <td class="col-md-1 text-left"><a href="%(edit_url)s">%(m_title)s</a></td>
                                <td class="col-md-1">%(range)s</td>
                                <td class="col-md-2">%(device)s</td>
                                <td class="col-md-2">%(step)s</td>
                                <td class="col-md-3">%(annotation)s</td>                                                                                              
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            m_id=i[1],
                                            m_title= i[2],
                                            range= i[3],
                                            device= i[4],
                                            step= i[5], 
                                            annotation= i[6],                                                                                        
                                            edit_url="%s/@@update_ceshiff/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_ceshiff/%s" % (contexturl,i[0]))
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1
        else:
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-2 text-center">%(m_id)s</td>
                                <td class="col-md-2 text-left">%(m_title)s</td>
                                <td class="col-md-1">%(range)s</td>
                                <td class="col-md-2">%(device)s</td>
                                <td class="col-md-2">%(step)s</td>
                                <td class="col-md-3">%(annotation)s</td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            m_id=i[1],
                                            m_title= i[2],
                                            range= i[3],
                                            device= i[4],
                                            step= i[5], 
                                            annotation= i[6])
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1            
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data
    

class Ceshiryajaxsearch(ajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """
    grok.name('ceshiry_ajaxsearch')

    def searchview(self,viewname="ceshiry_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        if self.searchview().canbeInput:        
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-1 text-center">%(name)s</td>
                                <td class="col-md-1 text-left"><a href="%(edit_url)s">%(sex)s</a></td>
                                <td class="col-md-1">%(age)s</td>
                                <td class="col-md-1">%(edu_level)s</td>
                                <td class="col-md-1">%(post)s</td>                                
                                <td class="col-md-2">%(certificate_code)s</td>
                                <td class="col-md-3">%(unit)s</td>                                                                                              
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            name=i[1],
                                            sex= i[2],
                                            age= i[3],
                                            edu_level= i[4],
                                            post= i[5], 
                                            certificate_code= i[6],  
                                            unit= i[7],                                                                                                                                    
                                            edit_url="%s/@@update_ceshiry/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_ceshiry/%s" % (contexturl,i[0]))
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1
        else:
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-2 text-center">%(name)s</td>
                                <td class="col-md-2 text-left">%(sex)s</td>
                                <td class="col-md-1">%(age)s</td>
                                <td class="col-md-1">%(edu_level)s</td>
                                <td class="col-md-1">%(post)s</td>                                
                                <td class="col-md-2">%(certificate_code)s</td>
                                <td class="col-md-3">%(unit)s</td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            name=i[1],
                                            sex= i[2],
                                            age= i[3],
                                            edu_level= i[4],
                                            post= i[5], 
                                            certificate_code= i[6],  
                                            unit= i[7])
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1            
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data
    
                
class Ceshixmajaxsearch(ajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """
    grok.name('ceshixm_ajaxsearch')

    def searchview(self,viewname="ceshixm_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        if self.searchview().canbeInput:        
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-2 text-center">%(device)s</td>
                                <td class="col-md-1 text-left"><a href="%(edit_url)s">%(name)s</a></td>
                                <td class="col-md-2">%(t_remark)s</td>
                                <td class="col-md-1">%(t_strument)s</td>
                                <td class="col-md-2">%(t_value)s</td>                                
                                <td class="col-md-2">%(t_result)s</td>                                                                                             
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            device=i[1],
                                            name= i[2],
                                            t_remark= i[3],
                                            t_strument= i[4],
                                            t_value= i[5], 
                                            t_result= i[6],                                                                                                                                   
                                            edit_url="%s/@@update_ceshixm/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_ceshixm/%s" % (contexturl,i[0]))
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1
        else:
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-3 text-center">%(device)s</td>
                                <td class="col-md-2 text-left">%(name)s</td>
                                <td class="col-md-2">%(t_remark)s</td>
                                <td class="col-md-1">%(t_strument)s</td>
                                <td class="col-md-2">%(t_value)s</td>                                
                                <td class="col-md-2">%(t_result)s</td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            device=i[1],
                                            name= i[2],
                                            t_remark= i[3],
                                            t_strument= i[4],
                                            t_value= i[5], 
                                            t_result= i[6])
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1                
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data
    

class Ceshibgajaxsearch(ajaxsearch):
    """AJAX action for search DB.
    receive front end ajax transform parameters
    """
    grok.name('ceshibg_ajaxsearch')

    def searchview(self,viewname="ceshibg_listings"):
        searchview = getMultiAdapter((self.context, self.request),name=viewname)
        return searchview

    def output(self,start,size,totalnum,resultDicLists):
        """根据参数total,resultDicLists,返回json 输出,resultDicLists like this:
        [(u'C7', u'\u4ed6\u7684\u624b\u673a')]"""
        outhtml = ""
        k = 0
        contexturl = self.context.absolute_url()
        if self.searchview().canbeInput:        
            for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-1 text-center">%(t_id)s</td>
                                <td class="col-md-1 text-left"><a href="%(edit_url)s">%(bailor)s</a></td>
                                <td class="col-md-1">%(device)s</td>
                                <td class="col-md-1">%(t_address)s</td>
                                <td class="col-md-1">%(t_device)s</td>                                
                                <td class="col-md-1">%(t_man)s</td> 
                                <td class="col-md-1">%(reference)s</td>
                                <td class="col-md-1">%(signer)s</td>
                                <td class="col-md-1">%(assessor)s</td>                                
                                <td class="col-md-1">%(t_result)s</td>                                                                                                                             
                                <td class="col-md-1 text-center">
                                <a href="%(edit_url)s" title="edit">
                                  <span class="glyphicon glyphicon-pencil" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                <td class="col-md-1 text-center">
                                <a href="%(delete_url)s" title="delete">
                                  <span class="glyphicon glyphicon-trash" aria-hidden="true">
                                  </span>
                                </a>
                                </td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            t_id=i[1],
                                            bailor= i[2],
                                            device= i[3],
                                            t_address= i[4],
                                            t_device= i[5], 
                                            t_man= i[6],  
                                            reference= i[7],
                                            signer= i[8],
                                            assessor= i[9], 
                                            t_result= i[10],                                                                                                                                                                            
                                            edit_url="%s/@@update_ceshibg/%s" % (contexturl,i[0]),
                                            delete_url="%s/@@delete_ceshibg/%s" % (contexturl,i[0]))
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1
        else:
             for i in resultDicLists:
                out = """<tr class="text-left">
                                <td class="col-md-2 text-center">%(t_id)s</td>
                                <td class="col-md-2 text-left">%(bailor)s</td>
                                <td class="col-md-1">%(device)s</td>
                                <td class="col-md-1">%(t_address)s</td>
                                <td class="col-md-1">%(t_device)s</td>                                
                                <td class="col-md-1">%(t_man)s</td> 
                                <td class="col-md-1">%(reference)s</td>
                                <td class="col-md-1">%(signer)s</td>
                                <td class="col-md-1">%(assessor)s</td>                                
                                <td class="col-md-1">%(t_result)s</td>
                                </tr> """% dict(objurl="%s/@@view" % contexturl,
                                            t_id=i[1],
                                            bailor= i[2],
                                            device= i[3],
                                            t_address= i[4],
                                            t_device= i[5], 
                                            t_man= i[6],  
                                            reference= i[7],
                                            signer= i[8],
                                            assessor= i[9], 
                                            t_result= i[10])
                outhtml = "%s%s" %(outhtml ,out)
                k = k + 1           
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data
    
                        
###### database actions
# Delete Update Input block
class DeleteModel(form.Form):
    "delete the specify model recorder"
    implements(IPublishTraverse)
    grok.context(Iormfolder)
    grok.name('delete_model')
    grok.require('emc.kb.input_db')

    label = _(u"delete model data")
    fields = field.Fields(IModel).omit('id')
    ignoreContext = False

    id = None
    #receive url parameters
    def publishTraverse(self, request, name):
        if self.id is None:
            self.id = name
            return self
        else:
            raise NotFound()

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='model')
        #to do
        #fetch the pending deleting  record
        return locator.getByCode(self.id)

    def update(self):
        self.request.set('disable_border', True)
        #Let z3c.form do its magic
        super(DeleteModel, self).update()


    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete model recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='model')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/model_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/model_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/model_listings')

class InputModel(form.Form):
    """input db model table data
    """

    grok.context(Iormfolder)
    grok.name('input_model')
    grok.require('emc.kb.input_db')
    label = _(u"Input model data")
    fields = field.Fields(IModel).omit('modelId')
    ignoreContext = True

    def update(self):
        self.request.set('disable_border', True)

        # Get the model table query funcations
#         locator = getUtility(IModelLocator)
        # to do
        # fetch first record as sample data
#         self.screening = locator.screeningById(self.screeningId)

        # Let z3c.form do its magic
        super(InputModel, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit model recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='model')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/model_listings')

        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/model_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/model_listings')

class UpdateModel(form.Form):
    """update model table row data
    """

    implements(IPublishTraverse)
    grok.context(Iormfolder)
    grok.name('update_model')
    grok.require('emc.kb.input_db')

    label = _(u"update model data")
    fields = field.Fields(IModel).omit('id')
    ignoreContext = False
    id = None
    #receive url parameters
    # reset content
    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='model')
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.id)


    def publishTraverse(self, request, name):
        if self.id is None:
            self.id = name
            return self
        else:
            raise NotFound()

    def update(self):
        self.request.set('disable_border', True)

        # Get the model table query funcations
#         locator = getUtility(IModelLocator)
        # to do
        # fetch first record as sample data
#         self.screening = locator.screeningById(self.screeningId)

        # Let z3c.form do its magic
        super(UpdateModel, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='model')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/model_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/model_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/model_listings')
##发射机数据库操作
class DeleteFashej(DeleteModel):
    "delete the specify fashej recorder"

    grok.name('delete_fashej')
    label = _(u"delete fa she ji data")
    fields = field.Fields(IFashej).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='fashej')
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.id)

    def update(self):
        self.request.set('disable_border', True)

        #Let z3c.form do its magic
        super(DeleteFashej, self).update()

    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete model recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='fashej')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@fashej_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashej_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashej_listings')


class InputFashej(InputModel):
    """input db fashej table data
    """

    grok.name('input_fashej')

    label = _(u"Input fa she ji data")
    fields = field.Fields(IFashej).omit('id')

    def update(self):
        self.request.set('disable_border', True)

        # Get the model table query funcations
#         locator = getUtility(IModelLocator)
        # to do
        # fetch first record as sample data
#         self.screening = locator.screeningById(self.screeningId)

        # Let z3c.form do its magic
        super(InputFashej, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit model recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='fashej')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@fashej_listings')

        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashej_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashej_listings')


class UpdateFashej(UpdateModel):
    """update model table row data
    """
    grok.name('update_fashej')
    label = _(u"update fa she ji data")
    fields = field.Fields(IFashej).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='fashej')
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.id)

    def update(self):
        self.request.set('disable_border', True)
        # Let z3c.form do its magic
        super(UpdateFashej, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """

        data, errors = self.extractData()
        data['id'] = self.id
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='fashej')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@fashej_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashej_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashej_listings')

##end发射机 数据库操作

##接收机 数据库操作
class DeleteJieshouj(DeleteModel):
    "delete the specify jieshouj recorder"

    grok.name('delete_jieshouj')
    label = _(u"delete jie shou ji data")
    fields = field.Fields(IJieshouj).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='jieshouj')
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.id)

    def update(self):
        self.request.set('disable_border', True)

        #Let z3c.form do its magic
        super(DeleteJieshouj, self).update()


    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete model recorder
        """

        data, errors = self.extractData()        
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='jieshouj')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@jieshouj_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshouj_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshouj_listings')

class InputJieshouj(InputModel):
    """input db jieshouj table data
    """

    grok.name('input_jieshouj')

    label = _(u"Input jie shou ji data")
    fields = field.Fields(IJieshouj).omit('id')

    def update(self):
        self.request.set('disable_border', True)

        # Get the model table query funcations
#         locator = getUtility(IModelLocator)
        # to do
        # fetch first record as sample data
#         self.screening = locator.screeningById(self.screeningId)

        # Let z3c.form do its magic
        super(InputJieshouj, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit model recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='jieshouj')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@jieshouj_listings')

        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshouj_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshouj_listings')

class UpdateJieshouj(UpdateModel):
    """update model table row data
    """
    grok.name('update_jieshouj')
    label = _(u"update jieshouj data")
    fields = field.Fields(IJieshouj).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='jieshouj')
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.id)

    def update(self):
        self.request.set('disable_border', True)
        # Let z3c.form do its magic
        super(UpdateJieshouj, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """

        data, errors = self.extractData()
        data['id'] = self.id
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='jieshouj')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@jieshouj_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshouj_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshouj_listings')
# end 接收机 数据库操作

## 发射天线 数据库操作
class DeleteFashetx(DeleteModel):
    "delete the specify Fashetx recorder"

    grok.name('delete_fashetx')
    label = _(u"delete fa she tian xian data")
    fields = field.Fields(IFashetx).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='fashetx')
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.id)

    def update(self):
        self.request.set('disable_border', True)

        #Let z3c.form do its magic
        super(DeleteFashetx, self).update()


    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete model recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='fashetx')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@fashetx_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashetx_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashetx_listings')

class InputFashetx(InputModel):
    """input db fashetx table data
    """

    grok.name('input_fashetx')

    label = _(u"Input fa she tian xian data")
    fields = field.Fields(IFashetx).omit('id')

    def update(self):
        self.request.set('disable_border', True)

        # Get the model table query funcations
#         locator = getUtility(IModelLocator)
        # to do
        # fetch first record as sample data
#         self.screening = locator.screeningById(self.screeningId)

        # Let z3c.form do its magic
        super(InputFashetx, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit model recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='fashetx')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@fashetx_listings')

        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashetx_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashetx_listings')

class UpdateFashetx(UpdateModel):
    """update model table row data
    """
    grok.name('update_fashetx')
    label = _(u"update fa she tian xian data")
    fields = field.Fields(IFashetx).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='fashetx')
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.id)

    def update(self):
        self.request.set('disable_border', True)
        # Let z3c.form do its magic
        super(UpdateFashetx, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """

        data, errors = self.extractData()
        data['id'] = self.id
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='fashetx')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@fashetx_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashetx_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@fashetx_listings')
# end 发射天线 数据库操作
## 接收天线 数据库操作
class DeleteJieshoutx(DeleteModel):
    "delete the specify Jieshoutx recorder"

    grok.name('delete_jieshoutx')
    label = _(u"delete jie shou tian xian data")
    fields = field.Fields(IJieshoutx).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='jieshoutx')
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.id)

    def update(self):
        self.request.set('disable_border', True)

        #Let z3c.form do its magic
        super(DeleteJieshoutx, self).update()


    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete jieshoutx recorder
        """

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='jieshoutx')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@jieshoutx_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshoutx_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshoutx_listings')

class InputJieshoutx(InputModel):
    """input db jieshoutx table data
    """

    grok.name('input_jieshoutx')
    label = _(u"Input jie shou tian xian data")
    fields = field.Fields(IJieshoutx).omit('id')

    def update(self):
        self.request.set('disable_border', True)

        # Let z3c.form do its magic
        super(InputJieshoutx, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit jieshoutianxian recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='jieshoutx')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@jieshoutx_listings')

        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshoutx_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshoutx_listings')

class UpdateJieshoutx(UpdateModel):
    """update model table row data
    """
    grok.name('update_jieshoutx')
    label = _(u"update jie shou tian xian data")
    fields = field.Fields(IJieshoutx).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='jieshoutx')
        # to do
        # fetch first record as sample data
        return locator.getByCode(self.id)

    def update(self):
        self.request.set('disable_border', True)
        # Let z3c.form do its magic
        super(UpdateJieshoutx, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """

        data, errors = self.extractData()
        data['id'] =self.id
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='jieshoutx')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@jieshoutx_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshoutx_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@jieshoutx_listings')
# end 接收天线 数据库操作
## 滤波器 数据库操作
class DeleteLvboq(DeleteModel):
    "delete the specify Lvboq recorder"

    grok.name('delete_lvboq')
    label = _(u"delete jie shou tian xian data")
    fields = field.Fields(ILvboq).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='lvboq')
        return locator.getByCode(self.id)

    def update(self):
        self.request.set('disable_border', True)
        super(DeleteLvboq, self).update()

    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete jieshoutx recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='lvboq')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@lvboq_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@lvboq_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@lvboq_listings')

class InputLvboq(InputModel):
    """input db Lvboq table data
    """
    grok.name('input_lvboq')
    label = _(u"Input jie shou tian xian data")
    fields = field.Fields(ILvboq).omit('id')

    def update(self):
        self.request.set('disable_border', True)

        # Let z3c.form do its magic
        super(InputLvboq, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit Lvboq recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='lvboq')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@lvboq_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@lvboq_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@lvboq_listings')

class UpdateLvboq(UpdateModel):
    """update Lvboq table row data
    """
    grok.name('update_lvboq')
    label = _(u"update jie shou tian xian data")
    fields = field.Fields(ILvboq).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='lvboq')
        return locator.getByCode(self.id)

    def update(self):
        self.request.set('disable_border', True)
        # Let z3c.form do its magic
        super(UpdateJieshoutx, self).update()

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """
        data, errors = self.extractData()
        data['id'] =self.id
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='lvboq')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@lvboq_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@lvboq_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@lvboq_listings')
# end 滤波器 数据库操作

## 典型天线增益子库 数据库操作
class DeleteDianxingtxzyzk(DeleteModel):
    "delete the specify Dianxingtxzyzk recorder"

    grok.name('delete_dianxingtxzyzk')
    label = _(u"delete jie shou tian xian data")
    fields = field.Fields(IDianxingtxzyzk).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='dianxingtxzyzk')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete jieshoutx recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='dianxingtxzyzk')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@dianxingtxzyzk_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@dianxingtxzyzk_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@dianxingtxzyzk_listings')

class InputDianxingtxzyzk(InputModel):
    """input db Lvboq table data
    """
    grok.name('input_dianxingtxzyzk')
    label = _(u"Input jie shou tian xian data")
    fields = field.Fields(IDianxingtxzyzk).omit('id')

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit Lvboq recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='dianxingtxzyzk')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@dianxingtxzyzk_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@dianxingtxzyzk_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@dianxingtxzyzk_listings')

class UpdateDianxingtxzyzk(UpdateModel):
    """update Lvboq table row data
    """
    grok.name('update_lvboq')
    label = _(u"update jie shou tian xian data")
    fields = field.Fields(IDianxingtxzyzk).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='dianxingtxzyzk')
        return locator.getByCode(self.id)


    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """
        data, errors = self.extractData()
        data['id'] =self.id
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='dianxingtxzyzk')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@dianxingtxzyzk_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@dianxingtxzyzk_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@dianxingtxzyzk_listings')
# end 典型天线增益子库 数据库操作

## 天线子库 数据库操作
class DeleteTianxianzk(DeleteModel):
    "delete the specify Tianxianzk recorder"

    grok.name('delete_tianxianzk')
    label = _(u"delete tian xian ziku data")
    fields = field.Fields(ITianxianzk).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='tianxianzk')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete tianxianzk recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='tianxianzk')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@tianxianzk_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@tianxianzk_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@tianxianzk_listings')

class InputTianxianzk(InputModel):
    """input db Lvboq table data
    """
    grok.name('input_tianxianzk')
    label = _(u"Input tian xian ziku data")
    fields = field.Fields(ITianxianzk).omit('id')

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit tianxianzk recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='tianxianzk')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@tianxianzk_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@tianxianzk_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@tianxianzk_listings')

class UpdateDianxingtxzyzk(UpdateModel):
    """update Lvboq table row data
    """
    grok.name('update_tianxianzk')
    label = _(u"update tian xian ziku data")
    fields = field.Fields(ITianxianzk).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='tianxianzk')
        return locator.getByCode(self.id)


    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """
        data, errors = self.extractData()
        data['id'] =self.id
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='tianxianzk')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@tianxianzk_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@tianxianzk_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@tianxianzk_listings')
# end 典型天线增益子库 数据库操作

###### enviroment lib actions
## 靶场 数据库操作
class DeleteBachang(DeleteModel):
    "delete the specify Bachang recorder"

    grok.name('delete_bachang')
    label = _(u"delete ba chang data")
    fields = field.Fields(IBachang).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='bachang')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete Bachang recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='bachang')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@bachang_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachang_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachang_listings')

class InputBachang(InputModel):
    """input db bachang table data
    """
    grok.name('input_bachang')
    label = _(u"Input ba chang data")
    fields = field.Fields(IBachang).omit('id')

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit bachang recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='bachang')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@bachang_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachang_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachang_listings')

class UpdateBachang(UpdateModel):
    """update Bachang table row data
    """
    grok.name('update_bachang')
    label = _(u"update ba chang data")
    fields = field.Fields(IBachang).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='bachang')
        return locator.getByCode(self.id)


    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """
        data, errors = self.extractData()
        data['id'] =self.id
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='bachang')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@bachang_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachang_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachang_listings')
# end 靶场 数据库操作
## 靶场遮挡物 数据库操作
class DeleteBachangzhdw(DeleteModel):
    "delete the specify Bachangzhdw recorder"

    grok.name('delete_bachangzhdw')
    label = _(u"delete ba chang data")
    fields = field.Fields(IBachangzhdw).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='bachangzhdw')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete Bachangzhdw recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='bachangzhdw')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@bachangzhdw_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachangzhdw_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachangzhdw_listings')

class InputBachangzhdw(InputModel):
    """input db bachangzhdw table data
    """
    grok.name('input_bachangzhdw')
    label = _(u"Input ba chang data")
    fields = field.Fields(IBachangzhdw).omit('id')

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit bachangzhdw recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='bachangzhdw')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@bachangzhdw_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachangzhdw_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachangzhdw_listings')

class UpdateBachangzhdw(UpdateModel):
    """update Lvboq table row data
    """
    grok.name('update_bachangzhdw')
    label = _(u"update ba chang data")
    fields = field.Fields(IBachangzhdw).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='bachangzhdw')
        return locator.getByCode(self.id)


    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """
        data, errors = self.extractData()
        data['id'] =self.id
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='bachangzhdw')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@bachangzhdw_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachangzhdw_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachangzhdw_listings')
# end 靶场遮挡物 数据库操作
## 靶场发射机 数据库操作
class DeleteBachangfshj(DeleteModel):
    "delete the specify Bachangfshj recorder"

    grok.name('delete_bachangfshj')
    label = _(u"delete ba chang data")
    fields = field.Fields(IBachangfshj).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='bachangfshj')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete Bachangfshj recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='bachangfshj')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@bachangfshj_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachangfshj_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachangfshj_listings')

class InputBachangfshj(InputModel):
    """input db bachangfshj table data
    """
    grok.name('input_bachangfshj')
    label = _(u"Input data")
    fields = field.Fields(IBachangfshj).omit('id')

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit bachangfshj recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='bachangfshj')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@bachangfshj_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachangfshj_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachangfshj_listings')

class UpdateBachangfshj(UpdateModel):
    """update Lvboq table row data
    """
    grok.name('update_bachangfshj')
    label = _(u"update data")
    fields = field.Fields(IBachangfshj).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='bachangfshj')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """
        data, errors = self.extractData()
        data['id'] =self.id
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='bachangfshj')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@bachangfshj_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachangfshj_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@bachangfshj_listings')
# end 靶场发射机 数据库操作
###### test lib actions
## 测试项目 数据库操作
class DeleteCeshixm(DeleteModel):
    "delete the specify Ceshixm recorder"

    grok.name('delete_ceshixm')
    label = _(u"delete data")
    fields = field.Fields(ICeshixm).omit('id')

    def getContent(self):
        locator = queryUtility(IDbapi, name='ceshixm')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete Ceshixm recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='ceshixm')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@ceshixm_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshixm_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshixm_listings')

class InputCeshixm(InputModel):
    """input db ceshixm table data
    """
    grok.name('input_ceshixm')
    label = _(u"Input data")
    fields = field.Fields(ICeshixm).omit('id')

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit ceshixm recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='ceshixm')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@ceshixm_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshixm_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshixm_listings')

class UpdateCeshixm(UpdateModel):
    """update Ceshixm table row data
    """
    grok.name('update_ceshixm')
    label = _(u"update data")
    fields = field.Fields(ICeshixm).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='ceshixm')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """
        data, errors = self.extractData()
        data['id'] =self.id
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='ceshixm')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@ceshixm_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshixm_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshixm_listings')
# end 靶场 数据库操作
## 测试报告 数据库操作
class DeleteCeshibg(DeleteModel):
    "delete the specify Ceshibg recorder"

    grok.name('delete_ceshibg')
    label = _(u"delete data")
    fields = field.Fields(ICeshibg).omit('id')

    def getContent(self):
        locator = queryUtility(IDbapi, name='ceshibg')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete Ceshibg recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='ceshibg')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@ceshibg_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshibg_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshibg_listings')

class InputCeshibg(InputModel):
    """input db ceshibg table data
    """
    grok.name('input_ceshibg')
    label = _(u"Input data")
    fields = field.Fields(ICeshibg).omit('id')

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit ceshibg recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='ceshibg')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@ceshibg_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshibg_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshibg_listings')

class UpdateCeshibg(UpdateModel):
    """update Ceshibg table row data
    """
    grok.name('update_ceshibg')
    label = _(u"update data")
    fields = field.Fields(ICeshibg).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='ceshibg')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """
        data, errors = self.extractData()
        data['id'] =self.id
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='ceshibg')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@ceshibg_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshibg_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshibg_listings')
# end 测试报告 数据库操作
## 测试方法 数据库操作
class DeleteCeshiff(DeleteModel):
    "delete the specify Ceshiff recorder"

    grok.name('delete_ceshiff')
    label = _(u"delete data")
    fields = field.Fields(ICeshiff).omit('id')

    def getContent(self):
        locator = queryUtility(IDbapi, name='ceshiff')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete Ceshiff recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='ceshiff')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@ceshiff_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshiff_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshiff_listings')

class InputCeshiff(InputModel):
    """input db ceshiff table data
    """
    grok.name('input_ceshiff')
    label = _(u"Input data")
    fields = field.Fields(ICeshiff).omit('id')

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit ceshiff recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='ceshiff')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@ceshiff_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshiff_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshiff_listings')

class UpdateCeshiff(UpdateModel):
    """update Ceshiff table row data
    """
    grok.name('update_ceshiff')
    label = _(u"update data")
    fields = field.Fields(ICeshiff).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='ceshiff')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """
        data, errors = self.extractData()
        data['id'] =self.id
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='ceshiff')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@ceshiff_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshiff_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshiff_listings')
# end 测试方法 数据库操作
## 测试实验室 数据库操作
class DeleteCeshishysh(DeleteModel):
    "delete the specify Ceshishysh recorder"

    grok.name('delete_ceshishysh')
    label = _(u"delete data")
    fields = field.Fields(ICeshishysh).omit('id')

    def getContent(self):
        locator = queryUtility(IDbapi, name='ceshishysh')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete Ceshishysh recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='ceshishysh')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@ceshishysh_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshishysh_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshishysh_listings')

class InputCeshishysh(InputModel):
    """input db ceshishysh table data
    """
    grok.name('input_ceshishysh')
    label = _(u"Input data")
    fields = field.Fields(ICeshishysh).omit('id')

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit ceshishysh recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='ceshishysh')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@ceshishysh_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshishysh_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshishysh_listings')

class UpdateCeshishysh(UpdateModel):
    """update Ceshishysh table row data
    """
    grok.name('update_ceshishysh')
    label = _(u"update data")
    fields = field.Fields(ICeshishysh).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='ceshishysh')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """
        data, errors = self.extractData()
        data['id'] =self.id
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='ceshishysh')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@ceshishysh_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshishysh_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshishysh_listings')
# end 测试实验室 数据库操作
## 测试人员 数据库操作
class DeleteCeshiry(DeleteModel):
    "delete the specify Ceshiry recorder"

    grok.name('delete_ceshiry')
    label = _(u"delete data")
    fields = field.Fields(ICeshiry).omit('id')

    def getContent(self):
        locator = queryUtility(IDbapi, name='ceshiry')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Delete"))
    def submit(self, action):
        """Delete Ceshiry recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='ceshiry')
        try:
            funcations.DeleteByCode(self.id)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@ceshiry_listings')
        confirm = _(u"Your data  has been deleted.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshiry_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data delete
        """
        confirm = _(u"Delete cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshiry_listings')

class InputCeshiry(InputModel):
    """input db ceshiry table data
    """
    grok.name('input_ceshiry')
    label = _(u"Input data")
    fields = field.Fields(ICeshiry).omit('id')

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Submit ceshiry recorder
        """
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='ceshiry')
        try:
            funcations.add(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@ceshiry_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshiry_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshiry_listings')

class UpdateCeshiry(UpdateModel):
    """update Ceshiry table row data
    """
    grok.name('update_ceshiry')
    label = _(u"update data")
    fields = field.Fields(ICeshiry).omit('id')

    def getContent(self):
        # Get the model table query funcations
        locator = queryUtility(IDbapi, name='ceshiry')
        return locator.getByCode(self.id)

    @button.buttonAndHandler(_(u"Submit"))
    def submit(self, action):
        """Update model recorder
        """
        data, errors = self.extractData()
        data['id'] =self.id
        if errors:
            self.status = self.formErrorsMessage
            return
        funcations = queryUtility(IDbapi, name='ceshiry')
        try:
            funcations.updateByCode(data)
        except InputError, e:
            IStatusMessage(self.request).add(str(e), type='error')
            self.request.response.redirect(self.context.absolute_url() + '/@@ceshiry_listings')
        confirm = _(u"Thank you! Your data  will be update in back end DB.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshiry_listings')

    @button.buttonAndHandler(_(u"Cancel"))
    def cancel(self, action):
        """Cancel the data input
        """
        confirm = _(u"Input cancelled.")
        IStatusMessage(self.request).add(confirm, type='info')
        self.request.response.redirect(self.context.absolute_url() + '/@@ceshiry_listings')
# end 测试人员 数据库操作