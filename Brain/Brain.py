#! /usr/bin/python

__author__="phr0zn"
__date__ ="$Jun 8, 2009 7:38:07 PM$"

from AlchemyDBHandler import AlchemyDBHandler

class Brain():

    _ENGINE = None
    _MODEL = "model"
    _KnowledgeBase = None

    def __init__(self):
        #self._ENGINE =AlchemyDBHandler("mysql://bot:phr0znb0t@192.168.1.143/bot")
        #self._ENGINE.importModel(_MODEL)
        #self._KnowledgeBase = self._ENGINE.model
        pass

    def __processCommands(self, response):
        """
            Processes incoming commands.
            
            @type response: Dictionary {"msg":"","user":""}
            @param response: User and message
            @rtype: Tuple
            @return: (Boolean, String)/(Success, Response)
        """
        cmd = response["msg"]
        GLOBALS = []
        LOCALS = []
        args = cmd[1:].split(" ")
        command = args[0]
        ## Get command function from database
        ## Execute command function
        
        
    def processMessage(self, response):
        """
            Processes incoming message from communication input.
            
            @type response: Dictionary {"msg":"","user":""}
            @param response: User and message
            @rtype: Tuple
            @return: (Boolean, String)/(Success, Response)
        """
        user = response["user"]
        msg = response["msg"]
        if msg[:1] == "!":
            self.__processCommands(response)

if __name__ == "__main__":
    print "Deze R tEh br4iNz!";
