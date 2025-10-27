import config as c

settings = "Настройки"
clear = "Очистить"
last = "Отменить изменение"
rect = "Квадрат"
oval = "Овал"
line = "Линия"
dot = "Точка"
signature = "Подпись"
dash = "Пунктир"
enter = "Ввод"
welcome = "Добро пожаловать в Апофема2D"
settings_lang = "Язык приложения"
settings_lang_descr = "Язык приложения изменится после перезапуска"
settings_rutext = "Русский"
settings_entext = "Английский"
lang_alert = "Язык сменится после перезапуска программы"
settings_work_color = "Цвет фигур"
settings_work_color_descr = "Измените цвет при рисовании"
work_color = "Авто-цвет"
alert_auto_color1 = "Автоматическая смена цветов включена"
alert_auto_color2 = "Автоматическая смена цветов выключена"
user_color_alert = "Автоматическая смена цветов заменена на ваш цвет"
user_color_alert1 = "Некорретный HEX-код"
user_color_alert2 = "Цвет возвращён по умолчанию"
settings_scale = "Масштаб поля"
settings_scale_descr = "Измените размер клеток на поле"
settings_scale_alert = "Изменение масштаба полностью очистит поле. Продолжить?"

def lang(language):
    global settings, clear, last, rect, oval, line, dot, signature, enter, welcome, settings_rutext, settings_entext, settings_lang, dash
    if language == "en":
        settings = "Settings"
        clear = "Clear all"
        last = "Undo changes"
        rect = "Rectangle"
        oval = "Oval"
        line = "Line"
        dot = "Point"
        signature = "Signature"
        dash = "Stipple"
        enter = "Enter"
        welcome = "Welcome to Apothema2D!"
        settings_lang = "Proramm Language"
        settings_rutext = "Russian"
        settings_entext = "English"
    elif language == "ru":
        settings = "Настройки"
        clear = "Очистить"
        last = "Отменить изменение"
        rect = "Квадрат"
        oval = "Овал"
        line = "Линия"
        dot = "Точка"
        signature = "Подпись"
        dash = "Пунктир"
        enter = "Ввод"
        welcome = "Добро пожаловать в Апофема2D"
        settings_lang = "Язык приложения"
        settings_rutext = "Русский"
        settings_entext = "Английский"
        
def langRu():
    global welcome
    lang("ru")
    print(welcome)
    
def langEn():
    global welcome
    lang("en")
    print(welcome)