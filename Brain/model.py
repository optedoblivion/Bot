
###############
##  Caution  ##
##############################################################
##  Classes must be names the exact same case as the table! ##
##############################################################

class actions(object):
    """
        Need to know name of action.
        What action is -- definition.
        Mood level for committing action.

    """
    getAction(self, moodLevel):
        pass

class actions_i_like(object):
    """
        Maps to action
        number of good points
    """
    pass

class actions_i_dont_like(object):
    """
        Maps to action
        number of bad points
    """
    pass

class reactions(object):
    """
        Maps to action.
        each action can have multiple reactions.
    """

class moods(object):
    """
        Moods
        Mood Level
    """
    pass

class peripherals(object):
    pass

class phrases(object):
    pass

class words_i_like(object):
    """
        Maps to word
        number of good points
    """
    pass

class words_i_dont_like(object):
    pass

class words(object):
    """
        Word
        part of speech (noun, verb, etc...)
    """
    pass