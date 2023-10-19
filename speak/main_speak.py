import time
import speech_recognition as sr

# 录下来你讲的话
def recordAudio():
    # 用麦克风记录下你的话
    print("开始麦克风记录下你的话")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data

if __name__ == '__main__':
    time.sleep(2)
    while True:
        data = recordAudio()
        print(data)