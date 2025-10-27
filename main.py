import tkinter as tk
import config as c
import GUI
import utils
import json
import text as txt

#    Copyright (c) 2025 ITDenik

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the Licens


# GUI.background.place(x=0, y=0)

# Загрузка данных при запуске
try:
    with open("settings.json", "r") as f: #
        download = json.load(f)
        c.figure_color = download[0]
        c.language = download[1]
        c.auto_color = download[2]
        c.scale = download[3]
    print("data loaded")
    
except Exception as e:
    print(f"LOAD ERROR: {e}")
    
def save(): # Выгрузка и сохранение данных при закрытии программы
    try:
        with open("settings.json", "w") as f: #
            important = [c.figure_color, c.language, c.auto_color, c.scale]
            json.dump(important, f)
        with open("objects.json", "w") as f: #
            for el1 in c.objects: #
                for el2 in el1:
                    if el2 == "signature":
                        el1.pop(5)
            json.dump(c.objects, f)
        print("data saved")    
    except Exception as e:
        print(f"SAVE ERROR: {e}")
    c.win.destroy()
   
# Обновление языка приложения
if c.language == "ru": 
    pass # По умолчанию
elif c.language == "en": # Английский перевод
    txt.lang("en")
    print(txt.settings)
    GUI.sett_btn.configure(text=txt.settings)
    GUI.rect_btn.configure(text=txt.rect)
    GUI.oval_btn.configure(text=txt.oval)
    GUI.line_btn.configure(text=txt.line)
    GUI.signature_btn.configure(text=txt.signature)
    GUI.dot_btn.configure(text=txt.dot)
    GUI.dash_btn.configure(text=txt.dash)
    GUI.clear_btn.configure(text=txt.clear)
    GUI.del_last_btn.configure(text=txt.last)
    GUI.line_btn.configure(text=txt.line)
    GUI.panel_title.configure(text=txt.welcome)
    GUI.settings_lang.configure(text=txt.settings_lang)
    GUI.ru_btn.configure(text=txt.settings_rutext)
    GUI.en_btn.configure(text=txt.settings_entext)
    GUI.settings_scale_text.configure(text=txt.settings_scale)

# Размещение объектов на экране
GUI.barline.place(x=765, y=0, relheight=1, relwidth=1)
GUI.sidebar.place(x=10, y=0, relheight=1, relwidth=1)
GUI.border_for_zone.place(x=0, y=100)

GUI.base_logo.place(x=150, y=300)
GUI.panel_title.place(x=70, y=20)
GUI.version_title.place(x=500, y=650)

GUI.sett_btn.place(x=0, y=0)
GUI.rect_btn.place(x=78, y=0)
GUI.oval_btn.place(x=78*2, y=0)
GUI.line_btn.place(x=78*3,y=0)
GUI.dot_btn.place(x=78*4, y=0)
GUI.signature_btn.place(x=78*5, y=0)
GUI.dash_btn.place(x=78*6, y=0)
GUI.canvas.place(x=5, y=5)
GUI.clear_btn.place(x=0, y=55)
GUI.del_last_btn.place(x=78, y=55)

# Разлиновка поля
utils.lines(GUI.canvas, c.scale)

try: # Загрузка объектов на поле
    with open("objects.json", "r") as f: #
        c.objects = json.load(f)
    print("objects loaded")
except Exception as e:
    print(f"OBJECTS ERROR: {e}")

# Повторное создание объектов на поле
for el in c.objects:
    print(f"object: {el}")
    el_index = c.objects.index(el)
    if el[4] == "rect":
        GUI.canvas.create_rectangle(el[0], el[1], el[2], el[3], outline=el[5], width=3)
    elif el[4] == "oval":
        GUI.canvas.create_oval(el[0], el[1], el[2], el[3], outline=el[5], width=3)
    elif el[4] == "dot":
        GUI.canvas.create_oval(el[0] - 7, el[1] - 7, el[2] + 7, el[3] + 7, fill=el[5], width=3)
    elif el[4] == "line":
        GUI.canvas.create_line(el[0], el[1], el[2], el[3], fill=el[5], width=3)
    elif el[4] == "signature":
        label = tk.Label(GUI.canvas, text=el[5], width=4, font=("Arial", 12))
        c.objects[el_index].insert(5, label)
        label.place(x=el[0], y=el[1])
    elif el[4] == "dash":
        GUI.canvas.create_line(el[0], el[1], el[2], el[3], dash=(20, 20), fill=el[5], width=3)
print(c.objects)
    
    

# Логика
GUI.canvas.bind("<Button-1>", utils.create_figure_ON)
GUI.canvas.bind("<B1-Motion>", utils.create_figure_OFF)
GUI.canvas.bind("<ButtonRelease-1>", utils.save_figure)
c.win.bind("<Control-z>", utils.del_last)

c.win.protocol("WM_DELETE_WINDOW", save)
c.win.mainloop()
