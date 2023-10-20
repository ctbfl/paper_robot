# playground
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

# 列出所有可用的语音
for voice in voices:
    print(f"ID: {voice.id}, Name: {voice.name}, Lang: {voice.languages}")

# 根据您的选择设置一个特定的语音
male_voice_id = None
for voice in voices:
    if "male" in voice.name.lower():
        male_voice_id = voice.id
        break

if male_voice_id:
    engine.setProperty('voice', male_voice_id)
else:
    print("未找到男性语音。")

# 然后您可以像之前那样继续使用engine来合成语音