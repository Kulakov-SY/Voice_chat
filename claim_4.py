from playsound import playsound

from rec_voice import Recognize

recognize = Recognize()


class Claim:
    def __init__(self):
        self.client_understand = 0

    async def claim(self):
        print('Расскажите, с чем у Вас возникла проблема: с установкой, с качеством продукции, с доставкой или другая '
              'проблема?')
        playsound(r'wav_file\\' + 'problem.wav')
        await recognize.rec_voice()

        if recognize.data.find('устан') != -1:
            playsound(r'wav_file\\' + 'problem_install.wav')
            print('Расскажите, какая проблема была с установкой?')
            await recognize.rec_voice()
            await self.finish()
        elif recognize.data.find('качест') != -1:
            playsound(r'wav_file\\' + 'problem_quality.wav')
            print('Расскажите, какая проблема была с качеством продукции?')
            await recognize.rec_voice()
            await self.finish()
        elif recognize.data.find('достав') != -1:
            playsound(r'wav_file\\' + 'problem_delivery.wav')
            print('Расскажите, какая проблема была с доставкой?')
            await recognize.rec_voice()
            await self.finish()
        else:
            await self.operator()

    async def finish(self):
        playsound(r'wav_file\\' + 'finish_answer.wav')
        print('Благодарим Вас, в ближайшее время с Вами свяжется профильный специалист для '
                                 'урегулирования проблемы.')

    async def operator(self):
        if self.client_understand > 1:
            playsound(r"wav_file\\" + 'operator.wav')
        else:
            self.client_understand = self.client_understand + 1
            playsound(r"wav_file\\" + 'dont_understand.wav')
            await self.claim()