#-*- coding: UTF-8 -*-
from zope.lifecycleevent.interfaces import IObjectAddedEvent
from AccessControl.SecurityManagement import getSecurityManager
from plone.app.contenttypes.interfaces import IFolder
from zope.component import adapter
from plone.registry.interfaces import IRecordModifiedEvent
from emc.kb.interfaces import IDbapi
from zope.component import queryUtility
from five import grok
import datetime
from emc.kb.interfaces import ILogSettings
from emc.policy import get_ip,fmt,getfullname_orid


@grok.subscribe(IFolder,IObjectAddedEvent)
def SetLayout(obj, event):
    """ when add folder objcet in resource lib,
    set the folder layout to "folder_contents"."""
    
    path = obj.absolute_url()
    pattern = "kb_folder/resources_folder"
    default_layout = "folder_contents"
    if pattern not in path:pass
    else:
        obj.setLayout(default_layout)
 
@adapter(ILogSettings, IRecordModifiedEvent)
def detectLogsetChange(settings, event):
    
    user = getSecurityManager().getUser()
    if user is None:return     
    ip = get_ip()
    if ip=="":ip=' '
    adminid = getfullname_orid(user)
    values = {'adminid':adminid,'userid':u'log设置','datetime':datetime.datetime.now().strftime(fmt),
              'ip':ip,'type':0,'operlevel':4,'result':1,'description':u''}                
    values['description'] = u"%s更改了log设置:%s,由%s改为%s" % (adminid,
                                                        event.record.fieldName,
                                                        event.oldValue,
                                                        event.newValue) 
    locator = queryUtility(IDbapi, name='adminlog')
    locator.add(values)    
