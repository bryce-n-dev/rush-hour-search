class path_length():
    def __init__(self):
        self.length = 0
    
    def add_length(self)->None:
        self.length+=1
    
    def get_length(self)->int:
        return self.length