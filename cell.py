from settings import Settings
import math
import random


class Cell:
    # 所有细胞共有的移动方向
    cells_move_x = 0
    cells_move_y = 0

    @staticmethod
    def set_cells_move():
        """设置所有细胞的移动方向"""
        Cell.cells_move_x = (random.random() - 0.5) * 2
        Cell.cells_move_y = (random.random() - 0.5) * 2

    # 构造方法
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
        # 细胞运动方向
        self.x_move = 0
        self.y_move = 0

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

    # def move_rules(self, world, cell_list):
    #     """细胞运动规则"""
    #
    #     # 获取周围细胞的中心坐标
    #     x_average, y_average = self.__get_center(cell_list)
    #
    #     # 细胞距离中心位置距离
    #     distance_x = x_average - self.x
    #     distance_y = y_average - self.y
    #
    #     # 将距离转换为中心方向
    #     x_toward_center = distance_x / self.search_radius
    #     y_toward_center = distance_y / self.search_radius
    #
    #     # 距离过近则对方向取反
    #     if distance_x < 0:
    #         x_toward_center = -x_toward_center
    #     if distance_y < 0:
    #         y_toward_center = -y_toward_center
    #
    #     # 获取一个-1到1之间的随机数
    #     # 单个细胞的随机数
    #     random_all_cell_x = (random.random() - 0.5) * 2
    #     random_all_cell_y = (random.random() - 0.5) * 2
    #
    #     # 最终运动方向
    #     x_move = x_toward_center + random_all_cell_x
    #     y_move = y_toward_center + random_all_cell_y
    #     return x_move, y_move
    #

    # 细胞运动方向改变
    def move_rules(self, world, cell_list):
        # 获取周围细胞的中心坐标
        x_average, y_average = self.__get_center(cell_list)

        # 将距离转换为中心方向
        x_toward_center = (x_average - self.x) / self.settings.cell_search_radius
        y_toward_center = (y_average - self.y) / self.settings.cell_search_radius

        # 距离过近则对方向取反
        if abs(x_toward_center) < self.settings.cell_distance:
            x_toward_center = -x_toward_center
        if abs(y_toward_center) < self.settings.cell_distance:
            y_toward_center = -y_toward_center

        # 获取一个-1到1之间的随机数
        x_random = (random.random() - 0.5) * 2 if self.__judge_through_rate(self.settings.cell_random_move_rate) else 0
        y_random = (random.random() - 0.5) * 2 if self.__judge_through_rate(self.settings.cell_random_move_rate) else 0

        # 最终运动方向
        x_move = self.__sigmoid(x_toward_center + x_random + Cell.cells_move_x) - 0.5
        y_move = self.__sigmoid(y_toward_center + y_random + Cell.cells_move_y) - 0.5

        return x_move, y_move

    def move(self, cell_list):
        """细胞运动"""
        x_move, y_move = self.move_rules(self.world, cell_list)
        self.x_move += x_move
        self.y_move += y_move

        self.__check_collision()

        if self.x_move > 1:
            self.x_move = 1
        if self.x_move < -1:
            self.x_move = -1

        self.x += self.x_move * self.speed
        self.y += self.y_move * self.speed

        self.__check_boundary()

    def __judge_through_rate(self, rate):
        """判断通过率"""
        if random.random() < rate:
            return True
        else:
            return False

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
        if self.x < self.world.left + self.size or self.x > self.world.right - self.size:
            self.x_move = -self.x_move
        if self.y < self.world.top + self.size or self.y > self.world.bottom - self.size:
            self.y_move = -self.y_move

    # 检测细胞碰撞
    def __check_collision(self):
        """检查细胞碰撞"""
        # self.world.refresh_cell_location(cell_list)
        for location in self.world.world_cell_location:
            if self.x == location[0] and self.y == location[1]:
                continue
            if (self.x - location[0]) ** 2 + (self.y - location[1]) ** 2 <= 0.5 * (self.size + location[2]) ** 2:
                self.x_move = -self.x_move
                self.y_move = -self.y_move

    # 检测细胞存活状态
    def check_alive(self):
        """检查细胞存活状态"""
        if self.oxygen <= 0 or self.carbon_dioxide >= 100000:
            self.alive = False

    def cell_change(self, cell_list):
        """细胞状态变化"""
        self.oxygen -= 1
        self.carbon_dioxide += 1
        if not self.alive:
            cell_list.remove(self)

    def update(self, cell_list):
        """更新细胞状态"""
        self.move(cell_list)
        self.cell_change(cell_list)
