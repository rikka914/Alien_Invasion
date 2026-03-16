import pygame
class Settings:
    """初始化游戏设置"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = self._extract_bg_color()
        #添加背景图片路径
        self.bg_image_path= 'images/BG.bmp'
    def _extract_bg_color(self):
        """从背景图片中提取颜色"""
        try:
            #加载图片
            image = pygame.image.load(self.bg_image_path)
            #获取图片左上角像素颜色
            color = image.get_at((0,0))
            #放回RGB值
            return color[:3]
        except Exception as e:
            print(f"无法加载图片或提取颜色: {e}")
            #失败时返回深蓝色
            return 0,51,102
