
<!DOCTYPE html>
<html>
<body>
  <h2>Содержание</h2>
  <ul>
    <li><a href="#Установка">Установка</a></li>
    <li><a href="#Использование">Использование</a></li>
    <li><a href="#Функциональность">Функциональность</a></li>
  </ul>
  <h2 id="Установка">Установка</h2>
  <p>Для использования этой программы выполните следующие инструкции:</p>
  <ol>
    <li>Клонируйте репозиторий на свою локальную машину.</li>
    <li>Установите необходимые зависимости, запустив следующую команду:</li>
  </ol>
  <pre><code>pip install -r requirements.txt</code></pre>
  <p>Убедитесь, что у вас есть необходимые аудиофайлы в директории <code>wav_file</code>. Эти файлы используются для голосовых подсказок и ответов.</p>
  <h2 id="Использование">Использование</h2>
  <p>Для запуска программы выполните файл <code>new_version.py</code>. Убедитесь, что у вас подключен микрофон для голосового ввода.</p>
  <pre><code>python new_version.py</code></pre>
  <h2 id="Функциональность">Функциональность</h2>
  <p>Программа предоставляет следующую функциональность:</p>
  <ol>
    <li><strong>Выбор клиента</strong>: После запуска программы голосовой ассистент приветствует пользователя и предлагает меню опций. Пользователь может сделать выбор, произнеся соответствующий номер.
      <ul>
        <li>Если пользователь выбирает 1, ассистент помогает существующим заказам доставки или общим вопросам по доставке.</li>
        <li>Если пользователь выбирает 2, ассистент осуществляет звонок сотруднику или специалисту.</li>
        <li>Если пользователь выбирает 3, ассистент помогает с оформлением предварительного заказа.</li>
        <li>Если пользователь выбирает 4, ассистент обрабатывает претензии или проблемы, связанные с установкой, качеством товара или доставкой.</li>
      </ul>
    </li>
    <li><strong>Распознавание голоса</strong>: Программа включает возможности распознавания голоса для понимания команд пользователя и соответствующего ответа. Она использует библиотеку Vosk для распознавания речи.</li>
    <li><strong>Доставка</strong>: Если пользователь выбирает помощь с доставкой, ассистент взаимодействует с модулем <code>delivery_1</code> для предоставления актуальной информации и обработки запросов на доставку.</li>
    <li><strong>Звонок сотруднику</strong>: Для запроса звонка сотруднику ассистент взаимодействует с модулем <code>employee_call_2</code>. Он собирает информацию об адресе пользователя и назначает встречу для измерений.</li>
    <li><strong>Продажа</strong>: Если пользователь хочет сделать предварительный заказ, ассистент взаимодействует с модулем <code>sale_3</code>. Он запрашивает у пользователя тип заказа, технические характеристики и варианты доставки.</li>
    <li><strong>Претензия</strong>: Для обработки претензий или проблем ассистент взаимодействует с модулем <code>claim_4</code>. Он позволяет пользователю описать проблему и предоставляет соответствующие подсказки для получения дополнительной информации.</li>
  </ol>
</body>
</html>
