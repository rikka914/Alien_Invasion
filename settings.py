class Settings:
    """初始化游戏设置"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        #提取图片主色调作为背景色
        self.bg_color = self.extract_dominant_color(self.bg_image_path)
        #添加背景图片路径
        self.bg_image_path= 'images/BG.bmp'
