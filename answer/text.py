greet = 'Привет, {name}, я телеграм бот, который поможет вам наслаждаться книгами в разных форматах. Вы можете читать книги из моей библиотеки, слушать аудиокниги, а также загружать свои собственные книги и делиться ими с другими пользователями. Я также могу рекомендовать вам книги по вашим интересам и предпочтениям.'

genres = 'Жанры - это раздел, в котором вы можете выбрать жанр аудиокниги, которая вам интересна. В нашем каталоге есть аудиокниги разных жанров, таких как фантастика, детектив, роман, история, психология и многие другие. Вы можете просмотреть список доступных жанров и узнать, сколько аудиокниг каждого жанра есть в нашей библиотеке. Вы также можете посмотреть рейтинги и отзывы других пользователей о аудиокнигах разных жанров. Если вы не знаете, какой жанр выбрать, вы можете воспользоваться функцией Случайный жанр, которая подберет для вас аудиокнигу из случайного жанра. Надеемся, что вы найдете аудиокнигу по своему вкусу и насладитесь ее прослушиванием. 🎧'

'''Заменить на json список'''
books = [
    {'title': 'Книга 1', 'genre': 'Любовный роман', 'path': 'books/book1.txt'},
    {'title': 'Книга 2', 'genre': 'Детектив', 'path': 'books/book2.txt'},
    {'title': 'Книга 3', 'genre': 'Фэнтези', 'path': 'books/book3.txt'},
    {'title': 'Книга 4', 'genre': 'Любовный роман', 'path': 'books/book4.txt'},
    {'title': 'Книга 5', 'genre': 'Детектив', 'path': 'books/book5.txt'},
]

profile = '{id}, {name}, вот ваша статистика\nКоличество прочитанных книг: {read_books}\nКоличество прослушанных книг: {listened_books}\nЛюбимые жанры: {favorite_genres}\nПодписка: {subscribtion}'
