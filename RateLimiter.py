class RateLimiter:
    '''
    Limits actions to a given delta threshold of time
    '''
    def __init__(self, deltaThreshold):
        self.deltaThreshold = deltaThreshold
    
    def canAct(self, previousTime, currentTime):
        return bool((currentTime - previousTime) > self.deltaThreshold)
    
    def canAct(self, deltaTime):
        return bool(deltaTime > self.deltaThreshold)