# PySQLPlayground
Игровая площадка для Python и SQL проектов вне учебы

Привет! В этом репозитории я буду выкладывать свои небольшие самостоятельные работы, постараюсь сделать их информативными. Понимаю, что опытным пользователям они могут быть не интересны, но уверен начинающие специалисты смогут найти в них что-нибудь интересное.


try:
    image_path = r"C:\Users\PC_Maks\Desktop\1.jpg"
    display(Image(filename=image_path))
except:
    image_url = "https://i.postimg.cc/yYDBx1qK/1.jpg"
    response = requests.get(image_url)
    image_data = response.content
    display(Image(image_data))
