#!/usr/bin/env python

import time
from Communication.TDIRC import TDIRC
from Brain import Brain

class Bot(object):

    """
        This is a Bot.  It's original purpose is for IRC.
        All functions will read from config files in the future!
    """
    
    __Communications = None
    __TERMINATE = False
    __BRAIN = None
    
    def __init__(self):
        """
            Initializes parent object.
            
            @type self: Object
            @param self: Parent instance.
            @rtype: None
            @return None
        """
        self.startAll()
        while not self.__TERMINATE:
            time.sleep(5)
        
    def startAll(self):
        """
            Starts all modules and connections.
            
            @type self: Object
            @param self: Parent instance.
            @rtype: Tuple
            @return (Boolean, String)
        """
        ret = [True, "All systems go!"]
        ret = self._attachBrain()
        ret = self._startCommunications()

    def _attachBrain(self):
        try:
            self.__BRAIN = Brain()
            return [True, ""]
        except Exception, e:
            return [False, str(e)]
        

    def _startCommunications(self):
        """
            Starts all communications
            
            @type self: Object
            @param self: Parent instance.
            @rtype: Tuple
            @return (Boolean, String)
        """
        ## Iteratively read and assign connections.
        try:
            tdirc = TDIRC()
            tdirc.setBrain(self.__BRAIN)
            return [True, ""]
        except Exception, e:
            import traceback
            traceback.print_exc()
            return [False, str(e)]
        
        
if __name__=="__main__":
    bot = Bot()