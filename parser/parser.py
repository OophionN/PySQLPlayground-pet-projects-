import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# Базовый URL для многостраничного парсинга
base_url = 'https://***********'
page_url_template = base_url + '********'

# Директория для сохранения изображений
image_dir = r'C:\Users\******\files_parser\image'
os.makedirs(image_dir, exist_ok=True)

# Функция для получения HTML страницы с правильной кодировкой
def get_html(url):
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = 'utf-8'  # Установим правильную кодировку
    return response.text

# Функция для получения всех ссылок на товары из всех страниц раздела
def get_all_product_links(base_url, total_pages):
    product_links = []
    for page in range(1, total_pages + 1):
        page_url = page_url_template.format(page=page)
        html = get_html(page_url)
        soup = BeautifulSoup(html, 'html.parser')
        
        # Найти все ссылки на товары
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('/products/') and href not in product_links:
                product_links.append(href)
        
        print(f"Обработана страница {page}/{total_pages}")
        time.sleep(0.1)  # Добавим таймаут для предотвращения перегрузки сервера
    
    return product_links

# Функция для загрузки изображения
def download_image(url, image_dir, image_name):
    if not url.startswith('http'):
        url = 'https://********' + url
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        image_path = os.path.join(image_dir, image_name)
        with open(image_path, 'wb') as out_file:
            for chunk in response.iter_content(1024):
                out_file.write(chunk)
        return image_path
    return None

# Функция для получения характеристик товара
def get_product_specs(soup):
    specs = {}
    table = soup.find('table', id='tech')
    if table:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) == 2:
                key = cols[0].text.strip()
                value = cols[1].text.strip()
                specs[key] = value
    return specs

# Функция для парсинга данных с одной страницы товара
def get_product_data(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    # Извлечение данных
    name_tag = soup.find('h1', id='pagetitle')
    name = name_tag.text.strip() if name_tag else 'N/A'
    
    # Извлечение всех изображений из блока "slides"
    images = []
    image_tags = soup.find_all('div', class_='slides')
    for image_tag in image_tags:
        for img in image_tag.find_all('img'):
            image_url = img['src']
            if not image_url.startswith('http'):
                image_url = 'https://******' + image_url
            image_name = os.path.basename(image_url)
            image_path = download_image(image_url, image_dir, image_name)
            images.append(image_path)
    
    # Преобразование списка изображений в строку
    images_str = ', '.join(images)
    
    article_tag = soup.select_one('span[itemprop="item"] span[itemprop="name"]')
    article = article_tag.text.strip() if article_tag else 'N/A'
    
    description_tag = soup.find('div', class_='detail_text')
    description = description_tag.find('p').text.strip() if description_tag and description_tag.find('p') else 'N/A'
    
    price_tag = soup.find('span', class_='price_value')
    price = price_tag.text.strip() if price_tag else 'N/A'
    
    unit = "шт."
    
    # Получение характеристик товара
    specs = get_product_specs(soup)

    return {
        'Наименование': name,
        'Картинки': images_str,
        'Артикул': article,
        'Описание': description,
        'Цена': price,
        'Единица': unit,
        'Ссылка': url,
        **specs  # Добавление всех характеристик в результат
    }

# Функция для многопоточного парсинга данных с товаров
def process_links(product_links):
    all_products = []
    counter = 0
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(get_product_data, 'https://*******' + link): link for link in product_links}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                product_data = future.result()
                all_products.append(product_data)
                counter += 1
                if counter % 10 == 0:
                    print(f"Обработано {counter} товаров")
            except Exception as e:
                print(f"Ошибка при обработке товара {url}: {e}")
    
    return all_products

# Получить ссылки на товары из указанного количества страниц
total_pages = 48  # Обработаем только указанные страницы (использовал для тестирования)
product_links = get_all_product_links(base_url, total_pages)
print(f"Найдено {len(product_links)} товаров")

# Многопоточный парсинг данных с товаров
all_products = process_links(product_links)

# Создать DataFrame и сохранить в CSV
df = pd.DataFrame(all_products)
df.to_csv(r'C:\Users\********\files_parser\products.csv', index=False)

print("Данные успешно сохранены в файл products.csv")
