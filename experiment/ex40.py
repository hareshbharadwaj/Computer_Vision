import cv2
import easyocr
from pathlib import Path

def extract_text_from_video(video_path):
    reader = easyocr.Reader(['en'])
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print(f"Video FPS: {fps}")  # ✅ Now it's used
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    extracted_text = []

    for frame_no in range(0, frame_count, 10):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        ret, frame = cap.read()
        if not ret:
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = reader.readtext(frame_rgb)
        frame_texts = [text for (bbox, text, prob) in results if prob > 0.5]
        if frame_texts:
            extracted_text.extend(frame_texts)

    cap.release()
    unique_text = list(dict.fromkeys(extracted_text))
    return unique_text

def main():
    video_path = "text_video.mp4"
    if not Path(video_path).exists():
        print(f"Error: Video file not found at {video_path}")
        return
    print("Extracting text from video...")
    text_results = extract_text_from_video(video_path)
    print("\nExtracted Text:")
    for idx, text in enumerate(text_results, 1):
        print(f"{idx}. {text}")

if __name__ == "__main__":
    main()
