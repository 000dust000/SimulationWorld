import unittest
from pygame import Surface
from settings import Settings
from cell import Cell
from simulationworld import SimulationWorld

class TestSimulationWorld(unittest.TestCase):
    def setUp(self):
        self.simulation_world = SimulationWorld()

    def test_init(self):
        self.assertIsInstance(self.simulation_world.settings, Settings)
        self.assertIsNone(self.simulation_world.screen)
        self.assertIsNone(self.simulation_world.bg_color)
        self.assertIsNone(self.simulation_world.fps)
        self.assertIsNone(self.simulation_world.clock)
        self.assertTrue(self.simulation_world.running)

    def test_game_init(self):
        self.simulation_world.game_init_()
        self.assertIsInstance(self.simulation_world.screen, Surface)
        self.assertEqual(self.simulation_world.bg_color, self.simulation_world.settings.bg_color)
        self.assertEqual(self.simulation_world.fps, self.simulation_world.settings.fps)