import cv2


def reverse_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    for frame in reversed(frames):
        out.write(frame)

    cap.release()
    out.release()


if __name__ == "__main__":
    input_video = r"C:\Users\hesh2\OneDrive\Documents\viji-cv\sample_video.mp4"
    output_video = "reversed.mp4"
    reverse_video(input_video, output_video)
    print("Video reversal completed!")