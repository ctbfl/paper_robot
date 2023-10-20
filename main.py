import sounddevice as sd
import numpy as np
import keyboard
from voice_recognition import speeh_recognition
from ai.chat import ChatBot
from read_txt_out import play_text
from pure_chatgpt import completion
RATE = 16000  # 采样率
CHANNELS = 1  # 单声道
DTYPE = np.int16  # 16bit位深度

def record_audio():
    audio_data = []
    with sd.InputStream(samplerate=RATE, channels=CHANNELS, dtype=DTYPE) as stream:
        print("正在录音...")
        while keyboard.is_pressed('space'):
            audio_chunk, overflowed = stream.read(RATE)
            audio_data.extend(audio_chunk)
        print("录音已停止.")
    
    audio_array = np.array(audio_data).astype(DTYPE)
    with open('test.pcm', 'wb') as pcm_file:
        pcm_file.write(audio_array.tobytes())

def process_audio(chatbot):
    print("处理 test.pcm ...")
    text = speeh_recognition()
    return text
                                 

my_chatbot = ChatBot()  
                                                                         
print("长按空格以开始录音，释放空格以停止录音。按 'esc' 退出程序。")
history = [{'role':'system','content':"你是一个paper robot, 性格开朗活泼, 你接下来会收到用户的交流，请你活泼开朗的回复他"}]

while True:
    if keyboard.is_pressed('esc'):
        break
    elif keyboard.is_pressed('space'):
        record_audio()
        text = process_audio(my_chatbot)
        print("你：",text)
        user_content = {'role':'user','content':text}
        history.append(user_content)
        print(history)
        chatgpt_response = completion(history)
        history.append({'role':'assistant','content':chatgpt_response})
        print("paper_robot:",chatgpt_response)
        action_result = my_chatbot.chat(chatgpt_response)
        print(action_result)
        play_text(chatgpt_response)  
        print("处理完成.请继续按空格录音.")   