import pygame


class Settings:
    def __init__(self):
        """初始化游戏设置"""

        """游戏界面设置"""
        # 设置游戏界面大小
        self.screen_width = 800
        self.screen_height = 600
        # 设置游戏界面标题
        self.caption = '生命游戏'
        # 设置游戏界面背景色
        self.bg_color = (0, 0, 0)
        # 设置游戏界面刷新率
        self.fps = 60

        """细胞设置"""
        # 设置细胞颜色为绿色
        self.cell_color = (0, 255, 0)
        # 细胞视觉半径
        self.cell_search_radius = 1

        # 设置细胞大小
        self.cell_size = 10
        # 设置细胞速度
        self.cell_speed = 4
        # 设置细胞生命状态

        self.cell_alive = True
        self.cell_health = 10000
        self.cell_oxygen = 10000
        self.cell_carbon_dioxide = 10000

        """生产者细胞设置"""
        # 设置生产者细胞颜色为绿色
        self.producer_cell_color = (0, 255, 0)
        self.producer_cell_size = 10
        self.producer_cell_speed = 4
        self.producer_cell_health = 10000
        self.producer_cell_oxygen = 10000
        self.producer_cell_carbon_dioxide = 10000
        self.producer_cell_search_radius = 1

        """消费者细胞设置"""
        # 设置消费者细胞颜色为红色
        self.consumer_cell_color = (255, 0, 0)
        self.consumer_cell_size = 10
        self.consumer_cell_speed = 4
        self.consumer_cell_health = 10000
        self.consumer_cell_oxygen = 10000
        self.consumer_cell_carbon_dioxide = 10000
        self.consumer_cell_search_radius = 1


        """世界设置"""
        self.world_oxygen = 100
        self.world_carbon_dioxide = 100
        self.world_day_time = 30
