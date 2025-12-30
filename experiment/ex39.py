import cv2
import numpy as np


def play_reverse_slowmo(video_path, speed_factor=0.5):
    """
    Play a video in reverse and slow motion
    Args:
        video_path (str): Path to the video file
        speed_factor (float): Speed factor (0.5 = half speed, 0.25 = quarter speed)
    """
    cap = cv2.VideoCapture(video_path)

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    delay = int((1.0 / fps) * 1000 / speed_factor)

    for frame in reversed(frames):
        cv2.imshow('Reverse Slow Motion', frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_file = "sample_video.mp4"
    play_reverse_slowmo(video_file, speed_factor=0.5)