import threading

from playsound import playsound

import delivery_1
from rec_voice import Recognize
from voice import voice
from w2n import make_num

recognize = Recognize()
delivery = delivery_1.Delivery()


class Employee_call:
    def __init__(self):
        self.text_order = None
        self.client_understand = 0
        self.client_date_data = None
        self.date = None
        self.flat = None
        self.street = None
        self.client_city = None

    async def call(self):
        print('Для вызова замерщика продиктуйте свой адрес: назовите город')
        playsound(r'wav_file\\' + 'client_house.wav')
        await recognize.rec_voice()
        self.client_city = recognize.data
        if len(recognize.data) > 1:
            await self.street_flat()
        else:
            await self.call()

    async def street_flat(self):
        print('Назовите,пожалуйста,улицу и номер дома')
        playsound(r'wav_file\\' + 'client_street.wav')
        await recognize.rec_voice()
        self.street = recognize.data
        if len(recognize.data) > 1:
            await self.number_flat()
        else:
            await self.street_flat()

    async def number_flat(self):
        print('Назовите,пожалуйста,номер квартиры')
        playsound(r'wav_file\\' + 'client_flat_number.wav')
        await recognize.rec_voice()
        self.flat = recognize.data

        thread1 = threading.Thread(target=self.e2_order_number_said, daemon=True)
        thread2 = threading.Thread(target=self.e2_order_number_voice, daemon=True)

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        playsound(r"wav_file\\" + 'all_right.wav')
        await self.client_date()

    def e2_order_number_said(self):
        playsound(r"wav_file\\" + 'check_address.wav')

    def e2_order_number_voice(self):
        print(f'Давайте проверим адрес,{recognize.full_data}. Все верно?')
        playsound(voice(example_text=f'{recognize.full_data}'))


    async def client_date(self):
        await recognize.rec_voice()
        if len(recognize.data) > 1:
            if recognize.data.find('да') != -1 or recognize.data.find('верн') != -1:
                print('Уточните,пожалуйста,удобную дату для замера')
                playsound(r'wav_file\\' + 'client_date.wav')
                await recognize.rec_voice()
                self.date = recognize.data
                await self.client_time()
            else:
                await self.call()
        else:
            await self.number_flat()

    async def client_time(self):
        print('Уточните,пожалуйста,удобное время для замера')
        playsound(r'wav_file\\' + 'client_time.wav')
        await recognize.rec_voice()
        self.client_date_data = recognize.data
        if len(recognize.data) > 1:
            print('Спасибо за обращение, специалист приедет в указанное время. В случае '
                  'изменений, с вами дополнительно свяжутся.')
            playsound(r'wav_file\\' + 'thanks.wav')
        else:
            await self.client_time()

    async def operator(self):
        if self.client_understand > 1:
            print('Извините, я переключу вас на оператора')
            playsound(r'wav_file\\' + 'operator.wav')
        else:
            print('Я не понимаю. Повторите еще раз')
            playsound(r'wav_file\\' + 'dont_understand.wav')
            self.client_understand = self.client_understand + 1
