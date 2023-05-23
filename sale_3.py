from playsound import playsound
from rec_voice import Recognize
recognize = Recognize()


class Sale:
    def __init__(self):
        self.client_understand_choice = 0
        self.flat_door = 0
        self.house_door = 0

    async def sale(self):
        print('Какая дверь нужна? квартирная или для загородного дома?')
        playsound(r"wav_file\\" + 'choice_apartment.wav')
        try:
            await recognize.rec_voice()
        except:
            await self.sale()

        if len(recognize.data) > 1:
            await self.choice_apartment()
            await recognize.rec_voice()

            if self.flat_door == 1:
                if len(recognize.data) > 1:
                    await self.flat_door_fun()
            elif self.house_door == 1:
                if len(recognize.data) > 1:
                    await self.house_door_fun()
        else:
            await self.sale()

    async def choice_apartment(self):
        if recognize.data.find('квар') != -1:
            self.flat_door = self.flat_door + 1
            await self.side_choice()
        elif recognize.data.find('дом') != -1:
            self.house_door = self.house_door + 1
            await self.side_choice()
        else:
            if self.client_understand_choice > 1:
                playsound(r"wav_file\\" + 'operator.wav')
            elif self.flat_door == 0 and self.house_door == 0:
                self.client_understand_choice = self.client_understand_choice + 1
                playsound(r"wav_file\\" + 'dont_understand.wav')
                await self.sale()

    async def flat_door_fun(self):
        print('Важна ли шумоизоляция?')
        playsound(r"wav_file\\" + 'check_noize.wav')
        await recognize.rec_voice()

        if len(recognize.data) > 1:
            await self.check_thickness_door()
            await recognize.rec_voice()

            if len(recognize.data) > 1:
                await self.check_thickness_wall()
                await recognize.rec_voice()

                if len(recognize.data) > 1:
                    await self.check_mirror()
                    await recognize.rec_voice()

                    if len(recognize.data) > 1:
                        await self.door_need()
                        await recognize.rec_voice()

                        if len(recognize.data) > 1:
                            await self.delivery()

                            if len(recognize.data) > 1:
                                await self.thanks()
                            else:
                                await self.delivery()
                        else:
                            await self.door_need()
                    else:
                        await self.check_mirror()

                else:
                    await self.check_thickness_wall()
            else:
                await self.check_thickness_door()

        else:
            await self.flat_door_fun()

    async def check_mirror(self):
        print('Вы хотели бы дверь с зеркалом?')
        playsound(r"wav_file\\" + 'check_mirror.wav')

    async def check_thickness_wall(self):
        print('Теперь уточните толщину дверного проема')
        playsound(r"wav_file\\" + 'check_thickness_wall.wav')

    async def check_thickness_door(self):
        print(
            'Какая необходима толщина полотна? Мы можем изготовить полотно толщиной сорок пять '
            'миллиметров, '
            'шестьдесят миллиметров, семьдесят пять миллиметров, девяносто миллиметров,  '
            'сто миллиметров')
        playsound(r"wav_file\\" + 'check_thickness_door.wav')

    async def house_door_fun(self):
        print('Дверь нужна с терморазрывом?')
        playsound(r"wav_file\\" + 'check_termo.wav')
        await recognize.rec_voice()
        if len(recognize.data) > 1:
            print(
                'Какая необходима толщина полотна? Мы можем изготовить полотно толщиной пятьдесят '
                'миллиметров, '
                'шестьдесят миллиметров, семьдесят пять миллиметров, девяносто миллиметров,  сто '
                'миллиметров')
            playsound(r"wav_file\\" + 'check_thickness_door.wav')
            await recognize.rec_voice()

            if len(recognize.data) > 1:
                print('Теперь уточните толщину дверного проема')
                playsound(r"wav_file\\" + 'check_thickness_wall.wav')
                await recognize.rec_voice()

                if len(recognize.data) > 1:
                    print('Вы хотели бы дверь со стеклопакетом?')
                    playsound(r"wav_file\\" + 'check_glasspack.wav')
                    await recognize.rec_voice()

                    if len(recognize.data) > 1:
                        print('Какое количество дверей необходимо?')
                        playsound(r"wav_file\\" + 'door_need.wav')
                        await recognize.rec_voice()

                        if len(recognize.data) > 1:
                            await self.door_need()
                            if len(recognize.data) > 1:
                                await self.delivery()
                                if len(recognize.data) > 1:
                                    await self.thanks()

    async def door_need(self):
        playsound(r"wav_file\\" + 'door_need.wav')
        print('Какое количество дверей необходимо?')

    async def delivery(self):
        playsound(r"wav_file\\" + 'delivery.wav')
        print('У Вас будет самовывоз или доставка?')
        await recognize.rec_voice()

    async def side_choice(self):
        print('Какое открывание нужно? Левое или правое?')
        playsound(r"wav_file\\" + 'door_side.wav')
        await recognize.rec_voice()

    async def thanks(self):
        playsound(r"wav_file\\" + 'thanks.wav')
        print('Благодарим вас за заявку!')
