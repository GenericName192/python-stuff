class User():

    def __init__(self):
        self.rank = -8
        self.progress = 0
    
    def printRank(self):
        return self.rank
    
    def printProgress(self):
        return self.progress
    
    def inc_progress(self, activityRank):

        if (activityRank < -8) or (activityRank == 0) or (activityRank > 8):
            raise ValueError("The value must be between -8 and 8 exculding 0")

        if self.rank == 8:
            return
        
        if (self.rank < 0 and activityRank > 0) or (self.rank > 0 and activityRank < 0):
            badFix = 1 # I hate this as a fix but I couldnt think of anything better
        else:
            badFix = 0

        if self.rank > activityRank:

            if abs(self.rank - activityRank) - badFix >= 2:
                pass

            else:
                self.progress += 1
                self.rankUp()

        elif self.rank == activityRank:
            self.progress += 3
            self.rankUp()

        elif self.rank < activityRank:
            difference = abs(self.rank - activityRank) - badFix
            self.progress += (10 * difference * difference)
            self.rankUp()

    def rankUp(self):
        while self.progress >= 100:

            if self.progress >= 100:
                self.progress -= 100
                self.rank += 1

                if self.rank == 0:
                    self.rank = 1

                if self.rank == 8:
                    self.progress = 0

    