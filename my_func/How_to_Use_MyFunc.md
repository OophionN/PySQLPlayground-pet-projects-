<h2>Добавление модуля с функциями в переменные среды Windows 11</h2> 
  <h2>Описанная ниже процедура позволяет вызывать ваши функции из среды в которой работаете (в моем случае это JupiterNotebook). В данном примере у меня уже есть Python-файл с именем my_func.py, в котором определены функции предварительной обработки датасетов.</h2>

<h3>Вот пошаговый алгоритм:</h3>

<ol>
  <li><strong>Подготовка Python-файла:</strong>
    <ul>
      <li>Сохраните ваш Python-файл (например, my_func.py) в каком-либо каталоге. Например, у меня это C:\Users\PC_Maks\all_repo</li>
    </ul>
  </li>
  <li><strong>Изменение переменных среды:</strong>
    <ul>
      <li>Откройте "Параметры системы" через Пуск -> Поиск и введите "Переменные среды" или "Environment Variables".</li>
      <li>Выберите "Переменные среды" в разделе "Дополнительные параметры системы".</li>
      <li>В открывшемся окне "Переменные среды" найдите раздел "Переменные среды пользователя" или "User variables".</li>
      <li>Найдите переменную с именем Path/PYTHONPATH и выберите "Изменить" (или создайте новую переменную с этим именем, если её нет).</li>
      <li>В открывшемся окне "Изменение переменных среды" добавьте новую строку, указав полный путь к каталогу, в котором находится ваш Python-файл. В моем случае это C:\Users\PC_Maks\all_repo</li>
      <li>Нажмите "ОК" во всех окнах для сохранения изменений.</li>
    </ul>
  </li>
</ol>


<h3>Пример на скриншоте</h3>
<img src="https://i.postimg.cc/FzKwxPpy/image.jpg">


### А можно при необходимости использовать следующий код, для вставки сразу в своей проект

```python
import os
import sys
import subprocess

# Блок для загрузки модуля в sys.path
module_name = "my_func"

# Проверяем, установлен ли модуль
try:
    __import__(module_name)
    print(f"Модуль '{module_name}' уже установлен.")
except ImportError:
    print(f"Модуль '{module_name}' не найден, загружаем с GitHub...")
    
    # Путь к скачиванию модуля
    github_url = "https://raw.githubusercontent.com/OophionN/PySQLPlayground-pet-projects-/main/my_func/my_func.py"
    download_path = f"{module_name}.py"
    
    # Загружаем модуль с GitHub
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        import requests
        response = requests.get(github_url)
        with open(download_path, 'wb') as file:
            file.write(response.content)
        print(f"Модуль '{module_name}' успешно загружен с GitHub.")
        
        # Добавляем путь к модулю в sys.path, чтобы можно было его импортировать
        sys.path.append(os.path.abspath("."))
    except Exception as e:
        print(f"Произошла ошибка при загрузке модуля: {e}")

# Импорт модуля
try:
    import my_func
    print("Модуль успешно импортирован.")
except ImportError as e:
    print(f"Ошибка импорта модуля: {e}")
