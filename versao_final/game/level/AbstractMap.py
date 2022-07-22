from abc import ABC, abstractmethod


class AbstractLevel(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def draw_background(self, screen):
        pass

    @abstractmethod
    def next_map(self,current_map): 
        pass
