import pygame
from settings import Settings
from cell import Cell
from world import World


class SimulationWorld:
    def __init__(self):
        """初始化状态"""
        self.settings = Settings()
        self.world = World()
        self.game_init_()
        self.cell_list = []

    def game_init_(self):
        """游戏初始化"""

        # 使用pygame绘制游戏界面
        pygame.init()
        # 设置游戏界面大小
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 设置游戏界面标题
        pygame.display.set_caption(self.settings.caption)
        # 设置游戏界面背景颜色
        self.bg_color = self.settings.bg_color
        # 设置游戏帧率
        self.fps = self.settings.fps
        # 设置游戏时钟
        self.clock = pygame.time.Clock()
        # 设置游戏状态
        self.running = True

    def draw_cell(self):
        """绘制细胞"""
        for cell in self.cell_list:
            pygame.draw.circle(self.screen, cell.color, (cell.x, cell.y), cell.size)

    def run_game(self):
        """游戏主循环"""
        while self.running:
            # 设置游戏帧率
            self.clock.tick(self.fps)
            # 监听游戏事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # 更新游戏状态
            self.screen.fill(self.bg_color)

            Cell.set_cells_move()
            for cell in self.cell_list:
                cell.update( self.cell_list)
            # 绘制细胞
            self.draw_cell()
            # 更新游戏界面
            pygame.display.flip()
        # 退出游戏
        pygame.quit()

if __name__ == '__main__':
    simulation_world = SimulationWorld()
    simulation_world.cell_list = [Cell(100, 100, simulation_world.world) for _ in range(10)]
    simulation_world.run_game()



