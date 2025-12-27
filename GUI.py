import tkinter as tk
import config as c
import os
import text as txt
import  utils
from tkinter import font
from tkinter import messagebox
import design_mode as dmode
import threading

# Показать все шрифты
#print(font.families())

toggle_settings = False # Флаг настроек
toggle_design_mode = False # Флаг режима проектирования

true_color = "#0FB978"
false_color = "#D22B44"
button_color = "#2E34A6" # Цвет кнопок
Btext_color = "#FFFFFF" # Цвет текста на кнопках
button_2stroke_color = "#062D68"
active_button_color = "#3A8AE5" # Цвет включённых кнопок 1 группы
active_button_color_2 = "#06728A" # Цвет включённых кнопок 2 группы
sidebar_color = "#303848" # Цвет верхней панели
barline_color = "#111E36" # Цвет боковой панели
menu_button_font = font.Font(size=11)
snowflakes = []

#
app_logo_path = c.resource_path("img/Logo.png") # Путь к логотипу
app_logo = tk.PhotoImage(file=app_logo_path) # Логотип
app_logo = app_logo.subsample(15, 15) # Изменить размер логотипа

app_logo_path_winter = c.resource_path("img/Logo_christmas.png") # Путь к логотипу
app_logo_winter = tk.PhotoImage(file=app_logo_path_winter) # Логотип
app_logo_winter = app_logo_winter.subsample(15, 15) # Изменить размер логотипа

git_link_path = c.resource_path("img/mygithub.png")
git_link = tk.PhotoImage(file=git_link_path)
git_link = git_link.subsample(9, 9)

snowflake_path = c.resource_path("img/snowflake.png") # Путь к логотипу
snowflake_pic = tk.PhotoImage(file=snowflake_path) # Логотип
snowflake_pic = snowflake_pic.subsample(5, 5) # Изменить размер логотипа

c.win.configure(bg="#1C2237") # Цвет окна

labels = [] # Список временных виджетов
def thread_dmode():
    analyze_thread = threading.Thread(target=dmode.analyze_figure, daemon=True)
    analyze_thread.start()

def BaseFont(size): # Получение основного шрифта
    ft = font.Font(family="Comic Sans MS", size=size)
    return ft

def choose_lang(lang): # Смена языка
    messagebox.showinfo(txt.info if c.language == "ru" else txt.info2, txt.lang_alert if c.language == "ru" else txt.lang_alert2)
    c.language = lang


def settings(): # Открытие настроек
    global toggle_settings, toggle_design_mode, sett_btn, base_logo, panel_title
    toggle_settings = not toggle_settings
    if toggle_settings:
        toggle_design_mode = False
        design_btn.configure(bg=button_2stroke_color)
        design_descr.place_forget()
        design_start_btn.place_forget()
        design_del_flags.place_forget()
        
        sett_btn.configure(bg=active_button_color_2)
        base_logo.place_forget()
        panel_title.configure(text=txt.settings if c.language == "ru" else txt.settings2)
        if c.theme == "christmas":
            for el in snowflakes:
                el.place_forget()
        utils.open_settings()
    else:
        export_sett_btn.place_forget()
        ru_btn.place_forget()
        en_btn.place_forget()
        settings_lang.place_forget()
        settings_lang_descr.place_forget()
        settings_work_color.place_forget()
        settings_work_color_descr.place_forget()
        settings_choose_color_btn.place_forget()
        settings_theme_btn.place_forget()
        work_color_button.place_forget()
        settings_scale_text.place_forget()
        settings_scale_text_descr.place_forget()
        settings_plus_button.place_forget()
        settings_minus_button.place_forget()
        theme_christmas_btn.place_forget()
        theme_std_btn.place_forget()
        theme_dark_btn.place_forget()
        theme_light_btn.place_forget()
        theme_cream_btn.place_forget()
        base_logo.place(x=150, y=300)
        panel_title.configure(text=txt.welcome if c.language == "ru" else txt.welcome2)
        sett_btn.configure(bg=button_2stroke_color)
        a = 0
        if c.theme == "christmas":
            for el in snowflakes:
                coords = ((85, 350), (140, 260), (230, 275), (330, 250), (410, 400))
                el.place(x=coords[a][0], y=coords[a][1])
                a += 1
               
def design(): # Открытие режима проектирования
    global toggle_design_mode, toggle_settings, sett_btn, base_logo, panel_title, button_color, base_logo
    toggle_design_mode = not toggle_design_mode
    if toggle_design_mode:
        toggle_settings = False
        sett_btn.configure(bg=button_2stroke_color)
        
        design_btn.configure(bg=active_button_color_2)
        export_sett_btn.place_forget()
        base_logo.place_forget()
        settings_lang.place_forget()
        settings_lang_descr.place_forget()
        settings_work_color.place_forget()
        settings_work_color_descr.place_forget()
        settings_choose_color_btn.place_forget()
        settings_scale_text.place_forget()
        settings_scale_text_descr.place_forget()
        settings_plus_button.place_forget()
        settings_minus_button.place_forget()
        settings_theme_btn.place_forget()
        ru_btn.place_forget()
        en_btn.place_forget()
        work_color_button.place_forget()
        theme_std_btn.place_forget()
        theme_christmas_btn.place_forget()
        theme_dark_btn.place_forget()
        theme_light_btn.place_forget()
        theme_cream_btn.place_forget()
                
        panel_title.configure(text=txt.design_start if c.language == "ru" else txt.design_start2)
        if c.theme == "christmas":
            for el in snowflakes:
                el.place_forget()
            
        filling_btn.config(state="disabled")    
        rect_btn.config(state="disabled")
        oval_btn.config(state="disabled")
        line_btn.config(state="disabled")
        dot_btn.config(state="disabled")
        dash_btn.config(state="disabled")
        curve_btn.config(state="disabled")
        brush_btn.config(state="disabled")
        c.current_figure = None
        
        rect_btn.configure(bg=button_color)
        oval_btn.configure(bg=button_color)
        line_btn.configure(bg=button_color)
        dot_btn.configure(bg=button_color)
        signature_btn.configure(bg=button_color)
        dash_btn.configure(bg=button_color)
        curve_btn.configure(bg=button_color)
        
        design_descr.place(x=30, y=100)
        design_start_btn.place(x=30, y=350)
        design_del_flags.place(x=110, y=350)
        dmode.start()
    elif not toggle_design_mode and not toggle_settings:
        c.draw = True
        design_btn.configure(bg=button_2stroke_color)
        panel_title.configure(text=txt.welcome if c.language == "ru" else txt.welcome2)
        design_descr.place_forget()
        design_del_flags.place_forget()
        a = 0
        if c.theme == "christmas":
            for el in snowflakes:
                coords = ((85, 350), (140, 260), (230, 275), (330, 250), (410, 400))
                el.place(x=coords[a][0], y=coords[a][1])
                a += 1
        
        design_start_btn.place_forget()
        base_logo.place(x=150, y=300)
        filling_btn.config(state="normal")
        rect_btn.config(state="normal")
        oval_btn.config(state="normal")
        line_btn.config(state="normal")
        dot_btn.config(state="normal")
        dash_btn.config(state="normal")
        curve_btn.config(state="normal")
        brush_btn.config(state="normal")        

# Темы
def change_theme(): # Смена темы приложения
    ru_btn.place_forget()
    en_btn.place_forget()
    settings_lang.place_forget()
    settings_lang_descr.place_forget()
    settings_work_color.place_forget()
    settings_work_color_descr.place_forget()
    settings_choose_color_btn.place_forget()
    settings_theme_btn.place_forget()
    work_color_button.place_forget()
    settings_scale_text.place_forget()
    settings_scale_text_descr.place_forget()
    settings_plus_button.place_forget()
    settings_minus_button.place_forget()
    
    panel_title.configure(text=txt.theme_mode if c.language == "ru" else txt.theme_mode2)
    theme_std_btn.place(x=10, y=80)
    theme_christmas_btn.place(x=100, y=80)
    theme_dark_btn.place(x=190, y=80)
    theme_light_btn.place(x=10, y=160)
    theme_cream_btn.place(x=100, y=160)

def edit_theme(bgr, bz_s, bs, bc1, bca1, bc2, bca2, tc, set_name): # Смена на новогоднюю тему
    global button_color, active_button_color, button_2stroke_color, active_button_color_2, app_logo_winter
    button_color = bc1
    active_button_color = bca1
    button_2stroke_color = bc2
    active_button_color_2 = bca2
    sidebar_color = bz_s
    Btext_color = tc
    
    c.win.configure(bg=bgr)
    if set_name == "christmas":
        base_logo.configure(image=app_logo_winter)
        for i in range(5):
            snowflake = tk.Label(sidebar, image=snowflake_pic, bg=sidebar_color)
            snowflakes.append(snowflake)
    else:
        base_logo.configure(image=app_logo)
        for el in snowflakes:
            el.place_forget()
    
    border_for_zone.configure(bg=sidebar_color)
    sidebar.configure(bg=sidebar_color)
    barline.configure(bg=bs)
    panel_title.configure(bg=sidebar_color, fg=Btext_color)
    version_title.configure(bg=sidebar_color, fg=Btext_color)
    github_link.configure(bg=sidebar_color)
    base_logo.configure(bg=sidebar_color)
    
    
    filling_btn.configure(bg=button_color, fg=Btext_color)
    rect_btn.configure(bg=button_color, fg=Btext_color)
    oval_btn.configure(bg=button_color, fg=Btext_color)
    line_btn.configure(bg=button_color, fg=Btext_color)
    dot_btn.configure(bg=button_color, fg=Btext_color)
    signature_btn.configure(bg=button_color, fg=Btext_color)
    dash_btn.configure(bg=button_color, fg=Btext_color)
    curve_btn.configure(bg=button_color, fg=Btext_color)
    brush_btn.configure(bg=button_color, fg=Btext_color)
    eraser_btn.configure(bg=button_color, fg=Btext_color)
    clear_btn.configure(bg=button_2stroke_color, fg=Btext_color)
    del_last_btn.configure(bg=button_2stroke_color, fg=Btext_color)
    color_btn.configure(bg=button_2stroke_color, fg=Btext_color)
    design_btn.configure(bg=button_2stroke_color, fg=Btext_color)
    sett_btn.configure(bg=active_button_color_2, fg=Btext_color)
    export_sett_btn.configure(bg=button_color, fg=Btext_color)
    
    export_obj_btn.configure(bg=button_2stroke_color, fg=Btext_color)
    settings_lang.configure(bg=sidebar_color, fg=Btext_color)
    settings_lang_descr.configure(bg=sidebar_color, fg=Btext_color)
    ru_btn.configure(bg=button_color, fg=Btext_color)
    en_btn.configure(bg=button_color, fg=Btext_color)
    settings_work_color.configure(bg=sidebar_color, fg=Btext_color)
    settings_work_color_descr.configure(bg=sidebar_color, fg=Btext_color)
    settings_choose_color_btn.configure(bg=button_color, fg=Btext_color)
    settings_theme_btn.configure(bg=button_color, fg=Btext_color)
    work_color_button.configure(bg=button_color, fg=Btext_color)
    settings_scale_text.configure(bg=sidebar_color, fg=Btext_color)
    settings_scale_text_descr.configure(bg=sidebar_color, fg=Btext_color)
    settings_plus_button.configure(bg=button_color, fg=Btext_color)
    settings_minus_button.configure(bg=button_color, fg=Btext_color)
    
    design_descr.configure(bg=sidebar_color, fg=Btext_color)
    design_start_btn.configure(bg=button_color, fg=Btext_color)
    
    theme_christmas_btn.configure(bg=button_color, fg=Btext_color)
    theme_std_btn.configure(bg=button_color, fg=Btext_color)
    theme_dark_btn.configure(bg=button_color, fg=Btext_color)
    theme_light_btn.configure(bg=button_color, fg=Btext_color)
    theme_cream_btn.configure(bg=button_color, fg=Btext_color)
    
    c.theme = set_name
    
# Основные кнопки    
def choose_rect(): # Выбор квадрата
    if c.current_figure == "rect":
        c.current_figure = None
        rect_btn.configure(bg=button_color)
    else:
        c.current_figure = "rect"
        rect_btn.configure(bg=active_button_color)
        oval_btn.configure(bg=button_color)
        line_btn.configure(bg=button_color)
        dot_btn.configure(bg=button_color)
        signature_btn.configure(bg=button_color)
        dash_btn.configure(bg=button_color)
        curve_btn.configure(bg=button_color)
        brush_btn.configure(bg=button_color)
        eraser_btn.configure(bg=button_color)
        filling_btn.configure(bg=button_color)
    
def choose_oval(): # Выбор овала
    if c.current_figure == "oval":
        c.current_figure = None
        oval_btn.configure(bg=button_color)
    else:
        c.current_figure = "oval"
        oval_btn.configure(bg=active_button_color)
        rect_btn.configure(bg=button_color)
        line_btn.configure(bg=button_color)
        dot_btn.configure(bg=button_color)
        signature_btn.configure(bg=button_color)
        dash_btn.configure(bg=button_color)
        curve_btn.configure(bg=button_color)
        brush_btn.configure(bg=button_color)
        eraser_btn.configure(bg=button_color)
        filling_btn.configure(bg=button_color)
    
def choose_line(): # Выбор линии
    if c.current_figure == "line":
        c.current_figure = None
        line_btn.configure(bg=button_color)
    else:
        c.current_figure = "line"
        line_btn.configure(bg=active_button_color)
        rect_btn.configure(bg=button_color)
        oval_btn.configure(bg=button_color)
        dot_btn.configure(bg=button_color)
        signature_btn.configure(bg=button_color)
        dash_btn.configure(bg=button_color)
        curve_btn.configure(bg=button_color)
        brush_btn.configure(bg=button_color)
        eraser_btn.configure(bg=button_color)
        filling_btn.configure(bg=button_color)

def choose_dot(): # Выбор точки
    if c.current_figure == "dot":
        c.current_figure = None
        dot_btn.configure(bg=button_color)
    else:
        c.current_figure = "dot"
        dot_btn.configure(bg=active_button_color)
        line_btn.configure(bg=button_color)
        rect_btn.configure(bg=button_color)
        oval_btn.configure(bg=button_color)
        signature_btn.configure(bg=button_color)
        dash_btn.configure(bg=button_color)
        curve_btn.configure(bg=button_color)
        brush_btn.configure(bg=button_color)
        eraser_btn.configure(bg=button_color)
        filling_btn.configure(bg=button_color)
    
def choose_sign(): # Выбор подписи
    if c.current_figure == "signature":
        c.current_figure = None
        signature_btn.configure(bg=button_color)
    else:
        c.current_figure = "signature"
        signature_btn.configure(bg=active_button_color)
        dot_btn.configure(bg=button_color)
        line_btn.configure(bg=button_color)
        rect_btn.configure(bg=button_color)
        oval_btn.configure(bg=button_color)
        dash_btn.configure(bg=button_color)
        curve_btn.configure(bg=button_color)
        brush_btn.configure(bg=button_color)
        eraser_btn.configure(bg=button_color)
        filling_btn.configure(bg=button_color)
    
def choose_dash(): # Выбор пунктира
    if c.current_figure == "dash":
        c.current_figure = None
        dash_btn.configure(bg=button_color)
    else:
        c.current_figure = "dash"
        dash_btn.configure(bg=active_button_color)
        signature_btn.configure(bg=button_color)
        dot_btn.configure(bg=button_color)
        line_btn.configure(bg=button_color)
        rect_btn.configure(bg=button_color)
        oval_btn.configure(bg=button_color)
        curve_btn.configure(bg=button_color)
        brush_btn.configure(bg=button_color)
        eraser_btn.configure(bg=button_color)
        filling_btn.configure(bg=button_color)
   
def choose_curve(): # Выбор кривой
    if c.current_figure == "curve":
        c.current_figure = None
        curve_btn.configure(bg=button_color)
    else:
        c.current_figure = "curve"
        curve_btn.configure(bg=active_button_color)
        dash_btn.configure(bg=button_color)
        signature_btn.configure(bg=button_color)
        dot_btn.configure(bg=button_color)
        line_btn.configure(bg=button_color)
        rect_btn.configure(bg=button_color)
        oval_btn.configure(bg=button_color)
        brush_btn.configure(bg=button_color)
        eraser_btn.configure(bg=button_color)
        filling_btn.configure(bg=button_color)

def choose_brush():
   if c.current_figure == "brush":
        c.current_figure = None
        brush_btn.configure(bg=button_color)
   else:
        c.current_figure = "brush"
        brush_btn.configure(bg=active_button_color)
        curve_btn.configure(bg=button_color)
        dash_btn.configure(bg=button_color)
        signature_btn.configure(bg=button_color)
        dot_btn.configure(bg=button_color)
        line_btn.configure(bg=button_color)
        rect_btn.configure(bg=button_color)
        oval_btn.configure(bg=button_color)
        eraser_btn.configure(bg=button_color)
        filling_btn.configure(bg=button_color)

def choose_eraser():
    if c.current_figure == "eraser":
        c.current_figure = None
        eraser_btn.configure(bg=button_color)
    else:
        c.current_figure = "eraser"
        eraser_btn.configure(bg=active_button_color)
        brush_btn.configure(bg=button_color)
        curve_btn.configure(bg=button_color)
        dash_btn.configure(bg=button_color)
        signature_btn.configure(bg=button_color)
        dot_btn.configure(bg=button_color)
        line_btn.configure(bg=button_color)
        rect_btn.configure(bg=button_color)
        oval_btn.configure(bg=button_color)
        filling_btn.configure(bg=button_color)

def choose_filling():
    if c.current_figure == "filling":
        c.current_figure = None
        filling_btn.configure(bg=button_color)
    else:
        c.current_figure = "filling"
        filling_btn.configure(bg=active_button_color)
        eraser_btn.configure(bg=button_color)
        brush_btn.configure(bg=button_color)
        curve_btn.configure(bg=button_color)
        dash_btn.configure(bg=button_color)
        signature_btn.configure(bg=button_color)
        dot_btn.configure(bg=button_color)
        line_btn.configure(bg=button_color)
        rect_btn.configure(bg=button_color)
        oval_btn.configure(bg=button_color)           

# Поле        
border_for_zone = tk.Frame(c.win, bg="#3C465A", width=765, height=595)
canvas = tk.Canvas(border_for_zone, width=750, height=580, bg="#F8F9FA")

# Основная верхняя панель
sett_btn = tk.Button(c.win, text=txt.settings, width=10, height=2, command=settings, bg=button_2stroke_color, fg=Btext_color)
clear_btn = tk.Button(c.win, text=txt.clear, width=10, height=2, command=lambda: utils.lines(canvas, c.scale), bg=button_2stroke_color, activebackground="#E92E2E", fg=Btext_color)
del_last_btn = tk.Button(c.win, text=txt.last, width=18, height=2, command=lambda: utils.del_last(), bg=button_2stroke_color, activebackground="#E92E2E", fg=Btext_color)
color_btn = tk.Button(c.win, text=txt.change_color, width=18, height=2, command=lambda: utils.change_color(), bg=button_2stroke_color, activebackground=active_button_color, fg=Btext_color)
export_obj_btn = tk.Button(c.win, text=txt.export_objects, width=23, height=2, command=utils.export_objects, bg=button_2stroke_color, fg=Btext_color)
design_btn = tk.Button(c.win, text=txt.design, width=18, height=2, command=design, bg="#062D68", activebackground=active_button_color, fg=Btext_color)
rect_btn = tk.Button(c.win, text=txt.rect, width=10, height=3, command=choose_rect, bg=button_color, fg=Btext_color)
oval_btn = tk.Button(c.win, text=txt.oval, width=10, height=3, command=choose_oval, bg=button_color, fg=Btext_color)
line_btn = tk.Button(c.win, text=txt.line, width=10, height=3, command=choose_line, bg=button_color, fg=Btext_color)
dot_btn = tk.Button(c.win, text=txt.dot, width=10, height=3, command=choose_dot, bg=button_color, fg=Btext_color)
signature_btn = tk.Button(c.win, text=txt.signature, width=10, height=3, command=choose_sign, bg=button_color, fg=Btext_color) 
dash_btn = tk.Button(c.win, text=txt.dash, width=10, height=3, command=choose_dash, bg=button_color, fg=Btext_color)
curve_btn = tk.Button(c.win, text=txt.curve, width=10, height=3, command=choose_curve, bg=button_color, fg=Btext_color)
brush_btn = tk.Button(c.win, text=txt.brush, width=10, height=3, command=choose_brush, bg=button_color, fg=Btext_color)
eraser_btn = tk.Button(c.win, text=txt.eraser, width=8, height=3, command=choose_eraser, bg=button_color, fg=Btext_color)
filling_btn = tk.Button(c.win, text=txt.filling, width=10, height=3, command=choose_filling, bg=button_color, fg=Btext_color)

# Боковая панель
barline = tk.Frame(c.win, bg=barline_color, width=50)
sidebar = tk.Frame(barline, bg=sidebar_color, width=50)
base_logo = tk.Label(sidebar, image=app_logo, bg=sidebar_color) # Логотип
github_link =  tk.Label(sidebar, image=git_link, bg=sidebar_color) # Картинка с призывом

# Окно ввода подписи
field_input = tk.Entry(canvas, width=7, font=("Arial", 16), highlightcolor="#000000")
field_button = tk.Button(canvas, text=txt.enter, height=1, bg="#B4F7F4", command=utils.create_sign)

# Панель настроек
panel_title = tk.Label(sidebar, bg=sidebar_color, text=txt.welcome, font=BaseFont(20), fg=Btext_color, anchor="center")
version_title = tk.Label(sidebar, bg=sidebar_color, text=c.version, font=BaseFont(20), fg=Btext_color, anchor="center")
export_sett_btn = tk.Button(sidebar, text=txt.export_settings, width=23, height=2, command=utils.export_settings, bg=button_color, fg=Btext_color)
settings_lang = tk.Label(sidebar, bg=sidebar_color, text=txt.settings_lang, font=BaseFont(20), fg=Btext_color, anchor="center")
settings_lang_descr = tk.Label(sidebar, bg=sidebar_color, text=txt.settings_lang_descr, font=BaseFont(15), fg=Btext_color, anchor="center")
settings_work_color = tk.Label(sidebar, bg=sidebar_color, text=txt.settings_work_color, font=BaseFont(20), fg=Btext_color, anchor="center")
settings_work_color_descr = tk.Label(sidebar, bg=sidebar_color, text=txt.settings_work_color_descr, font=BaseFont(15), fg=Btext_color, anchor="center")
settings_choose_color_btn = tk.Button(sidebar, text=txt.palette, width=10, height=3,fg=Btext_color, bg=button_color, command=utils.enter_color, padx=10)
settings_theme_btn = tk.Button(sidebar, text=txt.theme, width=10, height=3,fg=Btext_color, bg=button_color, command=change_theme, padx=10)
settings_scale_text = tk.Label(sidebar, bg=sidebar_color, text=txt.settings_scale, font=BaseFont(20), fg=Btext_color, anchor="center")
settings_scale_text_descr = tk.Label(sidebar, bg=sidebar_color, text=txt.settings_scale_descr, font=BaseFont(15), fg=Btext_color, anchor="center")
settings_plus_button = tk.Button(sidebar, text="+", width=10, height=3, font=menu_button_font, command=lambda: utils.scale("+"), bg=button_color, fg=Btext_color)
settings_minus_button = tk.Button(sidebar, text="-", width=10, height=3, font=menu_button_font, command=lambda: utils.scale("-"), bg=button_color, fg=Btext_color)
ru_btn = tk.Button(sidebar, text=txt.settings_rutext, width=10, height=3, font=menu_button_font, command=lambda: choose_lang("ru"), bg=button_color, fg=Btext_color)
en_btn = tk.Button(sidebar, text=txt.settings_entext, width=10, height=3, font=menu_button_font, command=lambda: choose_lang("en"), bg=button_color, fg=Btext_color)
work_color_button = tk.Button(sidebar, text=txt.work_color, width=10, height=3, command=utils.change_work_color, bg=button_color, fg=Btext_color)

# Режим проектирования
design_descr = tk.Label(sidebar, bg=sidebar_color, text=txt.design_descr, font=BaseFont(20), fg=Btext_color, justify="left")
design_start_btn = tk.Button(sidebar, text=txt.design_start_btn, width=10, height=3, command=thread_dmode, bg=button_color, fg=Btext_color)
design_del_flags = tk.Button(sidebar, text=txt.design_delf_btn, width=18, height=3, command=dmode.del_letters, bg=true_color, fg=Btext_color)

# Окно с темами
theme_std_btn = tk.Button(sidebar, text=txt.standart_theme, width=10, height=3, command=lambda: edit_theme("#1C2237", "#303848", "#111E36", "#2E34A6", "#3A8AE5", "#062D68", "#06728A", "#FFFFFF", "standart"), bg=button_color, fg=Btext_color)
theme_christmas_btn = tk.Button(sidebar, text=txt.HNY_theme, width=10, height=3, command=lambda: edit_theme("#0C2B3E","#1A3B4F", "#2E7D32", "#2E6A95", "#4A90C2", "#B33A3A", "#D95D5D", "#FFFFFF", "christmas"), bg=button_color, fg=Btext_color)
theme_dark_btn = tk.Button(sidebar, text=txt.dark_theme, width=10, height=3, command=lambda: edit_theme("#121212", "#1E1E1E", "#0A0A0A", "#2D2D2D", "#3D3D3D", "#252525", "#353535", "#FFFFFF", "dark"), bg=button_color, fg=Btext_color)
theme_light_btn = tk.Button(sidebar, text=txt.light_theme, width=10, height=3, command=lambda: edit_theme("#F5F5F5", "#E0E0E0", "#BDBDBD", "#EEEEEE", "#E0E0E0", "#E8E8E8", "#D5D5D5", "#000000", "light"), bg=button_color, fg=Btext_color)
theme_cream_btn = tk.Button(sidebar, text=txt.cream_theme, width=10, height=3, command=lambda: edit_theme("#FAF8F5", "#F2EDE6", "#E5DED3", "#E6D5B9", "#D4B483", "#D7C1A9", "#C19A6B", "#000000", "cream"), bg=button_color, fg=Btext_color)
