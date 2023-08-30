"""
Модуль my_func содержит функции для предварительной обработки данных и проверки их на дубликаты и пропуски.

Функции:
- data_preprocessing: Производит предварительную обработку данных, модифицируя заголовки столбцов и строковые значения.
- check: Проверяет DataFrame на наличие дубликатов и пропусков и выводит соответствующую информацию.
    При обнаружении дубликатов имеется возможность их удалить.
- check_unique:Выводит уникальные значения и их количество для строковых столбцов, 
    диапазон значений для числовых и даты/времени столбцов, а также уникальные значения 
    для числовых столбцов, где уникальных значений не более 10. 
- transliterate производит транслитерации символов на латиницу
"""

import pandas as pd

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
        
        
def check(data, drop_dupl=True):
    """
    Проверяет DataFrame на наличие дубликатов и пропусков и выводит соответствующую информацию.
    При обнаружении дубликатов имеется возможность их удалить.

    Параметры:
    - data (DataFrame): DataFrame, который необходимо проверить.
    - drop_dupl (bool, по умолчанию True): Если True, дубликаты будут удалены из DataFrame.

    Возвращает:
    - None: Функция выводит информацию напрямую в консоль. 
            Если были обнаружены дубликаты и параметр drop_dupl установлен в True, то из исходного DataFrame дубликаты будут удалены.
            Если дубликаты найдены, но drop_dupl установлен в False, то дубликаты не удаляются.

    """
    if drop_dupl:
        try:
            display('Проверка на дубликаты:')
            duplicates = data.duplicated()
            duplicate_rows = data.loc[duplicates]
            display(duplicate_rows.info())
            display(duplicate_rows)
            display('----------------------')
            display('Пропуски:')
            display(data.isna().sum())
            display('Пропуски в процентном отношении к всему датасету:')
            display(data.isna().sum() / len(data) * 100)

            num_rows_before = len(data)
            data.drop_duplicates(inplace=True)
            num_rows_after = len(data)
            num_rows_deleted = num_rows_before - num_rows_after
            percent_deleted = round(num_rows_deleted / num_rows_before * 100, 2)
            display(f'Удалено дубликатов: {num_rows_deleted} строк ({percent_deleted}% от всего датасета)')
        
        except Exception as e:
            print(f'ERROR: {e}')
    else:
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




def transliterate(name):
    """
    Транслитерация заданной строки с кириллицы на латиницу согласно заранее установленному словарю.

    Параметры:
    name (str): Строка для транслитерации.

    Возвращает:
    str: Транслитерированная строка.

    Примечания:
    - Функция использует заранее установленный словарь для транслитерации, который может не включать все возможные символы.
    - Специальные и числовые символы удаляются в транслитерированной строке.
    """
    try:
        # Словарь для транслитерации
        slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
            'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
            'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
            'ц':'c','ч':'ch','ш':'sh','щ':'sch','ъ':'','ы':'y','ь':'','э':'e',
            'ю':'u','я':'ya', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'YO',
            'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
            'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H',
            'Ц':'C','Ч':'CH','Ш':'SH','Щ':'SCH','Ъ':'','Ы':'y','Ь':'','Э':'E',
            'Ю':'U','Я':'YA',',':'','?':'',' ':'_','~':'','!':'','@':'','#':'',
            '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
            ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
            '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
            'Є':'e', '—':''}

        # Циклическая замена всех букв в строке
        for key in slovar:
            name = name.replace(key, slovar[key])
        
        return name

    except Exception as e:
        print(f'ОШИБКА: {e}')
        return None
