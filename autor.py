# list of dirs

import os
import shutil


class Autor:
    _root_path = None

    def __init__(self, root_path, lang):
        """ privates """
        self._lang = lang
        self._root_path = root_path
        self._root_origin_path = None
        self._root_back_path = None
        self._root_final_path = None
        self._author = None

    def manage(self):
        """ process """
        print("")
        self.manage_dirs(self._root_path)  # manage dirs
        self.manage_backup()  # generates backups
        self.manage_files()  # process
        print("")

    def manage_dirs(self, root_path):
        print("**|BEGIN >> ")
        # original and final path
        self._root_origin_path = os.path.normpath(root_path)
        print("ii|origin>> ", self._root_origin_path)
        (head, tail) = os.path.split(os.path.normpath(root_path))
        self._author = tail
        self._root_back_path = os.path.join(head, "__backup", tail)
        print("ii|backup>> ", self._root_back_path)
        self._root_final_path = self._root_origin_path
        # self._root_final_path = os.path.join(head, Autor.__turn_author_name(tail))
        # if not os.path.exists(self._root_final_path):
        #     os.makedirs(self._root_final_path)
        print("ii|final >> ", self._root_final_path)
        print("**|END   >> ")
        print("")

    def manage_backup(self):
        # if os.path.exists(self._root_back_path):
        #     shutil.rmtree(self._root_back_path)
        print("**|BACKUP",self._root_origin_path, ">>", self._root_back_path)
        shutil.copytree(self._root_origin_path, self._root_back_path)

    def manage_files(self):
        ext = [".doc", ".docx", ".pdf", ".epub", ".mobi", ".html", ".htm", ".txt"]

        print("**|BEGIN >> ")
        for path, dirs, files in os.walk(self._root_origin_path):
            dirs.sort()
            files.sort()

            for f in files:
                filename = os.path.splitext(f)
                if filename[1] in ext:
                    #
                    # file name
                    #
                    file_name = filename[0]
                    file_ext = filename[1][1:]  # strips the dot
                    file_name_parts = file_name.split(" - ")  # expected name parts "name - author"
                    # file_name_author = Autor.__turn_author_name(file_name_parts[1])
                    file_name_author = self._author
                    file_name_name = file_name_parts[0]
                    file_final_name = '.'.join([file_name_author, file_name_name, self._lang, file_ext])
                    #
                    # file paths
                    #
                    file_origin = os.path.join(path, f)
                    file_destination = os.path.join(self._root_final_path, file_final_name)
                    #
                    # file copy
                    #
                    print("  +--")
                    print("  |", file_origin)
                    print("  |", file_destination)
                    shutil.copy(file_origin, file_destination)

        print("  +--")
        [
            shutil.rmtree(os.path.join(self._root_origin_path, d))  # rmdir
            for d in os.listdir(self._root_origin_path)  # all dirs in path
            if os.path.isdir(os.path.join(self._root_origin_path, d))  # only the dirs that not begin with _
            ]
        print("  +--")
        print("**|END   >> ")

    @staticmethod
    def __turn_author_name(name):
        parts = name.split()
        new_name = parts.pop() + ", "
        new_name += " ".join(parts)
        return new_name  # rootpath='/parley/ALEXANDRIA'
