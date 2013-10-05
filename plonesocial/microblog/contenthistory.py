from zope.component import queryUtility
from plonesocial.microblog.interfaces import IMicroblogTool
from plonesocial.microblog.statusupdate import StatusUpdate


def object_modified(obj, event):

    container = queryUtility(IMicroblogTool)
    status = StatusUpdate('obj modified', context=obj)
    container.add(status)
