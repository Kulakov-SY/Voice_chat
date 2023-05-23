import asyncio
import shutil
import time

from scipy.io.wavfile import write  # надо устанавливать
import sounddevice as sd
import tts

tts = tts.TTS()


class GenerateWav:
    async def create_wav(file_name, example_text):
        global file_to_create
        audio = tts.text_to_wav(example_text, "test-5.wav")
        file_to_create = "wav_file\\" + str(file_name) + '.wav'
        fs = 1000  # Частота дискретизации
        seconds = 0  # Продолжительность записи
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()  # Дождитесь окончания записи
        write(file_to_create, fs, myrecording)  # Сохранить как WAV файл
        shutil.copyfile(audio, file_to_create)


async def create_all(self):
    start_time = time.time()

    await self.create_wav(file_name='delivery_1', example_text='Вас интересует доставка по существующему заказу, '
                                                               'или требуется общая консультация по доставке?')
    await self.create_wav(file_name='dont_understand', example_text='Я не понимаю. Повторите еще раз')
    await self.create_wav(file_name='operator', example_text='Извините, я переключу вас на оператора')
    await self.create_wav(file_name='consult', example_text='Доставка осуществляется бесплатно ,в черте+ города '
                                                            'Самары, за исключением отдаленных районов. '
                                                            'День доставки можно выбрать при оформлении заказа, '
                                                            'в указанный день с Вами свяжется '
                                                            'монтажник для уточнения времени доставки и установки')
    await self.create_wav(file_name='client_order_number', example_text='Назовите но+мер зака+за')
    await self.create_wav(file_name='order_not_found', example_text='Зака+за не существует')
    await self.create_wav(file_name='order_number', example_text='Спасибо. Мне нужно уточнение. Ваш номер зака+за.')
    await self.create_wav(file_name='all_right', example_text='Всё ве+рно?')
    await self.create_wav(file_name='greetings', example_text="Добрый день! Вас приветствует голосовой помощник. \nЕсли"
                                                              "Вас интересует доставка по существующему заказу или "
                                                              "требуется общая консультация по доставке нажмите ОДИН. "
                                                              "\nЕсли вам необходимо вызвать замерщика нажмите ДВА."
                                                              "\nЕсли вы хотите оформить предзаказ на дверь нажмите ТРИ. "
                                                              "\nЕсли вы хотите оформить претензию то нажмите"
                                                              "ЧЕТЫРЕ")
    await self.create_wav(file_name='client_house',
                          example_text='Для вызова замерщика продиктуйте свой адрес: назовите город')
    await self.create_wav(file_name='client_street', example_text='Назовите,пожа+луйста,улицу и номер дома')
    await self.create_wav(file_name='client_flat_number', example_text='Назовите,пожа+луйста,номер квартиры')
    await self.create_wav(file_name='client_time', example_text='Уточните,пожа+луйста,удобное время для замера')
    await self.create_wav(file_name='client_date', example_text='Уточните,пожа+луйста,удобную дату для замера')
    await self.create_wav(file_name='thanks',
                          example_text='Спасибо за обращение. Cпециалист приедет в указанное вре+мя.'
                                       'В случае изменений, с вами дополнительно свяжутся.')
    await self.create_wav(file_name='check_address', example_text='Давайте проверим правильность адреса.')

    await self.create_wav(file_name='choice_apartment',
                          example_text='Какая дверь нужна, квартирная или для загородного дома?')
    await self.create_wav(file_name='check_noize', example_text='Важна ли шумоизоляция?')
    await self.create_wav(file_name='check_thickness_door', example_text='Какая необходима толщина полотна? Мы можем '
                                                                  'изготовить полотно толщиной '
                                                                  'сорок пять '
                                                                  'миллиметров,  шестьдесят миллиметров,  семьдесят '
                                                                  'пять миллиметров, '
                                                                  'девяносто '
                                                                  'миллиметров,  сто миллиметров')
    await self.create_wav(file_name='check_thickness_wall', example_text='Теперь уточните толщину дверного проема')
    await self.create_wav(file_name='check_mirror', example_text='Вы хотели бы дверь с зеркалом?')
    await self.create_wav(file_name='check_termo', example_text='Дверь нужна с терморазрывом?')
    await self.create_wav(file_name='check_glasspack', example_text='Вы хотели бы дверь со стеклопакетом?')
    await self.create_wav(file_name='door_need', example_text='Какое количество дверей необходимо?')
    await self.create_wav(file_name='door_side', example_text='Какое открывание нужно? ле+вое или правое?')
    await self.create_wav(file_name='thanks', example_text='Благодарим вас за зая+вку! В случае изменений, с вами '
                                                           'дополнительно свяжутся.')
    await self.create_wav(file_name='delivery', example_text='У Вас будет самовывоз или доставка?')
    await self.create_wav(file_name='problem', example_text='Расскажите, с чем у Вас возникла проблема: с '
                                                             'установкой, с качеством продукции, '
                           'с доставкой или другая проблема?')
    await self.create_wav(file_name='problem_install', example_text='Расскажите, какая проблема была с установкой?')
    await self.create_wav(file_name='problem_quality', example_text='Расскажите, какая проблема была с качеством продукции?')
    await self.create_wav(file_name='problem_delivery', example_text='Расскажите, какая проблема была с доставкой?')
    await self.create_wav(file_name='finish_answer', example_text='Благодарим Вас, в ближайшее время с Вами свяжется профильный специалист для '
                                 'урегулирования проблемы.')


    print("--- %s seconds ---" % (time.time() - start_time))

# if __name__ == '__main__':
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(create_all(self=GenerateWav))
#     loop.close()
#     print("--- %s seconds ---" % (time.time() - start_time))
