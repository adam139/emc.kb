import os
import tempfile

import sqlalchemy

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from zope.configuration import xmlconfig
from zope.component import provideUtility


class Base(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plone.formwidget.autocomplete
        import emc.project
        import emc.memberArea
        import emc.kb
        import emc.theme
        xmlconfig.file('configure.zcml', plone.formwidget.autocomplete, context=configurationContext)
        xmlconfig.file('configure.zcml', emc.project, context=configurationContext)        
        xmlconfig.file('configure.zcml', emc.kb, context=configurationContext)
        xmlconfig.file('configure.zcml', emc.theme, context=configurationContext)
        xmlconfig.file('configure.zcml', emc.memberArea, context=configurationContext)        
   
    def tearDownZope(self, app):
        pass
        # Clean up the database
#        os.unlink(self.dbFileName)
        
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'emc.theme:default')
        applyProfile(portal, 'emc.project:default')        
        applyProfile(portal, 'emc.kb:default')
        applyProfile(portal, 'emc.memberArea:default')


FIXTURE = Base()
INTEGRATION_TESTING = IntegrationTesting(bases=(FIXTURE,), name="Base:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(bases=(FIXTURE,), name="Base:Functional")
