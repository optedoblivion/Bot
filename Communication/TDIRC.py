from Base.IRCConnect import IRCConnect

class TDIRC(IRCConnect):
    
    """
        Teamdouche IRC Connection
    """
    
    def setBrain(self, brain):
        self._BRAIN = brain
    
    def __init__(self):
        """
            Initializes parent object.
            Sets up user data and calls super
            
            @type self: Object
            @param self: Parent instance.
            @rtype: None
            @return None
        """
        userData = {}
        userData["server"] = "irc.freenode.com"
        userData["username"] = "optedoblivion2"
        userData["port"] = 6667
        userData["password"] = "suenos"
        userData["realname"] = "OptedBot"
        userData["channels"] = ["#fo0k"]
        IRCConnect.__init__(self, userData)