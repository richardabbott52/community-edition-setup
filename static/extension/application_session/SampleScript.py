# oxAuth is available under the MIT License (2008). See http://opensource.org/licenses/MIT for full text.
# Copyright (c) 2016, Gluu
#
# Author: Yuriy Movchan
#

from org.gluu.model.custom.script.type.session import ApplicationSessionType
from org.gluu.util import StringHelper, ArrayHelper
from java.util import Arrays, ArrayList

import java

class ApplicationSession(ApplicationSessionType):
    def __init__(self, currentTimeMillis):
        self.currentTimeMillis = currentTimeMillis

    def init(self, configurationAttributes):
        print "Application session. Initialization"
        print "Application session. Initialized successfully"

        return True   

    def destroy(self, configurationAttributes):
        print "Application session. Destroy"
        print "Application session. Destroyed successfully"
        return True   

    def getApiVersion(self):
        return 2

    # Application calls it at start session request to allow notify 3rd part systems
    #   httpRequest is javax.servlet.http.HttpServletRequest
    #   authorizationGrant is org.gluu.oxauth.model.common.AuthorizationGrant
    #   configurationAttributes is java.util.Map<String, SimpleCustomProperty>
    def startSession(self, httpRequest, authorizationGrant, configurationAttributes):
        print "Application session. Starting external session"

        print "Application session. External session started successfully"
        return True

    # Application calls it at end session request to allow notify 3rd part systems
    #   httpRequest is javax.servlet.http.HttpServletRequest
    #   authorizationGrant is org.gluu.oxauth.model.common.AuthorizationGrant
    #   configurationAttributes is java.util.Map<String, SimpleCustomProperty>
    def endSession(self, httpRequest, authorizationGrant, configurationAttributes):
        print "Application session. Starting external session end"

        print "Application session. External session ended successfully"
        return True
