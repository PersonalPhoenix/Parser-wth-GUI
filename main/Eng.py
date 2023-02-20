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

#Родительский класс
class  Main_parser(ttk.Combobox):   

    #Список недопустимых варинатов парсинга городов
    zapret = ['Russia','Far Eastern District','Crimean Federal District','North-Western District','Volga District',
'North Caucasus District','Siberian District','Ural District','Central District','Southern District','Abkhazia','Azerbaijan',
'Armenia','Belarus','Belgium','Germany','Greece','Georgia','Israel','Spain','Italy','Kazakhstan','Cyprus','Kyrgyzstan',
'China','Latvia','Lithuania','Moldova','Mongolia','Portugal','USA','Tajikistan','Turkmenistan','Uzbekistan','Ukraine','Estonia','Serbia','Poland',
'Great Britain','Turkey','Czech Republic','Republic of Korea','Bulgaria','Vietnam','Taiwan','Iran','Benin','Back','']
    
    #Список стран
    eng_city_main = ['Choose a city','Russia','Abkhazia','Azerbaijan','Armenia','Belarus','Belgium','Germany','Greece','Georgia','Israel','Spain','Italy',
'Kazakhstan','Cyprus','Kyrgyzstan','China','Latvia','Lithuania','Moldova','Mongolia','Portugal','USA','Tajikistan','Turkmenistan',
'Uzbekistan','Ukraine','Estonia','Serbia','Poland','Great Britain','Turkey','Czech Republic','Republic of Korea','Bulgaria','Vietnam',
'Taiwan','Iran','Benin']

    #Список округов России
    eng_russia = ['Far Eastern District','Crimean Federal District','North-Western District','Volga District','North Caucasus District',
    'Siberian District','Ural District','Central District','Southern District','Back']

    #Список город/стран/округов и их id
    eng_city_dal_east = ['Aldan','Amursk','Arsenyev','Artem','Belogorsk (Amur region)','Birobidzhan','Blagoveshchensk','Vanino','Vladivostok',
'Dalnegorsk','Dolinsk','Other cities of the Far Eastern Federal District','Yelizovo','Kovalerovo','Komsomolsk-on-Amur','Lensk','Lesozavodsk',
'Magadan','Mirny','Nahodka','Neryungri','Nyurba','Petropavlovsk-Kamchatsky','Svobodny','Sovetskaya Gavan','Spassk Dalny','Tynda','Ussuriysk',
'Khabarovsk','Kholmsk','Yuzhno-Sakhalinsk','Yakutsk','Baсk']
    id_dal_east = [41,1203,172,160,176,11,24,595,15,1530,1168,89,1167,1529,48,240,1528,50,678,161,16,358,85,1166,33,808,219,173,20,1338,156,10]

    #Список город/стран/округов и их id
    eng_city_krim = ['Other cities of the CFR','Evpatoria','Kerch','Sevastopol','Simferopol','Feodosia','Yalta','Baсk']
    id_krim = [1532,1336,1335,1328,1334,1337,1091]
    
    #Список город/стран/округов и их id
    eng_city_n_w = ['Apatity','Arkhangelsk','Velikiye Luki','Veliky Novgorod','Veliky Ustyug','Vologda','Vorkuta','Vyborg',
'Gatchina','Guryevsk','Other cities of the NWFD','Inta','Kaliningrad','Kandalaksha','Kingisepp','Kirishi','Koryazhma','Kostomuksha',
'Kotlas','Lomonosov','Monchegorsk','Murmansk','Naryan-Mar','Novodvinsk','Petrozavodsk','Pechora','Pskov','Pushkin',
'Saint Petersburg','Severodvinsk','Slates','Sosnogorsk','Syktyvkar','Usinsk','Ustyuzhna','Ukhta','Cherepovets','Baсk']
    id_n_w = [1486,166,492,231,613,121,367,823,1075,793,72,617,152,614,462,600,1069,474,616,764,232,151,902,1068,147,615,153,1170,127,431,637,
    563,143,120,1660,154,169,]
    
    #Список город/стран/округов и их id
    eng_city_prv = ['Alexandrovsk','Almetyevsk','Arzamas','Balakovo','Balashov','Belebey','Beloretsk','Berezniki','Bor','Bugulma',
'Buguruslan','Buzuluk','Volzhsk','Volodarsk','Volsk','Votkinsk','Vyatskiye Polyany','Glazov','Dzerzhinsk','Dimitrovgrad',
'Other cities of the Volga Federal District','Yelabuga','Zhigulevsk','Zarechny','Zelenodolsk','Izhevsk','Ishimbai','Yoshkar-Ola','Kazan',
'Kinel','Kirov','Kotelnich','Kstovo','Kuznetsk','Leninogorsk','Naberezhnye Chelny','Neftekamsk','Nizhnekamsk','Nizhny Novgorod','October',
'Orenburg','Orsk','Penza','Perm','Pugachev','Salavat','Samara','Saransk','Sarapul','Saratov','Sarov','Solikamsk','Sorochinsk','Sterlitamak',
'Syzran','Togliatti','Tuymazy','Ulyanovsk','Ufa','Tchaikovsky','Chamzinka','Cheboksary','Engels','Baсk']
    id_prv = [699,142,1101,328,330,365,686,1165,1102,683,543,362,679,940,1590,1314,573,566,963,412,90,237,662,347,546,163,1466,234,235,
    659,148,433,759,709,1242,220,951,1360,134,1356,227,312,129,92,639,1434,184,260,1358,144,945,1359,638,259,477,379,381,149,183,626,
    935,233,1100]
        
    #Список город/стран/округов и их id
    eng_city_kavkaz = ['Budennovsk','Vladikavkaz','Georgievsk','Grozny','Derbent','Other cities with-KFO','Essentuki','Zheleznovodsk',
    'Kislovodsk','Makhachkala','Mineralnye Vody','Nazran','Nalchik','Nevinnomyssk','Pyatigorsk','Stavropol','Khasavyurt','Baсk']
    id_kavkaz = [725,674,1135,441,541,635,618,1145,396,675,1143,979,250,164,634,257,933]
    
    #Список город/стран/округов и их id
    eng_city_sibir = ['Abakan','Aginskoe','Angarsk','Anzhero-Sudzhensk','Achinsk','Barnaul','Belovo','Berdsk','Biysk','Bogotol','Bodaibo',
'Bratsk','Gorno - Altaysk','Other cities of the SFD','Dudinka','Zheleznogorsk','Irkutsk','Kamen-na-Ob','Kansk','Kemerovo','Krasnokamensk',
'Krasnoyarsk','Kuibyshev','Kyzyl','Leninsk-Kuznetsky','Mezhdurechensk','Nizhneudinsk','Novoaltaysk','Novokuznetsk','Novosibirsk','Norilsk',
'Omsk','Pervomaisk','Prokopyevsk','Rubtsovsk','Severobaikalsk','Tomsk','Tulun','Ulan-Ude','Usolye-Sibirskoe','Ust-Ilimsk','Ust-Kut',
'Chita','Shilka','Jurga','Baсk']
    id_sibir = [5,459,103,399,102,26,612,751,46,948,238,43,619,84,653,1017,18,248,179,3,99,4,1099,178,175,949,249,989,25,2,94,34,218,91,1105,
    14,44,247,12,246,145,159,13,799,177]
    
    #Список город/стран/округов и их id
    eng_city_ural = ['Bogdanovich','Verkhnyaya Pyshma','Other cities of the UFO','Yekaterinburg','Zavodoukovsk','Zlatoust','Ishim',
    'Kamensk-Uralsky','Kamyshlov','Krasnouralsk','Kurgan','Kusa','Kyshtym','Labytnangi','Magnitogorsk', 'Megion','Miass','Nadym',
    'Nefteyugansk','Nizhnevartovsk','Nizhny Tagil','Novy Urengoy','Noyabrsk','Nyagan','Pervouralsk','Pyt-Yah','Dir','Salekhard','Serov',
    'Sredneuralsk','Surgut','Tobolsk','Troitsk (Chelyabinsk region)','Turinsk','Tyumen','Uvelsky','Hurray','Urinsk','Uchaly','Khanty-Mansiysk',
    'Chelyabinsk','Shadrinsk','Yugorsk','Yuzhnouralsk','Baсk']
    id_ural = [390,1158,86,52,700,545,222,408,1161,434,185,553,1609,784,223,950,1185,1162,1107,93,221,482,1156,783,1020,1157,1038,849,769,1057,
    155,224,1131,162,1130,1155,1159,1492,785,51,812,1108,1129]
    
    #Список город/стран/округов и их id
    eng_city_tcentral = ['Alexandrov','Belgorod','Bobrov','Borisoglebsk','Borovsk','Bryansk','Vladimir','Volgorechensk','Voronezh','Voskresensk',
'Vyazniki','Vyazma','Goose-Crystal','Dedovsk','Dmitrov','Dolgoprudny','Domodedovo','Other cities of the Central Federal District','Yelets',
'Zheleznodorozhny','Zhukovsky','Zelenograd','Ivanovo','Ivanteevka','Istra','Kaluga','Kashira','Kireevsk','Klimovsk','Wedge','Klintsy','Carpets',
'Kolomna','Korolev','Kostroma','Krasnogorsk','Kuntsevo','Kursk','Livny','Lipetsk','Lobnya','Lytkarino','Lyubertsy','Michurinsk','Moscow','Murom',
'Mytishchi','Naro-Fominsk','Novomoskovsk','Noginsk','Obninsk','Odintsovo','Eagle','Orekhovo-Zuyevo','Pavlovsky Posad','Pogar','Podolsk','Pushkino',
'Ramenskoye','Reutov','Rostov','Rybinsk','Ryazan','Safonovo','Sergiev Posad','Serpukhov','Smolensk','Solnechnogorsk','Stary Oskol','Stupino',
'Tambov','Tver','Tula','Uglich','Furmanov','Khimki','Chekhov','Shchelkovo','Elektrogorsk','Elektrostal','Yaroslavl','Baсk']
    id_tcentral = [581,98,847,457,460,174,96,704,100,1631,955,436,815,743,564,657,589,67,522,777,667,814,111,557,393,171,1132,646,663,395,
    1194,446,400,450,105,1015,536,167,1495,165,1150,1465,320,1033,118,658,765,230,517,370,351,609,170,610,1149,1431,1151,883,718,608,1053,
    229,122,1672,168,242,239,1879,1025,1022,128,119,117,606,1643,559,607,605,1032,463,104]
    
    #Список город/стран/округов и их id
    eng_city_ug = ['Abinsk','Azov','Anapa','Absheronsk','Armavir','Astrakhan','Akhtubinsk','Bataysk','Belogorsk (Crimea)','Belorechensk',
    'Volgograd','Volgodonsk','Volzhsky','Gelendzhik','Gukovo','Gulkevichi','Other cities of the Southern Federal District','Yeysk',
    'Kamensk-Shakhtinsky','Kotovo','Krasnodar','Krymsk','Kurganinsk','Labinsk','Maykop','Millerovo', 'Novorossiysk','Novocherkassk',
    'Rostov-on-Don','Salsk','Sochi','Starominskaya','Taganrog','Temryuk','Timashevsk','Tikhoretsk','Tuapse','Ust-Labinsk','Cherkessk',
    'Shakhty','Elista','Baсk']
    id_ug = [756,532,590,1137,150,409,1140,643,1354,1063,139,391,631,253,1138,1133,158,251,1139,511,135,685,1136,1061,256,1052,252,632,125,
    1060,146,760,418,952,1142,1062,1144,1134,254,461,422]
    
    #Список городов Абхазии и их id
    eng_city_abhazia = ['Other cities of Azerbaijan','Sukhumi','Back']
    id_abhazia = [206,205]
    
    #Список городов Азербайджана и их id
    eng_city_azerbaizhdan = ['Baku','Other cities of Azerbaijan','Back']
    id_azerbaizhan = [190,191]
    
    #Список городов Армении и их id
    eng_city_armenia = ['Other cities of Armenia','Yerevan','Back']
    id_armenia = [210,209]
    
    #Список городов Беларуссии и их id
    eng_city_WR = ['Baranovichi','Bobruisk','Borisov','Brest','Vitebsk','Gomel','Gorki','Grodno','Other cities of Belarus',
 'Lida','Minsk','Mogilev','Polotsk','Rogachev','Back']
    id_WR = [627,300,755,629,186,628,753,349,182,445,181,384,187,258]
    
    #Список городов Бельгии и их id
    eng_city_belghuem = ['Antwerp','Other cities in Belghuem','Back']
    id_belghuem = [357,744]
    
    #Список городов Германии и их id
    eng_city_german = ['Other cities in Germany','Cologne','Stuttgart','Back']
    id_german = [236,1425,722]
    
    #Список городов Греции и их id
    eng_city_grec = ['Athens','Other cities in Greece','Back']
    id_grec = [1490,1491]

    #Список городов Грузии и их id
    eng_city_gruzia = ['Other cities of Georgia','Tbilisi','Back']
    id_gruzia = [208,207]

    #Список городов Израиля и их id
    eng_city_izrail = ['Ashdod','Beersheba','Other cities of Israel','Remez','Tel Aviv','Hodera','Back']
    id_izrail = [344,360,213,211,470,212]

    #Список городов Испании и их id
    eng_city_ispania =['Other cities in Spain','Cadiz','Urense','Back']
    id_ispania = [747,376,724]

    #Список городов Италии и их id
    eng_city_italy = ['Other cities in Italy','Maranello','Milan','Rimini','Back']
    id_italy = [748,261,1445,1414]

    #Список городов Казахстана и их id
    eng_city_kazahstan = ['Aktau','Aktobe','Almaty','Astana','Atyrau','Other cities of Kazakhstan','Zhezkazagan','Karaganda','Kokshetau',
 'Kostanay','Kyzylorda','Pavlodar','Petropavlovsk','Rudny','Families','Semipalatinsk','Taraz','Uralsk','Ust - Kamenogorsk','Shymkent','Back']
    id_kazahstan = [649,644,131,141,303,132,1554,137,651,540,729,133,267,648,1461,650,660,217,647,762]

    #Список городов Кипра и их id
    eng_city_kipr = ['','Back']
    id_kipr = ['']

    #Список городов Киргизии и их id
    eng_city_kirgiz = ['Bishkek','Dalian','Other cities of Kyrgyzstan','Back']
    id_kirgiz = [542,767]

    #Список городов Китая и их id
    eng_city_chine = ['Hong Kong','Dalian','Other cities in China','Beijing','Back']
    id_chine = [1605,840,839,838]

    #Список городов Латвии и их id
    eng_city_latvia = ['Other cities of Latvia','Riga','Back']
    id_latvia = [202,201]

    #Список городов Литвы и их id
    eng_city_litva = ['Vilnos','Other cities of Lithuania','Klaipeda','Back']
    id_litva = [354,215,214]

    #Список городов Молдовы и их id
    eng_city_moldova = ['Balti','Other cities of Moldova','Kishenev','Back']
    id_moldova = [525,200,199]

    #Список городов Монголии и их id
    eng_city_mongolia = ['Other cities of Mongolia','Ulaanbaatar','Back']
    id_mongolia = [245,244]

    #Список городов Португалии и их id
    eng_city_port = ['','Back']
    id_port = ['']

    #Список городов США и их id
    eng_city_usa = ['Other US cities','New York','Back']
    id_usa = [886,885]

    #Список городов Таджикистана и их id
    eng_city_tadzhstan = ['Other cities of Tajikistan','Dushanbe','Leninabad','Khujand','Back']
    id_tadzhstan = [194,192,193,954]

    #Список городов Туркменистана и их id
    eng_city_turkman = ['Ashgabat','Other cities of Turkmenistan','Back']
    id_turkman = [188,189]

    #Список городов Узбекистана и их id
    eng_city_uzbkst = ['Bishkek','Other cities of Uzbekistan','Tashkent','Back']
    id_uzbkst = [1458,216,827]

    #Список городов Украины и их id
    eng_city_ukrain = ['Vinnytsia','Dnepropetrovsk','Donetsk','Other cities of Ukraine','Zhytomyr','Zaporozhye','Izmail','Kiev','Kirovograd',
 'Kremenchuk','Lutsk','Lviv','Mariupol','Melitopol','Odessa','Poltava','Rivne','Sumy','Kharkiv','Chernihiv','Back']
    id_ukrain = [623,196,568,198,622,624,1092,455,620,1550,424,621,382,625,197,544,1289,539,195,1090]

    #Список городов Эстонии и их id
    eng_city_estonia = ['Other cities of Estonia','Tallinn','Back']
    id_estonia = [204,203]

    #Список городов Сербии и их id
    eng_city_serbia = ['Belgrade','Other cities in Serbia','Back']
    id_serbia = [1064,1065]

    #Список городов Польши и их id
    eng_city_poland = ['Warsaw','Wroclaw','Other cities Poland','Kielce','Krakow','Back']
    id_poland = [1238,1629,1240,1627,1239]

    #Список городов Великобритании и их id
    eng_city_great_br = ['Birmingham','Glasgow','Other UK cities','Liverpool','London','Manchester','Edinburgh','Back']
    id_great_br = [1244,1245,1249,1248,1243,1246,1247]

    #Список городов Турции и их id
    eng_city_turkchis = ['Other cities in Turkey','Istanbul','Back']
    id_turkchis = [1291,1290]

    #Список городов Чехии и их id
    eng_city_chexzia = ['Other Czech cities','Nymburk','Prague','Back']
    id_chexzia = [1366,1368,1365]

    #Список городов Кореи и их id
    eng_city_korea = ['Seoul','Back']
    id_korea = [1448]

    #Список городов Болгарии и их id
    eng_city_bolgaria = ['Burgas','Varna','Dobrich','Other cities of Bolgraia','Pleven','Plovdiv','Ruse','Sliven',
'Sofia','Stara-Zagora','Shumen','Back']
    id_bolgaria = [1511,1510,1515,1518,1514,1509,1512,1516,1508,1513,1517]

    #Список городов Вьетнама и их id
    eng_city_vietham = ['Other cities in Vietnam','Hanoi','Ho Chi Minh City','Back']
    id_vietham = [1608,1606,1607]

    #Список городов Тайваня и их id
    eng_city_taiwan = ['Other cities in Taiwan','Xinbei','Taipei','Back']
    id_taiwan = [1634,1633,1632]

    #Список городов Ирана и их id
    eng_city_iran = ['Other cities of Iran','Tehran','Back']
    id_iran = [1690,1689]

    #Список городов Бенина и их id
    eng_city_benin = ['Other cities of Benin','Cotonou','Porto-Novo','Back']    
    id_benin = [1824,1823,1822]

    #Список структур компании и их id
    eng_company = ['Company structure','Wholesaler', 'Distributor', 'Commercial Logistician', 'Own Retail', 'Manufacturer', 
 'Vending machines', 'Importer']
    id_s_c = ['all','opt','distr','comlog','rozn','proiz','vend','import']

    #Основное окно приложения
    win = tkinter.Tk()

    #Кнопка вкл звук
    on_dark = tkinter.PhotoImage(file='icons/zvuk.png')
    #Кнопка выкл звук
    off_dark = tkinter.PhotoImage(file='icons/zvuk_off.png')
    #Кнопка вкл звук
    on_light = tkinter.PhotoImage(file='icons/zvuk_light.png')
    #Кнопка выкл звук
    off_light = tkinter.PhotoImage(file='icons/zvuk_off_light.png')

    #Инициализируем музыку
    is_on = True #Изначально включено
    pygame.mixer.pre_init(44100, -16, 1, 512) #Звуковой эффект без задержки
    pygame.mixer.init() #Инициализируем миксер
    s_button = pygame.mixer.Sound('Sound/Button.mp3') #Звуковой эффект нажатия кнопки/выбора списка
    s_button.set_volume(0.25) #Уровень громкости эффекта нажатия
    s_error = pygame.mixer.Sound('Sound/error.mp3') #Звуковой эффект нажатия кнопки/выбора списка
    s_error.set_volume(0.5) #Уровень громкости эффекта нажатия
    pygame.mixer.music.load('Sound/Main-theme.mp3')
    pygame.mixer.music.set_volume(0.3) #Уровень громоксти музыки
    pygame.mixer.music.play(loops=-1) #Зацикленность музыки

    #Считываем положение главного окна
    x = win.winfo_x() #по х
    y = win.winfo_y() #по У
    
    #Переменная для парсинга данных в виде DataFrame
    dp = pd.DataFrame
  
    #Словарь для сохранения пути сохранения фалйа
    save = {}

    #Список для спаршенной информации
    catalog = []

    #Переменная выбора города
    eng_selection_main = 'Choose a city'

    #Переменная текущего времени для даты в названии файла
    timestr = time.strftime("%Y-%m-%d %H-%M-%S") #Берем текущую дату + время и переводим  строку
    vrema = timestr

    #Переменная выбора формата имени файла для сохранения (с датой/без даты)
    yes_not = False #Изначально без даты

    #Переменная выбора формата файла для сохранения
    format = 'Excel'

    #Переменная для перевода структуры компании в буквы для url
    value_cstr_comp = 'all'

    #Переменая для состояни приветсвенных окон
    zapusk = False 

    #переменная для указания пути
    put_save = r'C:\Users\applm\OneDrive\Рабочий стол\Parser с DataFrame\Parser\save.json'

    #для перевода города в цифру для url
    value_city = 0

        #Для приветственного окона
    if 'avto.json':
        try: #если json уже есть
            with open ('avto.json','r',encoding='utf-8') as f:
                zapusk = json.load(f)
        except: #если нет
            pass

        #Для сохранения темы
    if 'theme.json': 
        try: #если json уже есть
            with open ('theme.json','r',encoding='utf-8') as f:
                theme = json.load(f)
                if theme == '#18181a':
                    icon = on_dark
                    ok = '#18181a'
                else:
                    icon = on_light
                    ok = '#fdfff5'
        except: #если нет
            theme = '#18181a'
            icon = on_dark
            ok = '#18181a'

    #Для указания пути сохранения
    if put_save: 
        try: #если json уже есть
            with open ('save.json','r',encoding='utf-8') as f:
                gruz = json.load(f)
                directory = gruz['Путь']
        except: #если нет
            directory = os.getcwd()

        #Окно приветствия
    def WindowHello(self):
        def hel():
            Main_parser.s_button.play()
            time.sleep(0.1)
            hello.destroy()
        hello = tkinter.Toplevel()
        hello.title('Hi!')
        hello.geometry(f'200x150+{Main_parser.x+665}+{Main_parser.y+200}')
        hello.resizable(False,False)
        canvas = Canvas(hello, width=220,height=150)
        canvas.place(x=-10,y=0)
        canvas.create_rectangle(0,0,220,50,fill='#18181a')
        canvas1 = Canvas(hello, width=220,height=150)
        canvas1.place(x=-10,y=100)
        canvas1.create_rectangle(0,0,220,100,fill='#18181a')
        icons2 = tkinter.PhotoImage(file='icons/hand.png')
        hello.wm_iconphoto(False,icons2)
        Label1 = tkinter.Label(hello,text='Welcome!\nSelect interface language',font='arial 10')
        Label1.place(x=25,y=58)
        Label2 = tkinter.Label(hello,text='Copyright © 2023 P.V. Marshansky',font='arial 9',foreground='#fdfff5',background='#18181a')
        Label2.place(x=3,y=17)
        tkinter.Button(hello, text="Russian",font='arial 10',command=hel).place(x=33,y=112)
        tkinter.Button(hello, text="English",font='arial 10',command=hel).place(x=117,y=112)

    #Музыка
    def zvuk(self): #Переключатель ввиде кнопки
        Main_parser.s_button.play()
        if Main_parser.theme == '#18181a':
            if Main_parser.is_on: #Если кнопку нажали
                self.Sound.config(image = Main_parser.off_dark,background='#18181a') 
                Main_parser.is_on = False
                pygame.mixer.music.pause()
            else: #Если кноку нажали повторно
                self.Sound.config(image = Main_parser.on_dark,background='#18181a')
                Main_parser.is_on = True
                pygame.mixer.music.unpause()
        else:
            if Main_parser.is_on: #Если кнопку нажали
                self.Sound.config(image = Main_parser.off_light,background='#fdfff5') 
                Main_parser.is_on = False
                pygame.mixer.music.pause()
            else: #Если кноку нажали повторно
                self.Sound.config(image = Main_parser.on_light,background='#fdfff5')
                Main_parser.is_on = True
                pygame.mixer.music.unpause()

    #Окно завершения работы программы
    def WindowEnd(self):
        def exit():
            Main_parser.s_button.play()
            time.sleep(0.1)
            end.destroy()
        end = tkinter.Toplevel() #Создаем TopLevel окно
        end.title('The work is finished')#Задаем заголовок окна
        end.geometry(f'250x150+{Main_parser.x+640}+{Main_parser.y+290}') #Задаем изначальное расположение окна 
        end.resizable(False,False) #Запрет на изменение размеров онка
        icons1 = tkinter.PhotoImage(file='icons/info.png') #Задаем иконку окна
        end.wm_iconphoto(False,icons1) #Задаем иконку окна
        canvas = Canvas(end, width=310,height=100) #Cоздаем canvas полотно
        canvas.place(x=-10,y=100) #Размещаем canvas полотно
        canvas.create_rectangle(0,0,310,100,fill='#18181a') #Создаем прямоугольник
        canvas1 = Canvas(end, width=310,height=100) #Cоздаем canvas полотно
        canvas1.place(x=-10,y=0) #Размещаем canvas полотно
        canvas1.create_rectangle(0,0,310,50,fill='#18181a')#Создаем прямоугольник
        Labrl1 = tkinter.Label(end, text= 'Finish!',font='arial 14') #Cоздаем текстовую метку
        Labrl1.place(x=93,y=63) #Размещаем текстовую метку
        Labrl2 = tkinter.Label(end, text= 'Copyright © 2023 P.V. Marshansky',font='arial 9',background='#18181a',foreground='#fdfff5') #Cоздаем текстовую метку
        Labrl2.place(x=29,y=16) #Размещаем текстовую метку
        tkinter.Button(end, text="okey",font='arial 12', command=exit).place(x=100,y=110) #Создаем+размещаем кнопку 
    
    #Окно информации о копирайте
    def WindowCopyRight (self):
        def copy():
            Main_parser.s_button.play()
            time.sleep(0.1)
            copyright.destroy()
        copyright = tkinter.Toplevel()
        copyright.title('Help window')
        copyright.geometry(f'580x370+{Main_parser.x+475}+{Main_parser.y+130}')
        copyright.resizable(False,False)
        canvas = Canvas(copyright, width=590,height=280)
        canvas.place(x=-10,y=295)
        canvas.create_rectangle(0,0,590,280,fill='#18181a')
        canvas1 = Canvas(copyright, width=590,height=280)
        canvas1.place(x=-10,y=0)
        canvas1.create_rectangle(0,0,590,75,fill='#18181a')
        icons2 = tkinter.PhotoImage(file='icons/info.png')
        copyright.wm_iconphoto(False,icons2)
        Label1 = tkinter.Label(copyright,text='Copyright © 2023 P.V. Marshansky',font='arial 12',background='#18181a',foreground='#fdfff5')
        Label1.place(x=157,y=27)
        Label2 = tkinter.Label(copyright, text=f'''
All rights reserved. No part of this algorithm may be reproduced,
distributed or transmitted in any form or by any means,
including photocopying, recording or other electronic or mechanical methods,
without the prior written permission of the creator, except for brief references
contained in written or oral form, and some other
non-commercial purposes permitted by copyright law.
To receive permission requests, write to the creator at the address below:
Mail:
applmacter@mail.ru
Telegram:
https://t.me/marshansky (@marshansky)''',font='arial 9')
        Label2.place(x=69,y=86)
        tkinter.Button(copyright, text="okey",font='arial 12', width=10,command=copy).place(x=237,y=317)
    
    #Уведомление о пользовательском соглашении при выборе в меню User Agreement
    def soglahenie(self):
        def sogl():
            Main_parser.s_button.play()
            time.sleep(0.1)
            soglasie.destroy()
        soglasie = tkinter.Toplevel()
        soglasie.title('Help window')
        soglasie.geometry(f'380x150+{Main_parser.x+580}+{Main_parser.y+190}')
        soglasie.resizable(False,False)
        canvas = Canvas(soglasie, width=390,height=160)
        canvas.place(x=-10,y=0)
        canvas.create_rectangle(0,0,390,50,fill='#18181a')
        canvas1 = Canvas(soglasie, width=390,height=160)
        canvas1.place(x=-10,y=100)
        canvas1.create_rectangle(0,0,390,150,fill='#18181a')
        icons2 = tkinter.PhotoImage(file='icons/hand.png')
        soglasie.wm_iconphoto(False,icons2)
        Label1 = tkinter.Label(soglasie,text='''By using this application, you agree to the "User Agreement". 
See appendix 2"''',font='arial 9')
        Label1.place(x=10,y=58)
        Label2 = tkinter.Label(soglasie,text='Copyright © 2023 P.V. Marshansky',font='arial 9',foreground='#fdfff5',background='#18181a')
        Label2.place(x=90,y=17)
        tkinter.Button(soglasie,text="okey",font='arial 12',command=sogl, width=7).place(x=160,y=112)

    #Уведомление о руководстве пользования при выборе в меню manual
    def ruk(self):
        def rik():
            Main_parser.s_button.play()
            time.sleep(0.1)
            ruko.destroy()
        ruko = tkinter.Toplevel()
        ruko.title('Help window')
        ruko.geometry(f'380x150+{Main_parser.x+580}+{Main_parser.y+190}')
        ruko.resizable(False,False)
        canvas = Canvas(ruko, width=390,height=160)
        canvas.place(x=-10,y=0)
        canvas.create_rectangle(0,0,390,50,fill='#18181a')
        canvas1 = Canvas(ruko,width=390,height=160)
        canvas1.place(x=-10,y=100)
        canvas1.create_rectangle(0,0,390,150,fill='#18181a')
        icons2 = tkinter.PhotoImage(file='icons/hand.png')
        ruko.wm_iconphoto(False,icons2)
        Label1 = tkinter.Label(ruko,text='''Attached to this application is User Manual (see Appendix 1)''',font='arial 10')
        Label1.place(x=10,y=65)
        Label2 = tkinter.Label(ruko,text='Copyright © 2023 P.V. Marshansky',font='arial 9',foreground='#fdfff5',background='#18181a')
        Label2.place(x=90,y=17)
        tkinter.Button(ruko,text="okey",font='arial 12',command=rik, width=7).place(x=160,y=112)
    
    def path(self):
        def pith():
            Main_parser.s_button.play()
            time.sleep(0.1)
            put.destroy()
        put = tkinter.Toplevel()
        put.title('Changing the path')
        put.geometry(f'300x150+{Main_parser.x+610}+{Main_parser.y+190}')
        put.resizable(False,False)
        canvas = Canvas(put, width=390,height=160)
        canvas.place(x=-10,y=0)
        canvas.create_rectangle(0,0,390,50,fill='#18181a')
        canvas1 = Canvas(put,width=390,height=160)
        canvas1.place(x=-10,y=100)
        canvas1.create_rectangle(0,0,390,150,fill='#18181a')
        icons2 = tkinter.PhotoImage(file='icons/hand.png')
        put.wm_iconphoto(False,icons2)
        Label1 = tkinter.Label(put,text=f'Now the files will be saved in: \n {Main_parser.directory}',font='arial 10')
        Label1.pack(side='top',pady=60)
        tkinter.Button(put,text="okey",font='arial 12',command=pith, width=7).place(x=120,y=110)

        #Окно вопроса о закрытии программы
    def WindowClose (self):
        def not_exit():
            Main_parser.s_button.play()
            time.sleep(0.1)
            close.destroy()
        close = tkinter.Toplevel() #Создаем TopLevel окно
        close.title('Quit') #Задаем заголовок окна
        close.geometry(f'300x150+{Main_parser.x+610}+{Main_parser.y+180}') #Задаем изначальное расположение окна 
        close.resizable(False,False) #Запрет на изменение размеров онка
        icons1 = tkinter.PhotoImage(file='icons/quit.png') #Задаем иконку окна
        close.wm_iconphoto(False,icons1) #Задаем иконку окна
        canvas = Canvas(close, width=310,height=100) #Cоздаем canvas полотно
        canvas.place(x=-10,y=100) #Размещаем canvas полотно
        canvas.create_rectangle(0,0,310,100,fill='#18181a') #Создаем прямоугольник
        canvas1 = Canvas(close, width=310,height=100) #Cоздаем canvas полотно
        canvas1.place(x=-10,y=0) #Размещаем canvas полотно
        canvas1.create_rectangle(0,0,310,50,fill='#18181a') #Создаем прямоугольник
        Label1 = tkinter.Label(close, text= 'Are you sure you want to quit?',font='arial 14',foreground='red') #Cоздаем текстовую метку
        Label1.place(x=22,y=63) #Размещаем текстовую метку
        Label1 = tkinter.Label(close, text= 'Copyright © 2023 P.V. Marshansky',font='arial 9',foreground='#fdfff5',bg='#18181a') #Cоздаем текстовую метку
        Label1.place(x=55,y=17) #Размещаем текстовую метку
        Okey = tkinter.Button(close, text="oкey",font='arial 12',command=self.yes_exit, width=6) #Cоздаем кнопку подтверждения выхода
        Okey.place(x=82,y=110) #Размещаем кнопку подтверждения выхода
        Cancel = tkinter.Button(close, text="cancel",font='arial 12',command=not_exit) #Cоздаем кнопку отмены выхода
        Cancel.place(x=167,y=110) #Размещаем кнопку отмены выхода

    #Функция подтверждения закрытия программы
    def yes_exit(self):
        Main_parser.s_button.play()
        time.sleep(0.1)
        Main_parser.win.destroy() #Уничтожаем основное окно при выборе "Okey"
    def error_city (self):
        Main_parser.s_error.play()
        def irror_city():
            Main_parser.s_button.play()
            time.sleep(0.1)
            error.destroy()
        error = tkinter.Toplevel()
        error.title('ERROR')
        error.geometry(f'300x150+{Main_parser.x+610}+{Main_parser.y+190}')
        error.resizable(False,False)
        canvas = Canvas(error, width=390,height=160)
        canvas.place(x=-10,y=0)
        canvas.create_rectangle(0,0,390,50,fill='#18181a')
        canvas1 = Canvas(error,width=390,height=160)
        canvas1.place(x=-10,y=100)
        canvas1.create_rectangle(0,0,390,150,fill='#18181a')
        icons2 = tkinter.PhotoImage(file='icons/hand.png')
        error.wm_iconphoto(False,icons2)
        Label1 = tkinter.Label(error,text=f'{Main_parser.selection_main} invalid city value is set',font='arial 14',foreground='red')
        Label1.pack(side='top',pady=60)
        tkinter.Button(error,text="okey",font='arial 12',command=irror_city, width=7).place(x=110,y=110)
    
    def error_inet (self):
        Main_parser.s_error.play()
        def irror_inet():
            Main_parser.s_button.play()
            time.sleep(0.1)
            error.destroy()
        error = tkinter.Toplevel()
        error.title('ERROR')
        error.geometry(f'300x150+{Main_parser.x+610}+{Main_parser.y+190}')
        error.resizable(False,False)
        canvas = Canvas(error, width=390,height=160)
        canvas.place(x=-10,y=0)
        canvas.create_rectangle(0,0,390,50,fill='#18181a')
        canvas1 = Canvas(error,width=390,height=160)
        canvas1.place(x=-10,y=100)
        canvas1.create_rectangle(0,0,390,150,fill='#18181a')
        icons2 = tkinter.PhotoImage(file='icons/hand.png')
        error.wm_iconphoto(False,icons2)
        Label1 = tkinter.Label(error,text=f'The site is temporarily unavailable:( \nTry again later ',font='arial 12',foreground='red')
        Label1.pack(side='top',pady=60)
        Label2 = tkinter.Label(error,text=f'Also make sure you have an internet connection',font='arial 10',foreground='red',background='#18181a')
        Label2.place(x=5,y=17)
        tkinter.Button(error,text="okey",font='arial 12',command=irror_inet, width=7).place(x=120,y=110)

    #Функция GUI основного окна приложения
    def GUI(self):

        Main_parser.win.title("Panel to control")

        menubar = tkinter.Menu(self.win)

        self.win.config(menu=menubar)

        settings_vid = tkinter.Menu(menubar,tearoff=0)

        settings_obnova = tkinter.Menu(menubar,tearoff=0)

        settings_menu = tkinter.Menu(menubar,tearoff=0)

        settings_sprvk = tkinter.Menu(menubar,tearoff=0) 

        settings_vid2 = tkinter.Menu(settings_vid,tearoff=0)
        settings_vid3 = tkinter.Menu(settings_vid,tearoff=0)

        settings_menu.add_command(label='Reload',command=self.reload)
        settings_menu.add_command(label='Specify the path',command=self.put_file)
        settings_menu.add_separator()
        settings_menu.add_command(label='Exit',command=self.win.destroy, activebackground = 'red')
        menubar.add_cascade(label='File', menu=settings_menu)

        settings_vid.add_cascade(label='Theme',menu=settings_vid3)
        settings_vid3.add_radiobutton(label='Dark',command=self.dark_theme)
        settings_vid3.add_radiobutton(label='Light',command=self.light_theme)

        settings_vid.add_cascade(label='Languague', menu=settings_vid2)
        settings_vid2.add_command(label='Русский')
        settings_vid2.add_command(label='English')
        menubar.add_cascade(label='View', menu=settings_vid)

        settings_sprvk.add_command(label='Manual',command=self.ruk)
        settings_sprvk.add_command(label='Copyright',command=self.WindowCopyRight)
        settings_sprvk.add_command(label='Use argeement',command=self.soglahenie)
        menubar.add_cascade(label='Information', menu=settings_sprvk)

        settings_obnova.add_command(label='Update countries')
        settings_obnova.add_command(label='Update cities')
        menubar.add_cascade(label ='Update', menu=settings_obnova)
        
        screen_width = Main_parser.win.winfo_screenwidth()
        screen_width2 = screen_width//2 - 280
        screen_height = Main_parser.win.winfo_screenheight()
        screen_height2 = screen_height//2 - 300
        Main_parser.win.geometry(f'560x350+{screen_width2}+{screen_height2}')
        Main_parser.win.minsize(560,350)
        Main_parser.win.maxsize(1920,1080)
        icons = tkinter.PhotoImage(file='icons/chain.png')
        Main_parser.win.wm_iconphoto(False,icons)
        
        #Кнопка запуска
        self.btn_start = tkinter.Button(Main_parser.win,text='Start the programm',font='arial 16',command=self.parse)
        self.btn_start.place(x=180,y=225)
        
        #Убрать фокус элемента при его выборе в combobox
        def defocus(event):
            Main_parser.s_button.play()
            event.widget.master.focus_set()

        #Список городов
        self.spisok_main = ttk.Combobox(Main_parser.win,values=Main_parser.eng_city_main,font='arial 14',state="readonly",cursor='hand2')
        self.spisok_main.current('0')
        self.spisok_main.place(x=15,y=15)
        self.spisok_main.bind('<<ComboboxSelected>>',self.selected_city)
        self.spisok_main.bind("<FocusIn>", defocus)

        #Подпись под списков городов
        self.label1 = ttk.Label(Main_parser.win,text='*Specify the city \n For all cities - "Specify the city"', 
        font='arial 10',background='#18181a',foreground='#fdfff5')
        self.label1.place(x=15,y=50) 

        #Список структур компаний
        self.spisok_comp = ttk.Combobox(Main_parser.win,values=Main_parser.eng_company,font='arial 14',state="readonly")
        self.spisok_comp.current('0')
        self.spisok_comp.config(cursor="hand2")
        self.spisok_comp.place(x = 300, y = 15)
        self.spisok_comp.bind('<<ComboboxSelected>>',self.selected_str)
        self.spisok_comp.bind("<FocusIn>", defocus)

        #Список формата имени файла (с датой/без даты)
        self.sp_time = ttk.Combobox(Main_parser.win,values=['Without data','With data'],font='arial 14',state="readonly")
        self.sp_time.current('0')
        self.sp_time.config(cursor="hand2")
        self.sp_time.place(x=300,y=96.5)
        self.sp_time.bind('<<ComboboxSelected>>',self.selected_time)
        self.sp_time.bind("<FocusIn>", defocus)

        #Список формата файла
        self.sp_format = ttk.Combobox(Main_parser.win,values=['Excel','CSV','TXT'],font='arial 14',state="readonly")
        self.sp_format.current('0') 
        self.sp_format.config(cursor="hand2")
        self.sp_format.place(x=15,y=96.5)
        self.sp_format.bind('<<ComboboxSelected>>',self.selected_format)
        self.sp_format.bind("<FocusIn>", defocus)

        if Main_parser.theme == '#fdfff5':
            self.light_theme()
        else:
            self.dark_theme()

    #Функция для часов в 12-и часовом формате
    def chasi (self):
        if Main_parser.theme == '#fdfff5':
            Clock = tkinter.Label(Main_parser.win,text='' ,font=('arial', 12),background='#fdfff5', foreground='#18181a')
            Clock.place(x=10,y=315)
            Clock1 = tkinter.Label(Main_parser.win,text='' ,font=('arial', 12), background='#fdfff5', foreground='#18181a')
            Clock1.place(x=465,y=315)
        else:
            Clock = tkinter.Label(Main_parser.win,text='' ,font=('arial', 12),background='#18181a', foreground='#fdfff5')
            Clock.place(x=10,y=315)
            Clock1 = tkinter.Label(Main_parser.win,text='' ,font=('arial', 12), background='#18181a', foreground='#fdfff5')
            Clock1.place(x=465,y=315)
        string_time = strftime('''%H:%M:%S %p''')
        string_data = strftime('''%d.%m.%Y''')
        Clock.config(text=string_time)
        Clock.after(1000, self.chasi)
        Clock1.config(text=string_data)
        Clock1.after(60000, self.chasi)
        
    #Кнопка музыки
    def knopka_zvuka(self):
        self.Sound = tkinter.Button(Main_parser.win,image=Main_parser.icon,background=Main_parser.ok,command=self.zvuk)
        self.Sound.place(x=15,y=280)

    #Обработка выбора страны/округа/города
    def selected_city(self,event):
        Main_parser.selection_main = self.spisok_main.get()
        Main_parser.s_button.play()
        if Main_parser.selection_main == 'Choose a city':
            Main_parser.value_city = 0
        if Main_parser.selection_main == 'Russia':
            self.spisok_main['values'] = Main_parser.eng_russia

        if Main_parser.selection_main == 'Far Eastern District':
            self.spisok_main['values'] = Main_parser.eng_city_dal_east
        try:
            i=-1
            for elem in Main_parser.eng_city_dal_east:
                i+=1
                if elem== (Main_parser.selection_main) :
                    break
            Main_parser.value_city = Main_parser.id_dal_east[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Crimean Federal District':
            self.spisok_main['values'] = Main_parser.eng_city_krim
        try:
            i=-1
            for elem in Main_parser.eng_city_krim:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_krim[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'North-Western District':
            self.spisok_main['values'] = Main_parser.eng_city_n_w
        try:
            i=-1
            for elem in Main_parser.eng_city_n_w:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_n_w[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Volga District':
            self.spisok_main['values'] = Main_parser.eng_city_prv
        try:
            i=-1
            for elem in Main_parser.eng_city_prv:
                i+=1
                if elem == (Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_prv[i]
        except (IndexError):
            pass
            
        if Main_parser.selection_main == 'North Caucasus District':
            self.spisok_main['values'] = Main_parser.eng_city_kavkaz
        try:
            i=-1
            for elem in Main_parser.eng_city_kavkaz:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_kavkaz[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Siberian District':
            self.spisok_main['values'] = Main_parser.eng_city_sibir
        try:
            i=-1
            for elem in Main_parser.eng_city_sibir:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_sibir[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Ural District':
            self.spisok_main['values'] = Main_parser.eng_city_ural
        try:
            i=-1
            for elem in Main_parser.eng_city_ural:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_ural[i]
        except (IndexError):
            pass
            
        if Main_parser.selection_main == 'Central District':
            self.spisok_main['values'] = Main_parser.eng_city_tcentral
        try:
            i=-1
            for elem in Main_parser.eng_city_tcentral:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_tcentral[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Southern District':
            self.spisok_main['values'] = Main_parser.eng_city_ug
        try:
            i=-1
            for elem in Main_parser.eng_city_ug:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_ug[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Abkhazia':
            self.spisok_main['values'] = Main_parser.eng_city_abhazia
        try:
            i=-1
            for elem in Main_parser.eng_city_abhazia:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_abhazia[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Azerbaijan':
            self.spisok_main['values'] = Main_parser.eng_city_azerbaizhdan
        try:
            i=-1
            for elem in Main_parser.eng_city_azerbaizhdan:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_azerbaizhan[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Armenia':
            self.spisok_main['values'] = Main_parser.eng_city_armenia
        try:
            i=-1
            for elem in Main_parser.eng_city_armenia:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_armenia[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Belarus':
            self.spisok_main['values'] = Main_parser.eng_city_WR
        try:
            i=-1
            for elem in Main_parser.eng_city_WR:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_WR[i]
        except (IndexError):
            pass
            
        if Main_parser.selection_main == 'Belgium':
            self.spisok_main['values'] = Main_parser.eng_city_belghuem
        try:
            i=-1
            for elem in Main_parser.eng_city_belghuem:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_belghuem[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Germany':
            self.spisok_main['values'] = Main_parser.eng_city_german
        try:
            i=-1
            for elem in Main_parser.eng_city_german:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_german[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Greece':
            self.spisok_main['values'] = Main_parser.eng_city_grec
        try:
            i=-1
            for elem in Main_parser.eng_city_grec:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_grec[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Georgia':
            self.spisok_main['values'] = Main_parser.eng_city_gruzia
        try:
            i=-1
            for elem in Main_parser.eng_city_gruzia:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_gruzia[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Israel':
            self.spisok_main['values'] = Main_parser.eng_city_izrail
        try:
            i=-1
            for elem in Main_parser.eng_city_izrail:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_izrail[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Spain':
            self.spisok_main['values'] = Main_parser.eng_city_ispania
        try:
            i=-1
            for elem in Main_parser.eng_city_ispania:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_ispania[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Italy':
            self.spisok_main['values'] = Main_parser.eng_city_italy
        try:
            i=-1
            for elem in Main_parser.eng_city_italy:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_italy[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Kazakhstan':
            self.spisok_main['values'] = Main_parser.eng_city_kazahstan
        try:
            i=-1
            for elem in Main_parser.eng_city_kazahstan:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_kazahstan[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Cyprus':
            self.spisok_main['values'] = Main_parser.eng_city_kipr
        try:
            i=-1
            for elem in Main_parser.eng_city_kipr:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_kipr[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Kyrgyzstan':
            self.spisok_main['values'] = Main_parser.eng_city_kirgiz
        try:
            i=-1
            for elem in Main_parser.eng_city_kirgiz:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_kirgiz[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'China':
            self.spisok_main['values'] = Main_parser.eng_city_chine
        try:
            i=-1
            for elem in Main_parser.eng_city_chine:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_chine[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Latvia':
            self.spisok_main['values'] = Main_parser.eng_city_latvia
        try:
            i=-1
            for elem in Main_parser.eng_city_latvia:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_latvia[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Lithuania':
            self.spisok_main['values'] = Main_parser.eng_city_litva
        try:
            i=-1
            for elem in Main_parser.eng_city_litva:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_litva[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Moldova':
            self.spisok_main['values'] = Main_parser.eng_city_moldova
        try:
            i=-1
            for elem in Main_parser.eng_city_moldova:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_moldova[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Mongolia':
            self.spisok_main['values'] = Main_parser.eng_city_mongolia
        try:
            i=-1
            for elem in Main_parser.eng_city_mongolia:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_mongolia[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Portugal':
            self.spisok_main['values'] = Main_parser.eng_city_port
        try:
            i=-1
            for elem in Main_parser.eng_city_port:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_port[i]
        except (IndexError):
            pass
            
        if Main_parser.selection_main == 'USA':
            self.spisok_main['values'] = Main_parser.eng_city_usa
        try:
            i=-1
            for elem in Main_parser.eng_city_usa:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_usa[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Tajikistan':
            self.spisok_main['values'] = Main_parser.eng_city_tadzhstan
        try:
            i=-1
            for elem in Main_parser.eng_city_tadzhstan:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_tadzhstan[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Uzbekistan':
            self.spisok_main['values'] = Main_parser.eng_city_uzbkst
        try:
            i=-1
            for elem in Main_parser.eng_city_uzbkst:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_uzbkst[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Ukraine':
            self.spisok_main['values'] = Main_parser.eng_city_ukrain
        try:
            i=-1
            for elem in Main_parser.eng_city_ukrain:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_ukrain[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Estonia':
            self.spisok_main['values'] = Main_parser.eng_city_estonia
        try:
            i=-1
            for elem in Main_parser.eng_city_estonia:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_estonia[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Serbia':
            self.spisok_main['values'] = Main_parser.eng_city_serbia
        try:
            i=-1
            for elem in Main_parser.eng_city_serbia:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_serbia[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Poland':
            self.spisok_main['values'] = Main_parser.eng_city_poland
        try:
            i=-1
            for elem in Main_parser.eng_city_poland:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_poland[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Great Britain':
            self.spisok_main['values'] = Main_parser.eng_city_great_br
        try:
            i=-1
            for elem in Main_parser.eng_city_great_br:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_great_br[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Turkey':
            self.spisok_main['values'] = Main_parser.eng_city_turkchis
        try:
            i=-1
            for elem in Main_parser.eng_city_turkchis:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_turkchis[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Czech':
            self.spisok_main['values'] = Main_parser.eng_city_chexzia
        try:
            i=-1
            for elem in Main_parser.eng_city_chexzia:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_chexzia[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Republic of Korea':
            self.spisok_main['values'] = Main_parser.eng_city_korea
        try:
            i=-1
            for elem in Main_parser.eng_city_korea:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_korea[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Bulgaria':
            self.spisok_main['values'] = Main_parser.eng_city_bolgaria
        try:
            i=-1
            for elem in Main_parser.eng_city_bolgaria:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_bolgaria[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Vietnam':
            self.spisok_main['values'] = Main_parser.eng_city_vietham
        try:
            i=-1
            for elem in Main_parser.eng_city_vietham:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_vietham[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Taiwan':
            self.spisok_main['values'] = Main_parser.eng_city_taiwan
        try:
            i=-1
            for elem in Main_parser.eng_city_taiwan:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_taiwan[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Iran':
            self.spisok_main['values'] = Main_parser.eng_city_iran
        try:
            i=-1
            for elem in Main_parser.eng_city_iran:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_iran[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Benin':
            self.spisok_main['values'] = Main_parser.eng_city_benin
        try:
            i=-1
            for elem in Main_parser.eng_city_benin:
                i+=1
                if elem==(Main_parser.selection_main):
                    break
            Main_parser.value_city = Main_parser.id_benin[i]
        except (IndexError):
            pass

        if Main_parser.selection_main == 'Baсk':
            self.spisok_main['values'] = Main_parser.eng_russia

        if Main_parser.selection_main == 'Back':
            self.spisok_main['values'] = Main_parser.eng_city_main
            
    #Обработка выбора структуры компании
    def selected_str(self,event):
        Main_parser.selection_str_comp = self.spisok_comp.get()
        Main_parser.s_button.play()
        try:
            i=-1
            for elem in Main_parser.eng_company:
                i+=1
                if elem==(Main_parser.selection_str_comp):
                    break
            Main_parser.value_cstr_comp = Main_parser.id_s_c[i]
        except (IndexError):
            pass
    
    #Перезапуск главного окна в меню file
    def reload(self):
        self.win.winfo_children()[0].destroy()
        [child.destroy() for child in self.win.winfo_children()]
        self.GUI()

    #Установка белой темы при выборе в окне view
    def light_theme(self):
        Main_parser.theme = '#fdfff5'
        with open ('theme.json','w',encoding='utf-8') as file:
            json.dump(Main_parser.theme,file,indent=4,ensure_ascii=False)

        Main_parser.win.config(bg=Main_parser.theme)
        self.label1 = ttk.Label(Main_parser.win,text='*Specify the city \n For all cities - "Specify the city"',
        font='arial 10',background='#fdfff5',foreground='#18181a')
        self.label1.place(x=15,y=50)
        self.label2 = ttk.Label(Main_parser.win,text='*Specify the structure of the organization \n For all structures - "Organization structure"',
        font='arial 10',background='#fdfff5',foreground='#18181a')
        self.label2.place(x=300,y=50)
        self.label3 = ttk.Label(Main_parser.win,text='*Specify the file format',font='arial 10',background='#fdfff5',foreground='#18181a')
        self.label3.place(x=15,y=132)
        self.label4 = ttk.Label(Main_parser.win,text='*Specify file name format',font='arial 10',background='#fdfff5',foreground='#18181a')
        self.label4.place(x=300,y=132)
        self.Sound = tkinter.Button(Main_parser.win,image=Main_parser.on_light,background='#fdfff5',command=self.zvuk)
        self.Sound.place(x=15,y=280)
        self.chasi()


    #Установка темной темы при выборе в окне view
    def dark_theme(self):
        Main_parser.theme = '#18181a'
        with open ('theme.json','w',encoding='utf-8') as file:
            json.dump(Main_parser.theme,file,indent=4,ensure_ascii=False)

        Main_parser.win.config(bg=Main_parser.theme)
        self.label1 = ttk.Label(Main_parser.win,text='*Specify the city \n For all cities - "Specify the city"',
        font='arial 10',background='#18181a',foreground='#fdfff5')
        self.label1.place(x=15,y=50)
        self.label2 = ttk.Label(Main_parser.win,text='*Specify the structure of the organization \n For all structures - "Organization structure"',
        font='arial 10',background='#18181a',foreground='#fdfff5')
        self.label2.place(x=300,y=50)
        self.label3 = ttk.Label(Main_parser.win,text='*Specify the file format',font='arial 10',background='#18181a',foreground='#fdfff5')
        self.label3.place(x=15,y=132)
        self.label4 = ttk.Label(Main_parser.win,text='*Specify file name format',font='arial 10',background='#18181a',foreground='#fdfff5')
        self.label4.place(x=300,y=132)
        self.Sound = tkinter.Button(Main_parser.win,image=Main_parser.on_dark,background='#18181a',command=self.zvuk)
        self.Sound.place(x=15,y=280)
        self.chasi()

    #Фукнция указания пути сохранения файла
    def put_file(self):
        Main_parser.directory = fd.askdirectory(title="Specify the path where the program result will be saved", initialdir="/")
        if Main_parser.directory != "":
                self.path()
        else:
            pass
        Main_parser.save = {'Путь': Main_parser.directory}
        with open ('save.json','w',encoding='utf-8') as file:
            json.dump(Main_parser.save,file,indent=4,ensure_ascii=False)

    #Обработка выбора формата файла
    def selected_format (self,event):
        Main_parser.format = self.sp_format.get()
        Main_parser.s_button.play()
    
    #Обработка выбора имени формата файла
    def selected_time (self,event):
        Main_parser.yes_not = self.sp_time.get()
        Main_parser.s_button.play()
        if Main_parser.yes_not == 'With data': #Если выбранно с датой+временем
            Main_parser.yes_not = True
        else: #Если выбранно без даты+времени
            Main_parser.yes_not = False

    #Парсер
    def parse (self):
        Main_parser.s_button.play()
        if Main_parser.selection_main in Main_parser.zapret: #Инициализация ошибки запроса вы неверном городе
            self.error_city() #Вывод сообщения о неверно выбранном городе
        else:
            try: #Парсинг
                url_for_inb = f'http://foodmarkets.ru/firms/filter_result/7/{Main_parser.value_cstr_comp}/{Main_parser.value_city}/posted' #url запроса
                soup2 = BeautifulSoup(requests.get(url_for_inb).content, 'lxml') #создаем soup
                try: #Проверяем колличество страниц таблицы
                    try: #Если страниц больше 1
                        kekes = soup2.find ('span',class_='pagelink').contents[6].text #Забираем номер последней страницы
                        kek = int (kekes) #Меняем номер последней стр с str в int
                        inb = 1  
                        while inb <= kek: #Пробегаемся по каждой странице
                            url = f'http://foodmarkets.ru/firms/filter_result/7/{Main_parser.value_cstr_comp}/{Main_parser.value_city}/posted/page{inb}' #url запроса при стр > 1
                            soup = BeautifulSoup(requests.get(url).content, 'lxml')
                            for row in soup.select('tr:has(td.tcl)'): #Пробегаемся по каждой строке таблицы на данной стр
                                tds = [cell.get_text(strip=True, separator=' ') for cell in row.select('td')]
                                Main_parser.catalog.append(tds) #Добавляем новые значения в список
                                Main_parser.df = pd.DataFrame(Main_parser.catalog, columns=['Name company', 'Cities', 'Comments', 'Last message']) #Формируем DataFrame из списка
                            inb = inb+1
                    except: #Ошибка запроса на сайт (если он недоступен/нет интернет подключения)
                        self.error_inet()
                except: #Если одна страница 
                    kekes = None #Индикатор страниц отсутствует
                    try:
                        url = f'http://foodmarkets.ru/firms/filter_result/7/{Main_parser.value_cstr_comp}/{Main_parser.value_city}/posted' #url запроса при стр = 1
                        soup = BeautifulSoup(requests.get(url).content, 'lxml')
                        for row in soup.select('tr:has(td.tcl)'): #Пробегаемся по каждой строке таблицы
                            tds = [cell.get_text(strip=True, separator=' ') for cell in row.select('td')]
                            Main_parser.catalog.append(tds) #Добавляем новые значения в список
                            Main_parser.df = pd.DataFrame(Main_parser.catalog, columns=['Name company', 'Cities', 'Comments', 'Last message']) #Формируем DataFrame из списка
                    except: #Ошибка запроса на сайт (если он недоступен/нет интернет подключения)
                        self.error_inet()
                finally: #Сохранения результата парсерса в необходимом формате
                    if Main_parser.format == 'Excel':
                        self.excel()
                    elif Main_parser.format == 'CSV':
                        self.scv()
                    elif Main_parser.format == 'TXT':
                        self.txt() 
                    self.WindowEnd() #Вызываем окно завершения работы программы
                    Main_parser.catalog[:] = [] #очищаем список данных для последующих запросов
            except:
                self.error_inet()

    #Сохранение файла в Excel
    def excel(self):
        if Main_parser.yes_not == True: #Сохраняем файл с указанием даты+времени
            writer_exlc = pd.ExcelWriter(f'{Main_parser.directory}\{Main_parser.selection_str_comp} от {Main_parser.vrema}.xlsx', engine='xlsxwriter')
            Main_parser.df.to_excel(writer_exlc, sheet_name=f'{Main_parser.selection_str_comp}', index=False)
            writer_exlc.save()
        elif Main_parser.yes_not == False: #Сохраняем файл без даты+времени
            writer_exlc = pd.ExcelWriter(f'{Main_parser.directory}\{Main_parser.selection_str_comp}.xlsx', engine='xlsxwriter')
            Main_parser.df.to_excel(writer_exlc, sheet_name=f'{Main_parser.selection_str_comp}', index=False)
            writer_exlc.save()

    #Сохранение файла в CSV
    def scv (self):
        if Main_parser.yes_not == True: #Сохраняем файл с указанием даты+времени
            Main_parser.df.to_csv(f'{Main_parser.directory}\{Main_parser.selection_str_comp} от {Main_parser.vrema}.csv', sep='\t', encoding='utf-8')
        elif Main_parser.yes_not == False: #Сохраняем файл без даты+времени
            Main_parser.df.to_csv(f'{Main_parser.directory}\{Main_parser.selection_str_comp}.csv', sep='\t', encoding='utf-8')

    #Сохранение файла в TXT
    def txt(self):
        if Main_parser.yes_not == True: #Сохраняем файл с указанием даты+времени
            Main_parser.df.to_string(f'{Main_parser.directory}\{Main_parser.selection_str_comp} от {Main_parser.vrema}.txt', encoding='utf-8')
        elif Main_parser.yes_not == False: #Сохраняем файл без даты+времени
            Main_parser.df.to_string(f'{Main_parser.directory}\{Main_parser.selection_str_comp}.txt', encoding='utf-8')

    #Фукнция создания главного окна + приветственное окно
    def create_INTF_eng(self):
        self.GUI() #создание главного окна
        #Проверяем запускалось ли уже приложение
        if Main_parser.zapusk == False: #Если нет
            self.WindowHello()
            Main_parser.zapusk = True
            with open ('avto.json', 'w', encoding='utf-8') as f:
                json.dump(Main_parser.zapusk,f,indent=4,ensure_ascii=False)
        else: #Если да
            pass
        Main_parser.win.protocol("WM_DELETE_WINDOW",self.WindowClose) #Вызов окна подтверждения закрытия при нажатии "закрыть"
        self.knopka_zvuka() #Запуск музыки
        Main_parser.win.mainloop()

start = Main_parser() 
start.create_INTF_eng()
