import os
import random
import math
import time

# Emotion Engine

# set a target mood
# based on that target mood, use floor or ceil
# ceil is for Cheerful biased
# floor is for Pissed biased

class PersonaliPy:

    moods = {
                1.00:"Cheerful",
                2.00:"Happy",
                3.00:"Content",
                4.00:"Down",
                5.00:"Sad",
                6.00:"Destraught",
                7.00:"Bitter",
                8.00:"Angry",
                9.00:"Pissed"
            }

    MOOD = 2.00

    Terminate = False

    def __init__(self):
        pass
    
    def addModifier(self, change):
        self.OLDMOOD = self.MOOD
        if type(change) == type(1.11):
            self.MOOD = self.MOOD + change
            if self.MOOD > 9.00:
                self.MOOD = 9.00
        else:
            print "WARNING: Invalid Mood Modifier Type!"
    
    def delModifier(self, change):
        self.OLDMOOD = self.MOOD
        if type(change) == type(1.11):
            self.MOOD = self.MOOD - change
            if self.MOOD < 1.00:
                self.MOOD = 1.00
        else:
            print "WARNING: Invalid Mood Modifier Type!"
    
    def moodChanged(self):
        if self.OLDMOOD != self.MOOD:
            return True
        else:
            return False
    
    def getMood(self):
        return self.MOOD
    
    def displayMood(self):
        return str(self.moods[math.ceil(self.MOOD)])

# Actions
# Responses

# Good and Bad detector
# Alignment

# Attraction Engine

class Attraction:
    
    def __init__(self):
        pass
        

# Learning Engine...help?

class Learn:
    
    def __init__(self):
        pass

if __name__ == "__main__":
    
    bob = PersonaliPy()
    