from mesa.visualization.modules import CanvasGrid, ChartModule, PieChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

from .model import Pond

COLORS = {"water": "#0000AA", "land": "#008800"}

def pond_portrayal(pond_cell):
    if pond_cell is None:
        return
    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}
    (x, y) = pond_cell.pos
    portrayal["x"] = x
    portrayal["y"] = y
    portrayal["Color"] = COLORS[pond_cell.type]
    return portrayal


canvas_element = CanvasGrid(pond_portrayal, 100, 100, 500, 500)

model_params = {
    "height": 100,
    "width": 100
}
server = ModularServer(
    Pond, [canvas_element], "Pond Trade Model", model_params
)
