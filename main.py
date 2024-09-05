import keyboard
import pyautogui
import os
from GenerateText import generate_text_from_image
from TaskManager import add_task_to_google_tasks

print("'q'キーを押してスクリーンショットを撮影します。")
while True:
    if keyboard.is_pressed('q'):
        pyautogui.screenshot('image.png')
        print("スクリーンショットが保存されました: image.png")
        break

prompt = "この画像を要約し、タスク名と詳細を出力してください。タスク名と詳細は別々の行に出力してください。"
result = generate_text_from_image("image.png", prompt)
print(result)

# resultからタスク名と詳細を分離
lines = result.split('\n')
if len(lines) >= 2:
    task_title = lines[0]
    task_details = '\n'.join(lines[1:])
    
    # Google Tasksにタスクを追加
    task_result = add_task_to_google_tasks(task_title, task_details)
    print(f"タスクがGoogle Tasksに追加されました: {task_result['id']}")
else:
    print("タスク名と詳細を正しく分離できませんでした。")
    
os.remove("image.png")