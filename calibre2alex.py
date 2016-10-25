#
# byGoose!
#

from autor import Autor
import os

if __name__ == '__main__':
    print("calibre2alex-start")
    print("------------------")

    print("## BEGIN ================================ ")
    path = '/home/goose/Escritorio/PROCESO/procesar'
    path = './pruebas'
    lang = 'esp'
    [
        Autor(os.path.join(path, d), lang).manage()  # creates Autor and process
        for d in os.listdir(path)  # all dirs in path
        if os.path.isdir(os.path.join(path, d)) and d[0] != "_"  # only the dirs that not begin with _
    ]
    print("## END ================================== ")

    print("-------------")
    print("cal2goo-end")
