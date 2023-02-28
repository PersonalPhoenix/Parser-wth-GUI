import tkinter #импорт библиотеки GUI
from tkinter import ttk, Canvas #импорт набора виджетов и графики
import tkinter.filedialog as fd #импорт для указания пути
import requests #импорт запросов для парсинга
from bs4 import BeautifulSoup #импорт для парсинга
import pandas as pd #импорт pandas для DataFrame
import json #импорт для базы данных сохранения состояния переменных
import time #импорт для текущего времени в имени файла
from time import strftime #импорт для часов
import os #импорт для определения пути на ПК
import pygame #импорт для музыки и звуков
from start import version

#Родительский класс / Parent class
class  Main_parser_rus():

    #Список недопустимых варинатов парсинга городов
    zapret = ('Россия','Дальневосточный округ','Крымский федеральный округ','Северо-западный округ','Приволжский округ',
'Северо-Кавказский округ','Сибирский округ','Уралький округ','Центральный округ','Южный округ','Абхазия','Азербайджан',
'Армения','Беларуссия','Бельгия','Германия','Греция','Грузия','Израиль','Испания','Италия','Казахстан','Кипр','Киргизия',
'Китай','Латвия','Литва','Молдова','Монголия','Португалия','США','Таджикистан','Туркменистан','Узбекистан','Укарина','Эстония',
'Сербия','Польша','Великобритания','Турция','Чехия','Корея','Болгария','Вьетнам','Тайвань','Иран','Бенин','Назад','')
    
    #Список стран
    eng_city_main = ('Выбрать город','Россия','Абхазия','Азербайджан','Армения','Беларуссия','Бельгия','Германия','Греция','Грузия','Израиль',
'Испания','Италия','Казахстан','Кипр','Киргизия','Китай','Латвия','Литва','Молдова','Монголия','Португалия','США','Таджикистан','Туркменистан',
'Узбекистан','Укарина','Эстония','Сербия','Польша','Великобритания','Турция','Чехия','Корея','Болгария','Вьетнам','Тайвань','Иран','Бенин')

    #Список округов России
    eng_russia = ('Дальневосточный округ','Крымский федеральный округ','Северо-западный округ','Приволжский округ',
'Северо-Кавказский округ','Сибирский округ','Уралький округ','Центральный округ','Южный округ','Нaзaд')

    #Список городов округа и их id
    eng_city_dal_east = ('Алдан','Амурск','Арсеньев','Артем','Белогорск (Амурская область)','Биробиджан','Благовещенск','Ванино','Владивосток',
'Дальнегорск','Долинск','Елизово','Ковалерово','Комсомольск-на-Амуре','Ленск','Лесозаводск','Магадан','Мирный','Находка','Нерюнгри','Нюрба',
'Петропавловск-Камчатский','Свободный','Советская гавань','Спасск-Дальний','Тында','Уссурийск','Хабаровск','Холмск','Южно-Сахалинск','Якутск',
'Другие города дальневосточного округа','Назад')
    id_dal_east = (41,1203,172,160,176,11,24,595,15,1530,1168,1167,1529,48,240,1528,50,678,161,16,358,85,1166,33,808,219,173,20,1338,156,10,89)

    #Список городов округа и их id
    eng_city_krim = ('Евпатория', 'Керчь', 'Севастополь', 'Симферополь', 'Феодосия', 'Ялта', 'Другие города КФО','Назад')
    id_krim = (1336,1335,1328,1334,1337,1091,1532)
    
    #Список городов округа и их id
    eng_city_n_w = ('Апатиты','Архангельск','Великие Луки','Великий Новгород','Великий Устюг','Вологда','Воркута','Выборг',
'Гатчина','Гурьевск','Инта','Калининград','Кандалакша','Кингисепп','Кириши','Коряжма','Костомукша','Котлас','Ломоносов','Мончегорск',
'Мурманск','Нарьян-Мар','Новодвинск','Петрозаводск','Печора','Псков','Пушкин','Санкт-Петербург','Северодвинск','Сланцы','Сосногорск',
'Сыктывкар','Усинск','Устюжна','Ухта','Череповец','Другие города СЗФО','Назад')
    id_n_w = (1486,166,492,231,613,121,367,823,1075,793,617,152,614,462,600,1069,474,616,764,232,151,902,1068,147,615,153,1170,127,431,637,
    563,143,120,1660,154,169,72)
    
    #Список городов округа и их id
    eng_city_prv = ('Александровск','Альметьевск','Арзамас','Балаково','Балашов','Белебей','Белорецк','Березники','Бор','Бугульма',
'Бугуруслан','Бузулук','Волжск','Володарск','Вольск','Воткинск','Вятские поляны','Глазов','Дзержинск','Димитровград','Елабуга','Жигулевск',
'Заречный','Зеленодольск','Ижевск','Ишимбай','Ешкар-Ола','Казань','Кинель','Киров','Котельнич','Кстово','Кузнецк','Лениногорск',
'Набережные Челны','Нефтекамск','Нижнекамск','Нижний-Новгород','Октябрьск','Оренбург','Орск','Пенза','Пермь','Пугачев','Салават','Самара',
'Саранск','Сарапул','Саратов','Саров','Соликамск','Сорочинск','Стерлитамак','Сызрань','Тольятти','Туймазы','Ульяновск','Уфа','Чайковский',
'Чамзинка','Чебоксары','Энгэльс','Другие города Приволжского федерального округа','Назад')
    id_prv = (699,142,1101,328,330,365,686,1165,1102,683,543,362,679,940,1590,1314,573,566,963,412,237,662,347,546,163,1466,234,235,
    659,148,433,759,709,1242,220,951,1360,134,1356,227,312,129,92,639,1434,184,260,1358,144,945,1359,638,259,477,379,381,149,183,626,
    935,233,1100,90)
        
    #Список городов округа и их id
    eng_city_kavkaz = ('Буденновск','Владикавказ','Георгиевск','Грозный','Дербент','Ессентуки','Железноводск',
'Кисловодск','Махачкала','Минеральные Воды','Назрань','Нальчик','Невинномысск','Пятигорск','Ставрополь','Хасавюрт','Другие города СКФО','Назад')
    id_kavkaz = (725,674,1135,441,541,618,1145,396,675,1143,979,250,164,634,257,933,635)
    
    #Список городов округа и их id
    eng_city_sibir = ('Абакан','Агинское','Ангарск','Анжеро-Судженск','Ачинск','Барнаул','Булово','Бердск','Бийск','Боготол','Бодайбо',
'Братск','Горно- Алтайск','Дудинка','Железногорск','Иркутск','Камень-на-Оби','Канск','Кемерово','Краснокаменск',
'Красноярск','Куйбышев','Кызыл','Ленинск-Кузнецкий','Междуреченск','Нижнеудинск','Новоалтайск','Новокузнецк','Новосибирск','Норильск',
'Омск','Первомайск','Прокопьевск','Рубцовск','Северобайкальск','Томск','Тулун','Улан-Удэ','Усолье-Сибирское','Усть-Илимск','Усть-Кут',
'Чита','Шилка','Юрга','Другие города СФО','Назад')
    id_sibir = (5,459,103,399,102,26,612,751,46,948,238,43,619,653,1017,18,248,179,3,99,4,1099,178,175,949,249,989,25,2,94,34,218,91,1105,
    14,44,247,12,246,145,159,13,799,177,84)
    
    #Список городов округа и их id
    eng_city_ural = ('Богданович','Верхняя Пышма','Екатеринбург','Заводоуковск','Златоуст','Ишим',
    'Каменск-Уральский','Камышлов','Красноуральск','Курган','Куса','Кыштым','Лабытнанги','Магнитогорск','Мегион','Миасс','Надым',
    'Nefteyugansk','Нижневартовск','Нижний Тагил','Новый Уренгой','Ноябрьск','Нягань','Первоуральск','Пыть-Ях','Дир','Салехард','Серов',
    'Среднеуральск','Сургут','Тобольск','Троицк (Челябинская область)','Туринск','Тюмень','Увельский','Урай','Уринск','Учалы','Ханты-Мансийск',
    'Челябинск','Шадринск','Югорск','Южноуральск','Другие города УФО','Назад')
    id_ural = (390,1158,52,700,545,222,408,1161,434,185,553,1609,784,223,950,1185,1162,1107,93,221,482,1156,783,1020,1157,1038,849,769,1057,
    155,224,1131,162,1130,1155,1159,1492,785,51,812,1108,1129,86)
    
    #Список городов округа и их id
    eng_city_tcentral = ('Александров','Белгород','Бобров','Борисоглебск','Боровск','Брянск','Владимир','Волгореченск','Воронеж','Воскресенск',
'Вязники','Вязма','Гусь-Хрустальный','Дедовск','Дмитров','Долгопрудный','Домодедово','Елецк','Железнодорожный','Жуковский',
'Зеленоград','Иваново','Ивантеевка','Истра','Калуга','Кашира','Киреевск','Климовск','Клин','Клинцы','Ковры','Коломна','Королев','Кострома',
'Красногорск','Кунцево','Курск','Ливни','Липецк','Лобня','Лыткарино','Люберцы','Мичуринск','Москва','Муром','Мытищи','Наро-Фоминск',
'Новомосковск','Ногинск','Обнинск','Одинцово','Орел','Орехово-Зуево','Павловский Посад','Погар','Подольск','Пушкишо','Раменское','Реутов',
'Ростов','Рыбинск','Рязань','Сафоново','Сергиев-Посад','Серпухов','Смоленск','Солнечногорск','Старый Оскол','Ступино','Тамбов','Тверь','Тула',
'Углич','Furmanov','Химки','Чехов','Щелково','Электрогорск','Электросталь','Ярославль','Другие города ЦФО','Назад')
    id_tcentral = (581,98,847,457,460,174,96,704,100,1631,955,436,815,743,564,657,589,522,777,667,814,111,557,393,171,1132,646,663,395,
    1194,446,400,450,105,1015,536,167,1495,165,1150,1465,320,1033,118,658,765,230,517,370,351,609,170,610,1149,1431,1151,883,718,608,1053,
    229,122,1672,168,242,239,1879,1025,1022,128,119,117,606,1643,559,607,605,1032,463,104,67)
    
    #Список городов округа fи их id
    eng_city_ug = ('Абинск', 'Азов', 'Анапа', 'Апшеронск', 'Армавир', 'Астрахань', 'Ахтубинск', 'Батайск', 'Белогорск (Крым)', 'Белореченск',
'Волгоград', 'Волгодонск', 'Волжский', 'Геленджик','Гуково', 'Гулькевичи','Ейск','Каменск-Шахтинский', 'Котово', 'Краснодар', 'Крымск', 
'Курганинск', 'Лабинск', 'Майкоп', 'Миллерово', 'Новороссийск','Новочеркасск','Ростов-на-Дону','Salsk','Сочи','Starominskaya','Таганрог',
'Темрюк','Тимашевск','Тихорецк','Туапсе','Усть-Лабинск','Черкесск','Шахты','Элиста','Другие города Южного федерального округа','Назад')
    id_ug = (756,532,590,1137,150,409,1140,643,1354,1063,139,391,631,253,1138,1133,251,1139,511,135,685,1136,1061,256,1052,252,632,125,
    1060,146,760,418,952,1142,1062,1144,1134,254,461,422,158)
    
    #Список городов Абхазии и их id 
    eng_city_abhazia = ("Сухуми","Другие города Азербайджана","Назад")
    id_abhazia = (205,206)
    
    #Список городов Азербайджана и их id 
    eng_city_azerbaizhdan = ("Баку","Другие города Азербайджана","Назад")
    id_azerbaizhan = (190,191)
    
    #Список городов Армении и их id 
    eng_city_armenia = ("Ереван","Другие города Армении","Назад")
    id_armenia = (209,210)
    
    #Список городов Беларусии и их id 
    eng_city_WR = ('Барановичи','Бобруйск','Борисов','Брест','Витебск','Гомель','Горки','Гродно',
'Лида','Минск','Могилев','Полоцк','Рогачев','Другие города Беларуссии','Назад')
    id_WR = (627,300,755,629,186,628,753,349,445,181,384,187,258,182)
    
    #Список городов Бельгии и их id 
    eng_city_belghuem = ('Антверпен','Другие города Бельгии','Назад')
    id_belghuem = (357,744)
    
    #Список городов Германии и их id 
    eng_city_german = ('Кельн','Штутгарт','Другие города Германии','Назад')
    id_german = (1425,722,236)
    
    #Список городов Греции и их id 
    eng_city_grec = ('Афины','Другие города Греции','Назад')
    id_grec = (1490,1491)

    #Список городов Грузии и их id 
    eng_city_gruzia = ('Тбилиси','Другие города Грузии','Назад')
    id_gruzia = (207,208)

    #Список городов Израиля и их id 
    eng_city_izrail = ('Ашод','Беэр-Шева','Ремез','Тель-Авив','Ходера','Другие города Израиля','Назад')
    id_izrail = (344,360,211,470,212,213)

    #Список городов Испании и их id 
    eng_city_ispania =('Кадис','Уренсе','Другие города Испании','Назад')
    id_ispania = (376,724,747)

    #Список городов Италии и их id 
    eng_city_italy = ('Маранелло','Милан','Римини','Другие города Италии','Назад')
    id_italy = (261,1445,1414,748)

    #Список городов Казахстана и их id 
    eng_city_kazahstan = ('Актау', 'Актобе', 'Алматы', 'Астана', 'Атырау',  'Жезказаган', 'Караганда', 'Кокшетау',
'Костанай', 'Кызылорда', 'Павлодар', 'Петропавловск', 'Рудный','Семей', 'Семипалатинск', 'Тараз', 'Уральск', 'Усть - Каменогорск', 'Шымкент',
 'Другие города Казахстана','Назад')
    id_kazahstan = (649,644,131,141,303,1554,137,651,540,729,133,267,648,1461,650,660,217,647,762,132)

    #Список городов Кипра и их id 
    eng_city_kipr = ('','Назад')
    id_kipr = ('')

    #Список городов Киргизии и их id 
    eng_city_kirgiz = ('Бишкек','Другие города Киргизии','Назад')
    id_kirgiz = (542,767)

    #Список городов Китая и их id 
    eng_city_chine = ('Гонконг','Далянь','Пекин','Другие города Китая','Назад')
    id_chine = (1605,840,838,839)

    #Список городов Латвии и их id 
    eng_city_latvia = ('Рига','Другие города Латвии','Назад')
    id_latvia = (201,202)

    #Список городов Литвы и их id 
    eng_city_litva = ('Вильнос','Клайпеда','Другие города Литвы','Назад')
    id_litva = (354,214,215)

    #Список городов Молдовы и их id 
    eng_city_moldova = ('Бельцы','Кишенев','Другие города Молдовы','Назад')
    id_moldova = (525,199,200)

    #Список городов Монголии и их id 
    eng_city_mongolia = ('Улан-батор','Другие города Монголии','Назад')
    id_mongolia = (244,245)

    #Список городов Португалии и их id 
    eng_city_port = ('','Назад')
    id_port = ('')

    #Список городов США и их id 
    eng_city_usa = ('Нью-Йорк','Другие города США','Назад')
    id_usa = (885,886)

    #Список городов Таджикистана и их id 
    eng_city_tadzhstan = ('Душанбэ','Ленинопад','Худжанд','Другие города Таджикистана','Назад')
    id_tadzhstan = (192,193,954,194)

    #Список городов Туркменистана и их id
    eng_city_turkman = ('Ашхабат','Другие города Туркменистана','Назад')
    id_turkman = (188,189)

    #Список городов Узбекистана и их id 
    eng_city_uzbkst = ('Бишкек','Ташкент','Другие города Узбекистана','Назад')
    id_uzbkst = (1458,827,216)

    #Список городов Украины и их id 
    eng_city_ukrain = ('Винница','Днепропетровск','Донецк','Житомир','Запорожье','Исмаил','Киев','Кировоград',
 'Кременчуг','Луцк','Львов','Мариуполь','Мелитополь','Одесса','Полтава','Ровно','Сумы','Харьков','Чернигов','Другие города Украины','Назад')
    id_ukrain = (623,196,568,622,624,1092,455,620,1550,424,621,382,625,197,544,1289,539,195,1090,198)

    #Список городов Эстонии и их id 
    eng_city_estonia = ('Таллин','Другие города Эстонии','Назад')
    id_estonia =(203,204)

    #Список городов Сербии и их id 
    eng_city_serbia = ('Белград','Другие города Сербии','Назад')
    id_serbia = (1064,1065)

    #Список городов Польши и их id 
    eng_city_poland = ('Варшава','Вроцлав','Кельце','Краков','Другие города Польши','Назад')
    id_poland = (1238,1629,1627,1239,1240)

    #Список городов Великобритании и их id 
    eng_city_great_br = ('Бирмингем','Глазго','Ливерпуль','Лондон','Манчестер','Эдинбург','Другие города Великобритании','Назад')
    id_great_br = (1244,1245,1248,1243,1246,1247,1249)

    #Список городов Турции и их id 
    eng_city_turkchis = ('Стамбул','Другие города Турции','Назад')
    id_turkchis = (1290,1291)

    #Список городов Чехии и их id 
    eng_city_chexzia = ('Нимбурк','Прага','Другие города Чехии','Назад')
    id_chexzia = (1368,1365,1366)

    #Список городов Кореи и их id 
    eng_city_korea = ('Сеул','Назад')
    id_korea = (1448)

    #Список городов Болгарии и их id 
    eng_city_bolgaria = ('Бургас','Варна','Добрич','Плевен','Пловдив','Русе','Сливен',
'София','Стара-Загора','Шумен','Другие города Болгарии','Назад')
    id_bolgaria = (1511,1510,1515,1514,1509,1512,1516,1508,1513,1517,1518)

    #Список городов Вьетнама и их id 
    eng_city_vietham = ('Ханой','Хошимин','Другие города Вьетнама','Назад')
    id_vietham = (1606,1607,1608)

    #Список городов Тайваня и их id 
    eng_city_taiwan = ('Синьбэй','Тайбэй','Другие города Тайваня','Назад')
    id_taiwan = (1633,1632,1634)

    #Список городов Ирана и их id 
    eng_city_iran = ('Тегеран','Другие города Ирана','Назад')
    id_iran = (1689,1690)

    #Список городов Бенина и их id 
    eng_city_benin = ('Котону','Порто-Ново','Другие города Бенина','Назад')
    id_benin = (1823,1822,1824)

    #Список структур компании и их id 
    eng_company = ('Структура компании','Оптовик', 'Дистрибьютер', 'Комерческий логист', 'Розница', 'Производитель', 
 'Вендинговые автоматы', 'Импортер')
    id_s_c = ('all','opt','distr','comlog','rozn','proiz','vend','import')

    #Для сопостовления города и id
    lol = ()

    #Основное окно приложения
    win = tkinter.Tk()

    #Кнопка вкл звук темной темы
    on_dark = tkinter.PhotoImage(file='icons/zvuk.png')
    #Кнопка выкл звук темной темы
    off_dark = tkinter.PhotoImage(file='icons/zvuk_off.png')
    #Кнопка вкл звук светлой темы
    on_light = tkinter.PhotoImage(file='icons/zvuk_light.png')
    #Кнопка выкл звук светлой темы
    off_light = tkinter.PhotoImage(file='icons/zvuk_off_light.png')

    #Инициализируем музыку и звуковой эффект нажатия кнопок
    is_on = True 
    pygame.mixer.pre_init(44100, -16, 1, 512) 
    pygame.mixer.init()
    s_button = pygame.mixer.Sound('Sound/Button.mp3') 
    s_button.set_volume(0.25) 
    s_error = pygame.mixer.Sound('Sound/error.mp3') 
    s_error.set_volume(0.5) 
    pygame.mixer.music.load('Sound/Main-theme.mp3')
    pygame.mixer.music.set_volume(0.3) 
    pygame.mixer.music.play(loops=-1) 

    #Считываем положение главного окна
    x = win.winfo_x()
    y = win.winfo_y()
    
    #Переменная для парсинга данных в виде DataFrame
    df = pd.DataFrame
  
    #Словарь для сохранения пути сохранения файла
    save = {}

    #Список для спаршенной информации
    catalog = []

    #Переменная выбора города
    eng_selection_main = 'Выбрать город'

    #Переменная текущего времени для даты в названии файла
    timestr = time.strftime("%Y-%m-%d %H-%M-%S") 
    vrema = timestr

    #Переменная выбора формата имени файла для сохранения (с датой/без даты)
    yes_not = False

    #Переменная выбора формата файла для сохранения
    format = 'Excel'

    #Переменная для перевода структуры компании в буквы для url
    value_cstr_comp = 'all'

    #переменная для указания пути
    put_save = r'C:\Users\applm\OneDrive\Рабочий стол\Parser с DataFrame\Parser\save.json'

    #для перевода города в цифру для url
    value_city = 0

    #Для сохранения темы
    if 'theme.json': 
        try: 
            with open ('theme.json','r',encoding='utf-8') as f:
                theme = json.load(f)
                if theme == '#18181a':
                    icon = on_dark
                    ok = '#18181a'
                else:
                    icon = on_light
                    ok = '#fdfff5'
        except: 
            theme = '#18181a'
            icon = on_dark
            ok = '#18181a'

    #Для указания пути сохранения
    if put_save: 
        try:  
            with open ('save.json','r',encoding='utf-8') as f:
                gruz = json.load(f)
                directory = gruz['Путь']
        except: 
            directory = os.getcwd()

    #Музыка
    def zvuk(self): 
        Main_parser_rus.s_button.play() 
        if Main_parser_rus.theme == '#18181a': 
            if Main_parser_rus.is_on: 
                self.Sound.config(image = Main_parser_rus.off_dark,background='#18181a') 
                Main_parser_rus.is_on = False
                pygame.mixer.music.pause() 
            else: 
                self.Sound.config(image = Main_parser_rus.on_dark,background='#18181a')
                Main_parser_rus.is_on = True
                pygame.mixer.music.unpause()
        else: 
            if Main_parser_rus.is_on: 
                self.Sound.config(image = Main_parser_rus.off_light,background='#fdfff5') 
                Main_parser_rus.is_on = False
                pygame.mixer.music.pause()
            else: 
                self.Sound.config(image = Main_parser_rus.on_light,background='#fdfff5')
                Main_parser_rus.is_on = True
                pygame.mixer.music.unpause()

    #Окно завершения работы программы
    def WindowEnd(self):
        def exit(): 
            Main_parser_rus.s_button.play() 
            time.sleep(0.1) 
            end.destroy() 
        end = tkinter.Toplevel() 
        end.title('Работа закончена') 
        end.geometry(f'250x150+{Main_parser_rus.x+640}+{Main_parser_rus.y+290}') 
        end.resizable(False,False) 
        icons1 = tkinter.PhotoImage(file='icons/info.png') 
        end.wm_iconphoto(False,icons1) 
        canvas = Canvas(end, width=310,height=100) 
        canvas.place(x=-10,y=100) 
        canvas.create_rectangle(0,0,310,100,fill='#18181a') 
        canvas1 = Canvas(end, width=310,height=100) 
        canvas1.place(x=-10,y=0) 
        canvas1.create_rectangle(0,0,310,50,fill='#18181a')
        Labrl1 = tkinter.Label(end, text= 'Сделано!',font='arial 14') 
        Labrl1.place(x=93,y=63) 
        Labrl2 = tkinter.Label(end, text= 'Copyright © 2023 П.В. Маршанский',font='arial 9',background='#18181a',foreground='#fdfff5') 
        Labrl2.place(x=29,y=16)
        tkinter.Button(end, text="окей",font='arial 12', command=exit).place(x=100,y=110) 
    
    #Окно информации о копирайте
    def WindowCopyRight (self):
        def copy(): 
            Main_parser_rus.s_button.play() 
            time.sleep(0.1) 
            copyright.destroy()
        copyright = tkinter.Toplevel() 
        copyright.title('Окно справки')
        copyright.geometry(f'580x370+{Main_parser_rus.x+475}+{Main_parser_rus.y+130}')
        copyright.resizable(False,False) 
        canvas = Canvas(copyright, width=590,height=280) 
        canvas.place(x=-10,y=295) 
        canvas.create_rectangle(0,0,590,280,fill='#18181a') 
        canvas1 = Canvas(copyright, width=590,height=280) 
        canvas1.place(x=-10,y=0) 
        canvas1.create_rectangle(0,0,590,75,fill='#18181a') 
        icons2 = tkinter.PhotoImage(file='icons/info.png')
        copyright.wm_iconphoto(False,icons2) 
        Label1 = tkinter.Label(copyright,text='Copyright © 2023 П.В. Маршанский',font='arial 12',background='#18181a',foreground='#fdfff5') 
        Label1.place(x=157,y=27) 
        Label2 = tkinter.Label(copyright, text=f'''
Все права защищены. Никакая часть этого алгоритма не может быть воспроизведена,
распространена или передана в любой форме или любыми средствами,
включая фотокопирование, запись или другие электронные или механические методы,
без предварительного письменного разрешения создателя, за исключением кратких ссылок, 
содержащихся в письменной или устной форме, и некоторых других
некоммерческих целей, разрешенных закон об авторском праве.
Чтобы получать запросы на разрешение, напишите создателю по указанному ниже адресу:
Mail:
applmacter@mail.ru
Telegram:
https://t.me/marshansky (@marshansky)''',font='arial 9') 
        Label2.place(x=69,y=86) 
        tkinter.Button(copyright, text="okey",font='arial 12', width=10,command=copy).place(x=237,y=317) 

    #Уведомление о пользовательском соглашении
    def soglahenie(self):
        def sogl(): 
            Main_parser_rus.s_button.play() 
            time.sleep(0.1) 
            soglasie.destroy() 
        soglasie = tkinter.Toplevel() 
        soglasie.title('Окно справки') #
        soglasie.geometry(f'380x150+{Main_parser_rus.x+580}+{Main_parser_rus.y+190}') 
        soglasie.resizable(False,False) 
        canvas = Canvas(soglasie, width=390,height=160) 
        canvas.place(x=-10,y=0) 
        canvas.create_rectangle(0,0,390,50,fill='#18181a') 
        canvas1 = Canvas(soglasie, width=390,height=160) 
        canvas1.place(x=-10,y=100) 
        canvas1.create_rectangle(0,0,390,150,fill='#18181a') 
        icons2 = tkinter.PhotoImage(file='icons/hand.png') 
        soglasie.wm_iconphoto(False,icons2)
        Label1 = tkinter.Label(soglasie,text='''Используя это приложение, вы соглашаетесь с "Пользовательским соглашением". 
См. приложение 2''',font='arial 9') 
        Label1.place(x=10,y=58)
        Label2 = tkinter.Label(soglasie,text='Copyright © 2023 П.В. Маршанский',font='arial 9',foreground='#fdfff5',background='#18181a') 
        Label2.place(x=90,y=17) 
        tkinter.Button(soglasie,text="окей",font='arial 12',command=sogl, width=7).place(x=160,y=112) 

    #Уведомление о руководстве пользования
    def ruk(self):
        def rik(): 
            Main_parser_rus.s_button.play() 
            time.sleep(0.1) 
            ruko.destroy()
        ruko = tkinter.Toplevel() 
        ruko.title('Окно справки') 
        ruko.geometry(f'380x150+{Main_parser_rus.x+580}+{Main_parser_rus.y+190}') 
        ruko.resizable(False,False) 
        canvas = Canvas(ruko, width=390,height=160) 
        canvas.place(x=-10,y=0) 
        canvas.create_rectangle(0,0,390,50,fill='#18181a') 
        canvas1 = Canvas(ruko,width=390,height=160) 
        canvas1.place(x=-10,y=100)
        canvas1.create_rectangle(0,0,390,150,fill='#18181a') 
        icons2 = tkinter.PhotoImage(file='icons/hand.png') 
        ruko.wm_iconphoto(False,icons2) 
        Label1 = tkinter.Label(ruko,text='К этому приложению прилагается Руководство пользователя (см. Приложение 1)',font='arial 10') 
        Label1.place(x=10,y=65)
        Label2 = tkinter.Label(ruko,text='Copyright © 2023 П.В. Маршанский',font='arial 9',foreground='#fdfff5',background='#18181a') 
        Label2.place(x=90,y=17)
        tkinter.Button(ruko,text="окей",font='arial 12',command=rik, width=7).place(x=160,y=112) 
    
    #Окно уведомления об изменении пути сохранения файла
    def path(self):
        def pith(): 
            Main_parser_rus.s_button.play() 
            time.sleep(0.1) 
            put.destroy() 
        put = tkinter.Toplevel() 
        put.title('Изменение пути') 
        put.geometry(f'300x150+{Main_parser_rus.x+610}+{Main_parser_rus.y+190}') 
        put.resizable(False,False) 
        canvas = Canvas(put, width=390,height=160) 
        canvas.place(x=-10,y=0)
        canvas.create_rectangle(0,0,390,50,fill='#18181a') 
        canvas1 = Canvas(put,width=390,height=160)
        canvas1.place(x=-10,y=100) 
        canvas1.create_rectangle(0,0,390,150,fill='#18181a') 
        icons2 = tkinter.PhotoImage(file='icons/hand.png') 
        put.wm_iconphoto(False,icons2) 
        Label1 = tkinter.Label(put,text=f'Теперь файлы будут сохранены в: \n {Main_parser_rus.directory}',font='arial 10') 
        Label1.pack(side='top',pady=60) 
        tkinter.Button(put,text="окей",font='arial 12',command=pith, width=7).place(x=120,y=110)  

    #Окно вопроса о закрытии программы
    def WindowClose (self):
        def not_exit(): 
            Main_parser_rus.s_button.play() 
            time.sleep(0.1) 
            close.destroy() 
        close = tkinter.Toplevel() 
        close.title('Выход') 
        close.geometry(f'300x150+{Main_parser_rus.x+610}+{Main_parser_rus.y+180}') 
        close.resizable(False,False) 
        icons1 = tkinter.PhotoImage(file='icons/quit.png') 
        close.wm_iconphoto(False,icons1) 
        canvas = Canvas(close, width=310,height=100) 
        canvas.place(x=-10,y=100) 
        canvas.create_rectangle(0,0,310,100,fill='#18181a') 
        canvas1 = Canvas(close, width=310,height=100) 
        canvas1.place(x=-10,y=0) 
        canvas1.create_rectangle(0,0,310,50,fill='#18181a') 
        Label1 = tkinter.Label(close, text= 'Вы уверены, что хотите выйти?',font='arial 14',foreground='red')
        Label1.place(x=22,y=63) 
        Label1 = tkinter.Label(close, text= 'Copyright © 2023 П.В. Маршанский',font='arial 9',foreground='#fdfff5',bg='#18181a') 
        Label1.place(x=55,y=17) 
        Okey = tkinter.Button(close, text="окей",font='arial 12',command=self.yes_exit, width=6) 
        Okey.place(x=82,y=110)
        Cancel = tkinter.Button(close, text="отмена",font='arial 12',command=not_exit) 
        Cancel.place(x=167,y=110) 

    #Функция подтверждения закрытия программы
    def yes_exit(self):
        Main_parser_rus.s_button.play() 
        time.sleep(0.1) 
        Main_parser_rus.win.destroy() 

    #Окно ошибки неверно выбранного города для парсинга
    def error_city (self):
        Main_parser_rus.s_error.play()
        def irror_city(): 
            Main_parser_rus.s_button.play() 
            time.sleep(0.1) 
            error.destroy() 
        error = tkinter.Toplevel() 
        error.title('ОШИБКА') 
        error.geometry(f'300x150+{Main_parser_rus.x+610}+{Main_parser_rus.y+190}') 
        error.resizable(False,False) 
        canvas = Canvas(error, width=390,height=160)
        canvas.place(x=-10,y=0)
        canvas.create_rectangle(0,0,390,50,fill='#18181a') 
        canvas1 = Canvas(error,width=390,height=160) 
        canvas1.place(x=-10,y=100) 
        canvas1.create_rectangle(0,0,390,150,fill='#18181a') 
        icons2 = tkinter.PhotoImage(file='icons/hand.png') 
        error.wm_iconphoto(False,icons2)
        Label1 = tkinter.Label(error,text=f'{Main_parser_rus.selection_main} недопустимое значение города',font='arial 14',foreground='red') 
        Label1.pack(side='top',pady=60) 
        tkinter.Button(error,text="окей",font='arial 12',command=irror_city, width=7).place(x=110,y=110)
    
    #Окно ошибки при отсутсвтии интернета/сайт не доступен
    def error_inet (self):
        Main_parser_rus.s_error.play()
        def irror_inet(): 
            Main_parser_rus.s_button.play() 
            time.sleep(0.1) 
            error.destroy() 
        error = tkinter.Toplevel() 
        error.title('ОШИБКА')
        error.geometry(f'300x150+{Main_parser_rus.x+610}+{Main_parser_rus.y+190}')
        error.resizable(False,False)
        canvas = Canvas(error, width=390,height=160)
        canvas.place(x=-10,y=0)
        canvas.create_rectangle(0,0,390,50,fill='#18181a')
        canvas1 = Canvas(error,width=390,height=160)
        canvas1.place(x=-10,y=100) 
        canvas1.create_rectangle(0,0,390,150,fill='#18181a')
        icons2 = tkinter.PhotoImage(file='icons/hand.png')
        error.wm_iconphoto(False,icons2)
        Label1 = tkinter.Label(error,text=f'Сайт временно недоступен:( \nПопробуйте позже ',font='arial 12',foreground='red')
        Label1.pack(side='top',pady=60)
        Label2 = tkinter.Label(error,text=f'Также убедитесь, что у вас есть подключение к интернету',font='arial 10',foreground='red',background='#18181a')
        Label2.place(x=5,y=17)
        tkinter.Button(error,text="окей",font='arial 12',command=irror_inet, width=7).place(x=120,y=110)

    #Функция GUI основного окна приложения
    def GUI(self):
        
        #Заголовок основного окна
        Main_parser_rus.win.title("Панель управления") 

        #Главное меню
        menubar = tkinter.Menu(self.win) 
        self.win.config(menu=menubar)

        #Пункт меню Вид
        settings_vid = tkinter.Menu(menubar,tearoff=0) 

        #Пункт меню Обновление
        settings_obnova = tkinter.Menu(menubar,tearoff=0) 

        #Пункт меню Файл
        settings_menu = tkinter.Menu(menubar,tearoff=0) 

        #Пункт меню Справка
        settings_sprvk = tkinter.Menu(menubar,tearoff=0)    

        #Подпункты меню 1)Язык и 2)Тема
        settings_vid2 = tkinter.Menu(settings_vid,tearoff=0) #1)
        settings_vid3 = tkinter.Menu(settings_vid,tearoff=0) #2)

        #Пункт меню Файл
        settings_menu.add_command(label='Перезагрузить',command=self.reload) 
        settings_menu.add_command(label='Указать путь',command=self.put_file) 
        settings_menu.add_separator() 
        settings_menu.add_command(label='Выход',command=self.win.destroy, activebackground = 'red') 
        menubar.add_cascade(label='Файл', menu=settings_menu) 

        #Подпункт меню Вид, Тема
        settings_vid.add_cascade(label='Тема',menu=settings_vid3) 
        settings_vid3.add_radiobutton(label='Темная',command=self.dark_theme) 
        settings_vid3.add_radiobutton(label='Светлая',command=self.light_theme) 

        #Подпункт меню Вид, Язык
        settings_vid.add_cascade(label='Язык', menu=settings_vid2) 
        settings_vid2.add_command(label='Русский (Russian)') 
        settings_vid2.add_command(label='English (Английский)',command=self.versia_eng)

        #Пункт меню Вид 
        menubar.add_cascade(label='Вид', menu=settings_vid) 

        #Пункт меню Справка 
        settings_sprvk.add_command(label='Руковоство пользования',command=self.ruk) 
        settings_sprvk.add_command(label='Copyright',command=self.WindowCopyRight) 
        settings_sprvk.add_command(label='Пользовательское соглашение',command=self.soglahenie) 
        menubar.add_cascade(label='Справка', menu=settings_sprvk) 

        #Пункт меню Обновление 
        settings_obnova.add_command(label='Обновить страны') 
        settings_obnova.add_command(label='Обновить города') 
        menubar.add_cascade(label ='Обновление', menu=settings_obnova) 
        
        #Размеры + начальное расположение основного окна 
        screen_width = Main_parser_rus.win.winfo_screenwidth() 
        screen_width2 = screen_width//2 - 280 
        screen_height = Main_parser_rus.win.winfo_screenheight() 
        screen_height2 = screen_height//2 - 300 
        Main_parser_rus.win.geometry(f'560x350+{screen_width2}+{screen_height2}') 
        Main_parser_rus.win.minsize(560,350)
        Main_parser_rus.win.resizable(False,False)

        #Иконка главного окна 
        icons = tkinter.PhotoImage(file='icons/chain.png')
        Main_parser_rus.win.wm_iconphoto(False,icons) 
        
        #Кнопка запуска 
        self.btn_start = tkinter.Button(Main_parser_rus.win,text='Запустить программу',font='arial 16',command=self.parse) 
        self.btn_start.place(x=165,y=225) 
        
        #Удаление фокуса с выбранного элемента в списке 
        def defocus(event):
            Main_parser_rus.s_button.play() 
            event.widget.master.focus_set() 

        #Список городов / List of cities
        self.spisok_main = ttk.Combobox(Main_parser_rus.win,values=Main_parser_rus.eng_city_main,font='arial 14',state="readonly",cursor='hand2') 
        self.spisok_main.current('0') 
        self.spisok_main.config(cursor="hand2") 
        self.spisok_main.place(x=15,y=15) 
        self.spisok_main.bind('<<ComboboxSelected>>',self.selected_city) 
        self.spisok_main.bind("<FocusIn>", defocus) 

        #Список структур компаний 
        self.spisok_comp = ttk.Combobox(Main_parser_rus.win,values=Main_parser_rus.eng_company,font='arial 14',state="readonly")
        self.spisok_comp.current('0')
        self.spisok_comp.config(cursor="hand2")
        self.spisok_comp.place(x = 300, y = 15)
        self.spisok_comp.bind('<<ComboboxSelected>>',self.selected_str)
        self.spisok_comp.bind("<FocusIn>", defocus)

        #Список формата имени файла 
        self.sp_time = ttk.Combobox(Main_parser_rus.win,values=['Без даты','С датой'],font='arial 14',state="readonly")
        self.sp_time.current('0') 
        self.sp_time.config(cursor="hand2") 
        self.sp_time.place(x=300,y=96.5) 
        self.sp_time.bind('<<ComboboxSelected>>',self.selected_time) 
        self.sp_time.bind("<FocusIn>", defocus) 

        #Список форматов сохранения файла 
        self.sp_format = ttk.Combobox(Main_parser_rus.win,values=['Excel','CSV','TXT'],font='arial 14',state="readonly") 
        self.sp_format.current('0') 
        self.sp_format.config(cursor="hand2") 
        self.sp_format.place(x=15,y=96.5) 
        self.sp_format.bind('<<ComboboxSelected>>',self.selected_format) 
        self.sp_format.bind("<FocusIn>", defocus) 

    #Часы и дата в главном окне 
    def chasi (self):
        if Main_parser_rus.theme == '#fdfff5': 
            Clock = tkinter.Label(Main_parser_rus.win,text='' ,font=('arial', 12),background='#fdfff5', foreground='#18181a')
            Clock.place(x=10,y=315) 
            Clock1 = tkinter.Label(Main_parser_rus.win,text='' ,font=('arial', 12), background='#fdfff5', foreground='#18181a')
            Clock1.place(x=465,y=315) 
        else:
            Clock = tkinter.Label(Main_parser_rus.win,text='' ,font=('arial', 12),background='#18181a', foreground='#fdfff5')
            Clock.place(x=10,y=315)
            Clock1 = tkinter.Label(Main_parser_rus.win,text='' ,font=('arial', 12), background='#18181a', foreground='#fdfff5') 
            Clock1.place(x=465,y=315)
        string_time = strftime('''%H:%M:%S''')
        string_data = strftime('''%d.%m.%Y''') 
        Clock.config(text=string_time) 
        Clock.after(1000, self.chasi) 
        Clock1.config(text=string_data) 
        Clock1.after(60000, self.chasi)
    
    #Кнопка паузы/анпаузы музыки 
    def knopka_zvuka(self): 
        self.Sound = tkinter.Button(Main_parser_rus.win,image=Main_parser_rus.icon,background=Main_parser_rus.ok,command=self.zvuk)
        self.Sound.place(x=15,y=280) 
    
    #Установка начальной темы главного окна 
        if Main_parser_rus.theme == '#fdfff5':
            self.light_theme()
        else: 
            self.dark_theme()

    #Функция определения выбранног города с конвертацией в id для url 
    def selected_city(self,event):
        Main_parser_rus.selection_main = self.spisok_main.get()
        Main_parser_rus.s_button.play()
        
        if Main_parser_rus.selection_main == 'Выбрать город':
            Main_parser_rus.value_city = 0

        if Main_parser_rus.selection_main == 'Россия':
            self.spisok_main['values'] = Main_parser_rus.eng_russia

        if Main_parser_rus.selection_main == 'Дальневосточный округ':
            self.spisok_main['values'] = Main_parser_rus.eng_city_dal_east
            Main_parser_rus.lol = Main_parser_rus.id_dal_east

        if Main_parser_rus.selection_main == 'Крымский федеральный округ':
            self.spisok_main['values'] = Main_parser_rus.eng_city_krim
            Main_parser_rus.lol = Main_parser_rus.id_krim

        if Main_parser_rus.selection_main == 'Северо-Западный округ':
            self.spisok_main['values'] = Main_parser_rus.eng_city_n_w
            Main_parser_rus.lol = Main_parser_rus.id_n_w

        if Main_parser_rus.selection_main == 'Приволжский округ':
            self.spisok_main['values'] = Main_parser_rus.eng_city_prv
            Main_parser_rus.lol = Main_parser_rus.id_prv

        if Main_parser_rus.selection_main == 'Северо-Кавказкий округ':
            self.spisok_main['values'] = Main_parser_rus.eng_city_kavkaz
            Main_parser_rus.lol = Main_parser_rus.id_kavkaz

        if Main_parser_rus.selection_main == 'Сибирский округ':
            self.spisok_main['values'] = Main_parser_rus.eng_city_sibir
            Main_parser_rus.lol = Main_parser_rus.id_sibir

        if Main_parser_rus.selection_main == 'Уральский округ':
            self.spisok_main['values'] = Main_parser_rus.eng_city_ural
            Main_parser_rus.lol = Main_parser_rus.id_ural

        if Main_parser_rus.selection_main == 'Центральный округ':
            self.spisok_main['values'] = Main_parser_rus.eng_city_tcentral
            Main_parser_rus.lol = Main_parser_rus.id_tcentral

        if Main_parser_rus.selection_main == 'Южный округ':
            self.spisok_main['values'] = Main_parser_rus.eng_city_ug
            Main_parser_rus.lol = Main_parser_rus.id_s_c

        if Main_parser_rus.selection_main == 'Абхазия':
            self.spisok_main['values'] = Main_parser_rus.eng_city_abhazia
            Main_parser_rus.lol = Main_parser_rus.id_abhazia

        if Main_parser_rus.selection_main == 'Азербайджан':
            self.spisok_main['values'] = Main_parser_rus.eng_city_azerbaizhdan
            Main_parser_rus.lol = Main_parser_rus.id_azerbaizhan

        if Main_parser_rus.selection_main == 'Армения':
            self.spisok_main['values'] = Main_parser_rus.eng_city_armenia
            Main_parser_rus.lol = Main_parser_rus.id_armenia

        if Main_parser_rus.selection_main == 'Беларуссия':
            self.spisok_main['values'] = Main_parser_rus.eng_city_WR
            Main_parser_rus.lol = Main_parser_rus.id_WR

        if Main_parser_rus.selection_main == 'Бельгия':
            self.spisok_main['values'] = Main_parser_rus.eng_city_belghuem
            Main_parser_rus.lol = Main_parser_rus.id_belghuem

        if Main_parser_rus.selection_main == 'Германия':
            self.spisok_main['values'] = Main_parser_rus.eng_city_german
            Main_parser_rus.lol = Main_parser_rus.id_german

        if Main_parser_rus.selection_main == 'Греция':
            self.spisok_main['values'] = Main_parser_rus.eng_city_grec
            Main_parser_rus.lol = Main_parser_rus.id_grec

        if Main_parser_rus.selection_main == 'Грузия':
            self.spisok_main['values'] = Main_parser_rus.eng_city_gruzia
            Main_parser_rus.lol = Main_parser_rus.id_gruzia

        if Main_parser_rus.selection_main == 'Израиль':
            self.spisok_main['values'] = Main_parser_rus.eng_city_izrail
            Main_parser_rus.lol = Main_parser_rus.id_izrail

        if Main_parser_rus.selection_main == 'Испания':
            self.spisok_main['values'] =Main_parser_rus.eng_city_ispania
            Main_parser_rus.lol =Main_parser_rus.id_ispania

        if Main_parser_rus.selection_main == 'Италия':
            self.spisok_main['values'] =Main_parser_rus.eng_city_italy
            Main_parser_rus.lol =Main_parser_rus.id_italy

        if Main_parser_rus.selection_main == 'Казахстан':
            self.spisok_main['values'] =Main_parser_rus.eng_city_kazahstan
            Main_parser_rus.lol =Main_parser_rus.id_kazahstan

        if Main_parser_rus.selection_main == 'Кипр':
            self.spisok_main['values'] =Main_parser_rus.eng_city_kipr
            Main_parser_rus.lol =Main_parser_rus.id_kipr

        if Main_parser_rus.selection_main == 'Киргизия':
            self.spisok_main['values'] =Main_parser_rus.eng_city_kirgiz
            Main_parser_rus.lol =Main_parser_rus.id_kirgiz

        if Main_parser_rus.selection_main == 'Китай':
            self.spisok_main['values'] = Main_parser_rus.eng_city_chine
            Main_parser_rus.lol = Main_parser_rus.id_chine

        if Main_parser_rus.selection_main == 'Латвия':
            self.spisok_main['values'] = Main_parser_rus.eng_city_latvia
            Main_parser_rus.lol = Main_parser_rus.id_latvia
            
        if Main_parser_rus.selection_main == 'Литва':
            self.spisok_main['values'] = Main_parser_rus.eng_city_litva
            Main_parser_rus.lol = Main_parser_rus.id_litva
            
        if Main_parser_rus.selection_main == 'Молдова':
            self.spisok_main['values'] = Main_parser_rus.eng_city_moldova
            Main_parser_rus.lol = Main_parser_rus.id_moldova
            
        if Main_parser_rus.selection_main == 'Монголия':
            self.spisok_main['values'] = Main_parser_rus.eng_city_mongolia
            Main_parser_rus.lol = Main_parser_rus.id_mongolia
            
        if Main_parser_rus.selection_main == 'Португалия':
            self.spisok_main['values'] = Main_parser_rus.eng_city_port
            Main_parser_rus.lol = Main_parser_rus.id_port
            
        if Main_parser_rus.selection_main == 'США':
            self.spisok_main['values'] = Main_parser_rus.eng_city_usa
            Main_parser_rus.lol = Main_parser_rus.id_usa
            
        if Main_parser_rus.selection_main == 'Таджикистан':
            self.spisok_main['values'] = Main_parser_rus.eng_city_tadzhstan
            Main_parser_rus.lol = Main_parser_rus.id_tadzhstan
            
        if Main_parser_rus.selection_main == 'Узбекистан':
            self.spisok_main['values'] = Main_parser_rus.eng_city_uzbkst
            Main_parser_rus.lol = Main_parser_rus.id_uzbkst
            
        if Main_parser_rus.selection_main == 'Украина':
            self.spisok_main['values'] = Main_parser_rus.eng_city_ukrain
            Main_parser_rus.lol = Main_parser_rus.id_ukrain
            
        if Main_parser_rus.selection_main == 'Эстония':
            self.spisok_main['values'] = Main_parser_rus.eng_city_estonia
            Main_parser_rus.lol = Main_parser_rus.id_estonia
            
        if Main_parser_rus.selection_main == 'Сербия':
            self.spisok_main['values'] = Main_parser_rus.eng_city_serbia
            Main_parser_rus.lol = Main_parser_rus.id_serbia
            
        if Main_parser_rus.selection_main == 'Польша':
            self.spisok_main['values'] = Main_parser_rus.eng_city_poland
            Main_parser_rus.lol = Main_parser_rus.id_poland
            
        if Main_parser_rus.selection_main == 'Великобритания':
            self.spisok_main['values'] = Main_parser_rus.eng_city_great_br
            Main_parser_rus.lol = Main_parser_rus.id_great_br
            
        if Main_parser_rus.selection_main == 'Турция':
            self.spisok_main['values'] = Main_parser_rus.eng_city_turkchis
            Main_parser_rus.lol = Main_parser_rus.id_turkchis
        
        if Main_parser_rus.selection_main == 'Туркменистан':
            self.spisok_main['values'] = Main_parser_rus.eng_city_turkman
            Main_parser_rus.lol = Main_parser_rus.id_turkman
            
        if Main_parser_rus.selection_main == 'Чехия':
            self.spisok_main['values'] = Main_parser_rus.eng_city_chexzia
            Main_parser_rus.lol = Main_parser_rus.id_chexzia
            
        if Main_parser_rus.selection_main == 'Корея':
            self.spisok_main['values'] = Main_parser_rus.eng_city_korea
            Main_parser_rus.lol = Main_parser_rus.id_korea

        if Main_parser_rus.selection_main == 'Болгария':
            self.spisok_main['values'] = Main_parser_rus.eng_city_bolgaria
            Main_parser_rus.lol = Main_parser_rus.id_bolgaria

        if Main_parser_rus.selection_main == 'Вьетнам':
            self.spisok_main['values'] = Main_parser_rus.eng_city_vietham
            Main_parser_rus.lol = Main_parser_rus.id_vietham

        if Main_parser_rus.selection_main == 'Тайвань':
            self.spisok_main['values'] = Main_parser_rus.eng_city_taiwan
            Main_parser_rus.lol = Main_parser_rus.id_taiwan

        if Main_parser_rus.selection_main == 'Иран':
            self.spisok_main['values'] = Main_parser_rus.eng_city_iran
            Main_parser_rus.lol = Main_parser_rus.id_iran

        if Main_parser_rus.selection_main == 'Бенин':
            self.spisok_main['values'] = Main_parser_rus.eng_city_benin
            Main_parser_rus.lol = Main_parser_rus.id_benin

        kek = self.spisok_main['values']

        try:
            i=-1
            for elem in kek:
                i+=1
                if elem == (Main_parser_rus.selection_main) :
                    break
            Main_parser_rus.value_city = Main_parser_rus.lol[i]
        except (IndexError):
            pass
        
        if Main_parser_rus.selection_main == 'Нaзaд':
            self.spisok_main['values'] = Main_parser_rus.eng_russia

        if Main_parser_rus.selection_main == 'Назад':
            self.spisok_main['values'] = Main_parser_rus.eng_city_main

    #Функция обработки выбора структуры компании для url 
    def selected_str(self,event):
        Main_parser_rus.selection_str_comp = self.spisok_comp.get()
        Main_parser_rus.s_button.play()
        try:
            i=-1
            for elem in Main_parser_rus.eng_company:
                i+=1
                if elem==(Main_parser_rus.selection_str_comp):
                    break
            Main_parser_rus.value_cstr_comp = Main_parser_rus.id_s_c[i]
        except (IndexError):
            pass
    
    #Функция перезапуска приложения 
    def reload(self):
        self.win.winfo_children()[0].destroy()
        [child.destroy() for child in self.win.winfo_children()]
        self.GUI()

    #Светлая тема приложения 
    def light_theme(self):
        Main_parser_rus.theme = '#fdfff5'
        with open ('theme.json','w',encoding='utf-8') as file:
            json.dump(Main_parser_rus.theme,file,indent=4,ensure_ascii=False)
        Main_parser_rus.win.config(bg=Main_parser_rus.theme)
        self.label1 = ttk.Label(Main_parser_rus.win,text='*Укажите город \n Для всех городов - "Укажите город"',
        font='arial 10',background='#fdfff5',foreground='#18181a')
        self.label1.place(x=15,y=50)
        self.label2 = ttk.Label(Main_parser_rus.win,text='*Укажите структуру компании \n Для всех структур - "Структура компании"',
        font='arial 10',background='#fdfff5',foreground='#18181a')
        self.label2.place(x=300,y=50)
        self.label3 = ttk.Label(Main_parser_rus.win,text='*Укажите формат файла',font='arial 10',background='#fdfff5',foreground='#18181a')
        self.label3.place(x=15,y=132)
        self.label4 = ttk.Label(Main_parser_rus.win,text='*Укажите формат имени файла',font='arial 10',background='#fdfff5',foreground='#18181a')
        self.label4.place(x=300,y=132)
        self.Sound = tkinter.Button(Main_parser_rus.win,image=Main_parser_rus.on_light,background='#fdfff5',command=self.zvuk)
        self.Sound.place(x=15,y=280)
        self.chasi()

    #Темная тема приложения 
    def dark_theme(self):
        Main_parser_rus.theme = '#18181a'
        with open ('theme.json','w',encoding='utf-8') as file:
            json.dump(Main_parser_rus.theme,file,indent=4,ensure_ascii=False)
        Main_parser_rus.win.config(bg=Main_parser_rus.theme)
        self.label1 = ttk.Label(Main_parser_rus.win,text='*Укажите город \n Для всех городов - "Укажите город"',
        font='arial 10',background='#18181a',foreground='#fdfff5')
        self.label1.place(x=15,y=50)
        self.label2 = ttk.Label(Main_parser_rus.win,text='*Укажите структуру компании \n Для всех структур - "Структура компании"',
        font='arial 10',background='#18181a',foreground='#fdfff5')
        self.label2.place(x=300,y=50)
        self.label3 = ttk.Label(Main_parser_rus.win,text='*Укажие формат файла',font='arial 10',background='#18181a',foreground='#fdfff5')
        self.label3.place(x=15,y=132)
        self.label4 = ttk.Label(Main_parser_rus.win,text='*Укажите формат имени файла',font='arial 10',background='#18181a',foreground='#fdfff5')
        self.label4.place(x=300,y=132)
        self.Sound = tkinter.Button(Main_parser_rus.win,image=Main_parser_rus.on_dark,background='#18181a',command=self.zvuk)
        self.Sound.place(x=15,y=280)
        self.chasi()

    #Функция указания пути сохранения файла 
    def put_file(self):
        Main_parser_rus.directory = fd.askdirectory(title="Укажите куда будет сохранен результат программы", initialdir="/")
        if Main_parser_rus.directory != "":
                self.path()
        else:
            pass
        Main_parser_rus.save = {'Путь': Main_parser_rus.directory}
        with open ('save.json','w',encoding='utf-8') as file:
            json.dump(Main_parser_rus.save,file,indent=4,ensure_ascii=False)

    #Функция выбора формата файла 
    def selected_format (self,event):
        Main_parser_rus.format = self.sp_format.get()
        Main_parser_rus.s_button.play()
    
    #Функция выбора формата имени файла 
    def selected_time (self,event):
        Main_parser_rus.yes_not = self.sp_time.get()
        Main_parser_rus.s_button.play()
        if Main_parser_rus.yes_not == 'С датой': 
            Main_parser_rus.yes_not = True
        else:
            Main_parser_rus.yes_not = False

    #Парсер
    def parse (self):
        Main_parser_rus.s_button.play()
        if Main_parser_rus.selection_main in Main_parser_rus.zapret: 
            self.error_city() 
        else:
            url_for_inb = f'http://foodmarkets.ru/firms/filter_result/7/{Main_parser_rus.value_cstr_comp}/{Main_parser_rus.value_city}/posted' 
            soup2 = BeautifulSoup(requests.get(url_for_inb).content, 'lxml') 
            try: 
                kekes = soup2.find ('span',class_='pagelink').contents[6].text 
                kek = int (kekes) 
                inb = 1  
                while inb <= kek: 
                    url = f'http://foodmarkets.ru/firms/filter_result/7/{Main_parser_rus.value_cstr_comp}/{Main_parser_rus.value_city}/posted/page{inb}' 
                    soup = BeautifulSoup(requests.get(url).content, 'lxml')
                    for row in soup.select('tr:has(td.tcl)'): 
                        tds = [cell.get_text(strip=True, separator=' ') for cell in row.select('td')]
                        Main_parser_rus.catalog.append(tds) 
                        Main_parser_rus.df = pd.DataFrame(Main_parser_rus.catalog, columns=['Структура компании', 'Город(а)', 'Комментариев', 'Последнее сообщение'])
                    inb = inb+1
            except: 
                kekes = None 
                try:
                    url = f'http://foodmarkets.ru/firms/filter_result/7/{Main_parser_rus.value_cstr_comp}/{Main_parser_rus.value_city}/posted' 
                    soup = BeautifulSoup(requests.get(url).content, 'lxml')
                    for row in soup.select('tr:has(td.tcl)'): 
                        tds = [cell.get_text(strip=True, separator=' ') for cell in row.select('td')]
                        Main_parser_rus.catalog.append(tds)
                        Main_parser_rus.df = pd.DataFrame(Main_parser_rus.catalog, columns=['Структура компании', 'Город(а)', 'Комментариев', 'Последнее сообщение'])
                except:
                    self.error_inet()
            finally:
                print ('okay')
                if Main_parser_rus.format == 'Excel':
                    self.excel()
                elif Main_parser_rus.format == 'CSV':
                    self.csv()
                elif Main_parser_rus.format == 'TXT':
                    self.txt()
                self.WindowEnd()
                Main_parser_rus.catalog[:] = [] 

    #Сохранение в excel 
    def excel(self):
        if Main_parser_rus.yes_not == True: 
            writer_exlc = pd.ExcelWriter(f'{Main_parser_rus.directory}\{Main_parser_rus.selection_str_comp} от {Main_parser_rus.vrema}.xlsx', engine='xlsxwriter')
            Main_parser_rus.df.to_excel(writer_exlc,sheet_name=f'{Main_parser_rus.selection_str_comp}', index=False)
            writer_exlc.save()
        elif Main_parser_rus.yes_not == False: 
            writer_exlc = pd.ExcelWriter(f'{Main_parser_rus.directory}\{Main_parser_rus.selection_str_comp}.xlsx', engine='xlsxwriter')
            Main_parser_rus.df.to_excel(writer_exlc, sheet_name=f'{Main_parser_rus.selection_str_comp}',index=False)
            writer_exlc.save()

    #Сохранение в csv 
    def csv (self):
        if Main_parser_rus.yes_not == True: 
            Main_parser_rus.df.to_csv(f'{Main_parser_rus.directory}\{Main_parser_rus.selection_str_comp} от {Main_parser_rus.vrema}.csv', sep='\t', encoding='utf-8')
        elif Main_parser_rus.yes_not == False: 
            Main_parser_rus.df.to_csv(f'{Main_parser_rus.directory}\{Main_parser_rus.selection_str_comp}.csv', sep='\t', encoding='utf-8')

    #Сохранение в txt 
    def txt(self):
        if Main_parser_rus.yes_not == True: 
            Main_parser_rus.df.to_string(f'{Main_parser_rus.directory}\{Main_parser_rus.selection_str_comp} от {Main_parser_rus.vrema}.txt', encoding='utf-8')
        elif Main_parser_rus.yes_not == False: 
            Main_parser_rus.df.to_string(f'{Main_parser_rus.directory}\{Main_parser_rus.selection_str_comp}.txt', encoding='utf-8')
    
    #Для изменения языка
    def versia_eng (self):
            Main_parser_rus.s_button.play() 
            time.sleep(1)
            Main_parser_rus.win.destroy()
            from eng import Main_parser_eng
            version = False
            with open ('version.json','w',encoding='utf-8') as f:
                json.dump(version,f,indent=4,ensure_ascii=False)

    #Инициализация интерфейса и приветственного окона 
    def create_INTF_eng(self):
        self.GUI() 
        Main_parser_rus.win.protocol("WM_DELETE_WINDOW",self.WindowClose) 
        self.knopka_zvuka()
        Main_parser_rus.win.mainloop()

#Инициализация класса и функции запуска 
start = Main_parser_rus() 
start.create_INTF_eng()
