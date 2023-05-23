import json
import re
import threading

from num2words import num2words
from playsound import playsound

from rec_voice import Recognize
from voice import voice
from w2n import make_num

recognize = Recognize()


class Delivery:
    def __init__(self):
        self.text_order = None
        self.client_understand = 0

    async def delivery(self):
        while True:
            print('Вас интересует доставка по существующему заказу или требуется общая консультация по доставке?')
            playsound(r'wav_file\\' + 'delivery_1.wav')
            await recognize.rec_voice()

            if len(recognize.full_data) > 1:
                await self.choice_consult_order()
                break

    async def choice_consult_order(self):
        if recognize.full_data.find('зака') != -1 or recognize.full_data.find('кас') != -1:
            await self.order_number()

        elif recognize.full_data.find('консуль') != -1:
            await self.consult()

        else:
            await self.operator()

    async def operator(self):
        if self.client_understand > 1:
            print('Извините, я переключу вас на оператора')
            playsound(r"wav_file\\" + 'operator.wav')
        else:
            print('Я не понимаю. Повторите еще раз')
            playsound(r"wav_file\\" + 'dont_understand.wav')
            self.client_understand = self.client_understand + 1
            await self.delivery()




    async def consult(self):
        print(
            'Доставка осуществляется бесплатно ,в черте города Самары, за исключением отдаленных районов. '
            'День доставки можно выбрать при оформлении заказа, в указанный день с Вами свяжется '
            'монтажник для уточнения времени доставки и установки')
        playsound(r"wav_file\\" + 'consult.wav')

    def d1_order_number_said(self):
        playsound(r"wav_file\\" + 'order_number.wav')

    def d1_order_number_voice(self):
        print('тут называем голосовой номер заказа')
        playsound(voice(f"{self.text_order}"))


    async def order_number(self):
        while True:
            print('Назовите номер заказа')
            playsound(r"wav_file\\" + 'client_order_number.wav')  # назовите номер заказа
            await recognize.rec_voice()
            if len(recognize.data) > 1:
                self.text_order = make_num(recognize.data)
                print(self.text_order, 'это номер заказа в цифрах')

            thread1 = threading.Thread(target=self.d1_order_number_said, daemon=True)
            thread2 = threading.Thread(target=self.d1_order_number_voice, daemon=True)

            thread1.start()
            thread2.start()

            thread1.join()
            thread2.join()

            playsound(r"wav_file\\" + 'all_right.wav')


    async def find_number(self):
        while True:
            await recognize.rec_voice()
            print(recognize.data, 'в find_number')
            if len(recognize.data) > 1:
                if recognize.data.find('да') != -1 or recognize.data.find('верн') != -1:
                    # проверку на пустые сообщения

                    if self.text_order.isdigit():
                        with open('1.json', 'r', encoding='utf-8') as f:  # открыли файл с данными
                            text = json.load(f)  # загнали все, что получилось в переменную
                            orderNumber = str(text['ShopOrderId'])
                            if orderNumber == self.text_order:
                                value = text['Address']
                                print(value, ' - данные с json по ключу "адрес"')
                                findNumber = re.findall('(\d+)', value)  # отсеять числа
                                for i in findNumber:  # идем по цифрам в цикле
                                    test = num2words(i, lang='ru')  # перевод в текстовое число
                                    value = value.replace(i, test)  # замена цифр на текст
                                    print(value, ' |||- конвертирую цифры с адреса в буквы для озвучки')
                                voice(value)
                                break
                            else:
                                print('Заказа не существует')
                                playsound(r"wav_file\\" + 'order_not_found.wav')
            else:
                await self.order_number()
