from mesa import Agent

class PondCell(Agent):
    """
    A pond cell.

    Attributes:
        x, y: Grid coordinates
        condition: Can be "water", "land"
        unique_id: (x,y) tuple.

    unique_id isn't strictly necessary here, but it's good
    practice to give one to each agent anyway.
    """

    def __init__(self, pos, model):
        """
        Create a new pond_cell.
        Args:
            pos: The pond_cell's coordinates on the grid.
            model: standard model reference for agent.
        """
        super().__init__(pos, model)
        self.pos = pos
        self.type = "land"

    def step(self):
        # doing nothing at the moment
        self.type = self.type
