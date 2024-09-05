import PIL.Image
import google.generativeai as genai
import os
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()
# API_KEYの設定
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def generate_text_from_image(image_path, prompt):
    img = PIL.Image.open(image_path)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt, img])
    return response.text