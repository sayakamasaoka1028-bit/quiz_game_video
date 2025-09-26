import pygame
import sys
from pygame._sdl2 import VideoPlayer

pygame.init()

# 正しい動画ファイルパスを指定
video_path = "assets/videos/プログラミングクイズ (Ubuntu) 2025-09-26 16-42-15.mp4"

# ウィンドウを作成
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("動画再生テスト")

try:
    player = VideoPlayer(video_path, screen)
    player.set_size((640, 480))
    player.play()
except ImportError:
    print("pygame._sdl2 が必要です")
    sys.exit()
except FileNotFoundError:
    print(f"動画ファイルが見つかりません: {video_path}")
    sys.exit()

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 動画フレームを更新
    player.update()

pygame.quit()
