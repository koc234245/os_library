import os

def make_file():
    user_folder = input("введите имя первой папки: ")
    user_folder2 = input("введите имя второй папки: ")
    user_file = input("введите имя файла: ") + ".txt"

    for dirpath, dirnames, filenames in os.walk(user_folder):
        for filename in filenames:
          os.remove(os.path.join(dirpath, filename))
          os.removedirs(os.path.join(dirpath))

    os.makedirs(user_folder + "/" + user_folder2)
    os.chdir(user_folder + "/" + user_folder2)
    text_file = open(user_file, "w")
    in_text_message = input("что написать в файле?: ")
    text_file.write(in_text_message)
    print("Вы создали папку '" + user_folder + "' В ней папку '" + user_folder2 + "' с файлом '" + user_file + "' и написали там '" + in_text_message +"'")

confirmation = input("желаете создать файл? Введите 'да' или 'нет':" )
match confirmation:
    case "да": 
        make_file()
        confirmation = eval("True")
        print(confirmation)
        print(type(confirmation))
    case "нет":
        print("хорошо")
        confirmation = eval("False")
        print(confirmation)
        print(type(confirmation))
    case _:
        print("Упс, вы что-то не то написали")
