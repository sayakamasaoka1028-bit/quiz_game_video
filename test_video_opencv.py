import cv2
import pygame
import sys

# Pygame 初期化
pygame.init()

# 動画ファイルパス
video_path = "assets/videos/プログラミングクイズ (Ubuntu) 2025-09-26 16-42-15.mp4"

# OpenCV で動画を読み込み
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"動画ファイルが見つかりません: {video_path}")
    sys.exit()

# 動画の幅と高さを取得
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Pygame ウィンドウ作成
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("動画再生テスト")

clock = pygame.time.Clock()
running = True

while running:
    ret, frame = cap.read()
    if not ret:
        break  # 動画終了

    # BGR から RGB に変換
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Pygame で表示するために変換
    frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

    # 画面に描画
    screen.blit(frame, (0, 0))
    pygame.display.update()

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # フレームレート制御
    clock.tick(30)  # 30 FPS

cap.release()
pygame.quit()
