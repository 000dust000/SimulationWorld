from cell import Cell
from settings import Settings
import random

class ProducerCell(Cell):
    """生产者细胞"""
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.size = self.settings.producer_cell_size
        self.speed = self.settings.producer_cell_speed
        self.color = self.settings.producer_cell_color
        self.health = self.settings.producer_cell_health
        self.oxygen = self.settings.producer_cell_oxygen
        self.carbon_dioxide = self.settings.producer_cell_carbon_dioxide
        self.search_radius = self.settings.producer_cell_search_radius


