from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import Grid
from mesa.time import RandomActivation

from PondTradeModel.agent import PondCell

class Pond(Model):

    def __init__(self, height=100, width=100):
        """

        Args:
            height, width: The size of the grid to model

        """
        # Set up model objects
        self.schedule = RandomActivation(self)
        self.grid = Grid(height, width, torus=False)

        # Seteach cell with Prob = density
        for (contents, x, y) in self.grid.coord_iter():
            # Create a pond_cell
            new_pond_cell = PondCell((x, y), self)
            if self.random.random() < 0.5:
                new_pond_cell.type = "land"
            else:
                new_pond_cell.type = "water"
            self.grid._place_agent((x, y), new_pond_cell)
            self.schedule.add(new_pond_cell)

        self.running = True
        

    def step(self):
        """
        Advance the model by one step.
        """
        self.schedule.step()
