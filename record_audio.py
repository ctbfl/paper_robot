import pyaudio, wave
from tqdm import tqdm

DEVICE_ID = 31

pa = pyaudio.PyAudio()
try:
    stream = pa.open(format=pyaudio.paInt16, 
                     channels=1, 
                     rate=48000, 
                     input=True, 
                     frames_per_buffer=2048, 
                     input_device_index=DEVICE_ID)
except Exception as e:
    print("Error:", str(e))
    pa.terminate()
    exit()

record_buf = [] 

for i in tqdm(range(8 * 5)):
    audio_data = stream.read(2048)
    record_buf.append(audio_data)

wf = wave.open('01.wav', 'wb')
wf.setnchannels(1)  # 设置为单声道
wf.setsampwidth(2)
wf.setframerate(48000)  # 使用48000的采样率
wf.writeframes(b"".join(record_buf))
wf.close()

stream.stop_stream()
stream.close()
pa.terminate()
