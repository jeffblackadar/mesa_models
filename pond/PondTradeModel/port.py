from mesa import Agent


class Port(Agent):

    def __init__(self, pos, model):
        """
        Create a port, in the given state, at the given x, y position.
        """
        super().__init__(pos, model)
        self.x, self.y = pos
        self.color = "black"
        self.type = "port"        


    @property
    def neighbors(self):
        return self.model.grid.neighbor_iter((self.x, self.y))


    def neighbors_outer(self, radius):
        return self.model.grid.iter_neighbors((self.x, self.y),False,radius)       
    

    @property
    def considered(self):
        return self.isConsidered is True

    def step(self):
        # assume no state change
        self._nextState = self.state
        self.model.grid.place_agent(self,(self.x, self.y))
        
    """
        self.cells_cut = 0
        if self.state > 0:
            for neighbor in self.neighbors_outer(self.mill_radius):
                if neighbor.isForestMature() == True:
                    neighbor._nextState = neighbor.FORESTCUT
                    neighbor.forest_age = 0
                    neighbor.isConsidered = True
                    self.cells_cut = self.cells_cut + 1
                    if self.cells_cut >= self.max_cut:
                        break
        # Did mill harvest enough            
        if self.cells_cut < self.max_cut:
            self._nextState = 0
            print("Mill is out of business!")
            self.color = "grey"
    """ 


    def advance(self):
        """
        Set the state to the new computed state -- computed in step().
        """
        self.state = self._nextState
