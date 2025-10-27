import tkinter as tk
import sys
import os

# pyinstaller --name="Apofema2D beta 0.1.1" --onefile --noconsole --icon=img/Logo.ico main.py
# pyinstaller Apofema2D_beta_0.1.1.spec

def resource_path(relative_path): # Получение правильного пути
    try:
        base_path = sys._MEIPASS
    except Exception as e:
        base_path = os.path.abspath(".")
        print(e)
    return os.path.join(base_path, relative_path)

win = tk.Tk()
width, height = 1200, 650 # Размеры окна
win.geometry(f"{width}x{height}+100+30")
win.title("Апофема2D")
iconPath = resource_path("img/Logo.ico") # Путь к иконке
win.iconbitmap(iconPath)
version = "v1.0" # Текущая версия приложения

#lock_color = False
current_figure = "rect" #  Выбранная фигура
auto_color = True # Состояние автосмены цвета
scale = 40 # Размер клеток на поле
language = "ru" # Язык приложения
figure_color = "black" # Выбранный цвет фигур
scaling = ["rect", "oval", "line", "dash"] # Разрешенные фигуры для масштабирования

objects = [] # Список фигур на поле

