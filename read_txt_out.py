import pyttsx3
import sounddevice as sd
import numpy as np
import wave

def play_text(text):
    engine = pyttsx3.init()

    # 设置属性，如语速和音量 (可选)
    engine.setProperty('rate', 150)  # 语速
    engine.setProperty('volume', 0.9)  # 音量

    # 在当前目录下保存音频数据
    temp_audio_filename = "my_temp.wav"
    engine.save_to_file(text, temp_audio_filename)
    engine.runAndWait()

    with wave.open(temp_audio_filename, 'rb') as wave_file:
        framerate = wave_file.getframerate()
        frames = wave_file.readframes(wave_file.getnframes())
        audio_data = np.frombuffer(frames, dtype=np.int16)

    sd.play(audio_data, framerate)
    sd.wait()  # 等待音频播放完成

if __name__ == '__main__':
    # 测试
    play_text("你好，这是一个测试。")

