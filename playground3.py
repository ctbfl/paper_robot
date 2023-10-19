import sounddevice as sd
import numpy as np
import keyboard
from scipy.io.wavfile import write

RATE = 16000  # 采样率
CHANNELS = 1  # 双声道

def record_audio():
    audio_data = []
    with sd.InputStream(samplerate=RATE, channels=CHANNELS) as stream:
        print("正在录音...")                                                                                                                                      
        while keyboard.is_pressed('space'):
            audio_chunk, overflowed = stream.read(RATE)
            audio_data.extend(audio_chunk)
        print("录音已停止.")
    
    audio_array = np.array(audio_data)
    write('test.wav', RATE, audio_array)

def process_audio():
    # 在这里添加后续函数来处理 test.wav 并执行相关操作
    print("处理 test.wav ...")

print("长按空格以开始录音，释放空格以停止录音。按 'esc' 退出程序。")

while True:
    if keyboard.is_pressed('esc'):
        break
    elif keyboard.is_pressed('space'):
        record_audio()
        process_audio()
