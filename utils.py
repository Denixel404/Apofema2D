import tkinter as tk
from tkinter import messagebox, colorchooser
import GUI
import config
import design_mode as dm
import text as txt
import json
import re
import copy
import design_mode as dm


frame = 0 # количество кадров для хаотичной линии 
mouseX, mouseY = None, None # Временные координаты щелчка мыши
creature = None # Временное сохранение фигуры
color_flag = None # Индикатор цвета
dots = {"coords":[], "flags":[]} # Временное сохранение точек для кривой
positions = [] # Временное сохранение координат для кисти

def open_settings(): # Открытие меню настроек
    # Отображение элеиентов
    GUI.settings_lang.place(x=20, y=90)
    GUI.settings_lang_descr.place(x=20, y=130)
    GUI.ru_btn.place(x=20, y=190)
    GUI.en_btn.place(x=130, y=190)
    GUI.settings_work_color.place(x=20, y=270)
    GUI.settings_work_color_descr.place(x=20, y=310)
    GUI.work_color_button.place(x=20, y=370)
    GUI.settings_choose_color_btn.place(x=110, y=370)
    GUI.settings_theme_btn.place(x=218, y=370)
    GUI.settings_scale_text.place(x=20, y=450)
    GUI.settings_scale_text_descr.place(x=20, y=490)
    GUI.settings_plus_button.place(x=20, y=550)
    GUI.settings_minus_button.place(x=130, y=550)
    
def lines(canvas, rate, clear_all=True): # Отрисовка поля
    global color_flag
    if clear_all:
        canvas.delete("all") # Очистка канвас
        for w in config.objects: # Удаление всех надписей
            try:
                if re.match(r".!frame.!canvas.!label\d+", str(w[5])) or re.match(r".!frame.!canvas.!label", str(w[5])): # Выявление объектов tk.Label
                    print("Label detect")
                    w[5].place_forget()
            except IndexError:
                continue
        config.objects.clear() # Очистка списка объектов
    else:
        try:
            with open(config.resource_path("data/grid.json"), "r") as f:
                grid_d = json.load(f)
            for line in grid_d:
                canvas.delete(line)
        except:
            print("File grid.json was not open")
    # Количество линий для разного масштаба
    iterationx = [75, 38, 20, 10, 5] # по оси Х
    iterationy = [58, 29, 15, 8, 4] # по оси У
    color_flag = canvas.create_rectangle(0, 0, 20, 20, fill=config.figure_color)
    grid = []
    
    if rate == 10: # Установка пары значений
        countx = iterationx[0]
        county = iterationy[0]
    elif rate == 20:
        countx = iterationx[1]
        county = iterationy[1]
    elif rate == 40:
        countx = iterationx[2]
        county = iterationy[2]
    elif rate == 80:
        countx = iterationx[3]
        county = iterationy[3]
    elif rate == 160:
        countx = iterationx[4]
        county = iterationy[4]
    else:
        print("FATAL ERROR: invalid count of lines")
    
    rate = rate # Промежуток
    x1 = 1
    x2 = 1
    y1 = 0
    y2 = 577
    
    for line_y in range(countx): # Разлиновка поля по оси У
        line = canvas.create_line(x1, y1, x2, y2)
        grid.append(line)
        x1 += rate
        x2 += rate
    
    y1 = 1
    y2 = 1
    x1 = 0
    x2 = 747
    
    for line_x in range(county): # Разлиновка по оси Х
        line = canvas.create_line(x1, y1, x2, y2)
        grid.append(line)
        y1 += rate
        y2 += rate
    
    with open(config.resource_path("data/grid.json"), "w") as f:
        json.dump(grid, f)

def draw_curve(event): # Отрисовка кривой после нажатия Enter
    global dots
    id = GUI.canvas.create_line(dots["coords"], fill=config.figure_color, width=3)
    for i in dots["flags"]:
        GUI.canvas.delete(i)
    config.objects.append([copy.deepcopy(dots["coords"]), "curve", id, config.figure_color])
    dots["coords"] = []
    dots["flags"] = []
    print("curve was drawn")
    print(config.objects)
    config.win.unbind("<Return>")

def create_figure_ON(event): # Зажатие клавиши при создании фигуры
    global mouseX, mouseY, current_figureG, creature, dots, positions
    mouseX, mouseY = event.x, event.y
    if config.current_figure == "rect": # Рисование квадрата
        creature = GUI.canvas.create_rectangle(mouseX, mouseY, mouseX, mouseY, outline=config.figure_color, width=3)
    elif config.current_figure == "oval": # Рисование круга или овала
        creature = GUI.canvas.create_oval(mouseX, mouseY, mouseX, mouseY, outline=config.figure_color, width=3)
    elif config.current_figure == "line": # Рисование прямой линии
        creature = GUI.canvas.create_line(mouseX, mouseY, mouseX, mouseY, fill=config.figure_color, width=3)
    elif config.current_figure == "dot": # Рисование точки
        creature = GUI.canvas.create_oval(mouseX - 7, mouseY - 7, mouseX + 7, mouseY + 7, fill=config.figure_color, width=3)
    elif config.current_figure == "signature": # Рисование подписи
        print(config.current_figure)
        GUI.field_input.place(x=event.x, y=event.y)
        GUI.field_button.place(x=event.x+90, y=event.y)
    elif config.current_figure == "dash": # Рисование пунктира
        creature = GUI.canvas.create_line(mouseX, mouseY, mouseX, mouseY, dash=(20, 20), fill=config.figure_color, width=3)
    elif config.current_figure == "curve": # Рисование прямой
        config.win.bind("<Return>", draw_curve)
        dots["coords"].append([mouseX, mouseY])
        dots["flags"].append(GUI.canvas.create_oval(mouseX - 3, mouseY - 3, mouseX + 3, mouseY + 3, fill="gray"))
        print(f"dots: {dots}")
    elif config.current_figure == "brush":
        positions.append((mouseX, mouseY))
        positions.append((mouseX, mouseY))
        creature = GUI.canvas.create_line(positions, fill=config.figure_color, width=3)
    elif config.current_figure == "eraser":
        objID = GUI.canvas.find_closest(x=event.x, y=event.y)
        del_accept = True
        
        with open(config.resource_path("data/grid.json"), "r") as f:
            grid = json.load(f) # Чтение файла с индентификаторами сетки
        for id in grid:
            if objID[0] == id:
                del_accept = False
        
        if del_accept:
            GUI.canvas.delete(objID)
            for obj in config.objects:
                if objID[0] in obj:
                    config.objects.remove(obj)
                    
    elif config.current_figure == "filling":
        objID = GUI.canvas.find_closest(x=event.x, y=event.y)
        edit_accept = True
        
        with open(config.resource_path("data/grid.json"), "r") as f:
            grid = json.load(f) # Чтение файла с индентификаторами сетки
        for id in grid:
            if objID[0] == id:
                edit_accept = False
        
        if edit_accept:
            GUI.canvas.itemconfig(objID, fill=config.figure_color)
            for obj in config.objects:
                if objID[0] in obj:
                    figID = config.objects.index(obj)
                    print(figID)
                    if len(obj) == 9 and "line" not in obj and "dash" not in obj and "curve" not in obj and "brush" not in obj and "signature" not in obj:
                        config.objects[figID][7] = True
                        config.objects[figID][8] = config.figure_color        
    else:
        print(f"ERROR: Invalid figure code. {config.current_figure} does not exist")

def create_figure_OFF(event): # Масштабирование фигуры
    global mouseX, mouseY, current_figure, creature, frame
    if config.current_figure in config.scaling and config.draw:
        GUI.canvas.coords(creature, mouseX, mouseY, event.x, event.y) # Изменение размера фигуры
    elif not config.draw:
        dm.resize_vertex(event)
    elif config.current_figure == "brush" and config.draw:
        frame += 1
        if len(positions) <= 150 and frame % 5 == 0: # Ограничение кадров
            positions.append((event.x, event.y))
            creature = GUI.canvas.create_line(positions, fill=config.figure_color, width=3)
      
def save_figure(event):# Дополнительное сохранение фигуры
    global mouseX, mouseY, current_figure, creature, color_flag, positions, frame
    if config.current_figure not in config.black_save and config.draw: # Сохранение если фигура разрешена и если включен режим свободного рисования
        config.objects.append([mouseX, mouseY, event.x, event.y, config.current_figure, config.figure_color, creature, False, None]) # Добавление информации о фигуре в список объектов
    elif config.current_figure == "brush" and config.draw:
        #positions = set(positions)
        config.objects.append([[copy.deepcopy(positions)], config.current_figure, config.figure_color, creature]) # Добавление информации о хаотичной линии в список объектов
        print(len(positions))
        positions.clear()
        frame = 0
    #print(f"OBJECTS: {config.objects}")
    
    if config.auto_color: # Автоматическая смена цвета
        if config.figure_color == "black":
            config.figure_color = "red"
        elif config.figure_color == "red":
            config.figure_color = "green"
        elif config.figure_color == "green":
            config.figure_color = "blue"
        elif config.figure_color == "blue":
            config.figure_color = "black"
        GUI.canvas.itemconfig(color_flag, fill=config.figure_color)
    
def del_last(event=None): # Удаление последнего объекта на поле
    try:
        obj = config.objects[-1]
        if obj[1] == "curve":
            GUI.canvas.delete(obj[2])
            config.objects.remove(obj)
        elif obj[4] != "signature":
            GUI.canvas.delete(obj[6])
            config.objects.remove(obj)
        else:
            obj[5].place_forget()
            print(f"o: {obj[5]}")
            config.objects.remove(obj)
    
    except IndexError:
        print("Warn: No figures on the field or invalid index")

def create_sign(): # Создание поля с подписью
    global mouseX, mouseY
    GUI.field_input.place_forget()
    GUI.field_button.place_forget()
    text = GUI.field_input.get()
    lenght = len(text)
    print(lenght)
    if lenght < 5:
        width = 4
    elif lenght >= 5 and lenght < 15:
        width = 12
    else:
        width = 20
    label = tk.Label(GUI.canvas, text=text, width=width, font=("Arial", 12))
    config.objects.append([mouseX, mouseY, mouseX, mouseY, config.current_figure, label, text, width])
    label.place(x=mouseX, y=mouseY)
    print(config.objects)
    
def change_work_color(): # Вкл\выкл автоматическую смену цвета
    config.auto_color = not config.auto_color
    if config.auto_color:
        config.figure_color = "black"
        GUI.canvas.itemconfig(color_flag, fill=config.figure_color)
        alert = txt.alert_auto_color1 if config.language == "ru" else txt.alert_auto_color12
    else:
        alert = txt.alert_auto_color2 if config.language == "ru" else txt.alert_auto_color22
    messagebox.showinfo(txt.info if config.language == "ru" else txt.info2, alert)
    
def change_color(): # Кнопка смены цветов на основной панели
    if config.figure_color == "black":
        config.figure_color = "red"
    elif config.figure_color == "red":
        config.figure_color = "green"
    elif config.figure_color == "green":
        config.figure_color = "blue"
    else:
        config.figure_color = "black"
    GUI.canvas.itemconfig(color_flag, fill=config.figure_color)
    
def enter_color(): # Обработать пользовательский цвет 
    new_color = colorchooser.askcolor()[1] # Выбор цвета через интерфейс
    if new_color != None:
        config.figure_color = new_color
        GUI.canvas.itemconfig(color_flag, fill=config.figure_color)
    else:
        pass
    
def scale(direction): # Изменение масштаба клеток
    old_value = config.scale
    if direction == "+":
        if config.scale < 160:
            config.scale *= 2
        else:
            print("WARN: invalid value 'config.scale'")
    elif direction == "-":
        if config.scale > 10:
            config.scale /= 2
        else:
            print("WARN: invalid value 'config.scale'")
     
    if old_value != config.scale: # Проверка на совпадение масштаба
        lines(GUI.canvas, config.scale, False)
        
def open_design_mode():
    print("open design mode")
    
def start_ai():
    dm.analyze_figure()
    