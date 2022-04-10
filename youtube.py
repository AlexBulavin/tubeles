__author__ = 'Alex Bulavin'
# Пример взят вот отсюда: https://www.youtube.com/watch?v=ROoo1eoOOvg
# С SSL сертификатом какая-то проблема. На 13:45 10.04.2022 не могу её решить
# Проблема решена следующим образом:
# В левом верхнем углу PyCharm кликаем на слове PyCharm
# В выпадающем меню выбираем Preferences
# В разделе Project ИМЯ ПРОЕКТА выбираем Python Interpreter
# Там указано, какую версию Python использует проект.
# Входим через finder в папку размещения той версии Python, которая используется в проекте
# Например /Applications/Python 3.9
# Находим файл Install Certificates.command
# Кликаем по нему два раза
# Находим файл Update Shell Profile.command
# Кликаем по нему два раза
# Сертификат установлен

from pytube import YouTube

DOWNLOAD_FOLDER = '/Users/alex/Downloads/YouTube'
video_url = 'https://www.youtube.com/watch?v=3FIS2MiAXW8'
video_obj = YouTube(video_url)

stream = video_obj.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)