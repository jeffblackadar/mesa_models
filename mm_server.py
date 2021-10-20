from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from MoneyModel import MoneyModel


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "red",
                 "r": 0.5}
    return portrayal


grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

model_params = {
    "N": UserSettableParameter('slider', "Number of agents", 100, 2, 200, 1,
                               description="Choose how many agents to include in the model"),
    "width": 10,
    "height": 10
}

server = ModularServer(MoneyModel,
                       [grid],
                       "Money Model",
                       model_params)
server.port = 8521
server.launch()
