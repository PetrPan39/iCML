import os
import json
import cv2
from emotion_gesture_speech_detector import EmotionGestureSpeechDetector

def process_media(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in [".jpg", ".jpeg", ".png", ".mp4"]:
        return {"error": f"Formát {ext} není podporován"}

    img = cv2.imread(file_path)
    if img is None:
        return {"error": "Chyba při načítání obrázku"}

    detector = EmotionGestureSpeechDetector()
    results = detector.detect_emotions(img)

    return results

if __name__ == "__main__":
    from tkinter import Tk, filedialog

    def open_file():
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title="Vyber soubor")
        if file_path:
            result = process_media(file_path)
            print(json.dumps(result, indent=2, ensure_ascii=False))

    open_file()