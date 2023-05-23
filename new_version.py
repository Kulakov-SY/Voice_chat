import asyncio

import generateWav
from claim_4 import Claim
from delivery_1 import *
from employee_call_2 import Employee_call
from sale_3 import Sale

delivery_1 = Delivery()
employee_call_2 = Employee_call()
sale_3 = Sale()
claim_4 = Claim()


async def client_choice(first_choice):

    print(
        "Добрый день! Вас приветствует голосовой помощник. \nЕсли Вас интересует доставка по существующему заказу или "
        "требуется общая консультация по доставке нажмите ОДИН. \nЕсли вам необходимо вызвать замерщика нажмите ДВА. "
        "\nЕсли вы хотите оформить предзаказ на дверь нажмите ТРИ. \nЕсли вы хотите оформить претензию то нажмите "
        "ЧЕТЫРЕ")
    playsound(r'wav_file\\' + 'greetings.wav')

    if int(first_choice) == 1:
        await delivery_1.delivery()
    if int(first_choice) == 2:
        await employee_call_2.call()
    if int(first_choice) == 3:
        await sale_3.sale()
    if int(first_choice) == 4:
        await claim_4.claim()


if __name__ == '__main__':
    # first_choice = int(input("Введите число: "))
    await generateWav.create_all(self=generateWav.GenerateWav)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client_choice(2))
    loop.close()
