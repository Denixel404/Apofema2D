import GUI
import tkinter as tk
import config as c
import math
import text as txt

show_letters = True # Показывать обозначения фигур
closed = False # Замкнутость фигуры
vertexes = [] # Координаты вершин фигуры
flags = [] # Помеченные вершины
sides = [] # Длины сторон фигуры
angeles = [] # Углы фигуры
widgets = []
S = 0
P = 0

r = 5 # Радиус окружности (точки вершины)
figure_id = None # ID найденной кривой
index_in_objects = None # Индекс найденной кривой в общем списке объектов

def start(): #
    c.draw = False

def close_points(x1, y1, x2, y2): # Проверить близкие ли точки
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    #print(f"x1 {x1}, x2 {x2}, y1 {y1}, y2 {y2}")
    #print(d)
    if d < 10: # Точки близкие
        return True
    else: # Иначе нет
        return False
    
def S_points(x1, y1, x2, y2): # Найти расстояние между 2 точками
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    #print(f"x1 {x1}, x2 {x2}, y1 {y1}, y2 {y2}")
    #print(d)
    return d

def line_length(x1, y1, x2, y2): # Найти длину вектора
    l = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return l

def vector_coords(x1, y1, x2, y2): # Вычислить координаты вектора
    x = x2 - x1
    y = y2 - y1
    return x, y

def scalar_vector_product(a, b): # Вычислить скалярное произведение векторов
    ab = a[0] * b[0] + a[1] * b[1]
    print(a, b)
    return ab
    
def vectors_angle(ab, l1, l2): # Вычислить угол между векторами
    cosa = ab / ((l1 * c.scale) * (l2 * c.scale)) # Вычисление косинуса
    print(cosa)
    try:
        arad = math.acos(cosa) # Вычисление аркосинуса в радианах
    except ValueError:
        true_range = max(-1, min(1, cosa)) # Стабилизация погрешности
        arad = math.acos(true_range)
        
    adeg =  math.degrees(arad) # Перевод радиан в градусы
    a = round(adeg, 1)
    return a

def similarity(a, b): # Проверить являются ли два числа одинаковыми с учётом погрешности
    d = abs(a - b) # Модуль разности 2 чисел
    print(d)
    if d < 1:
        return True
    else:
        return False
  
def analyze_figure(): # Анализировать фигуру на поле
    print("analyze")
    GUI.design_start_btn.config(state="disabled")
    
    sym = "ABCDEFGHIKLMNOPQTUVWXYZ0123456789"
    
    global vertexes, sides, angeles, widgets, closed, flags, r, figure_id, S, P
    vertexes.clear() # Сброс списка до по-умолчания
    sides.clear() # Сброс списка до по-умолчания
    for id in flags:
        GUI.canvas.delete(id)
    flags.clear() # Сброс списка до по-умолчания
    angeles.clear() # Сброс списка до по-умолчания
    
    figure = txt.dm_figure if c.language == "ru" else txt.dm_figure2
    
    if len(widgets) > 0:
        for w in widgets:
            w.place_forget()
        widgets.clear()
    
    for obj in c.objects:
        if obj[1] == "curve": # Проверка на ломанную линию
            vertexes.append(obj[0])
            figure_id = obj[2] 
            print(len(vertexes[0]))
            print(f"vertexes: {vertexes}")
        else:
            GUI.design_descr.configure(text=txt.design_descr_error if c.language == "ru" else txt.design_descr_error2)
    
    if len(vertexes) == 0:
        GUI.design_descr.configure(text=txt.design_descr_error if c.language == "ru" else txt.design_descr_error2)
        GUI.design_start_btn.configure(state="normal")
        return
        
    # Проверка на замкнутость линий   
    if close_points(x1=vertexes[0][0][0], y1=vertexes[0][0][1], x2=vertexes[0][-1][0], y2=vertexes[0][-1][1]):
        closed = True
        vertexes[0].pop() # Удаление последней маловажной вершины из соображений замкнутости фигуры
        vertexes[0].append(vertexes[0][0])
    else:
        closed = False
        
    # Проверка фигуры
    if len(vertexes[0]) == 2:
        figure = txt.line if c.language == "ru" else txt.line2
    elif len(vertexes[0]) == 3:
        figure = txt.angle if c.language == "ru" else txt.angle2
    elif len(vertexes[0]) == 4 and closed:
        figure = txt.triangle if c.language == "ru" else txt.triangle2
    elif len(vertexes[0]) == 5 and closed:
        figure = txt.rectangle if c.language == "ru" else txt.rectangle2
    else:
        GUI.design_descr.configure(text=txt.design_descr_error if c.language == "ru" else txt.design_descr_error2) 
    
    if closed:
        for vertex in vertexes[0][:-1]:
            flags.append(GUI.canvas.create_oval(vertex[0]-r, vertex[1]-r, vertex[0]+r, vertex[1]+r, fill="gray"))
    else: 
        for vertex in vertexes[0]:
            flags.append(GUI.canvas.create_oval(vertex[0]-r, vertex[1]-r, vertex[0]+r, vertex[1]+r, fill="gray"))
       
    i = 1 # Индекс координат второй точки для вычисления длины
    try:
        for coords in vertexes[0]: # Поиск длин сторон
            if i < len(vertexes[0]):
                sides.append(round(line_length(coords[0], coords[1], vertexes[0][i][0], vertexes[0][i][1]) / c.scale, 1))
                i += 1
                
        P = round(sum(sides), 1) # Вычисление периметра
    except IndexError:
        check = len(vertexes)
        if check == 0: # Проверка на наличие фигуры
            GUI.design_descr.configure(text=txt.design_descr_error)
            print("WARN: list 'vertexes' is empty")
            GUI.design_start_btn.config(state="normal") # Включение кнопки
            return # Остановка выполнения
    
    if len(vertexes[0]) == 3 and not closed: # Вычисляем угол
        a_coords = vector_coords(vertexes[0][1][0], vertexes[0][1][1], vertexes[0][0][0], vertexes[0][0][1])
        b_coords = vector_coords(vertexes[0][1][0], vertexes[0][1][1], vertexes[0][2][0], vertexes[0][2][1])
        
        ab = scalar_vector_product(a_coords, b_coords)
        
        A = vectors_angle(ab, sides[0], sides[1])
        angeles.append(A)
    
    elif len(vertexes[0]) == 4 and closed: # Вычисляем параметры треугольника
        
        # Поиск углов
        # Вычисляем координаты 2 смежных сторон (векторов)
        a_coords = vector_coords(vertexes[0][1][0], vertexes[0][1][1], vertexes[0][0][0], vertexes[0][0][1])
        b_coords = vector_coords(vertexes[0][1][0], vertexes[0][1][1], vertexes[0][2][0], vertexes[0][2][1])
        # Вычисляем их скалярное произведение
        ab = scalar_vector_product(a_coords, b_coords)
        # Находим 1 угол между ними
        A = vectors_angle(ab, sides[0], sides[1])
        angeles.append(A)
        
        a_coords = vector_coords(vertexes[0][2][0], vertexes[0][2][1], vertexes[0][1][0], vertexes[0][1][1])
        b_coords = vector_coords(vertexes[0][2][0], vertexes[0][2][1], vertexes[0][0][0], vertexes[0][0][1])
        # Вычисляем их скалярное произведение
        ab = scalar_vector_product(a_coords, b_coords)
        # Находим 1 угол между ними
        A = vectors_angle(ab, sides[1], sides[2])
        angeles.append(A)
        
        a_coords = vector_coords(vertexes[0][0][0], vertexes[0][0][1], vertexes[0][2][0], vertexes[0][2][1])
        b_coords = vector_coords(vertexes[0][0][0], vertexes[0][0][1], vertexes[0][1][0], vertexes[0][1][1])
        # Вычисляем их скалярное произведение
        ab = scalar_vector_product(a_coords, b_coords)
        # Находим 1 угол между ними
        A = vectors_angle(ab, sides[2], sides[0])
        angeles.append(A)
        
        # Вычисление площади
        p = P / 2 # Полупериметр
        S = round(math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])), 1)
        
        # Поиск особенностей
        if similarity(sides[0], sides[1]) and similarity(sides[1], sides[2]) and similarity(sides[2], sides[0]):
            figure = txt.equilateralT if c.language == "ru" else txt.equilateralT2
        elif similarity(angeles[0], angeles[1]) or similarity(angeles[1], angeles[2]) or similarity(angeles[2], angeles[0]):
            figure = txt.isoscelesT if c.language == "ru" else txt.isoscelesT2
    
    elif len(vertexes[0]) == 5 and closed: # Вычисляем параметры четырёхугольника
        a_coords = vector_coords(vertexes[0][0][0], vertexes[0][0][1], vertexes[0][1][0], vertexes[0][1][1])
        b_coords = vector_coords(vertexes[0][0][0], vertexes[0][0][1], vertexes[0][3][0], vertexes[0][3][1])
        # Вычисляем их скалярное произведение
        ab = scalar_vector_product(a_coords, b_coords)
        # Находим 1 угол между ними
        A = vectors_angle(ab, sides[0], sides[3])
        angeles.append(A)
        
        # Поиск углов
        # Вычисляем координаты 2 смежных сторон (векторов)
        a_coords = vector_coords(vertexes[0][1][0], vertexes[0][1][1], vertexes[0][0][0], vertexes[0][0][1])
        b_coords = vector_coords(vertexes[0][1][0], vertexes[0][1][1], vertexes[0][2][0], vertexes[0][2][1])
        # Вычисляем их скалярное произведение
        ab = scalar_vector_product(a_coords, b_coords)
        # Находим 1 угол между ними
        A = vectors_angle(ab, sides[0], sides[1])
        angeles.append(A)
        
        a_coords = vector_coords(vertexes[0][2][0], vertexes[0][2][1], vertexes[0][1][0], vertexes[0][1][1])
        b_coords = vector_coords(vertexes[0][2][0], vertexes[0][2][1], vertexes[0][3][0], vertexes[0][3][1])
        # Вычисляем их скалярное произведение
        ab = scalar_vector_product(a_coords, b_coords)
        # Находим 1 угол между ними
        A = vectors_angle(ab, sides[1], sides[2])
        angeles.append(A)
        
        a_coords = vector_coords(vertexes[0][3][0], vertexes[0][3][1], vertexes[0][0][0], vertexes[0][0][1])
        b_coords = vector_coords(vertexes[0][3][0], vertexes[0][3][1], vertexes[0][2][0], vertexes[0][2][1])
        # Вычисляем их скалярное произведение
        ab = scalar_vector_product(a_coords, b_coords)
        # Находим 1 угол между ними
        A = vectors_angle(ab, sides[2], sides[3])
        angeles.append(A)
        
        # Поиск особенностей
        if similarity(sides[0], sides[2]) and similarity(sides[1], sides[3]): # Фигура - параллелограмм
            figure = txt.parallelogram if c.language == "ru" else txt.parallelogram2
            arad = math.radians(angeles[0])
            S = round(sides[0] * sides[1] * math.sin(arad), 1)
            if similarity(angeles[0], angeles[1]) and similarity(angeles[2], angeles[3]) and similarity(sides[0], sides[1]): # Фигура - квадрат
                figure = txt.square if c.language == "ru" else txt.square2
                print("sq")
                S = round(sides[0] ** 2, 1)
            else:
                print(similarity(angeles[0], angeles[1]), similarity(angeles[2], angeles[3]), similarity(sides[0], sides[1]))
        else:
            S = 0
         
                
    # Вывод информации
    if c.language == "ru":  
        info = f'''
Фигура: {figure}
Длины сторон: {sides}
Углы (градусы): {angeles}
Периметр: {P}
Площадь: {S}
'''
    else:
        info = f'''
Figure: {figure}
length of sides: {sides}
Angeles (degrees): {angeles}
Perimeter: {P}
Square: {S}
'''
    
    i = 0
    if closed and show_letters:
        for vertex in vertexes[0][:-1]:
            new_widget = tk.Label(GUI.canvas, text=sym[i])
            widgets.append(new_widget)
            new_widget.place(x=vertex[0]-30, y=vertex[1]-30)
            i += 1
    elif show_letters:
        for vertex in vertexes[0]:
            new_widget = tk.Label(GUI.canvas, text=sym[i])
            widgets.append(new_widget)
            new_widget.place(x=vertex[0]-30, y=vertex[1]-30)
            i += 1
    
    GUI.design_descr.configure(text=info) 
    print(f"vertexes: {vertexes}")
    print(f"flags: {flags}")
    GUI.design_start_btn.config(state="normal")

true_vert = None

def resize_vertex(event): # Передвижение вершин
    global vertexes, flags, r, true_vert, figure
    print(f"flags: {flags}")
    mouse_pos_x = event.x
    mouse_pos_y = event.y
    match = False
    
    for vertex in vertexes[0]:
        circle_center_x = vertex[0] + r
        circle_center_y = vertex[1] + r
        
        s = S_points(circle_center_x, circle_center_y, mouse_pos_x, mouse_pos_y)
        if s <= r + 5:
            match = True
            true_vert = vertex
        else:
            print(vertex, s, r)
            continue
        if match:
            break
    print(vertexes, true_vert)
    index = vertexes[0].index(true_vert) 
    dot = flags[index] 
    
    # Изменение положения вершин
    GUI.canvas.coords(dot, mouse_pos_x-r, mouse_pos_y-r, mouse_pos_x+r, mouse_pos_y+r)
    vertexes[0][index][0] = mouse_pos_x
    vertexes[0][index][1] = mouse_pos_y
    print(figure_id)
    print(vertexes)
    GUI.canvas.coords(figure_id, vertexes[0])
    print(flags)
    
def del_letters(): # Выкл/вкл обозначения, скрыть их
    global widgets, show_letters
    show_letters = not show_letters
    
    if not show_letters: # Очистить поле от обозначений
        GUI.design_del_flags.config(bg=GUI.false_color)
        if len(widgets) > 0:
            for w in widgets:
                w.place_forget()
        widgets.clear()
    else:
        GUI.design_del_flags.config(bg=GUI.true_color)
    

    
    
    
    
    

