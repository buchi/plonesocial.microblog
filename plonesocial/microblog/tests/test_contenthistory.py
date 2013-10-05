import unittest2 as unittest
from zope.component import queryUtility
from zope.event import notify
from Products.Archetypes.event import ObjectEditedEvent

from plonesocial.microblog.interfaces import IMicroblogTool
from plone.app.testing import TEST_USER_ID, setRoles

from plonesocial.microblog.testing import \
    PLONESOCIAL_MICROBLOG_INTEGRATION_TESTING


class TestNestedStatusContainer(unittest.TestCase):

    layer = PLONESOCIAL_MICROBLOG_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.container = queryUtility(IMicroblogTool)
        parent_id = self.portal.invokeFactory('Folder', 'parent')
        self.parent_context = self.portal[parent_id]

        child_id = self.parent_context.invokeFactory('Document', 'child')
        self.child_context = self.parent_context[child_id]
        self.child_context.unmarkCreationFlag()


    def test_status_update_on_modification(self):
        notify(ObjectEditedEvent(self.child_context))
        self.assertEquals('obj modified', list(self.container.values())[0].text)