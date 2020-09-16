from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext import declarative
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
os.environ['NLS_LANG'] = '.AL32UTF8'

# Set up the i18n message factory for our package
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('emc.kb')

InputDb = "emc.kb:Input db"
DoVote = "emc.kb:Do vote"

ORMBase = declarative.declarative_base()
# common user (no sys user) can not  connect as sysdba
ora_engine = create_engine('oracle+cx_oracle://emc:Micro0plone@kwsensen.f3322.net:1521/?service_name=orclpdb1&encoding=UTF-8&events=true')
#ora_engine = create_engine('oracle+cx_oracle://sys:EMCcontainer1@kwsensen.f3322.net:1521/?service_name=orclpdb1&mode=2&encoding=UTF-8&events=true')

Session_log = sessionmaker(bind=ora_engine)
log_session = Session_log()
pas_session = log_session
kb_session = log_session
t_session = log_session
