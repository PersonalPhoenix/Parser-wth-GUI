import tkinter

from tkinter import ttk, Canvas

import tkinter.filedialog as fd

import requests

from bs4 import BeautifulSoup

import pandas as pd

import json

import time

from time import strftime

import os

import pygame

import config

#Parent class
class  Main_parser_eng():   

    #List of invalid parsing options
    zapret = (
            'Russia', 'Central District', 'Crimean Federal District',
            'Far Eastern District', 'North Caucasus District', 'North-Western District',
            'Siberian District', 'Southern District', 'Ural District',
            'Volga District','Abkhazia', 'Armenia',
            'Azerbaijan', 'Belarus', 'Belgium',
            'China', 'Cyprus', 'Czech Republic',
            'Estonia', 'Georgia', 'Germany',
            'Great Britain', 'Greece', 'Israel',
            'Italy', 'Kazakhstan', 'Kyrgyzstan',
            'Latvia', 'Lithuania', 'Moldova',
            'Mongolia', 'Poland', 'Portugal',
            'Serbia', 'Spain', 'Tajikistan',
            'Turkey', 'Turkmenistan', 'USA',
            'Ukraine', 'Uzbekistan', 'Back', '')

    #List of countries
    eng_city_main = (
            'Choose a city', 'Russia', 'Abkhazia', 'Armenia',
            'Azerbaijan', 'Belarus', 'Belgium', 'China',
            'Cyprus', 'Czech Republic', 'Estonia', 'Georgia',
            'Germany', 'Great Britain', 'Greece', 'Israel',
            'Italy', 'Kazakhstan', 'Kyrgyzstan', 'Latvia',
            'Lithuania', 'Moldova', 'Mongolia', 'Poland',
            'Portugal', 'Serbia', 'Spain', 'Tajikistan',
            'Turkey', 'Turkmenistan', 'USA', 'Ukraine',
            'Uzbekistan')

    #List of districts of Russia
    eng_russia = (
            'Central District', 'Crimean Federal District', 'Far Eastern District',
            'North Caucasus District', 'North-Western District', 'Siberian District',
            'Southern District', 'Ural District', 'Volga District','Back')

    #List of cities in the district and their IDs
    eng_city_dal_east = (
            'Aldan', 'Amursk', 'Arsenyev', 'Artem',
            'Belogorsk (Amur region)', 'Birobidzhan', 'Blagoveshchensk', 'Dalnegorsk',
            'Dolinsk', 'Khabarovsk', 'Kholmsk', 'Komsomolsk-on-Amur',
            'Kovalerovo', 'Lensk', 'Lesozavodsk', 'Magadan',
            'Mirny', 'Nahodka', 'Neryungri', 'Nyurba',
            'Petropavlovsk-Kamchatsky', 'Sovetskaya Gavan', 'Spassk Dalny', 'Svobodny',
            'Tynda', 'Ussuriysk', 'Vanino', 'Vladivostok',
            'Yakutsk', 'Yelizovo', 'Yuzhno-Sakhalinsk', 'Other cities of the Far Eastern Federal District',
            'Back')
    
    id_dal_east = (
            41, 1203, 172, 160,
            176, 11, 24, 1530,
            1168, 20, 1338, 48,
            1529, 240, 1528, 50,
            678, 161, 16, 358,
            85, 33, 808, 1166,
            219, 173, 595, 15,
            10, 1167, 156,89)
    
    #List of cities in the district and their IDs
    eng_city_krim = (
            'Evpatoria', 'Feodosia', 'Kerch', 'Sevastopol',
            'Simferopol', 'Yalta', 'Other cities of the CFR',
            'Back')

    id_krim = (
            1336, 1337, 1335, 1328,
            1334, 1091, 1532)

    # List of cities in the district and their IDs
    eng_city_n_w = (
            'Apatity', 'Arkhangelsk', 'Cherepovets', 'Gatchina',
            'Guryevsk', 'Inta', 'Kaliningrad', 'Kandalaksha',
            'Kingisepp', 'Kirishi', 'Koryazhma', 'Kostomuksha',
            'Kotlas', 'Lomonosov', 'Monchegorsk', 'Murmansk',
            'Naryan-Mar', 'Novodvinsk', 'Pechora', 'Petrozavodsk',
            'Pskov', 'Pushkin', 'Saint Petersburg', 'Severodvinsk',
            'Slates', 'Sosnogorsk', 'Syktyvkar', 'Ukhta',
            'Usinsk', 'Ustyuzhna', 'Velikiye Luki', 'Veliky Novgorod',
            'Veliky Ustyug', 'Vologda', 'Vorkuta', 'Vyborg',
            'Other cities of the NWFD', 'Back')

    id_n_w = (
            1486, 166, 169, 1075,
            793, 617, 152, 614,
            462, 600, 1069, 474,
            616, 764, 232, 151,
            902, 1068, 615, 147,
            153, 1170, 127, 431,
            637, 563, 143, 154,
            120, 1660, 492, 231,
            613, 121, 367, 823,
            72)
    
    #List of cities in the district and their IDs
    eng_city_prv = (
            'Alexandrovsk', 'Almetyevsk', 'Arzamas', 'Balakovo',
            'Balashov', 'Belebey', 'Beloretsk', 'Berezniki',
            'Bor', 'Bugulma', 'Buguruslan', 'Buzuluk',
            'Chamzinka', 'Cheboksary', 'Dimitrovgrad', 'Dzerzhinsk',
            'Engels', 'Glazov', 'Ishimbai', 'Izhevsk',
            'Kazan', 'Kinel', 'Kirov', 'Kotelnich',
            'Kstovo', 'Kuznetsk', 'Leninogorsk', 'Naberezhnye Chelny',
            'Neftekamsk', 'Nizhnekamsk', 'Nizhny Novgorod', 'October',
            'Orenburg', 'Orsk', 'Penza', 'Perm',
            'Pugachev', 'Salavat', 'Samara', 'Saransk',
            'Sarapul', 'Saratov', 'Sarov', 'Solikamsk',
            'Sorochinsk', 'Sterlitamak', 'Syzran', 'Tchaikovsky',
            'Togliatti', 'Tuymazy', 'Ufa', 'Ulyanovsk',
            'Volodarsk', 'Volsk', 'Volzhsk', 'Votkinsk',
            'Vyatskiye Polyany', 'Yelabuga', 'Yoshkar-Ola', 'Zarechny',
            'Zelenodolsk', 'Zhigulevsk', 'Other cities of the Volga Federal District', 'Back')

    id_prv = (
            699, 142, 1101, 328,
            330, 365, 686, 1165,
            1102, 683, 543, 362,
            935, 233, 412, 963,
            1100, 566, 1466, 163,
            235, 659, 148, 433,
            759, 709, 1242, 220,
            951, 1360, 134, 1356,
            227, 312, 129, 92,
            639, 1434, 184, 260,
            1358, 144, 945, 1359,
            638, 259, 477, 626,
            379, 381, 183, 149,
            940, 1590, 679, 1314,
            573, 237, 234, 347,
            546, 662, 90)
        
    #List of cities in the district and their IDs
    eng_city_kavkaz = (
            'Budennovsk', 'Derbent', 'Essentuki', 'Georgievsk',
            'Grozny', 'Khasavyurt', 'Kislovodsk', 'Makhachkala',
            'Mineralnye Vody', 'Nalchik', 'Nazran', 'Nevinnomyssk',
            'Pyatigorsk', 'Stavropol', 'Vladikavkaz', 'Zheleznovodsk',
            'North Caucasus District', 'Back')

    id_kavkaz = (
            725, 541, 618, 1135,
            441, 933, 396, 675,
            1143, 250, 979, 164,
            634, 257, 674, 1145,
            635)

    #List of cities in the district and their IDs
    eng_city_sibir = (
            'Abakan', 'Achinsk', 'Aginskoe', 'Angarsk',
            'Anzhero-Sudzhensk', 'Barnaul', 'Belovo', 'Berdsk',
            'Biysk', 'Bodaibo', 'Bogotol', 'Bratsk',
            'Chita', 'Dudinka', 'Gorno - Altaysk', 'Irkutsk',
            'Jurga', 'Kamen-na-Ob', 'Kansk', 'Kemerovo',
            'Krasnokamensk', 'Krasnoyarsk', 'Kuibyshev', 'Kyzyl',
            'Leninsk-Kuznetsky', 'Mezhdurechensk', 'Nizhneudinsk', 'Norilsk',
            'Novoaltaysk', 'Novokuznetsk', 'Novosibirsk', 'Omsk',
            'Pervomaisk', 'Prokopyevsk', 'Rubtsovsk', 'Severobaikalsk',
            'Shilka', 'Tomsk', 'Tulun', 'Ulan-Ude',
            'Usolye-Sibirskoe', 'Ust-Ilimsk', 'Ust-Kut', 'Zheleznogorsk',
            'Other cities of the Siberian district', 'Back')

    id_sibir = (
            5, 102, 459, 103,
            399, 26, 612, 751,
            46, 238, 948, 43,
            13, 653, 619, 18,
            177, 248, 179, 3,
            99, 4, 1099, 178,
            175, 949, 249, 94,
            989, 25, 2, 34,
            218, 91, 1105, 14,
            799, 44, 247, 12,
            246, 145, 159, 1017,
            84)
    
    #List of cities in the district and their IDs
    eng_city_ural = (
            'Bogdanovich', 'Chelyabinsk', 'Dir', 'Hurray',
            'Ishim', 'Kamensk-Uralsky', 'Kamyshlov', 'Khanty-Mansiysk',
            'Krasnouralsk', 'Kurgan', 'Kusa', 'Kyshtym',
            'Labytnangi', 'Magnitogorsk', 'Megion', 'Miass',
            'Nadym', 'Nefteyugansk', 'Nizhnevartovsk', 'Nizhny Tagil',
            'Novy Urengoy', 'Noyabrsk', 'Nyagan', 'Pervouralsk',
            'Pyt-Yah', 'Salekhard', 'Serov', 'Shadrinsk',
            'Sredneuralsk', 'Surgut', 'Tobolsk', 'Troitsk (Chelyabinsk region)',
            'Turinsk', 'Tyumen', 'Uchaly', 'Urinsk',
            'Uvelsky', 'Verkhnyaya Pyshma', 'Yekaterinburg', 'Yugorsk',
            'Zavodoukovsk', 'Zlatoust', 'Other cities Ural District', 'Back')

    id_ural = (
            390, 812, 1038, 1159,
            222, 408, 1161, 51,
            434, 185, 553, 1609,
            784, 223, 950, 1185,
            1162, 1107, 93, 221,
            482, 1156, 783, 1020,
            1157, 849, 769, 1108,
            1057, 155, 224, 1131,
            162, 1130, 785, 1492,
            1155, 1158, 52, 1129,
            700, 545,86)
    

    #List of cities in the district and their IDs
    eng_city_tcentral = (
            'Alexandrov', 'Belgorod', 'Bobrov', 'Borisoglebsk',
            'Borovsk', 'Bryansk', 'Carpets', 'Chekhov',
            'Dedovsk', 'Dmitrov', 'Dolgoprudny', 'Domodedovo',
            'Eagle', 'Elektrogorsk', 'Elektrostal', 'Furmanov',
            'Goose-Crystal', 'Istra', 'Ivanovo', 'Ivanteevka',
            'Kaluga', 'Kashira', 'Khimki', 'Kireevsk',
            'Klimovsk', 'Klintsy', 'Kolomna', 'Korolev',
            'Kostroma', 'Krasnogorsk', 'Kuntsevo', 'Kursk',
            'Lipetsk', 'Livny', 'Lobnya', 'Lytkarino',
            'Lyubertsy', 'Michurinsk', 'Moscow', 'Murom',
            'Mytishchi', 'Naro-Fominsk', 'Noginsk', 'Novomoskovsk',
            'Obninsk', 'Odintsovo', 'Orekhovo-Zuyevo', 'Pavlovsky Posad',
            'Podolsk', 'Pogar', 'Pushkino', 'Ramenskoye',
            'Reutov', 'Rostov', 'Ryazan', 'Rybinsk',
            'Safonovo', 'Sergiev Posad', 'Serpukhov', 'Shchelkovo',
            'Smolensk', 'Solnechnogorsk', 'Stary Oskol', 'Stupino',
            'Tambov', 'Tula', 'Tver', 'Uglich',
            'Vladimir', 'Volgorechensk', 'Voronezh', 'Voskresensk',
            'Vyazma', 'Vyazniki', 'Wedge', 'Yaroslavl',
            'Yelets', 'Zelenograd', 'Zheleznodorozhny', 'Zhukovsky',
            'Other cities of the Central Federal District', 'Baсk')

    id_tcentral = (
            581, 98, 847, 457,
            460, 174, 446, 607,
            743, 564, 657, 589,
            170, 1032, 463, 1643,
            815, 393, 111, 557,
            171, 1132, 559, 646,
            663, 1194, 400, 450,
            105, 1015, 536, 167,
            165, 1495, 1150, 1465,
            320, 1033, 118, 658,
            765, 230, 370, 517,
            351, 609, 610, 1149,
            1151, 1431, 883, 718,
            608, 1053, 122, 229,
            1672, 168, 242, 605,
            239, 1879, 1025, 1022,
            128, 117, 119, 606,
            96, 704, 100, 1631,
            436, 955, 395, 104,
            522, 814, 777, 667,
            67)

    
    #List of cities in the district and their IDs
    eng_city_ug = (
            'Abinsk', 'Absheronsk', 'Akhtubinsk', 'Anapa',
            'Armavir', 'Astrakhan', 'Azov', 'Bataysk',
            'Belogorsk (Crimea)','Belorechensk', 'Cherkessk', 'Elista',
            'Gelendzhik', 'Gukovo', 'Gulkevichi', 'Kamensk-Shakhtinsky',
            'Kotovo', 'Krasnodar','Krymsk','Kurganinsk',
            'Labinsk', 'Maykop', 'Millerovo', 'Novocherkassk',
            'Novorossiysk', 'Rostov-on-Don', 'Salsk', 'Shakhty',
            'Sochi', 'Starominskaya', 'Taganrog', 'Temryuk',
            'Tikhoretsk', 'Timashevsk', 'Tuapse', 'Ust-Labinsk',
            'Volgodonsk', 'Volgograd', 'Volzhsky', 'Yeysk', 'Other cities Southern District',
            'Back')

    id_ug = (
            756, 1137, 1140, 590,
            150, 409, 532, 643,
            1354, 1063, 254, 422,
            253, 1138, 1133, 1139,
            511, 135, 685, 1136,
            1061, 256, 1052, 632,
            252, 125, 1060, 461,
            146, 760, 418, 952,
            1062, 1142, 1144, 1134,
            391, 139, 631, 251, 158)

    #List of cities of Abkhazia and their IDs
    eng_city_abhazia = (
            'Sukhumi', 'Other cities of Azerbaijan', 'Back')

    id_abhazia = (
            205, 206)
    
    #List of cities of Azerbaijan and their IDs
    eng_city_azerbaizhdan = (
            'Baku', 'Other cities of Azerbaijan', 'Back')

    id_azerbaizhan = (
            190, 191)
    
    #List of Armenian cities and their IDs
    eng_city_armenia = (
            'Yerevan', 'Other cities of Armenia', 'Back')

    id_armenia = (
            209, 210)
    
    #List of cities in Belarus and their IDs
    eng_city_WR = (
            'Baranovichi', 'Bobruisk', 'Borisov', 
            'Brest', 'Gomel', 'Gorki', 'Grodno',
            'Lida', 'Minsk', 'Mogilev', 'Polotsk',
            'Rogachev', 'Vitebsk','Other cities of Belarus',
            'Back')

    id_WR = (
            627, 300, 755,
            629, 628, 753, 349,
            445, 181, 384, 187,
            258, 186, 182)

    #List of cities in Belgium and their IDs
    eng_city_belghuem = (
            'Antwerp', 'Other cities in Belghuem', 'Back')

    id_belghuem = (
            357, 744)
    
    #List of German cities and their IDs
    eng_city_german = (
            'Cologne', 'Stuttgart',
            'Other cities in Germany', 'Back')

    id_german = (
            1425, 722, 236)
    
    #List of Greek cities and their IDs
    eng_city_grec = (
            'Athens', 'Other cities in Greece', 'Back')

    id_grec = (
            1490, 1491)

    #List of Georgian cities and their IDs
    eng_city_gruzia = (
            'Tbilisi','Other cities of Georgia','Back')

    id_gruzia = (
            207, 208)

    #List of Israeli cities and their IDs
    eng_city_izrail = (
            'Ashdod', 'Beersheba', 'Hodera',
            'Remez','Tel Aviv', 'Other cities of Israel',
            'Back')

    id_izrail = (
            344, 360, 212,
            211, 470, 213)

    #List of Spanish cities and their IDs
    eng_city_ispania =(
            'Cadiz', 'Urense', 
            'Other cities in Spain', 'Back')

    id_ispania = (
            376, 724, 747)

    #List of Italian cities and their IDs
    eng_city_italy = (
            'Maranello', 'Milan', 
            'Rimini', 'Other cities in Italy', 'Back')

    id_italy = (
            261, 1445,
            1414, 748)

    #List of cities of Kazakhstan and their IDs
    eng_city_kazahstan = (
            'Aktau', 'Aktobe', 'Almaty', 'Astana',
            'Atyrau', 'Karaganda', 'Kokshetau', 'Kostanay',
            'Kyzylorda', 'Pavlodar', 'Petropavlovsk', 'Rudny',
            'Semey', 'Semipalatinsk', 'Shymkent','Taraz',
            'Uralsk', 'Ust - Kamenogorsk', 'Zhezkazagan', 'Other cities of Kazakhstan',
            'Back')

    id_kazahstan = (
            649, 644, 131, 141,
            303, 137, 651, 540,
            729, 133, 267, 648,
            1461, 762, 650, 660,
            217, 647, 1554, 132) 

    #List of cities in Cyprus and their IDs
    eng_city_kipr = ('', 'Back')
    id_kipr = ('')

    #List of cities of Kyrgyzstan and their IDs
    eng_city_kirgiz = (
            'Bishkek', 'Dalian',
            'Other cities of Kyrgyzstan', 'Back')

    id_kirgiz = (
            542, 767)

    #List of Chinese cities and their IDs
    eng_city_chine = (
            'Beijing', 'Dalian',
            'Hong Kong', 'Other cities in China',
            'Back')

    id_chine = (
            838, 840,
            1605, 839)

    #List of Latvian cities and their IDs
    eng_city_latvia = (
            'Riga', 'Other cities of Latvia', 'Back')

    id_latvia = (
            201, 202)

    #List of Lithuanian cities and their IDs
    eng_city_litva = (
            'Klaipeda', 'Vilnos',
            'Other cities of Lithuania', 'Back')

    id_litva = (
            214, 354,
            215)

    #List of Moldovan cities and their IDs
    eng_city_moldova = (
            'Balti', 'Kishenev',
            'Other cities of Moldova', 'Back')

    id_moldova = (
            525, 199,
            200)

    #List of cities in Mongolia and their IDs
    eng_city_mongolia = (
            'Ulaanbaatar', 'Other cities of Mongolia', 'Back')

    id_mongolia = (
            244, 245)

    #List of Portuguese cities and their IDs
    eng_city_port = ('', 'Back')

    id_port = ('')

    #СList of US cities and their IDs
    eng_city_usa = (
            'New York', 'Other USA cities','Back')

    id_usa = (
            885, 886)

    #List of cities in Tajikistan and their IDs
    eng_city_tadzhstan = (
            'Dushanbe', 'Khujand',
            'Leninabad', 'Other cities of Tajikistan',
            'Back')

    id_tadzhstan = (
            192, 954,
            193, 194)

    #List of cities of Turkmenistan and their IDs
    eng_city_turkman = (
            'Ashgabat', 'Other cities of Turkmenistan', 'Back')

    id_turkman = (
            188, 189)

    #List of cities of Uzbekistan and their IDs
    eng_city_uzbkst = (
            'Bishkek', 'Tashkent', 'Other cities of Uzbekistan', 'Back')

    id_uzbkst = (
            1458, 827, 216)

    #List of Ukrainian cities and their IDs
    eng_city_ukrain = (
            'Chernihiv', 'Dnepropetrovsk', 'Donetsk', 'Izmail',
            'Zhytomyr', 'Zaporozhye', 'Kharkiv', 'Kiev',
            'Kirovograd', 'Kremenchuk', 'Lutsk', 'Lviv',
            'Mariupol', 'Melitopol', 'Odessa', 'Poltava',
            'Rivne', 'Sumy', 'Vinnytsia', 'Other cities of Ukraine',
            'Back')

    id_ukrain = (
            1090, 196, 568, 1092,
            622, 624, 195, 455,
            620, 1550, 424, 621,
            382, 625, 197, 544,
            1289, 539, 623, 198)

    #List of Estonian cities and their IDs
    eng_city_estonia = (
            'Tallinn', 'Other cities of Estonia', 'Back')

    id_estonia =(
            203, 204)

    #List of cities in Serbia and their IDs
    eng_city_serbia = (
            'Belgrade', 'Other cities in Serbia', 'Back')

    id_serbia = (
            1064, 1065)

    #List of Polish cities and their IDs
    eng_city_poland = (
            'Kielce', 'Krakow', 'Warsaw',
            'Wroclaw', 'Other cities Poland',
            'Back')

    id_poland = (
            1627, 1239, 1238,
            1629, 1240)

    #List of UK cities and their IDs
    eng_city_great_br = (
            'Birmingham', 'Edinburgh', 'Glasgow',             
            'Liverpool', 'London', 'Manchester',
            'Other UK cities', 'Back')

    id_great_br = (
            1244, 1247, 1245, 
            1248, 1243, 1246,
            1249)
 
    #List of cities in Turkey and their IDs
    eng_city_turkchis = (
            'Istanbul', 'Other cities in Turkey',
            'Back')

    id_turkchis = (
            1290, 1291)

    #List of Czech cities and their IDs
    eng_city_chexzia = (
            'Nymburk', 'Prague', 'Other Czech cities',
            'Back')

    id_chexzia = (
            1368, 1365, 1366)

    #List of Korean cities and their IDs
    eng_city_korea = (
            'Seoul','Back')

    id_korea = (
            1448)

    #List of Bulgarian cities and their IDs
    eng_city_bolgaria = (
            'Burgas', 'Dobrich','Varna', 'Pleven',
            'Plovdiv', 'Ruse', 'Shumen', 'Sliven',
            'Sofia', 'Stara-Zagora', 'Other cities of Bolgraia',
            'Back')

    id_bolgaria = (
            1511, 1515, 1510, 1514,
            1509, 1512, 1517, 1516,
            1508, 1513, 1518)

    #СList of cities in Vietnam and their IDs
    eng_city_vietham = (
            'Hanoi', 'Ho Chi Minh City', 'Other cities in Vietnam',
            'Back')

    id_vietham = (
            1606, 1607, 1608)

    #List of cities in Taiwan and their IDs
    eng_city_taiwan = (
            'Taipei', 'Xinbei', 'Other cities in Taiwan',
            'Back')

    id_taiwan = (
            1632, 1633, 1634)

    #List of cities in Iran and their IDs
    eng_city_iran = (
            'Tehran', 'Other cities of Iran', 'Back')

    id_iran = (
            1689, 1690)

    #List of Benin cities and their IDs
    eng_city_benin = (
            'Cotonou', 'Porto-Novo', 'Other cities of Benin',
            'Back')

    id_benin = (
            1823, 1822, 1824)

    #List of company structures and their IDs
    eng_company = (
            'Company structure', 'Commercial Logistician',
            'Distributor', 'Importer',
            'Manufacturer', 'Retail',
            'Vending machines', 'Wholesaler')

    id_s_c = (
            'all', 'comlog', 'distr', 'import',
            'proiz', 'rozn', 'vend', 'opt')

    #For id cities
    lol = []

    #Main window
    win = tkinter.Tk()

    #On sound button (Dark theme)
    on_dark = tkinter.PhotoImage(file='icons/zvuk.png')
    #Off sound button (Dark theme)
    off_dark = tkinter.PhotoImage(file='icons/zvuk_off.png')
    #On sound button (Light theme)
    on_light = tkinter.PhotoImage(file='icons/zvuk_light.png')
    #Off sound button (Light theme)
    off_light = tkinter.PhotoImage(file='icons/zvuk_off_light.png')

    #Initialize the music and the sound effect of pressing the buttons
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

    #Reading the position of the main window
    x = win.winfo_x()
    y = win.winfo_y()
    
    #Variable for parsing data in the form of a DataFrame
    df = pd.DataFrame
  
    #Dictionary for saving the file save path
    save = {}

    #List for parse
    catalog = []

    #City selection variable
    eng_selection_main = 'Choose a city'

    #The current time variable for the date in the file name
    timestr = time.strftime("%Y-%m-%d %H-%M-%S") 
    vrema = timestr

    #Variable for selecting the file name format to save (with/without date)
    yes_not = False

    #Variable for selecting the file format to save
    format = 'Excel'

    #Variable for translating company structure into letters for url
    value_cstr_comp = 'all'

    #variable for specifying the path
    put_save = r'C:\Users\applm\OneDrive\Рабочий стол\Parser с DataFrame\Parser\save.json'

    #to convert a city to a digit for a url
    value_city = 0

    #For the welcome window
    if 'avto.json':
        try: 
            with open ('avto.json','r',encoding='utf-8') as f:
                zapusk = json.load(f)
        except: 
            zapusk = False 

    #To save the theme
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

    #To specify the save path
    if put_save: 
        try:  
            with open ('save.json','r',encoding='utf-8') as f:
                gruz = json.load(f)
                directory = gruz['Путь']
        except: 
            directory = os.getcwd()

    #Welcome Window
    def WindowHello(self):
        hello = tkinter.Toplevel()
        hello.title('Hi!')
        hello.geometry(f'200x150+{Main_parser_eng.x+665}+{Main_parser_eng.y+200}') 
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
        tkinter.Button(hello, text="Russian",font='arial 10',command=self.versia_rus).place(x=33,y=112)
        tkinter.Button(hello, text="English",font='arial 10').place(x=117,y=112) 

    #Music
    def zvuk(self): 
        Main_parser_eng.s_button.play() 
        if Main_parser_eng.theme == '#18181a': 
            if Main_parser_eng.is_on: 
                self.Sound.config(image = Main_parser_eng.off_dark,background='#18181a') 
                Main_parser_eng.is_on = False
                pygame.mixer.music.pause() 
            else: 
                self.Sound.config(image = Main_parser_eng.on_dark,background='#18181a')
                Main_parser_eng.is_on = True
                pygame.mixer.music.unpause()
        else: 
            if Main_parser_eng.is_on: 
                self.Sound.config(image = Main_parser_eng.off_light,background='#fdfff5') 
                Main_parser_eng.is_on = False
                pygame.mixer.music.pause()
            else: 
                self.Sound.config(image = Main_parser_eng.on_light,background='#fdfff5')
                Main_parser_eng.is_on = True
                pygame.mixer.music.unpause()

    #Program Shutdown window
    def WindowEnd(self):
        def exit(): 
            Main_parser_eng.s_button.play() 
            time.sleep(0.1) 
            end.destroy() 
        end = tkinter.Toplevel() 
        end.title('The work is finished') 
        end.geometry(f'250x150+{Main_parser_eng.x+640}+{Main_parser_eng.y+290}') 
        end.resizable(False,False) 
        icons1 = tkinter.PhotoImage(file='icons/info.png') 
        end.wm_iconphoto(False,icons1) 
        canvas = Canvas(end, width=310,height=100) 
        canvas.place(x=-10,y=100) 
        canvas.create_rectangle(0,0,310,100,fill='#18181a') 
        canvas1 = Canvas(end, width=310,height=100) 
        canvas1.place(x=-10,y=0) 
        canvas1.create_rectangle(0,0,310,50,fill='#18181a')
        Labrl1 = tkinter.Label(end, text= 'Finish!',font='arial 14') 
        Labrl1.place(x=93,y=63) 
        Labrl2 = tkinter.Label(end, text= 'Copyright © 2023 P.V. Marshansky',font='arial 9',background='#18181a',foreground='#fdfff5') 
        Labrl2.place(x=29,y=16)
        tkinter.Button(end, text="okey",font='arial 12', command=exit).place(x=100,y=110) 
    
    #Copyright Information Window
    def WindowCopyRight (self):
        def copy(): 
            Main_parser_eng.s_button.play() 
            time.sleep(0.1) 
            copyright.destroy()
        copyright = tkinter.Toplevel() 
        copyright.title('Help window')
        copyright.geometry(f'580x370+{Main_parser_eng.x+475}+{Main_parser_eng.y+130}')
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

    #Notification of the User Agreement
    def soglahenie(self):
        def sogl(): 
            Main_parser_eng.s_button.play() 
            time.sleep(0.1) 
            soglasie.destroy() 
        soglasie = tkinter.Toplevel() 
        soglasie.title('Help window') #
        soglasie.geometry(f'380x150+{Main_parser_eng.x+580}+{Main_parser_eng.y+190}') 
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

    #Notice of the User Manual
    def ruk(self):
        def rik(): 
            Main_parser_eng.s_button.play() 
            time.sleep(0.1) 
            ruko.destroy()
        ruko = tkinter.Toplevel() 
        ruko.title('Help window') 
        ruko.geometry(f'380x150+{Main_parser_eng.x+580}+{Main_parser_eng.y+190}') 
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
    
    #Notification window for changing the file save path
    def path(self):
        def pith(): 
            Main_parser_eng.s_button.play() 
            time.sleep(0.1) 
            put.destroy() 
        put = tkinter.Toplevel() 
        put.title('Changing the path') 
        put.geometry(f'300x150+{Main_parser_eng.x+610}+{Main_parser_eng.y+190}') 
        put.resizable(False,False) 
        canvas = Canvas(put, width=390,height=160) 
        canvas.place(x=-10,y=0)
        canvas.create_rectangle(0,0,390,50,fill='#18181a') 
        canvas1 = Canvas(put,width=390,height=160)
        canvas1.place(x=-10,y=100) 
        canvas1.create_rectangle(0,0,390,150,fill='#18181a') 
        icons2 = tkinter.PhotoImage(file='icons/hand.png') 
        put.wm_iconphoto(False,icons2) 
        Label1 = tkinter.Label(put,text=f'Now the files will be saved in: \n {Main_parser_eng.directory}',font='arial 10') 
        Label1.pack(side='top',pady=60) 
        tkinter.Button(put,text="okey",font='arial 12',command=pith, width=7).place(x=120,y=110)  

    #The window of the question about closing the program
    def WindowClose (self):
        def not_exit(): 
            Main_parser_eng.s_button.play() 
            time.sleep(0.1) 
            close.destroy() 
        close = tkinter.Toplevel() 
        close.title('Quit') 
        close.geometry(f'300x150+{Main_parser_eng.x+610}+{Main_parser_eng.y+180}') 
        close.resizable(False,False) 
        icons1 = tkinter.PhotoImage(file='icons/quit.png') 
        close.wm_iconphoto(False,icons1) 
        canvas = Canvas(close, width=310,height=100) 
        canvas.place(x=-10,y=100) 
        canvas.create_rectangle(0,0,310,100,fill='#18181a') 
        canvas1 = Canvas(close, width=310,height=100) 
        canvas1.place(x=-10,y=0) 
        canvas1.create_rectangle(0,0,310,50,fill='#18181a') 
        Label1 = tkinter.Label(close, text= 'Are you sure you want to quit?',font='arial 14',foreground='red')
        Label1.place(x=22,y=63) 
        Label1 = tkinter.Label(close, text= 'Copyright © 2023 P.V. Marshansky',font='arial 9',
        foreground='#fdfff5',bg='#18181a') 
        Label1.place(x=55,y=17) 
        Okey = tkinter.Button(close, text="oкey",font='arial 12',command=self.yes_exit, width=6) 
        Okey.place(x=82,y=110)
        Cancel = tkinter.Button(close, text="cancel",font='arial 12',command=not_exit) 
        Cancel.place(x=167,y=110) 

    #Program closing confirmation function
    def yes_exit(self):
        Main_parser_eng.s_button.play() 
        time.sleep(0.1) 
        Main_parser_eng.win.destroy() 

    #Error window of incorrectly selected city for parsing
    def error_city (self):
        Main_parser_eng.s_error.play()
        def irror_city(): 
            Main_parser_eng.s_button.play() 
            time.sleep(0.1) 
            error.destroy() 
        error = tkinter.Toplevel() 
        error.title('ERROR') 
        error.geometry(f'300x150+{Main_parser_eng.x+610}+{Main_parser_eng.y+190}') 
        error.resizable(False,False) 
        canvas = Canvas(error, width=390,height=160)
        canvas.place(x=-10,y=0)
        canvas.create_rectangle(0,0,390,50,fill='#18181a') 
        canvas1 = Canvas(error,width=390,height=160) 
        canvas1.place(x=-10,y=100) 
        canvas1.create_rectangle(0,0,390,150,fill='#18181a') 
        icons2 = tkinter.PhotoImage(file='icons/hand.png') 
        error.wm_iconphoto(False,icons2)
        Label1 = tkinter.Label(error,text=f'{Main_parser_eng.selection_main} invalid city value is set',font='arial 14',foreground='red') 
        Label1.pack(side='top',pady=60) 
        tkinter.Button(error,text="okey",font='arial 12',command=irror_city, width=7).place(x=110,y=110)
    
    #Error window when there is no Internet/the site is unavailable
    def error_inet (self):
        Main_parser_eng.s_error.play()
        def irror_inet(): 
            Main_parser_eng.s_button.play() 
            time.sleep(0.1) 
            error.destroy() 
        error = tkinter.Toplevel() 
        error.title('ERROR')
        error.geometry(f'300x150+{Main_parser_eng.x+610}+{Main_parser_eng.y+190}') 
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

    #GUI function of the main application window
    def GUI(self):
        
        #Title of the main window
        Main_parser_eng.win.title("Panel to control") 

        #Main Menu
        menubar = tkinter.Menu(self.win) 
        self.win.config(menu=menubar)

        #Мenu item View
        settings_vid = tkinter.Menu(menubar,tearoff=0) 

        #Menu item Update
        settings_obnova = tkinter.Menu(menubar,tearoff=0) 

        #File menu item
        settings_menu = tkinter.Menu(menubar,tearoff=0) 

        #Menu item Information
        settings_sprvk = tkinter.Menu(menubar,tearoff=0)    

        #Menu items 1)Language and 2)Theme
        settings_vid2 = tkinter.Menu(settings_vid,tearoff=0) #1)
        settings_vid3 = tkinter.Menu(settings_vid,tearoff=0) #2)

        #File menu item
        settings_menu.add_command(label='Reload',command=self.reload) 
        settings_menu.add_command(label='Specify the path',command=self.put_file) 
        settings_menu.add_separator() 
        settings_menu.add_command(label='Exit',command=self.win.destroy, activebackground = 'red') 
        menubar.add_cascade(label='File', menu=settings_menu) 

        #Menu sub-item View, Theme
        settings_vid.add_cascade(label='Theme',menu=settings_vid3) 
        settings_vid3.add_radiobutton(label='Dark',command=self.dark_theme) 
        settings_vid3.add_radiobutton(label='Light',command=self.light_theme) 

        #Menu sub-item View, Language
        settings_vid.add_cascade(label='Language', menu=settings_vid2) 
        settings_vid2.add_command(label='Русский (Russian)',command=self.versia_rus) 
        settings_vid2.add_command(label='English (Английский)')

        #Пункт меню View / View menu item
        menubar.add_cascade(label='View', menu=settings_vid) 

        #Menu item Information
        settings_sprvk.add_command(label='Manual',command=self.ruk) 
        settings_sprvk.add_command(label='Copyright',command=self.WindowCopyRight) 
        settings_sprvk.add_command(label='Use argeement',command=self.soglahenie) 
        menubar.add_cascade(label='Information', menu=settings_sprvk) 

        #Menu item Update
        settings_obnova.add_command(label='Update countries') 
        settings_obnova.add_command(label='Update cities') 
        menubar.add_cascade(label ='Update', menu=settings_obnova) 
        
        #Dimensions + initial location of the main window
        screen_width = Main_parser_eng.win.winfo_screenwidth() 
        screen_width2 = screen_width//2 - 280 
        screen_height = Main_parser_eng.win.winfo_screenheight() 
        screen_height2 = screen_height//2 - 300 
        Main_parser_eng.win.geometry(f'560x350+{screen_width2}+{screen_height2}') 
        Main_parser_eng.win.minsize(560,350)
        Main_parser_eng.win.resizable(False,False)

        #Main window icon
        icons = tkinter.PhotoImage(file='icons/chain.png')
        Main_parser_eng.win.wm_iconphoto(False,icons) 
        
        #Start button
        self.btn_start = tkinter.Button(Main_parser_eng.win,text='Start the programm',font='arial 16',command=self.parse) 
        self.btn_start.place(x=180,y=225) 
        
        #Removing focus from the selected item in the list
        def defocus(event):
            Main_parser_eng.s_button.play() 
            event.widget.master.focus_set() 

        #List of cities
        self.spisok_main = ttk.Combobox(Main_parser_eng.win,values=Main_parser_eng.eng_city_main,font='arial 14',state="readonly",cursor='hand2') 
        self.spisok_main.current('0') 
        self.spisok_main.config(cursor="hand2") 
        self.spisok_main.place(x=15,y=15) 
        self.spisok_main.bind('<<ComboboxSelected>>',self.selected_city) 
        self.spisok_main.bind("<FocusIn>", defocus) 

        #List of company structures
        self.spisok_comp = ttk.Combobox(Main_parser_eng.win,values=Main_parser_eng.eng_company,font='arial 14',state="readonly")
        self.spisok_comp.current('0')
        self.spisok_comp.config(cursor="hand2")
        self.spisok_comp.place(x = 300, y = 15)
        self.spisok_comp.bind('<<ComboboxSelected>>',self.selected_str)
        self.spisok_comp.bind("<FocusIn>", defocus)

        #List of file name format
        self.sp_time = ttk.Combobox(Main_parser_eng.win,values=['Without data','With data'],font='arial 14',state="readonly")
        self.sp_time.current('0') 
        self.sp_time.config(cursor="hand2") 
        self.sp_time.place(x=300,y=96.5) 
        self.sp_time.bind('<<ComboboxSelected>>',self.selected_time) 
        self.sp_time.bind("<FocusIn>", defocus) 

        #List of file saving formats
        self.sp_format = ttk.Combobox(Main_parser_eng.win,values=['Excel','CSV','TXT'],font='arial 14',state="readonly") 
        self.sp_format.current('0') 
        self.sp_format.config(cursor="hand2") 
        self.sp_format.place(x=15,y=96.5) 
        self.sp_format.bind('<<ComboboxSelected>>',self.selected_format) 
        self.sp_format.bind("<FocusIn>", defocus) 

    #Clock and date in the main window
    def chasi (self):
        if Main_parser_eng.theme == '#fdfff5': 
            Clock = tkinter.Label(Main_parser_eng.win,text='' ,font=('arial', 12),background='#fdfff5', foreground='#18181a')
            Clock.place(x=10,y=315) 
            Clock1 = tkinter.Label(Main_parser_eng.win,text='' ,font=('arial', 12), background='#fdfff5', foreground='#18181a')
            Clock1.place(x=465,y=315) 
        else:
            Clock = tkinter.Label(Main_parser_eng.win,text='' ,font=('arial', 12),background='#18181a', foreground='#fdfff5')
            Clock.place(x=10,y=315)
            Clock1 = tkinter.Label(Main_parser_eng.win,text='' ,font=('arial', 12), background='#18181a', foreground='#fdfff5') 
            Clock1.place(x=465,y=315)
        try:
            string_time = strftime('''%I:%M:%S %p''')
            string_data = strftime('''%m.%d.%Y''') 
            Clock.config(text=string_time) 
            Clock.after(1000, self.chasi) 
            Clock1.config(text=string_data) 
            Clock1.after(60000, self.chasi)
        except:
            pass
    
    #Button pause/unpause music
    def knopka_zvuka(self): 
        self.Sound = tkinter.Button(Main_parser_eng.win,image=Main_parser_eng.icon,background=Main_parser_eng.ok,command=self.zvuk)
        self.Sound.place(x=15,y=280) 
    
    #Setting the initial theme of the main window
        if Main_parser_eng.theme == '#fdfff5':
            self.light_theme()
        else: 
            self.dark_theme()

    #The function of determining the selected city with conversion to id for url
    def selected_city(self,event):
        Main_parser_eng.selection_main = self.spisok_main.get()
        Main_parser_eng.s_button.play()
        
        if Main_parser_eng.selection_main == 'Choose a city':
            Main_parser_eng.value_city = 0

        if Main_parser_eng.selection_main == 'Russia':
            self.spisok_main['values'] = Main_parser_eng.eng_russia

        if Main_parser_eng.selection_main == 'Far Eastern District':
            self.spisok_main['values'] = Main_parser_eng.eng_city_dal_east
            Main_parser_eng.lol = Main_parser_eng.id_dal_east

        if Main_parser_eng.selection_main == 'Crimean Federal District':
            self.spisok_main['values'] = Main_parser_eng.eng_city_krim
            Main_parser_eng.lol = Main_parser_eng.id_krim

        if Main_parser_eng.selection_main == 'North-Western District':
            self.spisok_main['values'] = Main_parser_eng.eng_city_n_w
            Main_parser_eng.lol = Main_parser_eng.id_n_w

        if Main_parser_eng.selection_main == 'Volga District':
            self.spisok_main['values'] = Main_parser_eng.eng_city_prv
            Main_parser_eng.lol = Main_parser_eng.id_prv

        if Main_parser_eng.selection_main == 'North Caucasus District':
            self.spisok_main['values'] = Main_parser_eng.eng_city_kavkaz
            Main_parser_eng.lol = Main_parser_eng.id_kavkaz

        if Main_parser_eng.selection_main == 'Siberian District':
            self.spisok_main['values'] = Main_parser_eng.eng_city_sibir
            Main_parser_eng.lol = Main_parser_eng.id_sibir

        if Main_parser_eng.selection_main == 'Ural District':
            self.spisok_main['values'] = Main_parser_eng.eng_city_ural
            Main_parser_eng.lol = Main_parser_eng.id_ural

        if Main_parser_eng.selection_main == 'Central District':
            self.spisok_main['values'] = Main_parser_eng.eng_city_tcentral
            Main_parser_eng.lol = Main_parser_eng.id_tcentral

        if Main_parser_eng.selection_main == 'Southern District':
            self.spisok_main['values'] = Main_parser_eng.eng_city_ug
            Main_parser_eng.lol = Main_parser_eng.id_s_c

        if Main_parser_eng.selection_main == 'Abkhazia':
            self.spisok_main['values'] = Main_parser_eng.eng_city_abhazia
            Main_parser_eng.lol = Main_parser_eng.id_abhazia

        if Main_parser_eng.selection_main == 'Azerbaijan':
            self.spisok_main['values'] = Main_parser_eng.eng_city_azerbaizhdan
            Main_parser_eng.lol = Main_parser_eng.id_azerbaizhan

        if Main_parser_eng.selection_main == 'Armenia':
            self.spisok_main['values'] = Main_parser_eng.eng_city_armenia
            Main_parser_eng.lol = Main_parser_eng.id_armenia

        if Main_parser_eng.selection_main == 'Belarus':
            self.spisok_main['values'] = Main_parser_eng.eng_city_WR
            Main_parser_eng.lol = Main_parser_eng.id_WR

        if Main_parser_eng.selection_main == 'Belgium':
            self.spisok_main['values'] = Main_parser_eng.eng_city_belghuem
            Main_parser_eng.lol = Main_parser_eng.id_belghuem

        if Main_parser_eng.selection_main == 'Germany':
            self.spisok_main['values'] = Main_parser_eng.eng_city_german
            Main_parser_eng.lol = Main_parser_eng.id_german

        if Main_parser_eng.selection_main == 'Greece':
            self.spisok_main['values'] = Main_parser_eng.eng_city_grec
            Main_parser_eng.lol = Main_parser_eng.id_grec

        if Main_parser_eng.selection_main == 'Georgia':
            self.spisok_main['values'] = Main_parser_eng.eng_city_gruzia
            Main_parser_eng.lol = Main_parser_eng.id_gruzia

        if Main_parser_eng.selection_main == 'Israel':
            self.spisok_main['values'] = Main_parser_eng.eng_city_izrail
            Main_parser_eng.lol = Main_parser_eng.id_izrail

        if Main_parser_eng.selection_main == 'Spain':
            self.spisok_main['values'] =Main_parser_eng.eng_city_ispania
            Main_parser_eng.lol =Main_parser_eng.id_ispania

        if Main_parser_eng.selection_main == 'Italy':
            self.spisok_main['values'] =Main_parser_eng.eng_city_italy
            Main_parser_eng.lol =Main_parser_eng.id_italy

        if Main_parser_eng.selection_main == 'Kazakhstan':
            self.spisok_main['values'] =Main_parser_eng.eng_city_kazahstan
            Main_parser_eng.lol =Main_parser_eng.id_kazahstan

        if Main_parser_eng.selection_main == 'Cyprus':
            self.spisok_main['values'] =Main_parser_eng.eng_city_kipr
            Main_parser_eng.lol =Main_parser_eng.id_kipr

        if Main_parser_eng.selection_main == 'Kyrgyzstan':
            self.spisok_main['values'] =Main_parser_eng.eng_city_kirgiz
            Main_parser_eng.lol =Main_parser_eng.id_kirgiz

        if Main_parser_eng.selection_main == 'China':
            self.spisok_main['values'] = Main_parser_eng.eng_city_chine
            Main_parser_eng.lol = Main_parser_eng.id_chine

        if Main_parser_eng.selection_main == 'Latvia':
            self.spisok_main['values'] = Main_parser_eng.eng_city_latvia
            Main_parser_eng.lol = Main_parser_eng.id_latvia
            
        if Main_parser_eng.selection_main == 'Lithuania':
            self.spisok_main['values'] = Main_parser_eng.eng_city_litva
            Main_parser_eng.lol = Main_parser_eng.id_litva
            
        if Main_parser_eng.selection_main == 'Moldova':
            self.spisok_main['values'] = Main_parser_eng.eng_city_moldova
            Main_parser_eng.lol = Main_parser_eng.id_moldova
            
        if Main_parser_eng.selection_main == 'Mongolia':
            self.spisok_main['values'] = Main_parser_eng.eng_city_mongolia
            Main_parser_eng.lol = Main_parser_eng.id_mongolia
            
        if Main_parser_eng.selection_main == 'Portugal':
            self.spisok_main['values'] = Main_parser_eng.eng_city_port
            Main_parser_eng.lol = Main_parser_eng.id_port
            
        if Main_parser_eng.selection_main == 'USA':
            self.spisok_main['values'] = Main_parser_eng.eng_city_usa
            Main_parser_eng.lol = Main_parser_eng.id_usa
            
        if Main_parser_eng.selection_main == 'Tajikistan':
            self.spisok_main['values'] = Main_parser_eng.eng_city_tadzhstan
            Main_parser_eng.lol = Main_parser_eng.id_tadzhstan
            
        if Main_parser_eng.selection_main == 'Uzbekistan':
            self.spisok_main['values'] = Main_parser_eng.eng_city_uzbkst
            Main_parser_eng.lol = Main_parser_eng.id_uzbkst
            
        if Main_parser_eng.selection_main == 'Ukraine':
            self.spisok_main['values'] = Main_parser_eng.eng_city_ukrain
            Main_parser_eng.lol = Main_parser_eng.id_ukrain
            
        if Main_parser_eng.selection_main == 'Estonia':
            self.spisok_main['values'] = Main_parser_eng.eng_city_estonia
            Main_parser_eng.lol = Main_parser_eng.id_estonia
            
        if Main_parser_eng.selection_main == 'Serbia':
            self.spisok_main['values'] = Main_parser_eng.eng_city_serbia
            Main_parser_eng.lol = Main_parser_eng.id_serbia
            
        if Main_parser_eng.selection_main == 'Poland':
            self.spisok_main['values'] = Main_parser_eng.eng_city_poland
            Main_parser_eng.lol = Main_parser_eng.id_poland
            
        if Main_parser_eng.selection_main == 'Great Britain':
            self.spisok_main['values'] = Main_parser_eng.eng_city_great_br
            Main_parser_eng.lol = Main_parser_eng.id_great_br
            
        if Main_parser_eng.selection_main == 'Turkey':
            self.spisok_main['values'] = Main_parser_eng.eng_city_turkchis
            Main_parser_eng.lol = Main_parser_eng.id_turkchis
            
        if Main_parser_eng.selection_main == 'Czech':
            self.spisok_main['values'] = Main_parser_eng.eng_city_chexzia
            Main_parser_eng.lol = Main_parser_eng.id_chexzia
            
        if Main_parser_eng.selection_main == 'Republic of Korea':
            self.spisok_main['values'] = Main_parser_eng.eng_city_korea
            Main_parser_eng.lol = Main_parser_eng.id_korea

        if Main_parser_eng.selection_main == 'Bulgaria':
            self.spisok_main['values'] = Main_parser_eng.eng_city_bolgaria
            Main_parser_eng.lol = Main_parser_eng.id_bolgaria

        if Main_parser_eng.selection_main == 'Vietnam':
            self.spisok_main['values'] = Main_parser_eng.eng_city_vietham
            Main_parser_eng.lol = Main_parser_eng.id_vietham

        if Main_parser_eng.selection_main == 'Taiwan':
            self.spisok_main['values'] = Main_parser_eng.eng_city_taiwan
            Main_parser_eng.lol = Main_parser_eng.id_taiwan

        if Main_parser_eng.selection_main == 'Iran':
            self.spisok_main['values'] = Main_parser_eng.eng_city_iran
            Main_parser_eng.lol = Main_parser_eng.id_iran

        if Main_parser_eng.selection_main == 'Benin':
            self.spisok_main['values'] = Main_parser_eng.eng_city_benin
            Main_parser_eng.lol = Main_parser_eng.id_benin

        kek = self.spisok_main['values']

        try:
            i=-1
            for elem in kek:
                i+=1
                if elem == (Main_parser_eng.selection_main) :
                    break
            Main_parser_eng.value_city = Main_parser_eng.lol[i]
        except (IndexError):
            pass
        
        if Main_parser_eng.selection_main == 'Baсk':
            self.spisok_main['values'] = Main_parser_eng.eng_russia

        if Main_parser_eng.selection_main == 'Back':
            self.spisok_main['values'] = Main_parser_eng.eng_city_main
    
    #The function of processing the selection of the company structure for the url
    def selected_str(self,event):
        Main_parser_eng.selection_str_comp = self.spisok_comp.get()
        Main_parser_eng.s_button.play()
        try:
            i=-1
            for elem in Main_parser_eng.eng_company:
                i+=1
                if elem==(Main_parser_eng.selection_str_comp):
                    break
            Main_parser_eng.value_cstr_comp = Main_parser_eng.id_s_c[i]
        except (IndexError):
            pass
    
    #Application restart function
    def reload(self):
        self.win.winfo_children()[0].destroy()
        [child.destroy() for child in self.win.winfo_children()]
        self.GUI()

    #Light theme of the application
    def light_theme(self):
        Main_parser_eng.theme = '#fdfff5'
        with open ('theme.json','w',encoding='utf-8') as file:
            json.dump(Main_parser_eng.theme,file,indent=4,ensure_ascii=False)
        Main_parser_eng.win.config(bg=Main_parser_eng.theme)
        self.label1 = ttk.Label(Main_parser_eng.win,text='*Specify the city \n For all cities - "Specify the city"',
        font='arial 10',background='#fdfff5',foreground='#18181a')
        self.label1.place(x=15,y=50)
        self.label2 = ttk.Label(Main_parser_eng.win,text='*Specify the structure of the organization \n For all structures - "Organization structure"',
        font='arial 10',background='#fdfff5',foreground='#18181a')
        self.label2.place(x=300,y=50)
        self.label3 = ttk.Label(Main_parser_eng.win,text='*Specify the file format',font='arial 10',background='#fdfff5',foreground='#18181a')
        self.label3.place(x=15,y=132)
        self.label4 = ttk.Label(Main_parser_eng.win,text='*Specify file name format',font='arial 10',background='#fdfff5',foreground='#18181a')
        self.label4.place(x=300,y=132)
        self.Sound = tkinter.Button(Main_parser_eng.win,image=Main_parser_eng.on_light,background='#fdfff5',command=self.zvuk)
        self.Sound.place(x=15,y=280)
        self.chasi()

    #Dark theme of the application
    def dark_theme(self):
        Main_parser_eng.theme = '#18181a'
        with open ('theme.json','w',encoding='utf-8') as file:
            json.dump(Main_parser_eng.theme,file,indent=4,ensure_ascii=False)
        Main_parser_eng.win.config(bg=Main_parser_eng.theme)
        self.label1 = ttk.Label(Main_parser_eng.win,text='*Specify the city \n For all cities - "Specify the city"',
        font='arial 10',background='#18181a',foreground='#fdfff5')
        self.label1.place(x=15,y=50)
        self.label2 = ttk.Label(Main_parser_eng.win,text='*Specify the structure of the organization \n For all structures - "Organization structure"',
        font='arial 10',background='#18181a',foreground='#fdfff5')
        self.label2.place(x=300,y=50)
        self.label3 = ttk.Label(Main_parser_eng.win,text='*Specify the file format',font='arial 10',background='#18181a',foreground='#fdfff5')
        self.label3.place(x=15,y=132)
        self.label4 = ttk.Label(Main_parser_eng.win,text='*Specify file name format',font='arial 10',background='#18181a',foreground='#fdfff5')
        self.label4.place(x=300,y=132)
        self.Sound = tkinter.Button(Main_parser_eng.win,image=Main_parser_eng.on_dark,background='#18181a',command=self.zvuk)
        self.Sound.place(x=15,y=280)
        self.chasi()

    #The function of specifying the file save path
    def put_file(self):
        Main_parser_eng.directory = fd.askdirectory(title="Specify the path where the program result will be saved", initialdir="/")
        if Main_parser_eng.directory != "":
                self.path()
        else:
            pass
        Main_parser_eng.save = {'Путь': Main_parser_eng.directory}
        with open ('save.json','w',encoding='utf-8') as file:
            json.dump(Main_parser_eng.save,file,indent=4,ensure_ascii=False)

    #File format selection function
    def selected_format (self,event):
        Main_parser_eng.format = self.sp_format.get()
        Main_parser_eng.s_button.play()
    
    #File name format selection function
    def selected_time (self,event):
        Main_parser_eng.yes_not = self.sp_time.get()
        Main_parser_eng.s_button.play()
        if Main_parser_eng.yes_not == 'With data': 
            Main_parser_eng.yes_not = True
        else:
            Main_parser_eng.yes_not = False

    #Web - scrapper
    def parse (self):
        Main_parser_eng.s_button.play()
        if Main_parser_eng.selection_main in Main_parser_eng.zapret: 
            self.error_city() 
        else:
            url_for_inb = f'http://foodmarkets.ru/firms/filter_result/7/{Main_parser_eng.value_cstr_comp}/{Main_parser_eng.value_city}/posted' 
            soup2 = BeautifulSoup(requests.get(url_for_inb).content, 'lxml') 
            try: 
                kekes = soup2.find ('span',class_='pagelink').contents[6].text 
                kek = int (kekes) 
                inb = 1  
                while inb <= kek: 
                    url = f'http://foodmarkets.ru/firms/filter_result/7/{Main_parser_eng.value_cstr_comp}/{Main_parser_eng.value_city}/posted/page{inb}' 
                    soup = BeautifulSoup(requests.get(url).content, 'lxml')
                    for row in soup.select('tr:has(td.tcl)'): 
                        tds = [cell.get_text(strip=True, separator=' ') for cell in row.select('td')]
                        Main_parser_eng.catalog.append(tds) 
                        Main_parser_eng.df = pd.DataFrame(Main_parser_eng.catalog, columns=['Name company', 'Cities', 'Comments', 'Last message'])
                    inb = inb+1
            except: 
                kekes = None 
                try:
                    url = f'http://foodmarkets.ru/firms/filter_result/7/{Main_parser_eng.value_cstr_comp}/{Main_parser_eng.value_city}/posted' 
                    soup = BeautifulSoup(requests.get(url).content, 'lxml')
                    for row in soup.select('tr:has(td.tcl)'): 
                        tds = [cell.get_text(strip=True, separator=' ') for cell in row.select('td')]
                        Main_parser_eng.catalog.append(tds)
                        Main_parser_eng.df = pd.DataFrame(Main_parser_eng.catalog, columns=['Name company', 'Cities', 'Comments', 'Last message'])
                except:
                    self.error_inet()
            finally:
                print ('okay')
                if Main_parser_eng.format == 'Excel':
                    self.excel()
                elif Main_parser_eng.format == 'CSV':
                    self.csv()
                elif Main_parser_eng.format == 'TXT':
                    self.txt()
                self.WindowEnd()
                Main_parser_eng.catalog[:] = [] 

    #Saving to excel
    def excel(self):
        if Main_parser_eng.yes_not == True: 
            writer_exlc = pd.ExcelWriter(f'{Main_parser_eng.directory}\{Main_parser_eng.selection_str_comp} от {Main_parser_eng.vrema}.xlsx', engine='xlsxwriter')
            Main_parser_eng.df.to_excel(writer_exlc,sheet_name=f'{Main_parser_eng.selection_str_comp}', index=False)
            writer_exlc.save()
        elif Main_parser_eng.yes_not == False: 
            writer_exlc = pd.ExcelWriter(f'{Main_parser_eng.directory}\{Main_parser_eng.selection_str_comp}.xlsx', engine='xlsxwriter')
            Main_parser_eng.df.to_excel(writer_exlc, sheet_name=f'{Main_parser_eng.selection_str_comp}',index=False)
            writer_exlc.save()

    #Saving to csv
    def csv (self):
        if Main_parser_eng.yes_not == True: 
            Main_parser_eng.df.to_csv(f'{Main_parser_eng.directory}\{Main_parser_eng.selection_str_comp} от {Main_parser_eng.vrema}.csv', sep='\t', encoding='utf-8')
        elif Main_parser_eng.yes_not == False: 
            Main_parser_eng.df.to_csv(f'{Main_parser_eng.directory}\{Main_parser_eng.selection_str_comp}.csv', sep='\t', encoding='utf-8')

    #Saving to txt
    def txt(self):
        if Main_parser_eng.yes_not == True: 
            Main_parser_eng.df.to_string(f'{Main_parser_eng.directory}\{Main_parser_eng.selection_str_comp} от {Main_parser_eng.vrema}.txt', encoding='utf-8')
        elif Main_parser_eng.yes_not == False: 
            Main_parser_eng.df.to_string(f'{Main_parser_eng.directory}\{Main_parser_eng.selection_str_comp}.txt', encoding='utf-8')
    
    #For change language
    def versia_rus (self):
            Main_parser_eng.s_button.play() 
            time.sleep(1)
            Main_parser_eng.win.destroy()
            config.version = True
            with open ('version.json','w',encoding='utf-8') as f:
                json.dump(config.version,f,indent=4,ensure_ascii=False)
            from rus import Main_parser_rus
            
    #Initializing the interface and welcome window
    def create_INTF_eng(self):
        self.GUI() 
        Main_parser_eng.win.protocol("WM_DELETE_WINDOW",self.WindowClose) 
        self.knopka_zvuka()
        Main_parser_eng.win.mainloop()

#Initializing the class and the startup function
start = Main_parser_eng() 
start.create_INTF_eng()
