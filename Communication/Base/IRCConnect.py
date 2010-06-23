import sys

try:
    import thread
    import time
    import irclib
except Exception, e:
    print str(e)
    sys.exit(1)

class IRCConnect:

    """
        IRC Communication layer.
    """

    _IRC = None
    _SERVER = []
    _BRAIN = None

    def msg(self, channel, msg):
        """
            Sends a message to the channel.
            
            @type channel: String
            @param channel: Target IRC channel.
            @type msg: String
            @param msg: Message to relay to target channel
        """
        return self._IRC.connections[0].privmsg(channel, msg)

    def Listen(self, e):
        """
            Start Listening
        """
        while True:
            self._IRC.process_forever()

    def __init__(self, userData):
        """
            Initializes parent object.
            This requires a dictionary with the following keys present:
            1. server
            2. port
            3. username
            4. password
            5. realname
            6. channels
            
            @type self: Object
            @param self: Parent instance.
            @type userData: Dictionary
            @param userDate: Dictionary of IRC connection information
            @rtype: None
            @return None
        """
        self._IRC = irclib.IRC()
        self._IRC.add_global_handler("privmsg", self._handlePrivMsg)
        self._IRC.add_global_handler("pubmsg", self._handlePubMsg)
        self._SERVER = self._IRC.server()
        connResult = self._SERVER.connect(userData["server"], userData["port"], 
                         userData["username"], ircname = userData["realname"])
        print "Connected."
        time.sleep(6)
        ## Make this more elaborate and have autostart commands
        #for channel in userData["channels"]:
        channel = userData["channels"][0]
        cmd = "identify " + userData["password"]
        self.msg("nickserv", "identify suenos")
        print "NickServed"
        time.sleep(6)
        #self.msg("chanserv", "invite " + channel)
        #time.sleep(6)
        #print "chanserved"
        self._SERVER.join(channel)
        print "joined %s" % channel
        thread.start_new_thread(self.Listen, ("IRC-Listener",))
        #t = threading.Thread(target=self.Listen, name="IRC-Listener")
        #t.setDaemon(True)
        #t.start()

    def _handlePrivMsg(self, connection, event):
        """
            Handles all private messages.
            
            @type self: Object
            @param self: Parent instance.
            @rtype: None
            @return None
        """
        self._handlePubMessage(connection, event)

    def _handlePubMsg(self, connection, event):
        """
            Handles all public messages.
            
            @type self: Object
            @param self: Parent instance.
            @type connection: IRC Connection
            @param connection: Current connection passed in from handler.
            @type event: IRC Event
            @param event: Current event passed in from handler.
            @rtype: None
            @return None
        """
        response = {}
        response["user"] = event.source().split("/")[0]
        try:
            response["msg"] = str(event.arguments()[0]).lower()
        except Exception, e:
            response["msg"] = e
            #self.msg(event.channel)?
            return False
        
        ## Call brain for processing.
        self._BRAIN.processMessage(response)
        ## Grab callback python data and execute it.
        
        