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

button_color = "#2E34A6" # Цвет кнопок
Btext_color = "#FFFFFF" # Цвет текста на кнопках
button_2stroke_color = "#062D68"
active_button_color = "#3498DB" # Цвет включённых кнопок 1 группы
active_button_color_2 = "#06728A" # Цвет включённых кнопок 2 группы
sidebar_color = "#303848" # Цвет верхней панели
barline_color = "#111E36" # Цвет боковой панели
menu_button_font = font.Font(size=11)

app_logo_path = c.resource_path("img/Logo.png") # Путь к логотипу
app_logo = tk.PhotoImage(file=app_logo_path) # Логотип
app_logo = app_logo.subsample(15, 15) # Изменить размер логотипа
git_link_path = c.resource_path("img/mygithub.png")
git_link = tk.PhotoImage(file=git_link_path)
git_link = git_link.subsample(9, 9)


c.win.configure(bg="#1C2237") # Цвет окна

labels = [] # Список временных виджетов
def thread_dmode():
    analyze_thread = threading.Thread(target=dmode.analyze_figure)
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
        
        sett_btn.configure(bg=active_button_color_2)
        base_logo.place_forget()
        panel_title.configure(text=txt.settings if c.language == "ru" else txt.settings2)
        utils.open_settings()
    else:
        ru_btn.place_forget()
        en_btn.place_forget()
        settings_lang.place_forget()
        settings_lang_descr.place_forget()
        settings_work_color.place_forget()
        settings_work_color_descr.place_forget()
        settings_choose_color.place_forget()
        settings_choose_color_btn.place_forget()
        work_color_button.place_forget()
        settings_scale_text.place_forget()
        settings_scale_text_descr.place_forget()
        settings_plus_button.place_forget()
        settings_minus_button.place_forget()
        base_logo.place(x=150, y=300)
        panel_title.configure(text=txt.welcome if c.language == "ru" else txt.welcome2)
        sett_btn.configure(bg=button_color)
        
def design(): # Открытие режима проектирования
    global toggle_design_mode, toggle_settings, sett_btn, base_logo, panel_title, button_color
    toggle_design_mode = not toggle_design_mode
    if toggle_design_mode:
        toggle_settings = False
        sett_btn.configure(bg=button_color)
        
        design_btn.configure(bg=active_button_color_2)
        base_logo.place_forget()
        settings_lang.place_forget()
        settings_lang_descr.place_forget()
        settings_work_color.place_forget()
        settings_work_color_descr.place_forget()
        settings_choose_color.place_forget()
        settings_choose_color_btn.place_forget()
        settings_scale_text.place_forget()
        settings_scale_text_descr.place_forget()
        settings_plus_button.place_forget()
        settings_minus_button.place_forget()
        ru_btn.place_forget()
        en_btn.place_forget()
        work_color_button.place_forget()
                
        panel_title.configure(text=txt.design_start if c.language == "ru" else txt.design_start2)
            
        rect_btn.config(state="disabled")
        oval_btn.config(state="disabled")
        line_btn.config(state="disabled")
        dash_btn.config(state="disabled")
        curve_btn.config(state="disabled")
        c.current_figure = None
        
        rect_btn.configure(bg=button_color)
        oval_btn.configure(bg=button_color)
        line_btn.configure(bg=button_color)
        dot_btn.configure(bg=button_color)
        signature_btn.configure(bg=button_color)
        dash_btn.configure(bg=button_color)
        curve_btn.configure(bg=button_color)
        
        design_descr.place(x=30, y=100)
        design_start_btn.place(x=190, y=350)
        dmode.start()
    elif not toggle_design_mode and not toggle_settings:
        c.draw = True
        design_btn.configure(bg=button_2stroke_color)
        panel_title.configure(text=txt.welcome if c.language == "ru" else txt.welcome2)
        design_descr.place_forget()
        
        design_start_btn.place_forget()
        base_logo.place(x=150, y=300)
        rect_btn.config(state="normal")
        oval_btn.config(state="normal")
        line_btn.config(state="normal")
        dash_btn.config(state="normal")
        curve_btn.config(state="normal")
        
    

def choose_rect(): # Выбор квадрата
    c.current_figure = "rect"
    rect_btn.configure(bg=active_button_color)
    oval_btn.configure(bg=button_color)
    line_btn.configure(bg=button_color)
    dot_btn.configure(bg=button_color)
    signature_btn.configure(bg=button_color)
    dash_btn.configure(bg=button_color)
    curve_btn.configure(bg=button_color)
    
def choose_oval(): # Выбор овала
    c.current_figure = "oval"
    oval_btn.configure(bg=active_button_color)
    rect_btn.configure(bg=button_color)
    line_btn.configure(bg=button_color)
    dot_btn.configure(bg=button_color)
    signature_btn.configure(bg=button_color)
    dash_btn.configure(bg=button_color)
    curve_btn.configure(bg=button_color)
    
def choose_line(): # Выбор линии
    c.current_figure = "line"
    line_btn.configure(bg=active_button_color)
    rect_btn.configure(bg=button_color)
    oval_btn.configure(bg=button_color)
    dot_btn.configure(bg=button_color)
    signature_btn.configure(bg=button_color)
    dash_btn.configure(bg=button_color)
    curve_btn.configure(bg=button_color)

def choose_dot(): # Выбор точки
    c.current_figure = "dot"
    dot_btn.configure(bg=active_button_color)
    line_btn.configure(bg=button_color)
    rect_btn.configure(bg=button_color)
    oval_btn.configure(bg=button_color)
    signature_btn.configure(bg=button_color)
    dash_btn.configure(bg=button_color)
    curve_btn.configure(bg=button_color)
    
def choose_sign(): # Выбор подписи
    c.current_figure = "signature"
    signature_btn.configure(bg=active_button_color)
    dot_btn.configure(bg=button_color)
    line_btn.configure(bg=button_color)
    rect_btn.configure(bg=button_color)
    oval_btn.configure(bg=button_color)
    dash_btn.configure(bg=button_color)
    curve_btn.configure(bg=button_color)
    
def choose_dash(): # Выбор пунктира
   c.current_figure = "dash"
   dash_btn.configure(bg=active_button_color)
   signature_btn.configure(bg=button_color)
   dot_btn.configure(bg=button_color)
   line_btn.configure(bg=button_color)
   rect_btn.configure(bg=button_color)
   oval_btn.configure(bg=button_color)
   curve_btn.configure(bg=button_color)
   
def choose_curve(): # Выбор кривой
   c.current_figure = "curve"
   curve_btn.configure(bg=active_button_color)
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
sett_btn = tk.Button(c.win, text=txt.settings, width=10, height=3, command=settings, bg=button_color, fg=Btext_color)
clear_btn = tk.Button(c.win, text=txt.clear, width=10, height=2, command=lambda: utils.lines(canvas, c.scale), bg="#062D68", activebackground="#E92E2E", fg=Btext_color)
del_last_btn = tk.Button(c.win, text=txt.last, width=18, height=2, command=lambda: utils.del_last(), bg="#062D68", activebackground="#E92E2E", fg=Btext_color)
color_btn = tk.Button(c.win, text=txt.change_color, width=18, height=2, command=lambda: utils.change_color(), bg="#062D68", activebackground=active_button_color, fg=Btext_color)
design_btn = tk.Button(c.win, text=txt.design, width=18, height=2, command=design, bg="#062D68", activebackground=active_button_color, fg=Btext_color)
rect_btn = tk.Button(c.win, text=txt.rect, width=10, height=3, command=choose_rect, bg=button_color, fg=Btext_color)
oval_btn = tk.Button(c.win, text=txt.oval, width=10, height=3, command=choose_oval, bg=button_color, fg=Btext_color)
line_btn = tk.Button(c.win, text=txt.line, width=10, height=3, command=choose_line, bg=button_color, fg=Btext_color)
dot_btn = tk.Button(c.win, text=txt.dot, width=10, height=3, command=choose_dot, bg=button_color, fg=Btext_color)
signature_btn = tk.Button(c.win, text=txt.signature, width=10, height=3, command=choose_sign, bg=button_color, fg=Btext_color) 
dash_btn = tk.Button(c.win, text=txt.dash, width=10, height=3, command=choose_dash, bg=button_color, fg=Btext_color)
curve_btn = tk.Button(c.win, text=txt.curve, width=10, height=3, command=choose_curve, bg=button_color, fg=Btext_color)

# Боковая панель
barline = tk.Frame(c.win, bg=barline_color, width=50)
sidebar = tk.Frame(barline, bg=sidebar_color, width=50)
base_logo = tk.Label(sidebar, image=app_logo, bg=sidebar_color) # Логотип
github_link =  tk.Label(sidebar, image=git_link, bg=sidebar_color)

# Окно ввода подписи
field_input = tk.Entry(canvas, width=7, font=("Arial", 16), highlightcolor="#000000")
field_button = tk.Button(canvas, text=txt.enter, height=1, bg="#B4F7F4", command=utils.create_sign)

# Панель настроек
panel_title = tk.Label(sidebar, bg=sidebar_color, text=txt.welcome, font=BaseFont(20), fg=Btext_color, anchor="center")
version_title = tk.Label(sidebar, bg=sidebar_color, text=c.version, font=BaseFont(20), fg=Btext_color, anchor="center")
settings_lang = tk.Label(sidebar, bg=sidebar_color, text=txt.settings_lang, font=BaseFont(20), fg=Btext_color, anchor="center")
settings_lang_descr = tk.Label(sidebar, bg=sidebar_color, text=txt.settings_lang_descr, font=BaseFont(15), fg=Btext_color, anchor="center")
settings_work_color = tk.Label(sidebar, bg=sidebar_color, text=txt.settings_work_color, font=BaseFont(20), fg=Btext_color, anchor="center")
settings_work_color_descr = tk.Label(sidebar, bg=sidebar_color, text=txt.settings_work_color_descr, font=BaseFont(15), fg=Btext_color, anchor="center")
settings_choose_color = tk.Entry(sidebar, width=8, font=("Arial", 32), highlightcolor="#000000")
settings_choose_color.insert(0, "#HEX")
settings_choose_color_btn = tk.Button(sidebar, text=txt.enter, width=6, height=3,fg=Btext_color, bg=button_color, command=utils.enter_color, padx=10)
settings_scale_text = tk.Label(sidebar, bg=sidebar_color, text=txt.settings_scale, font=BaseFont(20), fg=Btext_color, anchor="center")
settings_scale_text_descr = tk.Label(sidebar, bg=sidebar_color, text=txt.settings_scale_descr, font=BaseFont(15), fg=Btext_color, anchor="center")
settings_plus_button = tk.Button(sidebar, text="+", width=10, height=3, font=menu_button_font, command=lambda: utils.scale("+"), bg=button_color, fg=Btext_color)
settings_minus_button = tk.Button(sidebar, text="-", width=10, height=3, font=menu_button_font, command=lambda: utils.scale("-"), bg=button_color, fg=Btext_color)
ru_btn = tk.Button(sidebar, text=txt.settings_rutext, width=10, height=3, font=menu_button_font, command=lambda: choose_lang("ru"), bg=button_color, fg=Btext_color)
en_btn = tk.Button(sidebar, text=txt.settings_entext, width=10, height=3, font=menu_button_font, command=lambda: choose_lang("en"), bg=button_color, fg=Btext_color)
work_color_button = tk.Button(sidebar, text=txt.work_color, width=10, height=3, command=utils.change_work_color, bg=button_color, fg=Btext_color)

# Режим проектирования
design_descr = tk.Label(sidebar, bg=sidebar_color, text=txt.design_descr, font=BaseFont(20), fg=Btext_color)
design_start_btn = tk.Button(sidebar, text=txt.design_start_btn, width=10, height=3, command=thread_dmode, bg=button_color, fg=Btext_color)

