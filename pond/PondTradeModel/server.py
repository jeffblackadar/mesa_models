from mesa.visualization.modules import CanvasGrid, ChartModule, PieChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

from .model import PondMap

COLORS = {"water": "#0000AA", "land": "#008800"}

def pond_portrayal(agent):
    if agent is None:
        return
    if agent.type=="mapcell":
        portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}
        (x, y) = agent.pos
        portrayal["x"] = x
        portrayal["y"] = y
        portrayal["Color"] = COLORS[agent.terrain]    

    if agent.type=="port":
        portrayal = {"Shape": "circle", "r": 2, "Filled": "true", "Layer": 1}
        (x, y) = agent.pos
        portrayal["x"] = x
        portrayal["y"] = y
        portrayal["Color"] = "#ffff00"



    return portrayal


canvas_element = CanvasGrid(pond_portrayal, 100, 100, 500, 500)

model_params = {
    "height": 100,
    "width": 100
}
server = ModularServer(
    PondMap, [canvas_element], "Pond Trade Model", model_params
)
