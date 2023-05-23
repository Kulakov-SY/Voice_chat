import os
import shutil
from scipy.io.wavfile import write  # надо устанавливать
import namegenerator  # надо устанавливать
import sounddevice as sd
from playsound import playsound  # надо устанавливать # pip install playsound==1.2.2
from tts import TTS

mnt = 'C:\\Users\\kulakov.sy\\PycharmProjects\\chat_bot_IM\\'
if not os.path.exists("wav_file"): os.makedirs("wav_file")

tts = TTS()


def voice(example_text):
    file_name = namegenerator.gen()
    file_to_create = "wav_file\\" + str(file_name) + '.wav'
    fs = 1000  # Частота дискретизации
    seconds = 0  # Продолжительность записи
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Дождитесь окончания записи
    write(file_to_create, fs, myrecording)  # Сохранить как WAV файл

    audio = tts.text_to_wav(example_text, "test-2.wav")

    shutil.copyfile(audio, file_to_create)
    # playsound(rf'{mnt + file_to_create}')
    return file_to_create
