import os

def create_files():
    # Содержимое файла index.html
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

</body> 
<script src="script.js">
</script>
</html>
<!-- Made by Fench's Apps -->'''

    # Содержимое файла style.css
    css_content = '''/* Made by Fench's Apps */'''

    # Содержимое файла script.js
    js_content = '''// Made by Fench's Apps'''

    # Создание файлов
    with open('index.html', 'w') as file:
        file.write(html_content)

    with open('style.css', 'w') as file:
        file.write(css_content)

    with open('script.js', 'w') as file:
        file.write(js_content)


def main():
    user_input = input("Хотите продолжить? (Y/N): ").strip().lower()

    if user_input in ['y', 'yes', 'yeah']:
        create_files()
        print("Файлы успешно созданы!")
    elif user_input in ['n', 'no', 'nope']:
        print("Скрипт завершает работу.")
    else:
        print("Неверный ввод. Повторите попытку!")
        main()


main()