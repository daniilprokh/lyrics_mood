# Приложение "LyricsMood"

## Средства разработки

Программа написана на языке программирования Python с использованием библиотек Qt, Mutagen, LyricsGenius, Watson Developer Cloud Python SDK, ParallelDots-Python-API:
* c помощью Qt реализовано: графический интерфейс, взаимодействие с файлами системы;
* c помощью Mutagen реализовано взаимодействие с тегами аудиофайла;
* с помощью LyricsGenius реализовано взаимодействие с данными, хранящимися на сайте Genius;
* с помощью Watson Developer Cloud Python SDK реализовано взаимодействие с системой IBM Watson;
* с помощью ParallelDots-Python-API реализовано взаимодействие с системой ParallelDots.

## Демонстрация использования программы для анализа настроения песни Twenty One Pilots - Choker
Сначала выберем нужный нам аудиофайл. Для этого выбираем опцию “Аудиофайл..”:![lm_git_1](https://user-images.githubusercontent.com/83980779/174878344-69f153c9-2b6e-4492-901c-53de3a3d7c42.png 'Опция "Аудиофайл.."')

В открывшемся окошке находим нужный нам аудиофайл и открываем его:![lm_git_2](https://user-images.githubusercontent.com/83980779/174878350-f946a961-f80f-4326-9178-a2eb4689e019.png 'Выбор аудиофайла "02. Choker.flac"')

Можно заметить, что в полях появились все исходные данные, кроме текста песни:![lm_git_3](https://user-images.githubusercontent.com/83980779/174878358-1d4dfa7f-2093-4187-81ce-7bee37a139b2.png 'Результат чтения тегов аудиофайла')

Так как текста песни в теге аудиофайла не оказалось, загрузим его из хранилища данных сайта Genius. Нажав на соответствующую кнопку, получаем текст:![lm_git_4](https://user-images.githubusercontent.com/83980779/174878367-cf36129d-8dab-4c08-ba94-369a4bb1a2b7.png 'Результат загрузки текста песни Twenty One Pilots - Choker с сайта Genius')

Перед анализом настроения текста с помощью ИИ-сервисов, выберем API, которые хотим использовать в анализе. Для этого выбираем опцию “Выбор API для анализа текста..”:![lm_git_5](https://user-images.githubusercontent.com/83980779/174878375-4c0e3b13-4d69-47d0-bf72-bc1812b97bd2.png 'Опция "Выбор API для анализа.."')

Для примера выберем первое API:![lm_git_6](https://user-images.githubusercontent.com/83980779/174878384-19bb9d91-2b0a-46e6-be68-c5a2d661c4d1.png 'Выбор "IBM Watson Tone Analyzer API"')

Всё что осталось сделать - это нажать на кнопку “Проанализировать настроение песни” и получить результат:![lm_git_7](https://user-images.githubusercontent.com/83980779/174878392-cdd7ea54-c46c-4160-a7d9-38ca1a780537.png 'Результат анализа текста песни выбранном API')
