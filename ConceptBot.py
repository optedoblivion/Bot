#! /usr/bin/python

__author__="phr0zn"
__date__ ="$Jun 8, 2009 6:46:04 PM$"

from Brain import Brain
from Communications import Communications
from Peripherals import Peripherals
from PersonaliPy import PersonaliPy

import time

def log(message):
    print message

class Bot():

    ## This does most of the communicating with the database.
    ## Also this will perform calculations.
    _Brain = None
    ## This is how bot is feeling.
    _Personality = None
    ## These are is/are the way(s) to communicate with bot
    _Communications = None
    ## These are like bot's four other senses.
    ## I gave so much to communications I decided to split it off.
    _Peripherals = None

    ## This is what tells bot to die.
    _terminate = False
    ## This is for debugging mostly.
    _verbose = False

    def __init__(self):
        self._Personality = PersonaliPy()
        self._Brain = Brain()
        self._Communications = Communications()
        self._Peripherals = Peripherals()

    def act(self, action):
        ## Perform action
        # Communicate back to orinigating communication.
        # Communicate back to originating periphereal.
        pass

    def actRandomly(self, moodLevel):
        log("Acting randomly...")
        action = self._Brain.processAction(moodLevel)
        self.act(action)

    def checkInputs(self):
        log("Checking inputs...")
        signals = self._Peripherals.checkAll()
        communication = self._Communications.getEvents()
        return signals

    def getMood(self):
        return self._Personality.getMood()

    def react(self, signal, moodLevel):
        ## Check signal here to see what we're doing
        action = self._Brain.processReaction(signal, moodLevel)
        self.act(action)

    def terminate(self):
        self._terminate = True

    def startup(self):
        """
            Starts all modules and connectetions.
            
            @type self: Object
            @param self: Parent instance.
            @rtype: boolean
            @return True/False
        """
        pass

    def run(self):
        """
            Calls I{self}.startup() and begins main loop.
            
            @type self: Object
            @param self: Parent instance.
            @rtype: None
            @return None
        """
        self.startup()
        while not self._terminate:
            # Check Mood
            moodLevel = self.getMood()
            # Check Inputs
            # if input: respond; else: commit random act
            signal = self.checkInputs()
            if signal:
                self.react(signal, moodLevel)
#            else:
#                self.actRandomly(moodLevel)

#            time.sleep(1)



if __name__ == "__main__":
    bot = Bot()
    bot.run()
