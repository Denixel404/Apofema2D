import tkinter as tk
import config as c
import GUI
import utils
import json
import text as txt
import webbrowser
import threading

#    Copyright (c) 2025 Denixel404

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the Licens

def Debug(): # Режим отладки для одновременной работы с приложением в консоли
    while True:
        print("Режим отладки активен")
        command = input("Введите команду: ")
        try:
            if command == "exit": # Выйти из режима отладки
                print("Вы вышли из режима отладки")
                return
            
            print(eval(command)) # Выполнить код или показать переменную
        except Exception as e:
            print("Ошибка при вводе команды")
            print(e)

def open_git(event): # Открытие ссылки на Гитхаб
    webbrowser.open_new(c.resource_link)

# Загрузка данных при запуске
try:
    with open("data/paths.json", "r") as f:
        paths = json.load(f)
        c.settings_file = paths[0]
        c.objects_file = paths[1]
        print(c.settings_file)
    with open(c.settings_file, "r") as f: # Чтение файла с настройками программы
        # Установка сохранённых значений 
        download = json.load(f)
        c.figure_color = download[0]
        c.language = download[1]
        c.auto_color = download[2]
        c.scale = download[3]
        c.theme = download[4]
    print("data loaded")
    
except Exception as e:
    print(f"LOAD ERROR: {e}")
    
def save(): # Выгрузка и сохранение данных при закрытии программы
    try:
        with open("settings.json", "w") as f: # Запись текущих настроек в файл для сохранения
            important = [c.figure_color, c.language, c.auto_color, c.scale, c.theme]
            json.dump(important, f)
        with open("objects.json", "w") as f: # Запись информации об объектах
            for el1 in c.objects: # Работа по правильному сохранению надписей
                for el2 in el1:
                    if el2 == "signature":
                        el1.pop(5)
            json.dump(c.objects, f)
        print("data saved")    
    except Exception as e:
        print(f"SAVE ERROR: {e}")
    c.win.destroy() # Закрытие окна
    c.win.quit()
   
# Обновление языка приложения
if c.language == "ru": 
    pass # По умолчанию
elif c.language == "en": # Английский перевод виджетов
    GUI.sett_btn.configure(text=txt.settings2)
    GUI.rect_btn.configure(text=txt.rect2)
    GUI.oval_btn.configure(text=txt.oval2)
    GUI.line_btn.configure(text=txt.line2)
    GUI.signature_btn.configure(text=txt.signature2)
    GUI.dot_btn.configure(text=txt.dot2)
    GUI.dash_btn.configure(text=txt.dash2)
    GUI.curve_btn.configure(text=txt.curve2)
    GUI.brush_btn.configure(text=txt.brush2)
    GUI.filling_btn.configure(text=txt.filling2)
    GUI.eraser_btn.configure(text=txt.eraser2)
    GUI.clear_btn.configure(text=txt.clear2)
    GUI.color_btn.configure(text=txt.change_color2)
    GUI.export_obj_btn.configure(text=txt.export_objects2)
    GUI.export_sett_btn.configure(text=txt.export_settings2)
    GUI.del_last_btn.configure(text=txt.last2)
    GUI.line_btn.configure(text=txt.line2)
    GUI.panel_title.configure(text=txt.welcome2)
    GUI.settings_lang.configure(text=txt.settings_lang2)
    GUI.settings_lang_descr.configure(text=txt.settings_lang_descr2)
    GUI.ru_btn.configure(text=txt.settings_rutext2)
    GUI.en_btn.configure(text=txt.settings_entext2)
    GUI.settings_work_color.configure(text=txt.work_color2)
    GUI.settings_work_color_descr.configure(text=txt.settings_work_color_descr2)
    GUI.work_color_button.configure(text=txt.work_color2)
    GUI.settings_theme_btn.configure(text=txt.theme2)
    GUI.settings_choose_color_btn.configure(text=txt.palette2)
    GUI.settings_scale_text.configure(text=txt.settings_scale2)
    GUI.settings_scale_text_descr.configure(text=txt.settings_scale_descr2)
    GUI.theme_std_btn.configure(text=txt.standart_theme2)
    GUI.theme_christmas_btn.configure(text=txt.HNY_theme2)
    GUI.theme_dark_btn.configure(text=txt.dark_theme2)
    GUI.theme_light_btn.configure(text=txt.light_theme2)
    GUI.theme_cream_btn.configure(text=txt.cream_theme2)
    GUI.design_btn.configure(text=txt.design2)
    GUI.design_descr.configure(text=txt.design_descr2)
    GUI.design_start_btn.configure(text=txt.design_start_btn2)
    GUI.design_del_flags.configure(text=txt.design_delf_btn2)

# Установка темы приложения
if c.theme == "christmas":
    GUI.edit_theme("#0C2B3E","#1A3B4F", "#2E7D32", "#2E6A95", "#4A90C2", "#B33A3A", "#D95D5D", "#FFFFFF", "christmas")
    GUI.sett_btn.configure(bg=GUI.button_2stroke_color)
elif c.theme == "dark":
    GUI.edit_theme("#121212", "#1E1E1E", "#0A0A0A", "#2D2D2D", "#3D3D3D", "#252525", "#353535", "#FFFFFF", "dark")
    GUI.sett_btn.configure(bg=GUI.button_2stroke_color)
elif c.theme == "light":
    GUI.edit_theme("#F5F5F5", "#E0E0E0", "#BDBDBD", "#EEEEEE", "#E0E0E0", "#E8E8E8", "#D5D5D5", "#000000", "light")
    GUI.sett_btn.configure(bg=GUI.button_2stroke_color)
elif c.theme == "cream":
    GUI.edit_theme("#FAF8F5", "#F2EDE6", "#E5DED3", "#E6D5B9", "#D4B483", "#D7C1A9", "#C19A6B", "#000000", "cream")
    GUI.sett_btn.configure(bg=GUI.button_2stroke_color)

# Размещение объектов на экране
GUI.barline.place(x=765, y=0, relheight=1, relwidth=1)
GUI.sidebar.place(x=10, y=0, relheight=1, relwidth=1)
GUI.border_for_zone.place(x=0, y=100)

a = 0
if c.theme == "christmas":
    for el in GUI.snowflakes:
        coords = ((85, 350), (140, 260), (230, 275), (330, 250), (410, 400))
        el.place(x=coords[a][0], y=coords[a][1])
        a += 1
        
GUI.base_logo.place(x=150, y=300)
GUI.panel_title.place(x=30, y=20)
GUI.version_title.place(x=500, y=650)
GUI.github_link.place(x=10, y=620)

GUI.filling_btn.place(x=0, y=0)
GUI.sett_btn.place(x=483, y=55)
GUI.rect_btn.place(x=78, y=0)
GUI.oval_btn.place(x=78*2, y=0)
GUI.line_btn.place(x=78*3,y=0)
GUI.dot_btn.place(x=78*4, y=0)
GUI.signature_btn.place(x=78*5, y=0)
GUI.dash_btn.place(x=78*6, y=0)
GUI.curve_btn.place(x=78*7, y=0)
GUI.brush_btn.place(x=78*8, y=0)
GUI.eraser_btn.place(x=78*9, y=0)
GUI.canvas.place(x=5, y=5)
GUI.clear_btn.place(x=0, y=55)
GUI.del_last_btn.place(x=78, y=55)
GUI.color_btn.place(x=213, y=55)
GUI.design_btn.place(x=348, y=55)
GUI.export_obj_btn.place(x=563, y=55)


# Разлиновка поля
utils.lines(GUI.canvas, c.scale)

try: # Загрузка объектов на поле
    with open(c.objects_file, "r") as f: #
        c.objects = json.load(f)
    print("objects loaded")
except Exception as e:
    print(f"OBJECTS ERROR: {e}")

# Повторное создание объектов на поле
for el in c.objects:
    print(f"object: {el}")
    el_index = c.objects.index(el)
    if el[1] == "curve":
        id = GUI.canvas.create_line(el[0], fill=el[3], width=3)
        el[2] = id # Замена идентификатора фигуры на новый
    elif el[1] == "brush":
        id = GUI.canvas.create_line(el[0], fill=el[2], width=3)
        el[3] = id # Замена идентификатора фигуры на новый
        pass
    elif el[4] == "rect":
        id = GUI.canvas.create_rectangle(el[0], el[1], el[2], el[3], outline=el[5], width=3)
        el[6] = id # Замена идентификатора фигуры на новый
        if el[7]: # Проверка: закрашена ли фигура
            GUI.canvas.itemconfig(id, fill=el[8])
    elif el[4] == "oval":
        id = GUI.canvas.create_oval(el[0], el[1], el[2], el[3], outline=el[5], width=3)
        el[6] = id # Замена идентификатора фигуры на новый
        if el[7]: # Проверка: закрашена ли фигура
            GUI.canvas.itemconfig(id, fill=el[8])
    elif el[4] == "dot":
        id = GUI.canvas.create_oval(el[0] - 7, el[1] - 7, el[2] + 7, el[3] + 7, fill=el[5], width=3)
        el[6] = id # Замена идентификатора фигуры на новый
        if el[7]: # Проверка: закрашена ли фигура
            GUI.canvas.itemconfig(id, fill=el[8])
    elif el[4] == "line":
        id = GUI.canvas.create_line(el[0], el[1], el[2], el[3], fill=el[5], width=3)
        el[6] = id # Замена идентификатора фигуры на новый
    elif el[4] == "signature":
        label = tk.Label(GUI.canvas, text=el[5], width=el[6], font=("Arial", 12))
        c.objects[el_index].insert(5, label)
        label.place(x=el[0], y=el[1])
    elif el[4] == "dash":
        id = GUI.canvas.create_line(el[0], el[1], el[2], el[3], dash=(20, 20), fill=el[5], width=3)
        el[6] = id # Замена идентификатора фигуры на новый
print(f"new objects list: {c.objects}") 

# Логика
GUI.canvas.bind("<Button-1>", utils.create_figure_ON)
GUI.canvas.bind("<B1-Motion>", utils.create_figure_OFF)
GUI.canvas.bind("<ButtonRelease-1>", utils.save_figure)
GUI.github_link.bind("<Button-1>", open_git)

if c.debug:
    console_thread = threading.Thread(target=Debug, daemon=True)
    console_thread.start()

c.win.protocol("WM_DELETE_WINDOW", save)
c.win.mainloop()
