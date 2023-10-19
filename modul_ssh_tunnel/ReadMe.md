<h1>Модуль для работы с MySQL через SSH-туннель</h1>
<p>Данный модуль предоставляет функции для работы с базой данных MySQL через SSH-туннель. Модуль может быть полезен для тех, кто работает с удалёнными серверами и базами данных, и хочет обеспечить безопасное соединение через SSH.</p>

<h2>Описание функций</h2>
<ul>
  <li><code>open_ssh_tunnel()</code>: Открывает SSH-туннель к удалённому серверу.</li>
  <li><code>mysql_connect()</code>: Подключается к базе данных MySQL через SSH-туннель.</li>
  <li><code>run_query(sql)</code>: Выполняет SQL-запрос к базе данных и возвращает результаты в виде DataFrame pandas.</li>
  <li><code>mysql_disconnect()</code>: Закрывает соединение с базой данных MySQL.</li>
  <li><code>close_ssh_tunnel()</code>: Закрывает SSH-туннель.</li>
</ul>

<h2>Пример использования</h2>
<pre><code>
# Импорт модуля
import module_name

# Открытие SSH-туннеля
module_name.open_ssh_tunnel()

# Подключение к базе данных MySQL
module_name.mysql_connect()

# Выполнение SQL-запроса
sql_query = "SELECT * FROM table_name"
data = module_name.run_query(sql_query)
print(data)

# Закрытие соединения с базой данных и SSH-туннелем
module_name.mysql_disconnect()
module_name.close_ssh_tunnel()
</code></pre>


<h2>Как использовать connect_sql.py?</h2>
  <p>
    Для инструкций по подключению и использованию модуля <code>connect_sql.py</code> ознакомьтесь с файлом 
    <a href="How_to_Use_connect_sql.py.md">How_to_Use_connect_sql.md</a>.
  </p>
