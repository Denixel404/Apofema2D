import tkinter as tk
import sys
import os

# Компиляция
# pyinstaller Apofema2D.spec

def resource_path(relative_path): # Получение правильного пути
    try:
        base_path = sys._MEIPASS
    except Exception as e:
        base_path = os.path.abspath(".")
        print(e)
    return os.path.join(base_path, relative_path)

win = tk.Tk()
width, height = 1350, 850 # Размеры окна
win.geometry(f"{width}x{height}+10+5")
# win.attributes("-fullscreen", True)
win.title("Апофема2D")
iconPath = resource_path("img/Logo.ico") # Путь к иконке
win.iconbitmap(iconPath)
version = "v2.3" # Текущая версия приложения
resource_link = "https://github.com/Denixel404/Apofema2D"
debug = False # Режим отладки. Не использовать без необходимости

draw = True # Рисование или масштабирование в режиме проектирования
current_figure = None #  Выбранная фигура
auto_color = True # Состояние автосмены цвета
scale = 40 # Размер клеток на поле
language = "ru" # Язык приложения
theme = "standart" # Выбранная тема
figure_color = "black" # Выбранный цвет фигур
scaling = ["rect", "oval", "line", "dash"] # Разрешенные фигуры для масштабирования
black_save = ["signature", "curve", "brush", "eraser", "filling"] # Запрещённые для сохранения объекты

objects = [] # Список фигур на поле
settings_file = "settings.json"
objects_file = "objects.json"

def trash(): # Удаление и чистка ненужных данных в программе
    global objects
    for obj in objects:
        try:
            if obj[1] == None:
                objects.remove(obj)
                print(f"Объект {obj} удалён")
            elif obj[4] == None:
                objects.remove(obj)
                print(f"Объект {obj} удалён")
        except IndexError:
            pass
                