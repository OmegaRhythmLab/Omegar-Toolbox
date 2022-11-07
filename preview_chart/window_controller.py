import pygame

from constants import *


class Window:
    """
    窗口
    """

    def __init__(self, title: str, bgimg_path: str) -> None:
        pygame.init()
        self.width = PREVIEW_TRACK_WIDTH*PREVIEW_TRACK_NUMBER+PREVIEW_SPLIT_WIDTH*(PREVIEW_TRACK_NUMBER+1)
        self.height = PREVIEW_WINDOW_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        self.bgimg = pygame.transform.scale(pygame.image.load(bgimg_path), (self.width, self.height))
        self.key_binding = {}
        self.key_release_binding = {}
        self.add_key_binding = self.key_binding.__setitem__
        self.add_key_release_binding = self.key_release_binding.__setitem__

    def start_drawing(self) -> None:
        """
        开始绘制帧时调用此函数
        """
        self.screen.blit(self.bgimg, (0, 0))
        for i in range(PREVIEW_TRACK_NUMBER+1):  # 绘制分割线
            rect_split_line = pygame.Rect(i*(PREVIEW_TRACK_WIDTH+PREVIEW_SPLIT_WIDTH), 0, PREVIEW_SPLIT_WIDTH, self.height)
            pygame.draw.rect(self.screen, PREVIEW_SPLIT_COLOR, rect_split_line)

    def draw_line(self, pos: float, alpha: float) -> None:
        """
        绘制判定线
        """
        real_pos = int(pos/CHART_FRAME_HEIGHT*self.height)
        pygame.draw.line(self.screen, (*PREVIEW_LINE_COLOR, int(alpha*255)), (0, real_pos), (self.width, real_pos), PREVIEW_LINE_WIDTH)

    def draw_note(self, pos: float, track: float) -> None:
        """
        绘制音符
        """
        real_pos_x = int((PREVIEW_TRACK_WIDTH+PREVIEW_SPLIT_WIDTH)*track+PREVIEW_SPLIT_WIDTH+PREVIEW_TRACK_WIDTH/2)
        real_pos_y = int(pos/CHART_FRAME_HEIGHT*self.height)
        rect_note = pygame.Rect((0, 0), PREVIEW_NOTE_SIZE)
        rect_note.center = (real_pos_x, real_pos_y)
        pygame.draw.rect(self.screen, PREVIEW_NOTE_COLOR, rect_note, border_radius=PREVIEW_NOTE_BORDER_RADIUS)

    def end_drawing(self) -> bool:
        """
        完成绘制帧时调用此函数，返回值表示是否退出游戏界面
        """
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key in self.key_binding:
                    self.key_binding[event.key]()
            elif event.type == pygame.KEYUP:
                if event.key in self.key_release_binding:
                    self.key_release_binding[event.key]()
        return False
