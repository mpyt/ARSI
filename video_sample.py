import cv2
import os


def extract_frames(video_path, output_dir="frames", sample_rate=1):

    video_name = os.path.splitext(os.path.basename(video_path))[0]
    save_dir = os.path.join(output_dir, video_name)
    os.makedirs(save_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Nelze otevřít video: {video_path}")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Video: {fps:.1f} FPS, celkem {total_frames} snímků")
    print(f"Sample rate: každý {sample_rate}. snímek → ~{total_frames // sample_rate} fotek")
    print(f"Výstupní složka: {save_dir}")

    frame_idx = 0
    saved = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % sample_rate == 0:
            filename = os.path.join(save_dir, f"frame_{frame_idx:06d}.jpg")
            # imencode + uložení ručně — řeší problém s diakritikou v cestě
            success, encoded = cv2.imencode(".jpg", frame)
            if success:
                encoded.tofile(filename)
                saved += 1

        frame_idx += 1

    cap.release()
    print(f"Hotovo! Uloženo {saved} snímků do složky '{save_dir}'")

if __name__ == "__main__":
    VIDEO_PATH = r"C:\Users\micha\Desktop\VŠB\Projekty\ARSI\videa_16_03_2026\1762-1.mp4"
    OUTPUT_DIR = r"C:\Users\micha\Desktop\VŠB\Projekty\ARSI\photo_samples"
    SAMPLE_RATE = 30

    extract_frames(VIDEO_PATH, OUTPUT_DIR, SAMPLE_RATE)