from settings import Settings
import math
import random


class Cell:
    def __init__(self, x, y, world):
        self.settings = Settings()
        self.world = world
        """初始化细胞"""

        # 细胞大小,速度,颜色
        self.size = self.settings.cell_size
        self.speed = self.settings.cell_speed
        self.color = self.settings.cell_color
        # 细胞坐标
        self.x = x
        self.y = y
        # 细胞生命状态
        self.alive = True
        self.health = self.settings.cell_health
        self.oxygen = self.settings.cell_oxygen
        self.carbon_dioxide = self.settings.cell_carbon_dioxide
        # 细胞视距半径
        self.search_radius = self.settings.cell_search_radius

    def __is_visible(self, cell):
        """判断细胞是否在可视范围内"""
        return (self.x - cell.x) ** 2 + (self.y - cell.y) ** 2 <= self.search_radius ** 2

    def __get_center(self, cell_list):
        """获取细胞视距范围内所有细胞的中心坐标"""
        x_average = 0
        y_average = 0
        cell_number = 0
        for cell in cell_list:
            if self.__is_visible(cell):
                x_average += cell.x
                y_average += cell.y
                cell_number += 1
        x_average = x_average / cell_number
        y_average = y_average / cell_number
        return x_average, y_average

    def move_rules(self, world, cell_list):
        """细胞运动规则"""

        # 获取周围细胞的中心坐标
        x_average, y_average = self.__get_center(cell_list)

        # 细胞距离中心位置距离
        distance_x = x_average - self.x
        distance_y = y_average - self.y

        # 将距离转换为中心方向
        x_toward_center = distance_x / self.search_radius
        y_toward_center = distance_y / self.search_radius

        # 距离过近则对方向qv'fan

        # 获取一个-1到1之间的随机数
        # 单个细胞的随机数
        random_all_cell_x = (random.random() - 0.5) * 2
        random_all_cell_y = (random.random() - 0.5) * 2

        # 最终运动方向
        x_move = x_toward_center + random_all_cell_x
        y_move = y_toward_center + random_all_cell_y
        return x_move, y_move

    def move(self, cell_list):
        """细胞运动"""
        x_move, y_move = self.move_rules(self.world, cell_list)
        self.x += x_move * self.speed
        self.y += y_move * self.speed

        self.__check_boundary()

    def __sigmoid(self, x):
        """Sigmoid函数"""
        if x < -10:
            return 0
        elif x > 10:
            return 1
        else:
            return 1 / (1 + math.exp(-x))

    def __check_boundary(self):
        """检查边界"""
        if self.x < self.world.left:
            self.x = self.world.left
        if self.x > self.world.right:
            self.x = self.world.right
        if self.y < self.world.top:
            self.y = self.world.top
        if self.y > self.world.bottom:
            self.y = self.world.bottom

    # 检测细胞存活状态
    def check_alive(self):
        """检查细胞存活状态"""
        if self.oxygen <= 0 or self.carbon_dioxide >= 100:
            self.alive = False

    def cell_change(self,cell_list):
        """细胞状态变化"""
        self.oxygen -= 1
        self.carbon_dioxide += 1
        if self.alive:
            cell_list.remove(self)

    def update(self,cell_list):
        """更新细胞状态"""
        self.move(cell_list)
        self.cell_change(cell_list)
