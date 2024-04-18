from settings import Settings

import time


class World:
    """世界的运行规则"""

    def __init__(self):
        """初始化世界状态"""
        self.settings = Settings()

        # 设置世界边界
        self.left = 0
        self.right = self.settings.screen_width
        self.top = 0
        self.bottom = self.settings.screen_height

        # 设置世界日夜属性
        self.day = True
        self.night = False

        # 设置世界氧气和二氧化碳
        self.oxygen = self.settings.world_oxygen
        self.carbon_dioxide = self.settings.world_carbon_dioxide

    def day_night_change(self):
        """设置白天黑夜"""
        if self.day:
            self.day = False
            self.night = True
        elif self.night:
            self.night = False
            self.day = True

    def update(self):
        """更新世界状态"""
        current_time = time.localtime()
        current_second = current_time.tm_sec
        if current_second % self.settings.world_day_time == 0:
            self.day_night_change()

    def oxygen_change(self, x):
        """氧气变化"""
        self.oxygen += x

    def carbon_dioxide_change(self, x):
        """二氧化碳变化"""
        self.carbon_dioxide += x