class Match(object):
    def __init__(self):
        self.matchType = "";
        self.mapName = "";
        self.matchLength = "";
        self.heroName = "";
        self.heroLevel = "";
        self.matchmakingRating = "";
        self.ratingAdjustmentPoints = "";
        self.matchDateTime = "";

    def makeMatch(matchType, mapName, matchLength, heroName, heroLevel, matchmakingRating, ratingAdjustmentPoints, matchDateTime):
        match = Match(matchType, mapName, matchLength, heroName, heroLevel, matchmakingRating, ratingAdjustmentPoints, matchDateTime);
        return match;

    def setMatchType(self, matchType):
        self.matchType = matchType;

    def setMapName(self, mapName):
        self.mapName = mapName;
    
    def setMatchLength(self, matchLength):
        self.matchLength = matchLength;

    def setHeroName(self, heroName):
        self.heroName = heroName;

    def setHeroLevel(self, heroLevel):
        self.heroLevel = heroLevel;

    def setMatchmakingRating(self, matchmakingRating):
        self.matchmakingRating = matchmakingRating;

    def setRatingAdjustmentPoints(self, ratingAdjustmentPoints):
        self.ratingAdjustmentPoints = ratingAdjustmentPoints;

    def setMatchDateTime(self, matchDateTime):
        self.matchDateTime = matchDateTime;

    # TODO: Complete Current Model
    # matchType - init data, derived
    # mapName - details
    # matchLength - not sure
    # heroName - details
    # heroLevel - not sure
    # matchmakingRating - calculated
    # ratingAdjustmentPoints - calculated
    # matchDateTime - details

    # TODO: Changes for Future Model
    # matchOutcome - details or init data
    # talent choices - tracker events
    # score result screen stats - tracker events
    # teammates and enemy team player names and hero picks - details
    # season - derived