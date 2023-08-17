"""
Модуль my_func содержит функции для предварительной обработки данных и проверки их на дубликаты и пропуски.
Функции:
- data_preprocessing: Производит предварительную обработку данных, модифицируя заголовки столбцов и строковые значения.
- check: Проверяет DataFrame на наличие дубликатов и пропусков и выводит соответствующую информацию.
    При обнаружении дубликатов имеется возможность их удалить.
- check_unique:Выводит уникальные значения и их количество для строковых столбцов, 
    диапазон значений для числовых и даты/времени столбцов, а также уникальные значения 
    для числовых столбцов, где уникальных значений не более 10. 
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
