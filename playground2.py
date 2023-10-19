import numpy as np
import sounddevice as sd
import soundfile as sf
import queue
import time

# 参数设置
samplerate = 48000  # 采样率
channels = 1  # 声道数
duration = 10  # 每块的录音时长，单位：秒
blocksize = int(samplerate * duration)  # 计算每块的样本数量

q = queue.Queue()  # 用于存储音频数据块

def callback(indata, frames, time, status):
    """将音频数据放入队列"""
    if status:
        print(status)
    q.put(indata.copy())

with sd.InputStream(samplerate=samplerate, channels=channels, blocksize=blocksize, callback=callback):
    while True:
        audio_block = q.get()
        # 这里处理你的音频块，例如保存到WAV文件或发送给语音识别系统
        filename = "block_{}.wav".format(int(time.time()))
        sf.write(filename, audio_block, samplerate)
