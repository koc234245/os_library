import os

for dirpath, dirnames, filenames in os.walk("papka"):
    for filename in filenames:
        os.remove(os.path.join(dirpath, filename))
        os.removedirs(os.path.join(dirpath))

def make_file():
    os.makedirs ("papka/papka_v_papke/")
    os.chdir("papka/papka_v_papke")
    text_file = open("text.txt", "w")
    text_file.write("здесь был космодесант here was space marines")
    
make_file()

    