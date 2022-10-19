import os
if os.path.isdir("papka"):
    os.remove("papka/papka_v_papke/text.txt")
    os.removedirs("papka/papka_v_papke")

if not os.path.isdir("papka"):
    os.mkdir ("papka")
    os.mkdir ("papka/papka_v_papke")
    os.chdir("papka/papka_v_papke")
    text_file = open("text.txt", "w")
    text_file.write("здесь был космодесант here was space marines")