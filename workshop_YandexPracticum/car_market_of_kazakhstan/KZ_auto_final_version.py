#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Описание-проекта" data-toc-modified-id="Описание-проекта-1"><span class="toc-item-num">1&nbsp;&nbsp;</span><font face="liberation serif" size="5">Описание проекта</font></a></span><ul class="toc-item"><li><span><a href="#Описание-данных." data-toc-modified-id="Описание-данных.-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span><font face="liberation serif" size="4">Описание данных.</font></a></span></li><li><span><a href="#Описание-задачи" data-toc-modified-id="Описание-задачи-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span><font face="liberation serif" size="4">Описание задачи</font></a></span></li></ul></li><li><span><a href="#Общая-подготовка" data-toc-modified-id="Общая-подготовка-2"><span class="toc-item-num">2&nbsp;&nbsp;</span><font face="liberation serif" size="5">Общая подготовка</font></a></span><ul class="toc-item"><li><span><a href="#Используем-стандартные-проверки,-с-использованием-шаблонных-функций-(заготовки-прошлых-периодов)" data-toc-modified-id="Используем-стандартные-проверки,-с-использованием-шаблонных-функций-(заготовки-прошлых-периодов)-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Используем стандартные проверки, с использованием шаблонных функций (заготовки прошлых периодов)</a></span><ul class="toc-item"><li><span><a href="#Изучим-наполнение-датасета" data-toc-modified-id="Изучим-наполнение-датасета-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Изучим наполнение датасета</a></span></li><li><span><a href="#Провека-на-очевидные-дубликаты-и-пропуски" data-toc-modified-id="Провека-на-очевидные-дубликаты-и-пропуски-2.1.2"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Провека на очевидные дубликаты и пропуски</a></span></li></ul></li><li><span><a href="#Обработка-пропусков." data-toc-modified-id="Обработка-пропусков.-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span><font face="liberation serif" size="5">Обработка пропусков.</font></a></span><ul class="toc-item"><li><span><a href="#Объем-двигателя." data-toc-modified-id="Объем-двигателя.-2.2.1"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>Объем двигателя.</a></span></li><li><span><a href="#Год-выпуска." data-toc-modified-id="Год-выпуска.-2.2.2"><span class="toc-item-num">2.2.2&nbsp;&nbsp;</span>Год выпуска.</a></span></li><li><span><a href="#Тип-топлива" data-toc-modified-id="Тип-топлива-2.2.3"><span class="toc-item-num">2.2.3&nbsp;&nbsp;</span>Тип топлива</a></span></li><li><span><a href="#Коробка-передач" data-toc-modified-id="Коробка-передач-2.2.4"><span class="toc-item-num">2.2.4&nbsp;&nbsp;</span>Коробка передач</a></span></li><li><span><a href="#Тип-привода" data-toc-modified-id="Тип-привода-2.2.5"><span class="toc-item-num">2.2.5&nbsp;&nbsp;</span>Тип привода</a></span></li><li><span><a href="#Итоги-чистки" data-toc-modified-id="Итоги-чистки-2.2.6"><span class="toc-item-num">2.2.6&nbsp;&nbsp;</span>Итоги чистки</a></span></li></ul></li><li><span><a href="#Обработка-типов." data-toc-modified-id="Обработка-типов.-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span><font face="liberation serif" size="5">Обработка типов.</font></a></span><ul class="toc-item"><li><span><a href="#Кодировка-стран" data-toc-modified-id="Кодировка-стран-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>Кодировка стран</a></span></li></ul></li><li><span><a href="#Анализ-данных." data-toc-modified-id="Анализ-данных.-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span><font face="liberation serif" size="5">Анализ данных.</font></a></span><ul class="toc-item"><li><span><a href="#Визуализация-даных-для-исследования" data-toc-modified-id="Визуализация-даных-для-исследования-2.4.1"><span class="toc-item-num">2.4.1&nbsp;&nbsp;</span>Визуализация даных для исследования</a></span></li><li><span><a href="#Топ-продаж-по-медиативной-цене-и-количество-проданных-авто" data-toc-modified-id="Топ-продаж-по-медиативной-цене-и-количество-проданных-авто-2.4.2"><span class="toc-item-num">2.4.2&nbsp;&nbsp;</span>Топ продаж по медиативной цене и количество проданных авто</a></span><ul class="toc-item"><li><span><a href="#Срез-для-выявления-покупок-для-частных-целей,-и-визуализация-результатов" data-toc-modified-id="Срез-для-выявления-покупок-для-частных-целей,-и-визуализация-результатов-2.4.2.1"><span class="toc-item-num">2.4.2.1&nbsp;&nbsp;</span>Срез для выявления покупок для частных целей, и визуализация результатов</a></span></li><li><span><a href="#Топ-10-бренды-по-количеству-приобретенных-авто" data-toc-modified-id="Топ-10-бренды-по-количеству-приобретенных-авто-2.4.2.2"><span class="toc-item-num">2.4.2.2&nbsp;&nbsp;</span>Топ-10 бренды по количеству приобретенных авто</a></span></li></ul></li><li><span><a href="#Динамика-продаж-по-рынку,-в-штуках-и-в-денежном-выражении." data-toc-modified-id="Динамика-продаж-по-рынку,-в-штуках-и-в-денежном-выражении.-2.4.3"><span class="toc-item-num">2.4.3&nbsp;&nbsp;</span>Динамика продаж по рынку, в штуках и в денежном выражении.</a></span></li><li><span><a href="#Посмотрим-детальнее-на-динамику,-по-типам:-брендов,-топлива,-приводу,-классу,-региону,-автоцентру-и-сегменту" data-toc-modified-id="Посмотрим-детальнее-на-динамику,-по-типам:-брендов,-топлива,-приводу,-классу,-региону,-автоцентру-и-сегменту-2.4.4"><span class="toc-item-num">2.4.4&nbsp;&nbsp;</span>Посмотрим детальнее на динамику, по типам: брендов, топлива, приводу, классу, региону, автоцентру и сегменту</a></span><ul class="toc-item"><li><span><a href="#Бренд" data-toc-modified-id="Бренд-2.4.4.1"><span class="toc-item-num">2.4.4.1&nbsp;&nbsp;</span>Бренд</a></span></li><li><span><a href="#Автоцентр" data-toc-modified-id="Автоцентр-2.4.4.2"><span class="toc-item-num">2.4.4.2&nbsp;&nbsp;</span>Автоцентр</a></span></li><li><span><a href="#Регион" data-toc-modified-id="Регион-2.4.4.3"><span class="toc-item-num">2.4.4.3&nbsp;&nbsp;</span>Регион</a></span></li><li><span><a href="#Тип-топлива" data-toc-modified-id="Тип-топлива-2.4.4.4"><span class="toc-item-num">2.4.4.4&nbsp;&nbsp;</span>Тип топлива</a></span></li><li><span><a href="#Класс" data-toc-modified-id="Класс-2.4.4.5"><span class="toc-item-num">2.4.4.5&nbsp;&nbsp;</span>Класс</a></span></li><li><span><a href="#Привод" data-toc-modified-id="Привод-2.4.4.6"><span class="toc-item-num">2.4.4.6&nbsp;&nbsp;</span>Привод</a></span></li><li><span><a href="#Сегмент" data-toc-modified-id="Сегмент-2.4.4.7"><span class="toc-item-num">2.4.4.7&nbsp;&nbsp;</span>Сегмент</a></span></li></ul></li><li><span><a href="#Исследование-средних-показателей-по-брендам-и-маркам" data-toc-modified-id="Исследование-средних-показателей-по-брендам-и-маркам-2.4.5"><span class="toc-item-num">2.4.5&nbsp;&nbsp;</span>Исследование средних показателей по брендам и маркам</a></span></li><li><span><a href="#Емкость-рынка" data-toc-modified-id="Емкость-рынка-2.4.6"><span class="toc-item-num">2.4.6&nbsp;&nbsp;</span>Емкость рынка</a></span></li><li><span><a href="#Оценим-долю-рынка-на-примере-компании-mercur-auto" data-toc-modified-id="Оценим-долю-рынка-на-примере-компании-mercur-auto-2.4.7"><span class="toc-item-num">2.4.7&nbsp;&nbsp;</span>Оценим долю рынка на примере компании mercur auto</a></span><ul class="toc-item"><li><span><a href="#Расчет-общей-доли-на-рынке-у-mercur-auto-(количественном-и-стоимостном-выражении)" data-toc-modified-id="Расчет-общей-доли-на-рынке-у-mercur-auto-(количественном-и-стоимостном-выражении)-2.4.7.1"><span class="toc-item-num">2.4.7.1&nbsp;&nbsp;</span>Расчет общей доли на рынке у mercur auto (количественном и стоимостном выражении)</a></span></li><li><span><a href="#Hасчета-доли-рынка-mercur-auto-по-маркам" data-toc-modified-id="Hасчета-доли-рынка-mercur-auto-по-маркам-2.4.7.2"><span class="toc-item-num">2.4.7.2&nbsp;&nbsp;</span>Hасчета доли рынка mercur auto по маркам</a></span></li><li><span><a href="#Рассчитаем-долю-рынка-mercur-auto-по-классам" data-toc-modified-id="Рассчитаем-долю-рынка-mercur-auto-по-классам-2.4.7.3"><span class="toc-item-num">2.4.7.3&nbsp;&nbsp;</span>Рассчитаем долю рынка mercur auto по классам</a></span></li></ul></li><li><span><a href="#Рассчет-для-mercur-auto-в-части-конкурентов" data-toc-modified-id="Рассчет-для-mercur-auto-в-части-конкурентов-2.4.8"><span class="toc-item-num">2.4.8&nbsp;&nbsp;</span>Рассчет для mercur auto в части конкурентов</a></span><ul class="toc-item"><li><span><a href="#Определение-ближайших-конкурентов-для-&quot;mercur-auto&quot;:" data-toc-modified-id="Определение-ближайших-конкурентов-для-&quot;mercur-auto&quot;:-2.4.8.1"><span class="toc-item-num">2.4.8.1&nbsp;&nbsp;</span>Определение ближайших конкурентов для "mercur auto":</a></span></li><li><span><a href="#Распределение-продаж-по-месяцам-или-годам-для-'mercur-auto'-и-их-основных-конкурентов" data-toc-modified-id="Распределение-продаж-по-месяцам-или-годам-для-'mercur-auto'-и-их-основных-конкурентов-2.4.8.2"><span class="toc-item-num">2.4.8.2&nbsp;&nbsp;</span>Распределение продаж по месяцам или годам для 'mercur auto' и их основных конкурентов</a></span></li><li><span><a href="#Распределение-продаж-по-регионам,-брендам-и-классам" data-toc-modified-id="Распределение-продаж-по-регионам,-брендам-и-классам-2.4.8.3"><span class="toc-item-num">2.4.8.3&nbsp;&nbsp;</span>Распределение продаж по регионам, брендам и классам</a></span></li></ul></li></ul></li><li><span><a href="#Итоговые-выводы." data-toc-modified-id="Итоговые-выводы.-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span><font face="liberation serif" size="5">Итоговые выводы.</font></a></span></li></ul></li></ul></div>

# # <font face='liberation serif' size=5>Описание проекта</font>
# 
# <font face='liberation serif' size=4>*Проект от Мастерской Яндекс - "Исследование авторынка Казахстана". Для исследования используются данные за 2019 год.*</font>

# ## <font face='liberation serif' size=4>Описание данных.</font>
# 
# <font face='liberation serif' size=4>Датасет с данными по продажам автомобилей в Казахстане за 2019 год. Данные получены из
# официальной статистики VAG, после перевода из эксель в csv обнаружились множественные
# проблемы с исходными данными: некорректные разделители десятичных разрядов, несоответствие
# данных типу данных. Дополнительной проблемой является то, что статистику собирал не один
# человек, поэтому есть неявные дубликаты - например, 4WD, 4 WD и 4-WD, а также одни и те же
# признаки могут быть записаны как на русском, так и на английском языке. Также необходимо
# очистить датасет от лишних столбцов, которые используют технические специалисты, но которые не
# нужны в управленческом учете.</font>
# 
# <font face='liberation serif' size=4>
#     
# - Год – год продажи;   
# - Месяц – месяц продажи;
# - Компания – название автоцентра;
# - Бренд – название продаваемой марки автомобиля;
# - Модель – название модели автомобиля;
# - Модификация – модификация модели автомобиля;
# - Год выпуска – год производства автомобиля;
# - Страна-производитель – страна, где произведен автомобиль;
# - Вид топлива – вид топлива, который использует автомобиль;
# - Объём двиг л – объем двигателя автомобиля в литрах;
# - Коробка передач – тип коробки переключения передач;
# - Тип привода – тип привода автомобиля;
# - Сегмент – сегмент, к которому относится автомобиль;
# - Регион – регион продажи;
# - Наименование дилерского центра – наименование автоцентра;
# - Тип клиента – юридическое или физическое лицо;
# - Форма расчета – наличный и безналичный расчет;
# - Количество – количество автомобилей в заказе;
# - Цена USD – цена автомобиля в долларах США;
# - Продажа USD – цена заказа (цена авто умноженная на количество и за вычетом скидок если есть);
# - Область – область продажи;
# - Сегментация 2013 – сегмент автомобиля актуальный;
# - Класс 2013 – класс автомобиля актуальный;
# - Сегментация Eng – английская сегментация;
# - Локализация производства – где произведен автомобиль;
# 
# Признаки-категории:
# - сегмент
# - класс
# - тип привода
# - коробка передач</font>

# ## <font face='liberation serif' size=4>Описание задачи</font>
# 
# <font face='liberation serif' size=4>*Вводная:* Вы являетесь аналитиком в компании <font color='darkblue'><b>ORBIS AUTO</b></font> и перед вами стоят следующие задачи при проведении исследования предоставленного датасета:
# 
# <font face='liberation serif' size=4>
#     
# 1. Очистить данные.
# 2. Исследовательский анализ данных:
#     - Столбцы;
#     - Строки;
#     - Анализ дубликатов;
#     - Анализ пропусков;
#     - Проанализировать тип данных в каждом столбце, используя python типы и экспертные знания; 
#     - Изменение типа данных и кодирование переменных;
#     - Анализ числовых признаков;
#     - Анализ категориальных признаков.
# 3. Проанализировать рынок.
# 4. Посчитать показатели:
#     - Прибыль и выручка
#     - Рынок
#     - Конкуренты
# 5. Сделать выводы / дать рекомендации</font>

# # <font face='liberation serif' size=5>Общая подготовка
# <font face='liberation serif' size=4>Установка библиотек</font>

# In[1]:


#!pip install tabulate
#plt.close('all')
#!pip install pandas_profiling
#!pip install gdown


# <font face='liberation serif' size=4>Обновление библиотек</font>

# In[2]:


#!pip install -qU pandas seaborn
#!pip install -qU pandas
#!pip install -qU seaborn


# <font face='liberation serif' size=4>Загрузка библиотек</font>

# In[3]:


import pandas as pd
import numpy as np
import re
from math import ceil
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib import colors
import plotly.graph_objects as go
import plotly.express as px
from scipy.stats import gaussian_kde
from plotly.subplots import make_subplots
from scipy.optimize import curve_fit
import seaborn as sns
from tabulate import tabulate
from typing import NoReturn
from scipy import stats as st
from scipy.stats import mannwhitneyu
from statistics import mode
from scipy.stats import ks_2samp
from scipy.stats import mode
from sklearn.preprocessing import LabelEncoder
from pandas_profiling import ProfileReport
import gdown
import warnings
warnings.filterwarnings("ignore")


# <font face='liberation serif' size=4>Настройка параметров</font>

# In[4]:


# опции картинок 
plt.rcParams["font.family"] = "Arial"
plt.rcParams['figure.figsize'] = (15, 8) 


# In[5]:


# опции табличек 
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_colwidth', 1000)


# In[6]:


try:
    data = pd.read_csv('/Users/PC_Maks/Desktop/study/workshop_yandex/kz_2019_final_all_dirt.csv',sep = ",", index_col=0)
    
except: 
    url = 'https://drive.google.com/uc?id=168eBeLZX8qZ2be1f6xdO1DXYd_GlpZT7'
    file_path = 'data.csv'
    gdown.download(url, file_path)
    data = pd.read_csv(file_path, sep=',', index_col=0)


# In[7]:


data.sample(10)


# In[8]:


data.info()


# <font face='liberation serif' size=4>Имеются пропуски, будем решать что с ними делать по мере проведения исследования, а вот типы данных поправим сейчас

# <font face='liberation serif' size=4>Для начала приведем названия столбцов к питоническому формату, а потом обработаем столбцы "год" и "месяц" 

# In[9]:


def data_preprocessing(data):
    """
    Производит предварительную обработку данных, модифицируя заголовки столбцов и строковые значения.

    Параметры:
    - data (DataFrame): исходный DataFrame, который требуется предобработать.

    Основные шаги функции:
    1. Преобразует заголовки столбцов к нижнему регистру и заменяет пробелы на нижние подчеркивания.
    2. Преобразует строковые значения всех столбцов к нижнему регистру.

    Возвращает:
    - DataFrame: предобработанный DataFrame с модифицированными заголовками столбцов и строковыми значениями.

    Пример:
    >>> data = pd.DataFrame({"First Name": ["John", "JANE"], "Last Name": ["DOE", "SMITH"]})
    >>> data_preprocessing(data)
       first_name last_name
    0       john       doe
    1       jane     smith
    """

    data.columns = data.columns.str.lower().str.replace(' ', '_')
    data = data.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

    return data


# In[11]:


data = data_preprocessing (data)


# In[12]:


data.info()


# In[13]:


month_dict = {
    'январь': '01',
    'февраль': '02',
    'март': '03',
    'апрель': '04',
    'май': '05',
    'июнь': '06',
    'июль': '07',
    'август': '08',
    'сентябрь': '09',
    'октябрь': '10',
    'ноябрь': '11',
    'декабрь': '12'
}

data['месяц'] = data['месяц'].map(month_dict)

data['дата'] = pd.to_datetime(data['год'].astype(str) + '-' + data['месяц'], format='%Y-%m')


# In[14]:


# удалим сразу старые столбцы 'год' и 'месяц', а также столбцы которые нам не потребуются для исследования
# "модификация", "сегмент", "наименование_дилерского_центра", "форма_расчета", "сегментация_eng", "локализация_производства"
data.drop(columns=['год', 'месяц', 'модификация', 'сегмент', 'наименование_дилерского_центра', 'форма_расчета',                   'сегментация_eng', 'тип_клиента', 'область', 'локализация_производства'], inplace=True)


# <font face='liberation serif' size=4>Скорректируем название столбцов, для удобства

# In[15]:


data.shape


# In[16]:


data.columns


# In[17]:


data = data.rename(columns={'страна-производитель': 'страна_производитель', 'вид_топлива': 'топливо',                        'объём_двиг,_л,':'объем_двигателя', 'цена,_usd':'цена',                        'продажа,_usd':'продажа', 'сегментация_2013':'сегментация', 'класс_2013':'класс'})


# In[18]:


old_cols=data.columns.tolist()
new_cols = ['company',
 'brand',
 'model',
 'year_of_production',
 'country',
 'fuel',
 'engine',
 'transmission',
 'drive_type',
 'region',
 'quantity',
 'price',
 'sale',
 'segmentation',
 'class_2013', 
           'date'
]

cols_change_dict = {i: v for i, v in zip (old_cols, new_cols)}
data.rename(columns=cols_change_dict, inplace=True)


# <font face='liberation serif' size=4>Проведем замену названий на более удобные в использовании, с учетом питонического формата

# In[19]:


data.shape


# ## Используем стандартные проверки, с использованием шаблонных функций (заготовки прошлых периодов)

# ### Изучим наполнение датасета 

# In[20]:


def check_unique(data):
    """
    Выводит уникальные значения и их количество для строковых столбцов, 
    диапазон значений для числовых и даты/времени столбцов, а также уникальные значения 
    для числовых столбцов, где уникальных значений не более 10.

    Параметры:
    - data (DataFrame): DataFrame, значения которого необходимо проверить.

    Возвращает:
    - None: Функция выводит информацию напрямую в ячейку выполнения кода.

        """
    for col in data.select_dtypes(include=['object']):
        print(f"Уникальные значения в столбце {col}:")
        print(data[col].unique())
        print(f"Количество уникальных значений: {data[col].nunique()}")
        print('---------------------')

    for col in data.select_dtypes(include=['datetime64', 'float64', 'int64']):
        print(f"Диапазон значений в столбце {col}:")
        print(f"Минимальное значение: {data[col].min()}")
        print(f"Максимальное значение: {data[col].max()}")
        print('---------------------')

    for col in data.select_dtypes(include=['int64', 'float64']):
        if len(data[col].unique()) > 10:
            print(f"В столбце {col} более 10 уникальных значений")
        else:
            print(f"Уникальные значения в столбце {col}:")
            print(data[col].unique())
        print(f"Количество уникальных значений: {data[col].nunique()}")
        print('---------------------')


# In[21]:


check_unique(data)


# <font face='liberation serif' size=4>Пропусков хватает((( посмотрим внимательнее на проспуски

# ### Провека на очевидные дубликаты и пропуски 

# In[22]:


def check(data):
    """
    Проверяет DataFrame на наличие дубликатов и пропусков, выводит соответствующую информацию.
    В случае наличия дубликатов удаляет их из исходного датасета.

    Параметры:
    - data (DataFrame): DataFrame, который необходимо проверить.

    Возвращает:
    - None: Функция выводит информацию напрямую в консоль.
    Прим. Удаление дубликатов отключено в данном проекте, с учетом комментариев тимлида об уникальности данных.
    
    """
    try:
        
        display('Проверка на дубликаты:')
        duplicates = data.duplicated()
        duplicate_rows = data.loc[duplicates]
        display(duplicate_rows.info())
        display(duplicate_rows.sample())
        display('----------------------')
        display('Пропуски:')
        display(data.isna().sum())
        display('Пропуски в процентном отношении к всему датасету:')
        display(data.isna().sum() / len(data) * 100)

        
    except Exception as e:
        print(f'ERROR: {e}')


# In[23]:


check(data)


# <font face='liberation serif' size=4>Несмотря на, результаты проверки на дубли (15К), взяв во внимание уточнение от тех, кто формировал выгрузку, что дублей по VIN не было, считаем что все авто уникальные.
# сейчас принимаю решение попробовать заполнить пропуски с учетом имеющихся данных (взять модели авто и год выпуска, и по аналогии с имеющимися данными заполнить пропуски в топливе, объеме, типе КПП, привода), допускаю некоторую неточность, но учитывая что в указанных столбцах пропуски не превышают 6%, считаю это допустимым. но для начала нужно "причесать" столбцы с пропусками

# ## <font face='liberation serif' size=5>Обработка пропусков.</font>

# ### Объем двигателя.
# <font face='liberation serif' size=4>Прийдется использовать функцию, но для начала подготовим данные, выставим заглушку и заменим тип на float

# In[24]:


def process_volume(volume):
    """
    Обрабатывает значения объема (двигателя), приводя их к стандартному формату.

    Функция выполняет следующие действия:
    - Убирает ненужные символы.
    - Преобразует значения, указанные в миллилитрах, в литры.
    - Заменяет пропуски или значения, равные 0, на 77.
    
    Параметры:
    - volume (str, int, float): Значение объема, которое необходимо обработать.

    Возвращает:
    - float: Обработанное значение объема в литрах с округлением до десятых.
    """
    if isinstance(volume, str):
        
        volume = re.sub(r'[^\d.,]', '', volume)
        volume = re.sub(',', '.', volume)
        if '.' not in volume and len(volume) > 3:
            volume = float(volume) / 1000
        else:
            volume = float(volume)

        volume = round(volume, 1)

    elif (isinstance(volume, int) or isinstance(volume, float)) and not np.isnan(volume):
        if volume > 100:  # Если значение указано в миллилитрах
            volume /= 1000

        volume = round(volume, 1)

    # Заменяем пропуски на значение 77
    if pd.isnull(volume) or volume == 0:
        volume = 77

    return volume


# In[25]:


data.engine = data.engine.apply(process_volume)
data.engine = data.engine.astype (float)
data.engine.unique()


# In[26]:


temp = data.engine.value_counts ().reset_index(drop=False)
temp.sort_values (by='engine', ascending = False).reset_index(drop=True).head(1)


# <font face='liberation serif' size=4>Теперь можем приступить к заполнению пропусков (заглушек - 77)

# In[27]:


# Замена всех 77 на NaN в столбце 'объем_двигателя'
data.engine.replace(77, np.nan, inplace=True)

# Группировка данных по модели и году выпуска
grouped = data.groupby('model')

# Заполнение пропусков в столбце 'объем_двигателя' минимальным значением по группам
data.engine = grouped['engine'].transform(lambda x: x.fillna(x.min())).round(1)
# выставим обратно заглушки на те значения, которые не заполнили в итоге
data.engine.fillna(77, inplace=True)


# In[28]:


temp = data.engine.value_counts ().reset_index(drop=False)
temp.sort_values (by='engine', ascending = False).reset_index(drop=True).head(1)


# <font face='liberation serif' size=4>Удалось заполнить только 1032 (пропуски и нули) значений, что тоже не плохо, мы снизили с 5.96 до 3,4 пропуски, остальное можем срезать

# In[29]:


data = data.query('engine<50')
data.engine.unique()


# ### Год выпуска.
# <font face='liberation serif' size=4>Пропуски в году выпуска, менее 1%, сильной роли не сыграют, но чтобы не терять даже эти данные, заменим на минимальные значение от модели

# In[30]:


data.year_of_production.unique()


# In[31]:


data.year_of_production = data.year_of_production.replace('\xa0', ' ', regex=True)
data.year_of_production = data.year_of_production.str.replace(' ', '')


# In[32]:


data.year_of_production.fillna(77, inplace=True)
data.year_of_production = data.year_of_production.astype (int)
#data = data.query('год_выпуска != 77')


# In[33]:


grouped = data.groupby ('model')['year_of_production'].agg (mode).reset_index(inplace=False)
grouped_exploded = grouped.explode('year_of_production')

grouped_exploded.year_of_production = grouped_exploded.year_of_production.apply(lambda x: x[0])

# Оставляем только столбцы 'модель' и 'год_выпуска'
grouped_processed = grouped_exploded[['model', 'year_of_production']]
grouped_processed = grouped_processed.query ('2000 < year_of_production <= 2019')
grouped_processed.year_of_production.unique()


# In[34]:


for index, row in grouped_processed.iterrows():
    # Выбираем соответствующую модель в основной таблице data
    model_fix = row['model']
    # Получаем значение года выпуска из grouped_processed
    year = row['year_of_production']
    
    # Обновляем значение года выпуска в основной таблице, если встречается 77
    data.loc[(data.model == model_fix) & (data.year_of_production == 77), 'year_of_production'] = year
    
data.year_of_production.replace(77, np.nan, inplace=True)    
    


# In[35]:


check (data)


# <font face='liberation serif' size=4>В результате манипуляций, количество пропусков в разделе год выпуска удалось снизить с 240 до 112, оставшиеся срезаем ( 0,35%)

# In[36]:


data = data.query ('year_of_production > 2000').reset_index (drop=True)


# In[37]:


grouped_processed.year_of_production.unique()


# ### Тип топлива
# 
# <font face='liberation serif' size=4>Сейчас пропусков 739, или 2,33%. Используем схему, которую использовали при обработке года выпуска

# In[38]:


check (data)


# In[39]:


data.fuel.unique()


# <font face='liberation serif' size=4>Изменять записи не нужно, только убрать пробелы

# In[40]:


data.fuel = data.fuel.str.replace(' ', '')
data.fuel.value_counts (dropna=False)


# <font face='liberation serif' size=4>Проведем кодировку через словарь (настало время костылей)

# In[41]:


fuel_dict = {
    'бензин': 'F',
    'дизель': 'D',
    'гибрид': 'HYB',
    'газовый': 'E',
    '0': 'not_defined'
}

data.fuel = data.fuel.map(fuel_dict)
data.fuel.fillna ('not_defined', inplace=True)
data.fuel.unique()


# In[42]:


grouped = data.groupby('model')['fuel'].agg (mode).reset_index(inplace=False)
grouped_exploded = grouped.explode('fuel')
grouped_exploded.fuel = grouped_exploded.fuel.apply(lambda x: x[0])


# In[43]:


list_code = ['F', 'D', 'HYB', 'E', 'not_defined']
grouped_exploded = grouped_exploded.query ('fuel in @list_code')
grouped_exploded.fuel.unique()


# In[44]:


for index, row in grouped_exploded.iterrows():
    # Выбираем соответствующую модель в основной таблице data
    model_fix = row['model']
    # Получаем значение типа топлива в grouped_exploded
    fuel_fix = row['fuel']
    
    # Обновляем значение топлива выпуска в основной таблице
    data.loc[(data.model == model_fix) & (data.fuel == 'not_defined'), 'fuel'] = fuel_fix
    
data.fuel.replace('not_defined', np.nan, inplace=True)  


# In[45]:


check (data)


# In[46]:


data.fuel.value_counts (dropna=False)


# In[47]:


data = data.dropna(subset='fuel').reset_index(drop=True)
data.fuel.unique()


# <font face='liberation serif' size=4>Получилось немного заполнить пропуски в разделе топливо, из 739 (2,33%) изначальных, осталось 289 (0,91%), остальное срезали. 

# ### Коробка передач
# <font face='liberation serif' size=4>Сейчас имеем 721 пропуск - 2.3%, используем знакомую схему со словарем, но для начала унифицируем типы, к пропускам отнесем также не указанные значения.

# In[48]:


check (data)


# In[49]:


data.transmission.fillna('0', inplace=True)
data.transmission.isna().sum ()


# In[50]:


data.transmission.unique()


# In[51]:


def replacing_transmission_type (cell: str) -> str:
    """
    Обработка значения коробки передач.

    Параметры:
    - cell (str): Исходное значение коробки передач.

    Возвращает:
    - str: 'mt' если коробка передач механическая,
           'at' если коробка передач автоматическая,
           'not_defined' если значение коробки передач не определено.
    """
    mechanical_keywords = ['мт', 'mт', 'мt', 'mt', 'м/т', 'm/т', 'm/t', 'м/t',                           'мех.', 'мппк', 'мкпп', 'механика', 'механическая', 'm', 'м']

    if cell in ['-', ' -', '0', 'n']:
        return 'not_defined'
    elif cell.lower() in mechanical_keywords:
        return 'mt'
    else:
        return 'at'

data.transmission = data.transmission.fillna('not_defined')
data.transmission = data.transmission.apply(replacing_transmission_type)


# In[52]:


data.transmission.unique()


# In[53]:


data.transmission.value_counts (dropna=False)


# <font face='liberation serif' size=4>Приступим к замене не определенных типов

# In[54]:


grouped = data.groupby ('model')['transmission'].agg (mode).reset_index(inplace=False)
grouped_exploded = grouped.explode('transmission')

grouped_exploded.transmission = grouped_exploded.transmission.apply(lambda x: x[0])

list_code = ['at','mt', 'not_defined']
grouped_exploded = grouped_exploded.query ('transmission in @list_code').reset_index(drop=True)


# In[55]:


for index, row in grouped_exploded.iterrows():
    # Выбираем соответствующую модель в основной таблице data
    model_fix = row['model']
    # Получаем значение типа топлива в grouped_exploded
    type_transm = row['transmission']
    
    # Обновляем значение топлива выпуска в основной таблице
    data.loc[(data.transmission == model_fix) & (data.transmission == 888),
             'transmission'] = type_transm


# In[56]:


data.transmission.value_counts (dropna=False)


# <font face='liberation serif' size=4>Убираем неопределившихся, а остальное возращаем к исходному виду

# In[57]:


data = data.query('transmission != "not_defined"').reset_index(drop=True)


# In[58]:


data.transmission.unique()


# In[59]:


data.shape


# <font face='liberation serif' size=4>В результате корректировок, нам удалось заменить 279 записей, из 829 изначальных пропусков/не определившихся, осталось 550 (срезаем 1,6%) 

# ### Тип привода
# <font face='liberation serif' size=4>Осталось разобраться с типом привода, сейчас класических 643 пропуска (2,08%), нужно еще посмотреть на нестандарные описания и число неизвестных значений веротяно изменится.
# 
# 'FWD' – передний привод
# 
# '4WD' – полный привод
# 
# 'RWD' – задний привод
# 
# '2WD’ – все остальное 

# In[60]:


check (data)


# In[61]:


data.drive_type.unique()


# <font face='liberation serif' size=4>будем использовать следующую схему распределения 
# 
# <font face='liberation serif' size=4>FWD (передний привод):
# 
# 'fwd'
# 'передний'
# 'передний ' (с пробелом в конце)
# 'ff'
# 
# <font face='liberation serif' size=4>4WD (полный привод):
# 
# 'quattro'
# '4wd'
# 'полный'
# 'awd'
# '4х4'
# '4x4'
# '4motion'
# 'полный ' (с пробелом в конце)
# '4х2.2'
# '4 wd'
# 'p/time'
# 
# <font face='liberation serif' size=4>RWD (задний привод):
# 
# 'rwd'
# 'задний'
# 'fr'
# 
# <font face='liberation serif' size=4>2WD (все остальное):
# 
# '2wd'
# '2 wd'
# '4x2'
# '4х2'
# '2х4'
# 'cvt'
# '0'
# 

# In[62]:


data.drive_type = data.drive_type.str.replace(' ', '')
data.drive_type.unique()


# In[63]:


data.drive_type.fillna('0', inplace=True)
data.drive_type.isna().sum ()


# In[64]:


def replacing_drive_type (cell: str) -> str:
    """
    Обработка значения типа привода автомобиля.

    Параметры:
    - cell (str): Исходное значение типа привода.

    Возвращает:
    - str: 'FWD' если привод передний,
           '2WD' если привод 2-х колёсный,
           'RWD' если привод задний,
           '4WD' если привод не определен или 4-х колёсный.
    """
    fwd_keywords = ['fwd', 'передний', 'ff']
    wd2_keywords = ['2wd', '4x2', '4х2', '2х4', 'cvt', '0']
    rwd_keywords = ['rwd', 'задний', 'fr']

    if cell in fwd_keywords:
        return 'FWD'
    elif cell in wd2_keywords:
        return '2WD'
    elif cell in rwd_keywords:
        return 'RWD'
    else:
        return '4WD'

data.drive_type = data.drive_type.apply(replacing_drive_type)


# In[65]:


data.drive_type.value_counts(dropna=False)


# <font face='liberation serif' size=4>Пропуски в приводе убрал.

# In[66]:


check (data)


# <font face='liberation serif' size=4>Осталось только удалить строки с пропускаи в столбце количество

# In[67]:


data=data.dropna().reset_index(drop=True)


# In[68]:


data.shape


# ### Итоги чистки
# 
# <font face='liberation serif' size=4>После всех чисток и замен, из 32854 изначальных строк, осталось 30504, или 93%. Приемлемо. Идем дальше

# ## <font face='liberation serif' size=5>Обработка типов.</font> 

# In[69]:


data.info()


# <font face='liberation serif' size=4>Заменим тип в "Количество", "Цена" и "Продажа" на int, такие тоные данные, как 6 знаков после запятой, нам не обязательны. 

# In[70]:


cols_to_int = ['price', 'sale', 'quantity', 'year_of_production']
data [cols_to_int] = data[cols_to_int].astype('int')


# In[71]:


#уберем пробелы в сегментации
data.segmentation = data.segmentation.str.strip()
data.class_2013 = data.class_2013.str.strip()
data.loc[data['class_2013'].str.contains('suv', case=False, na=False), 'class_2013'] = 'suv'


# In[72]:


# А столбцы fuel, transmission, segmentation, class сделаем категориальными
cols_to_int = ['fuel', 'transmission', 'segmentation', 'class_2013']
data [cols_to_int] = data[cols_to_int].astype('category')


# In[73]:


data.info()


# ### Кодировка стран

# In[74]:


data.country.unique ()


# In[75]:


# делаем резервную копию датасета
data2 = data.copy(deep = True)


# In[76]:


try:
    countries_codes = (pd.read_table('https://www.artlebedev.ru/country-list/', encoding='utf8')[0]
                       [['Наименование', 'Полное наименование', 'Alpha3']].\
                       rename(columns={'Наименование':'name', 'Полное наименование':'full_name'}))
    
except:
    countries_codes = pd.read_table('https://www.artlebedev.ru/country-list/tab/')


# In[77]:


countries_codes = data_preprocessing(countries_codes)


# <font face='liberation serif' size=4>До слияния кодировок, нужно внести правки в названия, например корея - учитывая что есть северная и июная, нужно скорректировать название.

# In[78]:


data.country = data.country.replace('корея', 'республика корея')
data.country = data.country.replace('белоруссия', 'беларусь')


# In[79]:


shortname_list = countries_codes.name.tolist()
fullname_list = countries_codes.fullname.tolist()
alpha_3 = countries_codes.alpha3.tolist()

# Создаем словари из списков
shortname_dict = {k: v for k, v in zip(shortname_list, alpha_3)}
fullname_dict = {k: v for k, v in zip(fullname_list, alpha_3)}

# Объединяем два словаря
final_dict = shortname_dict.copy()  # начинаем с копии первого словаря
for k, v in fullname_dict.items():
    if k not in final_dict.keys():
        final_dict[k] = v


# In[80]:


data.country = data.country.apply(lambda cell: final_dict.get(cell, cell))


# In[81]:


data.country.unique ()


# ## <font face='liberation serif' size=5>Анализ данных.</font>  

# <font face='liberation serif' size=4>Учитывая датасет с которым подошли к этапу анализа, пришло время посмотреть на числовые значения, в том числе на выбросы

# In[82]:


data.describe ()


# ### Визуализация даных для исследования

# In[83]:


def plot_distribution_and_box(data, columns):
    """
    Отображает гистограмму распределения и ящик с усами (Box plot) для указанных столбцов датасета.

    Эта функция использует Plotly для создания интерактивных графиков. Она предназначена для анализа 
    распределения значений в столбцах датасета. Для каждого указанного столбца функция выводит два графика: 
    гистограмму с линией плотности ядерной оценки (KDE) и ящик с усами.

    Параметры:
    - data (DataFrame): DataFrame, содержащий данные для анализа.
    - columns (list): Список столбцов, для которых необходимо создать графики.
    """
    for column in columns:
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        fig.add_trace(go.Histogram(x=data[column], nbinsx=25, histnorm='probability', name='Распределение', marker_color='steelblue'), secondary_y=False)
        fig.update_layout(title=f'Распределение значений в столбце {column}', xaxis_title=column, yaxis_title='Частота')
        fig.update_layout(xaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='lightgray'), yaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='lightgray'))
        
        kde = gaussian_kde(data[column])
        x_vals = sorted(data[column])
        y_vals = kde(x_vals)
        
        fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', line=dict(color='red', width=2), name='KDE'), secondary_y=True)
        fig.update_yaxes(title_text="Частота", secondary_y=False)
        fig.update_yaxes(title_text="Плотность", secondary_y=True)
        
        fig.show()
        
        fig = go.Figure()
        fig.add_trace(go.Box(x=data[column], name='Ящик с усами', marker_color='steelblue'))
        fig.update_layout(title=f'Ящик с усами для столбца {column}', xaxis_title=column)
        fig.update_layout(xaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='lightgray'), yaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='lightgray'))
        
        fig.show()


# In[84]:


columns_to_plot = ['price', 'engine', 'year_of_production', 'quantity']
plot_distribution_and_box(data, columns_to_plot)


# <font face='liberation serif' size=4>"Год производства" - в основном все машины 2018 года, 
# 
# <font face='liberation serif' size=4>медиативный объем двигателя 2 литра, в среднем 2.25, основная масса в пределах 3 литров, есть автомобили с объемом 17.5 (вероятно, автобусы или грузовики), 
# 
# <font face='liberation serif' size=4>"количество" - в основном покупают по 1 авто, но есть странные значения, в частности, 91 автомобиль (кто-то открывал такси?), большинство значений в диапазоне 1-4 
# 
# <font face='liberation serif' size=4>"цена" - подавляющее большинство автомобилей стоимостью в пределах 40000, аномальная высокая цена в 254958, могу пока предположить это стоимость всех авто для найденного ранее "таксопарка"
# 

# <font face='liberation serif' size=4>Посмотрим на распределение в части типов привода, топлива и КП и т.п.

# In[85]:


def category_plot(data, columns):
    """
    Отображает столбчатые диаграммы для категориальных переменных датасета в зависимости от их частоты.

    Эта функция использует Plotly для создания интерактивных графиков. Она предназначена для визуализации
    частоты уникальных значений категориальных переменных. Для каждого указанного столбца функция создает
    столбчатую диаграмму, отсортированную по убыванию частоты.

    Параметры:
    - data (DataFrame): DataFrame, содержащий данные для анализа.
    - columns (list): Список категориальных столбцов, для которых необходимо создать графики.
    """
    for c in columns:
        group_data = data.pivot_table(index=c, values='price', aggfunc='count').reset_index()
        group_data = group_data.sort_values(by='price', ascending=False)
        
        fig = make_subplots(specs=[[{"secondary_y": False}]])
        
        fig.add_trace(go.Bar(x=group_data[c], y=group_data['price'], name='Количество', marker_color='steelblue'))
        fig.update_layout(title=f'График распределение по типу {c}', xaxis_title=c, yaxis_title='Количество')
        fig.update_layout(xaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='lightgray'), yaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='lightgray'))
        
        fig.show()


# In[86]:


columns_to_plot = ['country', 'fuel', 'transmission', 'drive_type', 'segmentation', 'class_2013']
category_plot (data, columns_to_plot)


# <font face='liberation serif' size=4>Пока отмечаем аномалии и всплески, разбирать их будем чуть позже, сейчас займемся проверкой корреляции И расчетом ТОПов.

# ### Топ продаж по медиативной цене и количество проданных авто

# #### Срез для выявления покупок для частных целей, и визуализация результатов
# <font face='liberation serif' size=4>Перед расчетом, необходимо сначала исключить таксопарки, коммерческие закупки. Исходя из логики, могу сделать обоснованное предположение, что если покупается больше 2-х машин за один раз, то это маловероятно для частного использования, а также можно исключить сегмент - коммерческие автомобили, когда указано в явном виде 

# In[87]:


personal_data = data.query ('quantity <=2 and segmentation != "коммерческие автомобили"')


# In[88]:


personal_data.segmentation = personal_data.segmentation.astype ('object')
personal_data.segmentation.unique ()


# In[89]:


personal_data.class_2013 = personal_data.class_2013.astype ('object')
personal_data.class_2013.unique ()


# In[90]:


# посмотрим еще раз на визуализацию после выделенния "частных" покупок
columns_to_plot = ['country', 'fuel', 'transmission', 'drive_type', 'segmentation', 'class_2013']
category_plot (personal_data, columns_to_plot)


# <font face='liberation serif' size=4>Как можем отметить, самые популярные - внедорожники, на втором месте легковые авто, в основном продаются автомобили на бензине, с коробкой автомат, и с полным приводом. Если смотреть на класс - то самый популярный suv - по сути внедорожник городского типа, так называемый паркетник.

# In[91]:


columns_to_plot = ['price', 'engine', 'year_of_production', 'quantity']
plot_distribution_and_box(personal_data, columns_to_plot)


# <font face='liberation serif' size=4>Медиативное значение объема двигателя, после фильтрации, 2 литра, 
# цена в диапазоне от 15 до 35 тысяч долларов 

# #### Топ-10 бренды по количеству приобретенных авто

# In[92]:


group_brand = personal_data.groupby ('brand').agg({'sale':'sum', 'quantity':'sum'}).reset_index ().sort_values(by ='quantity', ascending = False)


# In[93]:


top_brands = group_brand.reset_index(drop=True).head (10)
top_brands


# In[94]:


top_brands_sale = group_brand.sort_values(by ='sale', ascending = False).reset_index(drop=True).head (10)
top_brands_sale


# <font face='liberation serif' size=4>Самая популярная марка - тойота, на втором месте хендай, и тройку лидеров замыкает ravon. 
# 
# <font face='liberation serif' size=4>А в части самой высокой выручки, первое место занимает ожидаемо тайота (очень большое количество продаж).

# ### Динамика продаж по рынку, в штуках и в денежном выражении.

# <font face='liberation serif' size=4>сначала посмотрим на общие продажи по дням

# In[95]:


def plot_dinamic (data, column1, column2, task=1):
    """
    Отображает динамику указанного столбца по датам. В зависимости от значения `task` может разделить линии по 
    значениям другого столбца или предоставить агрегированное представление.

    Эта функция использует Plotly Express для создания интерактивных линейных графиков. Она предназначена для 
    визуализации динамики указанного столбца (column2) по датам с возможностью разделения линий на основе значений 
    другого столбца (column1).

    Параметры:
    - data (DataFrame): DataFrame, содержащий данные для анализа.
    - column1 (str): Имя столбца, по которому, возможно, будет производиться разделение линий.
    - column2 (str): Имя столбца, агрегированное значение которого будет отображено на графике.
    - task (int, optional): Если равно 1, будет показана общая динамика column2. Если отличается от 1, 
                            график будет разделен по значениям column1. По умолчанию равно 1.
    """
    if task == 1:
        quantity_by_date = data.groupby(['date'])[column2].sum().reset_index()
        fig = px.line(quantity_by_date, x='date', y=column2, title=f'Распределение {column2} по месяцам')
        fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(buttons=list([
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])))
        fig.show()
    else:
        quantity_by_date = data.groupby(['date', column1])[column2].sum().reset_index()

        fig = px.line(quantity_by_date, x='date', y=column2, color=column1, title=f'Распределение {column2} по {column1} и месяцам')
        fig.update_xaxes(rangeslider_visible=True)
        fig.show()


# In[96]:


plot_dinamic (personal_data, 'quantity', 'quantity', task=1)


# <font face='liberation serif' size=4>Как видно из графика, пик продаж приходится на июнь 2019 года - 3467 приобретено автомобилей, а если взять более большой отрезок, то можно отметить общую активность покупателей на период с мая по сентябрь включительно. В июле значения немного снижаются, но могу предположить, что сезон отпусков и в авторынке имеет свой вес.

# In[97]:


plot_dinamic (personal_data, 'sale', 'sale', task=1)


# <font face='liberation serif' size=4>При анализе продаж в денежном выражении выявлена интересная динамика: в августе количество проданных автомобилей почти совпадает с их пиковым значением в июне. Однако общая стоимость приобретенных автомобилей в августе заметно ниже, даже по сравнению с маем. Это может свидетельствовать о том, что в августе покупатели приобретали автомобили более низкого ценового сегмента или модели дешевле.

# ### Посмотрим детальнее на динамику, по типам: брендов, топлива, приводу, классу, региону, автоцентру и сегменту

# #### Бренд

# In[98]:


data_subset_units = personal_data[personal_data['brand'].isin(top_brands.brand)]
plot_dinamic (data_subset_units, 'brand', 'quantity', task=2)


# In[99]:


plot_dinamic (data_subset_units, 'brand', 'sale', task=2)


# <font face='liberation serif' size=4>Лидеры по Продажам:
# 
#     - Toyota: Безоговорочный лидер по количеству проданных автомобилей на всем периоде наблюдения. Доход от продаж данного бренда также является наивысшим, достигая пика в более 61 млн.
#     - Hyundai: На втором месте по количеству продаж, однако по доходу занимает третье место после Toyota и Lexus. Интересно, что в апреле Hyundai уступал по доходам Lexus.
# 
# <font face='liberation serif' size=4>Бренды с Высоким Ценовым Сегментом:
# 
#     - Lexus: При меньшем количестве проданных автомобилей показывает высокий уровень дохода. Это говорит о том, что бренд сконцентрирован на премиум-сегменте рынка.
# 
# <font face='liberation serif' size=4>Бренды с Низким Ценовым Сегментом:
# 
#     - Ravon: На начальном этапе показывает внушительные продажи, однако после февраля 2019 года их продажи резко снижаются. К концу исследуемого периода продажи данного бренда практически исчезают.
# 
# 
# <font face='liberation serif' size=4>Общие Наблюдения:
# 
#     - Toyota имеет сильное влияние на рынок, так как общая динамика продаж автомобилей совпадает с графиком продаж данного бренда.
#     - Бренды Ravon и Lada сконцентрированы на бюджетном сегменте, так как при сравнительно высоком количестве продаж их доход меньше других брендов.
#     - Бренды JAC, Nissan, Renault, Volkswagen, и Chevrolet не показывают выдающихся результатов как по количеству, так и по доходу от продаж.
# 
# 
# <font face='liberation serif' size=4>Выводы показывают, что рынок автомобилей в Казахстане доминируется некоторыми ключевыми игроками, в то время как другие бренды занимают ниши или более низкие сегменты рынка. При принятии решений о запуске нового автосалона или расширении действующего бизнеса, необходимо учитывать эти данные для эффективного позиционирования и определения стратегии.

# #### Автоцентр

# In[100]:


group_brand = personal_data.groupby ('company').agg({'sale':'sum', 'quantity':'sum'}).reset_index ().sort_values(by ='quantity', ascending = False)
group_brand.sale = group_brand.sale.round (1)
top_company = group_brand.reset_index(drop=True).head (10)
top_company


# <font face='liberation serif' size=4>Ожидаемый лидер - официальный дилер тойота - почти 30% всех продаж, с целью более корректного исследования, исключим данного дилера из рейтинга 

# In[101]:


group_brand_no_toyota = group_brand.query ('company != "toyota motor kazakhstan"')
top_company_units = group_brand_no_toyota.reset_index(drop=True).head (10)
top_company_units


# In[102]:


data_subset_units = personal_data[personal_data.company.isin(top_company_units.company)]

plot_dinamic (data_subset_units, 'company', 'quantity', task=2)
plot_dinamic (data_subset_units, 'company', 'sale', task=2)


# <font face='liberation serif' size=4>Динамика продаж:
# 
# <font face='liberation serif' size=4>Узавто-Казахстан: Начинает как лидер продаж, однако со временем их продажи резко снижаются. Это указывает на возможные внутренние или внешние проблемы у компании.
# Astana-motors: С января 2019 года становится непререкаемым лидером рынка и удерживает это положение до сентября 2019 года. Отставание остальных участников составляет в 2-3 раза по выручке. Пик продаж этой компании приходится на май 2019 года с выручкой более 18 млн.
# Внешние факторы:
# 
# <font face='liberation serif' size=4>По данным из сети, Узавто-Казахстан сменил свою политику, увеличив экспорт популярных моделей, таких как Chevrolet Cobalt, даже при наличии спроса на внутреннем рынке. Это может объяснить снижение их продаж в Казахстане.
# Медианный чек:
# 
# <font face='liberation serif' size=4>Subaru Kazakhstan лидирует среди всех участников рынка по медианному чеку, достигая пика в 2,77 млн. 
# 
# <font face='liberation serif' size=4>Прим. удалось найти в сети информацию, что политика компании Узавто-Казахстан менялась, а именно был увеличен экспорт самых популярных моделей - шевроле кобальт, несмотря на, очереди на внутреннм рынке, могу предположить, что снижение продаж на рынке Казахстана связано именно с данными изменениями. 
# 

# #### Регион

# In[103]:


group_brand = personal_data.groupby ('region').agg({'sale':'sum', 'quantity':'sum'}).reset_index ().sort_values(by ='quantity', ascending = False)

top_company_units = group_brand.reset_index(drop=True).head (10)
display (top_company_units)

data_subset_units = personal_data[personal_data.region.isin(top_company_units.region)]


# In[104]:


plot_dinamic (data_subset_units, 'region', 'quantity', task=2)
plot_dinamic (data_subset_units, 'region', 'sale', task=2)


# <font face='liberation serif' size=4>Лидеры продаж:
# 
# <font face='liberation serif' size=4>Алматы и Астана являются абсолютными лидерами по продажам автомобилей на изучаемом отрезке. Эти города существенно превосходят другие регионы как по количеству продаж, так и по их объему в денежном выражении.
# Сравнивая их с другими участниками рейтинга, объем продаж в Алматы и Астане вместе взятых превышает объем продаж в остальных городах из ТОПа.
# 
# <font face='liberation serif' size=4>Характеристика рынков:
# 
# <font face='liberation serif' size=4>Алматы: Наиболее активный регион с точки зрения продаж. Высокие показатели, вероятно, обусловлены большим населением, активной экономикой и большим количеством бизнесов.
# Астана: Второй по величине рынок автомобилей с высоким уровнем экономической активности.
# Шымкент, Костанай и Атырау: Заметный рынок, но меньше по объемам, чем в Алматы и Астане.
# Другие города: Регионы, такие как Караганда, Уральск, Актау, Усть-Каменогорск и Актобе, имеют существенное количество продаж, хотя и в меньших объемах.
# 

# #### Тип топлива

# In[105]:


group_brand = personal_data.groupby ('fuel').agg({'sale':'sum', 'quantity':'sum'}).reset_index ().sort_values(by ='quantity', ascending = False)
top_fuel = group_brand.reset_index(drop=True).head (10)
top_fuel


# In[106]:


data_subset_units = personal_data[personal_data.fuel.isin(top_fuel.fuel)]
plot_dinamic (data_subset_units, 'fuel', 'quantity', task=2)
plot_dinamic (data_subset_units, 'fuel', 'sale', task=2)


# <font face='liberation serif' size=4>Результат ожидаемый - явный лидер - бензиновый двигатель

# #### Класс

# In[107]:


group_brand = personal_data.groupby ('class_2013').agg({'sale':'sum', 'quantity':'sum'}).reset_index ().sort_values(by ='quantity', ascending = False)
top_klass = group_brand.reset_index(drop=True).head (10)
display (top_klass)
data_subset_units = personal_data[personal_data.class_2013.isin(top_klass.class_2013)]
plot_dinamic (data_subset_units, 'class_2013', 'quantity', task=2)
plot_dinamic (data_subset_units, 'class_2013', 'sale', task=2)


# <font face='liberation serif' size=4>SUV (внедорожники) являются самым популярным классом автомобилей как по объему продаж (sale), так и по количеству проданных автомобилей (quantity). Это может быть связано с повышенной потребностью в автомобилях этого класса из-за их универсальности, пространства и проходимости.
# 
# <font face='liberation serif' size=4>Автомобили класса B занимают второе место по популярности среди покупателей, что может быть обусловлено их доступностью и практичностью для городской езды.
# 
# <font face='liberation serif' size=4>Автомобили класса E и C также имеют значительное количество продаж и проданных единиц, что говорит о спросе на более премиальные или большие автомобили.
# 
# <font face='liberation serif' size=4>Пикапы (pick-ups) и автомобили класса A и D также представлены в данных, но их продажи и количество значительно меньше, что может говорить о более ограниченном спросе или меньшей доступности этих типов автомобилей.
# 
# <font face='liberation serif' size=4>Классы автомобилей F, полноразмерные минивэны и компактвэны наименее представлены в продажах. Это может быть связано с меньшей популярностью этих типов автомобилей, их стоимостью или недостаточным предложением на рынке.

# #### Привод

# In[108]:


group_brand = personal_data.groupby ('drive_type').agg({'sale':'sum', 'quantity':'sum'}).reset_index ().sort_values(by ='quantity', ascending = False)
top_drive_type = group_brand.reset_index(drop=True).head (10)
display (top_drive_type)
data_subset_units = personal_data[personal_data.drive_type.isin(top_drive_type.drive_type)]
plot_dinamic (data_subset_units, 'drive_type', 'quantity', task=2)
plot_dinamic (data_subset_units, 'drive_type', 'sale', task=2)


# <font face='liberation serif' size=4>Переднеприводные автомобили лидировали вплоть до марта 2019 года, и занимали на март 2019 г. первое место с 1172 продажами, но с апреля 2019  начинают уступать первое место полноприводным авто с продажами на пике в августе 2019 - 1703 шт.
# Динамика продаж в денежном выражении более равномерная в части лидерства - первое место полноприводные авто, с пиком в июне в размере 65 млн.
# 
# <font face='liberation serif' size=4>Самым популярным типом привода является 4WD (полный привод), как по объему продаж (sale), так и по количеству проданных автомобилей (quantity). Это может говорить о высоком спросе на автомобили с полным приводом, что может быть связано с условиями дорожного движения, климатическими условиями или предпочтениями покупателей.
# 
# <font face='liberation serif' size=4>Вторым по популярности является FWD (передний привод). По объему продаж он уступает 4WD, хотя разница в количестве проданных автомобилей не так велика. Это может говорить о том, что автомобили с передним приводом в среднем дешевле автомобилей с полным приводом.
# 
# <font face='liberation serif' size=4>RWD (задний привод) является наименее популярным типом привода, продажи которого составляют всего лишь небольшую долю от общего числа продаж. Это может быть связано с тем, что автомобили с задним приводом часто ассоциируются с спортивными или премиальными автомобилями, которые обычно имеют более ограниченный рынок.
# 
# <font face='liberation serif' size=4>Привод 2WD также имеет значительное количество продаж и количество проданных автомобилей, что говорит о том, что эти автомобили также находятся в спросе, хотя и уступают по популярности автомобилям с полным и передним приводом.

# #### Сегмент

# In[109]:


group_brand = personal_data.groupby ('segmentation').agg({'sale':'sum', 'quantity':'sum'}).reset_index ().sort_values(by ='quantity', ascending = False)
top_segmentation = group_brand.reset_index(drop=True).head (10)
display (top_segmentation)
data_subset_units = personal_data[personal_data.segmentation.isin(top_segmentation.segmentation)]
plot_dinamic (data_subset_units, 'segmentation', 'quantity', task=2)
plot_dinamic (data_subset_units, 'segmentation', 'sale', task=2)


# <font face='liberation serif' size=4>В части количества проданных авто, внедорожники уверенно лидирует с июня 2019 года и на пике имеют 2118 проданных авто, второе место занимаю легкоые авто. В денежном выражении внедорожники удерживают лидерскую позицию на всем исследуемомо отрезке, и имеют пиковое значение почти в 71 млн.

# ### Исследование средних показателей по брендам и маркам

# <font face='liberation serif' size=4>Бренды уже рассматривали, там беззаговорочный лидер Tayota. теперь посмотрим по моделям

# In[110]:


group_brand = personal_data.groupby('model').agg({
    'price':'mean',
    'quantity':'sum',
    'class_2013':lambda x: x.mode()[0] if len(x.mode()) > 0 else None
}).reset_index().sort_values(by='price', ascending=False)

group_brand.price=group_brand.price.round (1)
top_brands = group_brand.reset_index(drop=True).head (10)
top_brands


# <font face='liberation serif' size=4>В основном представлены автомобили класса F и SUV. Это свидетельствует о предпочтении покупателей премиум-сегмента именно этих классов автомобилей.
# 
# <font face='liberation serif' size=4>Модель LX отличается от других наличием большого количества продаж (404 единицы), что говорит о ее популярности среди покупателей, несмотря на высокую среднюю цену.
# 
# <font face='liberation serif' size=4>С другой стороны, модели 911 Carrera S, G-class, LC и Genesis G90 продались в очень маленьком количестве (от 1 до 2 единиц), что может говорить о их эксклюзивности, либо о меньшей популярности среди покупателей по каким-то причинам.
# 
# <font face='liberation serif' size=4>Самой дорогой моделью является 911 Carrera S, что может свидетельствовать о её высоком статусе или ограниченной доступности.
# 
# <font face='liberation serif' size=4>Самым продаваемым автомобилем из списка является LX, несмотря на то что его цена значительно выше среднего.

# ### Емкость рынка

# In[111]:


total_sales = personal_data['quantity'].sum()
display ('Общий объем продаж:', total_sales)


# In[112]:


company_sales = personal_data.groupby('company')['quantity'].sum().sort_values(ascending=False)
display ('Продажи по салонам', company_sales)


# In[113]:


region_sales = personal_data.groupby('region')['quantity'].sum().sort_values(ascending=False)
display('Продажи по регионам', region_sales)


# In[114]:


sale_by_date = personal_data.groupby('date')['sale'].sum().reset_index()
sale_by_date


# <font face='liberation serif' size=4>Ранее уже проводился анализ данных направлений в срезе Топов, но если обобщить полученную информацию: 
# 
# <font face='liberation serif' size=4>Объем продаж: 
# 
# Всего было продано 27 155 единиц товара.
# 
# <font face='liberation serif' size=4>Продажи по компаниям:
# 
# Наибольший объем продаж приходится на компанию 'Toyota Motor Kazakhstan' с 10 440 проданными единицами.
# За ней следует 'Astana Motors' с 5 703 проданными единицами.
# 'Бипэк Авто' и 'Узавто-Казахстан' также показали значительные продажи - 2 728 и 1 727 единиц соответственно.
# Наименьшие показатели у компаний 'Sivi Finance Consulting' и 'SMC' - 4 и 1 единица соответственно.
# 
# <font face='liberation serif' size=4>Продажи по регионам:
# 
# Наибольший объем продаж был в Алматы (8 013 единиц), затем в Астане (5 881 единица).
# Другие крупные города, такие как Шымкент, Костанай и Атырау, также показали значительные показатели продаж.
# Наименьшие объемы продаж были в Щучинске (3 единицы).
# В общем, продажи сконцентрированы в крупных городах и у крупных автомобильных дистрибьюторов. Вероятно, это связано с наличием у этих дистрибьюторов большего количества автосалонов в крупных городах и лучшим доступом к ресурсам, таким как реклама и распределение.
# 
# Меньшие продажи в некоторых регионах и у некоторых дистрибьюторов могут указывать на необходимость усилить маркетинговые усилия или присмотреться к спросу в этих регионах.
# 
# <font face='liberation serif' size=4>Динамика продаж:
#     
# Судя по данным, продажи варьируются от месяца к месяцу.
# Наименьший объем продаж был в январе 2019 года (60 426 429), а наибольший - в июне 2019 года (113 785 455).
# Отмечается общий тренд к росту продаж с начала года: с января по июнь продажи почти удвоились.
# После июня 2019 года продажи немного снизились (в июле), но затем снова увеличились и стабилизировались на уровне около 103-105 млн в августе и сентябре.
# В общем, данная динамика может быть связана с сезонностью или другими факторами, влияющими на спрос. Так, например, рост продаж в первой половине года может быть связан со снижением стоимости автомобилей из-за модельного года или с покупкой автомобилей перед летними каникулами, перед отпусками и т.п.

# ### Оценим долю рынка на примере компании mercur auto

# #### Расчет общей доли на рынке у mercur auto (количественном и стоимостном выражении)

# In[115]:


total_quantity = data.quantity.sum()
total_sales = data.sale.sum()

mercur_quantity = data[data.company == 'mercur auto']['quantity'].sum()
mercur_sales = data[data.company == 'mercur auto']['sale'].sum()

quantity_market_share = (mercur_quantity / total_quantity) * 100
sales_market_share = (mercur_sales / total_sales) * 100

display (f"Количественная доля рынка компании 'mercur auto': {quantity_market_share:.2f}%")
display (f"Стоимостная доля рынка компании 'mercur auto': {sales_market_share:.2f}%")


# #### Hасчета доли рынка mercur auto по маркам

# In[116]:


total_sales_by_brand = data.groupby('brand')['sale'].sum()

mercur_sales_by_brand = data[data.company == 'mercur auto'].groupby('brand')['sale'].sum()

brand_market_share = (mercur_sales_by_brand / total_sales_by_brand) * 100

display ("Доли рынка компании 'mercur auto' по маркам:")
display (brand_market_share)


# #### Рассчитаем долю рынка mercur auto по классам

# In[117]:


total_sales_by_klass = data.groupby('class_2013')['sale'].sum()

mercur_sales_by_klass = data[data.company == 'mercur auto'].groupby('class_2013')['sale'].sum()

klass_market_share = (mercur_sales_by_klass / total_sales_by_klass) * 100

display ("Доли рынка компании 'mercur auto' по классам:")
display (klass_market_share)


# <font face='liberation serif' size=5> Общие вывод по mercur auto
# 
# <font face='liberation serif' size=4>*Общая доля рынка:* 
# 
# Компания 'mercur auto' занимает 2,43% рынка по количеству проданных автомобилей и 2.87% рынка по стоимости продаж. Это указывает на то, что средняя стоимость автомобиля, проданного компанией, выше среднего уровня по рынку.
# 
# <font face='liberation serif' size=4>*Доля рынка по маркам:*
# 
# Компания 'mercur auto' полностью доминирует на рынке брендов Audi, Porsche и Volkswagen, занимая 100% долю продаж по этим маркам. Это может указывать на эксклюзивные права на продажу или очень сильное присутствие в этом сегменте.
# По другим маркам у компании нет продаж, что может указывать на специализированный характер деятельности компании или на наличие эксклюзивных договоров с определенными производителями.
# 
# <font face='liberation serif' size=4>*Доля рынка по классам:*
# 
# Наибольшую долю рынка 'mercur auto' занимает в сегменте "спортивные автомобили", составляющую 84,04%. Это может говорить о том, что компания специализируется на продаже спортивных автомобилей или имеет выдающееся предложение в этом сегменте.
# Другие выдающиеся сегменты, в которых компания имеет заметное присутствие, включают "полноразмерные минивэны" с долей 18,41% и "микроавтобусы" с долей 9,71%.
# В некоторых классах, таких как "а класс", "большие автобусы", "компактвэн" и других, у компании нет продаж, что может говорить о целевой специализации компании или о стратегическом решении не работать с этими сегментами.
# Общий вывод: Компания 'mercur auto', вероятно, является специализированным дилером, сосредоточенным на определенных марках и классах автомобилей. Её присутствие особенно заметно в сегменте спортивных автомобилей, полноразмерных минивэнов и микроавтобусов. Это может указывать на то, что компания выбрала стратегию дифференциации и фокусируется на конкретных нишах рынка.

# ### Рассчет для mercur auto в части конкурентов

# In[118]:


company_ranking = data.groupby('company')['sale'].sum().sort_values(ascending=False)

display ("Лидеры рынка по объему продаж:")
display (company_ranking.head())


# <font face='liberation serif' size=4>Ранее мы уже смотрели на топ рынка по продажам, и отмечали лидирующие позиции toyota motor kazakhstan, теперь посмотрим на топ-5 в сравнении с mercur auto

# #### Определение ближайших конкурентов для "mercur auto":

# In[119]:


mercur_regions = data[data.company == 'mercur auto']['region'].unique()
mercur_brands = data[data.company == 'mercur auto']['brand'].unique()
mercur_klasses = data[data.company == 'mercur auto']['class_2013'].unique()

competitor_data = data[(data.region.isin(mercur_regions)) & 
                     (data.brand.isin(mercur_brands)) & 
                     (data.class_2013.isin(mercur_klasses))]


competitor_ranking = competitor_data.groupby('company')['sale'].sum().sort_values(ascending=False)

# Исключим "mercur auto" из списка, чтобы увидеть конкурентов
competitor_ranking = competitor_ranking[competitor_ranking.index != 'mercur auto']

display ("Ближайшие конкуренты 'mercur auto' по объему продаж:")
display (competitor_ranking.head())


# <font face='liberation serif' size=4>Странно, якобы никого нет, нужно проверить, исключая по очереди наши параметры

# In[120]:


regional_competitor_data = data[data.region.isin(mercur_regions)]
regional_competitor_ranking = regional_competitor_data.groupby('company')['sale'].sum().sort_values(ascending=False)
regional_competitor_ranking = regional_competitor_ranking[regional_competitor_ranking.index != 'mercur auto']
display ("Конкуренты 'mercur auto' по объему продаж в регионах:")
display (regional_competitor_ranking.head())


# <font face='liberation serif' size=4>По регионам явно проблем нет с поиском конкурентов 

# In[121]:


brand_competitor_data = data[data.brand.isin(mercur_brands)]
brand_competitor_ranking = brand_competitor_data.groupby('company')['sale'].sum().sort_values(ascending=False)
brand_competitor_ranking = brand_competitor_ranking[brand_competitor_ranking.index != 'mercur auto']
display ("Конкуренты 'mercur auto' по объему продаж среди брендов:")
display (brand_competitor_ranking.head())

klass_competitor_data = data[data.class_2013.isin(mercur_klasses)]
klass_competitor_ranking = klass_competitor_data.groupby('company')['sale'].sum().sort_values(ascending=False)
klass_competitor_ranking = klass_competitor_ranking[klass_competitor_ranking.index != 'mercur auto']
display ("Конкуренты 'mercur auto' по объему продаж в классах машин:")
display (klass_competitor_ranking.head())


# #### Распределение продаж по месяцам или годам для 'mercur auto' и их основных конкурентов

# In[122]:


# соберем данные по месяцам:
monthly_sales = data.groupby(['company', data['date'].dt.to_period('M')])['sale'].sum().reset_index()
# лидеров рынка по классам машин и mercur auto
list_of_competitors = ['mercur auto', 'toyota motor kazakhstan', 'бипэк авто', 'astana motors',                       'nissan manufacturing rus', 'автоцентр-бавария']
monthly_sales = monthly_sales.query('company == @ list_of_competitors')


# In[123]:


monthly_sales['date'] = monthly_sales['date'].astype(str)
fig = px.line(monthly_sales, x='date', y='sale', color='company', title='Распределение продаж по месяцам')
fig.update_xaxes(rangeslider_visible=True)
fig.show()


# <font face='liberation serif' size=4>*Лидеры рынка по регионам:*
# 
# Как уже отмечалось, компания "toyota motor kazakhstan" является абсолютным лидером рынка с продажами, превышающими 415 миллионов.
# Следом идут компании "бипэк авто" и "astana motors" с продажами около 117 и 115 миллионов соответственно.
# "вираж" и "nissan manufacturing rus" также находятся в списке лидеров, но их продажи значительно меньше — 45 и 42 миллиона соответственно.
# 
# <font face='liberation serif' size=4>*По брендам:*
# 
# На основе предоставленных данных 'mercur auto' является единственной компанией, предлагающей некоторые из рассматриваемых брендов. Это может указывать на эксклюзивное право 'mercur auto' на продажу этих брендов или на то, что конкуренты не работают с этими конкретными брендами.
# 
# <font face='liberation serif' size=4>*По классам машин:*
# 
# Снова, "toyota motor kazakhstan" лидирует с продажами более 468 миллионов.
# "бипэк авто" и "astana motors" следуют за ней с продажами 149 и 124 миллиона соответственно.
# "nissan manufacturing rus" и "автоцентр-бавария" замыкают пятерку лидеров с продажами 43 и 23 миллиона соответственно.
# 
# 
# <font face='liberation serif' size=4>*Общие выводы:*
# 
# "toyota motor kazakhstan" является ключевым игроком на рынке в рассматриваемых регионах и классах машин.
# 'mercur auto' имеет уникальное преимущество в определенных брендах, что может служить конкурентным преимуществом.
# Хотя 'mercur auto' может не иметь такого большого объема продаж, как некоторые из лидеров рынка, уникальные бренды и возможное эксклюзивное право на их продажу могут дать возможность для стратегического позиционирования и разработки маркетинговых кампаний. Посмотрим более детально на продажи по регионам, брендам и классам, в срезе лидеров рынка и mercur auto

# #### Распределение продаж по регионам, брендам и классам

# In[124]:


def plot_sales_by_category(data, category, list_of_competitors):
    """
    Составляет график продаж по заданной категории.

    Аргументы:
    - данные (pd.DataFrame): набор данных.
    - категория (str): категория, по которой следует группировать продажи (например, "бренд", "класс", "регион").
    - list_of_competitors (список): список конкурентов для фильтрации данных.

    Что возвращает:
    - ничего: отображает график.
    """
    grouped_data = data.groupby([category, 'company'])['sale'].sum().reset_index()
    filtered_data = grouped_data[grouped_data['company'].isin(list_of_competitors)]
    fig = px.bar(filtered_data, x=category, y='sale', color='company', title=f'Продажи по {category}')
    fig.show()


# In[125]:


plot_sales_by_category(data, 'brand', list_of_competitors)
plot_sales_by_category(data, 'class_2013', list_of_competitors)
plot_sales_by_category(data, 'region', list_of_competitors)


# <font face='liberation serif' size=5>Если кратко обобщить результаты визуализации
# 
# <font face='liberation serif' size=4>Бренды:
# 
# Toyota является абсолютным лидером, причем их дистрибьютор 'Toyota Motor Kazakhstan' контролирует наибольшую долю рынка. Другие выдающиеся бренды включают Lada, Hyundai, Lexus, и Kia.
# С другой стороны, 'Mercur Auto' предоставляет такие бренды как Audi, Porsche и Volkswagen. Несмотря на то, что Volkswagen имеет заметные продажи в 20,438,224, другие бренды этого дистрибьютора, такие как Audi и Porsche, имеют относительно меньший объем продаж.
#     
# <font face='liberation serif' size=4>Категории транспортных средств:
# 
# 'Toyota Motor Kazakhstan' и 'Astana Motors' доминируют в ряде высокодоходных категорий, таких как SUV, E класс и коммерческие транспортные средства.
# В то время как 'Mercur Auto' занимает значимые позиции в категориях F класс и микроавтобусы. Однако, в целом, их доля на рынке в этих категориях меньше по сравнению с 'Toyota Motor Kazakhstan' и 'Astana Motors'.
# 
# <font face='liberation serif' size=4>Сравнение с 'Mercur Auto':
# 
# Несмотря на то, что 'Mercur Auto' представляет несколько высококачественных брендов, их общий объем продаж ниже, чем у ключевых лидеров рынка.
# Они занимают ведущие позиции в определенных нишевых категориях, но их общий рыночный охват и разнообразие представленных категорий меньше по сравнению с главными игроками рынка.
# В заключении, 'Mercur Auto' является активным участником рынка, предоставляя ряд премиальных брендов и занимая лидирующие позиции в некоторых категориях. Однако, по общему объему продаж и разнообразию представленного транспорта, они уступают таким гигантам рынка, как 'Toyota Motor Kazakhstan' и 'Astana Motors'.

# ## <font face='liberation serif' size=5>Итоговые выводы.</font>  

# <font face='liberation serif' size=5>Общие выводы:
# 
# <font face='liberation serif' size=4>Объем продаж: 
#     
# Всего было продано 27 155 единиц товара.
# 
# <font face='liberation serif' size=4>Продажи по компаниям:
# 
# 'Toyota Motor Kazakhstan' является лидером рынка с 10 440 проданными единицами.
# 'Astana Motors' и 'Бипэк Авто' также являются ключевыми игроками с 5 703 и 2 728 проданными единицами соответственно.
# Компании 'Sivi Finance Consulting' и 'SMC' показали наименьший объем продаж - 4 и 1 единица соответственно.
# Между тем, компания "mercur auto" занимает долю рынка в размере 2.83% по количеству и 3.18% по стоимости.
# 
# <font face='liberation serif' size=4>Продажи по регионам:
# 
# Алматы и Астана являются ключевыми регионами с продажами 8 013 и 5 881 единиц соответственно.
# Города Шымкент, Костанай и Атырау также показали значительные показатели.
# Щучинск стоит выделить как регион с наименьшим объемом продаж - всего 3 единицы.
# Динамика продаж: Продажи имеют тенденцию к росту с января по июнь, вероятно, из-за сезонности или экономических факторов.
# 
# <font face='liberation serif' size=4>Классы автомобилей:
# 
# Самыми популярными являются автомобили класса F и SUV. В частности, "mercur auto" особенно сильно представлено в классе F (39.05%) и классе спортивных автомобилей (84.04%).
# Модель LX наиболее популярна среди покупателей, продавшись в количестве 404 единиц.
# Модели 911 Carrera S, G-class, LC и Genesis G90 менее популярны, с продажами в диапазоне от 1 до 2 единиц.
# 
# <font face='liberation serif' size=4>Выводы по компании Mercur Auto
# 
# <font face='liberation serif' size=4>-Рыночное положение: 
#     
# 'Mercur Auto' обладает количественной долей рынка в 2.43% и стоимостной долей в 2.87%. Это показывает, что хотя их общий объем продаж может быть меньше, чем у некоторых других игроков, они, вероятно, продавали автомобили более высокого класса или стоимости.
# 
# <font face='liberation serif' size=4>-По маркам: 
#     
# 'Mercur Auto' является единственным представителем марок Audi, Porsche и Volkswagen на рынке. Это дает им уникальное конкурентное преимущество в этих категориях.
# 
# <font face='liberation serif' size=4>-По классам: 
#     
# 'Mercur Auto' занимает лидирующие позиции в классе F (39.05%), полноразмерных минивэнах (18.41%) и спортивных автомобилях (84.04%). Это подтверждает их присутствие в премиум-сегменте.
# 
# <font face='liberation serif' size=4>Рекомендации:
# 
# <font face='liberation serif' size=4>-По классам:
#         
#         - F класс: Учитывая высокую долю рынка в 39.05%, Mercur Auto должна продолжать активное продвижение и укрепление своего положения в этом классе.
# 
#         - Полноразмерный минивэн: С долей рынка 18.41% следует рассмотреть возможность увеличения ассортимента и предложений в этой категории.
# 
#         - Спортивные автомобили: Огромная доля рынка в 84.04% указывает на доминирование компании в этом сегменте. Необходимо сохранить этот статус и возможно расширить ассортимент или предложить специальные акции.
# 
# <font face='liberation serif' size=4>- По городам:
# 
#         - Алматы: Учитывая его статус крупнейшего города и экономического центра страны, Mercur Auto должна активизировать свои усилия в этом регионе. Возможно, учитывая спрос на премиум-сегмент, стоит расширить присутствие в городе.
#         - Астана (Нур-Султан): Как столица страны, Астана представляет собой еще один важный регион для укрепления присутствия.
#         - Шымкент и другие крупные города: Предложить пробные поездки или провести рекламные кампании, чтобы привлечь больше клиентов из этих регионов.
#         
#     - Маркетинговые усилия: Рассмотреть возможность усилить рекламные кампании в регионах с меньшими продажами, а также провести исследование потребительских предпочтений в этих регионах.
# 
#     - Анализ конкурентов: Важно учитывать действия ключевых конкурентов, таких как 'Toyota Motor Kazakhstan' и 'Astana Motors', чтобы определить возможные стратегические шаги для увеличения доли рынка "mercur auto".
# 
# <font face='liberation serif' size=4>Учитывая вышеуказанные выводы и рекомендации, Mercur Auto имеет все шансы на успешное развитие на рынке. С учетом их уникального присутствия в определенных марках и классах автомобилей, важно сосредоточить усилия на сохранении этих позиций, а также на расширении присутствия в стратегически важных регионах.
