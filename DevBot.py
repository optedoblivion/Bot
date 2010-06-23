###########
# Imports #
################################################################################
import  os, sys, thread,\
        traceback, time,\
        xmlrpclib       
try:
    import irclib
    
except:
    print "\n\nImport of irclib has failed!  Please install python-irclib!\n\n"
    sys.exit(1)
    
from DocXMLRPCServer import DocXMLRPCServer
from DBHandler import DBHandler
from PersonaliPy import Mood

db = DBHandler()

################################################################################

#########################
# Credits:              #
#########################
#                       #
#   Martin Brabham      #
#                       #
#   Chris Soyars        #
#                       #
#########################

################
# DevBot Class #
################
class DevBot:###
################
    
    ##########################
    # Connection information #
    ##########################
    network = '10.10.20.7'   #
    port = 6667              #
    channel = '#dev'         #
    nick = 'DevBiotch'       #
    name = 'd3vb07'          #
    ##########################

    ########
    # Mood #
    #####################
    myMood = Mood()     #
    #####################    
    
    goodWords = ['computer', 'food', 'lunch']
    badWords = ['die', 'hate', 'lol cat', 'dance', 'suck it']
    
    #####################
    # Create IRC Object #
    #####################
    irc = irclib.IRC()###
    #####################

    ##################
    # Terminate Flag #
    ######################
    terminateFlag = False#
    ######################
    
    #####################
    # Add Handlers Here #
    #####################
    def __init__(self):##
    #####################
        
        #################
        # Add Handlers #
        ###############################################################
        self.irc.add_global_handler('privmsg', self.handlePrivMessage)#
        self.irc.add_global_handler('pubmsg', self.handlePubMessage)  #
        ###############################################################

        ########################################################
        # Create a server object, connect and join the channel #
        ########################################################################
        server = self.irc.server()                                             #
        server.connect(self.network, self.port, self.nick, ircname = self.name)#
        server.join(self.channel)                                              #
        ########################################################################

    ####################
    # Private messages #
    #################################################
    def handlePrivMessage (self, connection, event):#
    #################################################
    
        self.handlePubMessage(connection, event)
    
   
    ###################
    # Public messages #
    ################################################
    def handlePubMessage (self, connection, event):#
    ################################################

        ############
        # Get User #
        ####################################
        user = event.source().split('!')[0]#
        ####################################

        ###############################
        # Get Message  and force lower#
        ###############################
        msg = event.arguments()[0]    #
        msg = str(msg).lower()        #
        ###############################

        ################
        # Command List #
        ########################################################################
        cmdList = [                                                            #
                "!ops - Gives authorized users ops",                           #
                "!8ball - Have questions? Ask the magic 8-ball!",              #
                "!lsmodules <manager> - Lists all modules running in manager", #
"!stat <manager> [module] - Shows status of manager or a module on the manager",
                ""
                  ]

        #####################
        # Command Character #
        #####################
        cmdChar = '!'       #
        #####################

        ########################
        # Start Command Filter #
        ###########################
        try:                      #
            if msg[:1] == cmdChar:#
        ###########################

                ################
                # Get argv/cmd #
                ######################
                argv = msg.split(" ")#
                cmd = argv[0]        #
                ######################
                
                ############
                # Give Ops #
                ################################################################
                if cmd == "!ops":                                              #
                    if user.lower() == "reaper" or user.lower() == "staticv0id" or user.lower() == "ripper^^":
                        connection.mode(self.channel, "+o %s" % user)          #
                    else:                                                      #
                        connection.notice(self.channel, "You are not           \
                        authorized to have ops")                               #
                ################################################################
                
                ################
                # MAGICK 8BALL #
                ################################################################
                elif cmd == "!8ball":                                          #
                    responses = {                                              #
                                    1:"Signs point to yes.",                   #
                                    2:"Yes.",                                  #
                                    3:"Reply hazy, try again.",                #
                                    4:"Without a doubt.",                      #
                                    5:"My sources say no.",                    #
                                    6:"As I see it, yes.",                     #
                                    7:"You may rely on it.",                   #
                                    8:"Concentrate and ask again.",            #
                                    9:"Outlook not so good.",                  #
                                    10:"It is decidedly so.",                  #
                                    11:"Better not tell you now.",             #
                                    12:"Very doubtful.",                       #
                                    13:"Yes - definitely.",                    #
                                    14:"It is certain.",                       #
                                    15:"Cannot predict now.",                  #
                                    16:"Most likely.",                         #
                                    17:"Ask again later.",                     #
                                    18:"My reply is no.",                      #
                                    19:"Outlook good.",                        #
                                    20:"Don't count on it."                    #
                                }                                              #
                    import random                                              #
                    ans = random.randint(1,20)                                 #
                    connection.privmsg(self.channel, "8ball: %s"%responses[ans])
                ################################################################
                
                ##############
                # LS m0dul3s #
                ################################################################
                elif cmd == "!lsmodules":                                      #
                    if len(argv) == 2:                                         #
                        query = "SELECT address,port FROM manager_instances    \
                        WHERE LOWER(name) = '%s' LIMIT 1"                      \
                        % str(argv[1]).lower()                                 #
                        result = db.query(query)                               #
                        address = ""                                           #
                        port = 0                                               #
                        for row in result:                                     #
                            address = str(row[0])                              #
                            port = int(row[1])                                 #
                        if address and port:                                   #
                            s = xmlrpclib.Server('http://%s:%s' % (address,port))
                            results = s.getServices()                          #
                            response = ""                                      #
                            for res in results:                                #
                                response += str(res)                           #
                                response += " | "                              #
                            response = response[:(len(response)-3)]            #
                            response = "[%s]=-=[%s]"%(argv[1],response)        #
                            connection.notice(self.channel, response)          #
                        else:                                                  #
                            connection.notice(self.channel,                    \
                            "Module %s does not exist!" % argv[1])             #
                    else:                                                      #
                        connection.privmsg(self.channel,                       \
                                           "Incorrect number of arguments")    #
                ################################################################

                ########
                # Dice #
                ################################################################
                elif cmd == "!roll":                                           #
                    import random                                              #
                    num = random.randint(1,20)                                 #
                    connection.privmsg(self.channel, "Dice: %s" % num)         #
                ################################################################

                #####################
                # Display Help Menu #
                ################################################################
                elif cmd == "!help":                                           #
                    connection.privmsg(self.channel,                           \
"+---------------------------------=[HELP]=---------------------------------+")#
                    for cmd in cmdList:                                        #
                        connection.privmsg(self.channel, "\t%s"%cmd)           #
                    connection.privmsg(self.channel,                           \
"+--------------------------------------------------------------------------+")#
                ################################################################

                else:
                    """ This pulls external functions from the database! """
                    query = "SELECT function from devbot_cmds WHERE\
                            instance = 1 AND command LIKE '%s%s' LIMIT 1" %\
                            (cmd,'%')
                    function = db.query(query)
                    if function:
                        if function[0]:
                            function = function[0][0]
                            functions = function.split("\n")
                            for func in functions:
                                exec'%s'%str(func+"\n").replace("'","\'")
                            
                        else:
                            connection.privmsg(self.channel,\
                                            "Invalid command '%s'!" % cmd)
                    else:
                        connection.privmsg(self.channel,\
                            "Invalid command '%s'!" % cmd)
    
            ###############################
            # Filter Message for Chatting #
            ####################################################################
            else:                                                              #
                if str(self.nick).lower() in msg:                              #
                    if "hello" in msg:                                         #
                        connection.privmsg(self.channel, "Hello, %s" % user)   #
                    elif "die" in msg:                                         #
                        dieMsg = "Why do you want to kill me? ;("              #
                        connection.privmsg(self.channel, dieMsg)               #
                    elif "dance" in msg:                                       #
                        danceMsg = "You dance mother%@#$#$!"                   #
                        connection.kick(self.channel, user, danceMsg)          #
                for word in self.goodWords:                                    #
                    if str(word).lower() in msg:                               #
                        self.myMood.delModifier(0.10)                          #
                        print "good points"
                for word in self.badWords:                                     #
                    if str(word).lower() in msg:                               #
                        self.myMood.addModifier(0.10)                          #
                        print "bad points"
                if self.myMood.moodChanged:
                    
                    print "I am %s." % self.myMood.displayMood()
                    #connection.privmsg(self.channel,\
                    #"I am %s." % self.myMood.displayMood())
            ####################################################################

        ##########
        # WTF M8 #
        ##########################
        except Exception, data:  #
            traceback.print_exc()#
        ##########################
        
        ## Get commands and mapped functions (python functions)
        #query = "SELECT cmd, function FROM bot_commands"
        #commands = db.query(query)
        
        #try:
        #    if str(nick).lower() in msg:
        #        for command in commands:
        #            if str(command[0]) in msg:
        #                pass
        #except Exception, data:
        #    traceback.print_exc()

        ## Command Core
        #try:
        #    if msg[:len("grabber status")] == "grabber status":
        #        cmd = msg.split(" ")
        #        if len(cmd) == 3:
        #            query = "SELECT address,port FROM manager_instances WHERE LOWER(name) = '%s' LIMIT 1" % str(cmd[2]).lower()
        #            result = db.query(query)
        #            address = ""
        #            port = 0
        #            for row in result:
        #                address = str(row[0])
        #                port = int(row[1])
        #
        #            # connect via xmlrpc and get status and put in chat
        #            if address and port:
        #                s = xmlrpclib.Server('http://%s:%s' % (address,port))
        #                results = s.statusCheck()
        #                response = "-=[Working: 1337]=[In Queue: 6969]=[Stuff: 1234]=-"
        #                connection.notice(self.channel, response)
        #            else:
        #                connection.notice(self.channel, "Module %s does not exist!" % cmd[2])

   
    ##################
    # Send a Message #
    ###########################################################
    def sendMsg(self, message):                               #
        self.irc.connections[0].privmsg(self.channel, message)#
        return 0                                              #
    ###########################################################
    
    #################
    # Main Bot Loop #
    ###############################
    def Listen(self, e):          #
        threadName = str(e)       #
        ## Infinite Loop          #
        self.irc.process_forever()#
    ###############################
        

#############
# Main Init #
###########################
if __name__ == "__main__":#
###########################
    
    #################
    # Create Devbot #
    #################
    bot = DevBot()  #
    #################

    ##############
    # XMLRPC msg #
    ############################
    def msg(msg):              #
        return bot.sendMsg(msg)#
    ############################
    
    ####################
    # Start Bot Thread #
    ##################################################
    thread.start_new_thread(bot.Listen,('DevBot-1',))#
    ##################################################

    #######################
    # Setup XMLRPC Server #
    ########################################################################
    query = "SELECT address,port FROM devbot WHERE LOWER(name) = 'DevBot'  \
            LIMIT 1"                                                       #
    svrnfo = db.query(query)                                               #
    try:                                                                   #
        svrnfo = svrnfo[0]                                                 #
    except:                                                                #
        print "No instance found!"                                         #
        sys.exit(1)                                                        #
    server = DocXMLRPCServer(svrnfo, logRequests=0)                        #
    server.set_server_name("DevBot")                                       #
    server.register_function(msg)                                          #
    while not bot.terminateFlag:                                           #
        server.handle_request()                                            #
    ########################################################################
