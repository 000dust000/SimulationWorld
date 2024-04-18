from settings import Settings


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
