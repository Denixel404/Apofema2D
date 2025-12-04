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
version = "v2.1" # Текущая версия приложения
resource_link = "https://github.com/Denixel404/Apofema2D"

draw = True # Рисование или масштабирование в режиме проектирования
current_figure = None #  Выбранная фигура
auto_color = True # Состояние автосмены цвета
scale = 40 # Размер клеток на поле
language = "ru" # Язык приложения
figure_color = "black" # Выбранный цвет фигур
scaling = ["rect", "oval", "line", "dash"] # Разрешенные фигуры для масштабирования
black_save = ["signature", "curve"] # Запрещённые для сохранения объекты

objects = [] # Список фигур на поле

