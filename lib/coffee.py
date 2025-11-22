class Coffee:
    def __init__(self,brew):
        self.brew = brew

    @property
    def brew(self):
        return self._brew    
    
   