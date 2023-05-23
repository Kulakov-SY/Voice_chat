import json
from vosk import KaldiRecognizer
import pyaudio
import sounddevice as sd
from array import array
import vosk
from voice import mnt


vosk.SetLogLevel(-1)

device = sd.default.device  # или -> sd.default.device = 1, 3, python -m sounddevice просмотр
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])  # получаем частоту микрофона

voskModel = vosk.Model(rf'{mnt}' + 'model_small')  # маленькая модель голоса
rec = KaldiRecognizer(voskModel, samplerate)


class Recognize:
    def __init__(self):
        self.silence = 0
        self.client_said = []

    async def rec_voice(self):  # Обучаем матрицу ИИ и постоянно слушаем микрофон
        CHUNK = 11000
        cap = pyaudio.PyAudio()
        stream = cap.open(format=pyaudio.paInt16, channels=1, rate=samplerate, input=True, frames_per_buffer=8192)
        stream.start_stream()

        running = True
        while running:

            data_stream = stream.read(CHUNK)
            data_chunk = array('h', data_stream)
            vol = max(data_chunk)

            if rec.AcceptWaveform(data_stream):
                self.data = json.loads(rec.Result())['text']
                print(self.data, 'data')
                self.client_said.append(self.data)

            if vol >= 2000:
                self.silence = 0
            else:
                self.silence = self.silence + 1
                print(self.silence)
                if self.silence > 10:
                    running = False
                    print('клиент молчит')

        # end of recording
        stream.stop_stream()
        stream.close()

        self.full_data = ' '.join(self.client_said)
        print(self.full_data, 'full_data хранится в voice')

        self.silence = 0
        return self.full_data