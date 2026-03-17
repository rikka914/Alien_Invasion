import sys
from settings import Settings
from ship import Ship
import pygame

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        
        #加载背景图片
        self.bg_image = pygame.image.load(self.settings.bg_image_path)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            # 游戏帧率为60
            self.clock.tick(60)

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #按下方向键时 使飞船移动
                if event.key == pygame.K_RIGHT:
                    #向右移动飞船
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    #向左移动飞船
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                #松开方向键时 使飞船停止
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        #self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bg_image,(0,0))
        self.ship.blitme()

        #让最近绘制的屏幕可见
        pygame.display.flip()



if __name__ == '__main__':
    #创建实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
