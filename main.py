import cv2
import os

def extract_frames(video_path, output_folder, frame_rate=24):
    # Проверяем, существует ли папка для сохранения кадров
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Считываем видео
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Ошибка открытия видео.")
        return

    # Получаем информацию о видео
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Рассчитываем, через сколько кадров брать кадры для сохранения
    frame_step = int(fps / frame_rate)

    # Начинаем обработку видео
    current_frame = 0
    while current_frame < total_frames:
        # Перемещаемся к следующему кадру
        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
        ret, frame = cap.read()
        if not ret:
            break

        # Сохраняем кадр в файл
        frame_path = os.path.join(output_folder, f"frame_{current_frame}.jpg")
        cv2.imwrite(frame_path, frame)

        # Переходим к следующему кадру с шагом frame_step
        current_frame += frame_step

    # Закрываем видео
    cap.release()

# Путь к видео файлу и папка для сохранения кадров
video_path = "путь_к_видео/видео.mp4"
output_folder = "путь_к_папке_для_кадров"

# Вызываем функцию для извлечения кадров из видео
extract_frames(video_path, output_folder)
