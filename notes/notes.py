from note.note import *
# from notes.datatable import *
from datetime import date, datetime
import json

id_note = 0


class Notes:
    def __init__(self):
        self.__list_notes = []

    def get_list_notes(self):
        return str(self)

    def add_note(self):
        title_note = input("Заголовок заметки: ")
        body_note = input("Содержание заметки: ")
        global id_note
        id_note = id_note + 1
        dt_note = date.today()
        note = Note(id_note, dt_note,  title_note, body_note)
        self.__list_notes.append(note)

    def __str__(self):
        s = ""
        for i in self.__list_notes:
            s += str(i)
        return s

    def del_note(self, id_notes):
        try:
            id_n = int(id_notes)
            count = 0
            count1 = 0
            for i in self.__list_notes:
                count1 += 1
                if i.id == id_n:
                    self.__list_notes.remove(i)
                    print(f"Заметка под номером {id_notes} удалена!")
                else:
                    count += 1
            if count == count1:
                print(f"Заметки с id = {id_n} не существует!")
        except ValueError:
            print("Некорректный id!")

    def edit_note(self, id_notes):
        try:
            id_n = int(id_notes)
            count = 0
            count1 = 0
            for i in self.__list_notes:
                count1 += 1
                if i.id == id_n:
                    flag = True
                    while flag:
                        print("Что вы хотите изменить? \n"
                              "Нажмите 1 - если нужно изменить заголовок\n"
                              "Нажмите 2 - если нужно изменить содержание "
                              "заметки\n")
                        n = input()
                        if n == "1":
                            print("Введите новый заголовок")
                            i.title = input()
                            print(f"Заголовок заметки под номером{id_notes} "
                                  f"изменен!")
                            flag = False

                        elif n == "2":
                            print("Введите новое содержание заметки")
                            i.body = input()
                            print(f"Содержание заметки под номером {id_notes} "
                                  f"изменено!")
                            flag = False
                        else:
                            print("Введите 1 или 2")
                else:
                    count += 1
            if count == count1:
                print(f"Заметки с id = {id_n} не существует!")
        except ValueError:
            print("Некорректный id!")

    def search_date(self):
        date_note = input("Введите дату по образцу 01.01.2023: ")
        s = date_note.split(".")
        if len(s) == 3:
            try:
                if len(s[0]) == 2 and s[0][0] == "0":
                    day = int(s[0][1])
                else:
                    day = int(s[0])
                if len(s[1]) == 2 and s[1][0] == "0":
                    month = int(s[1][1])
                else:
                    month = int(s[1])
                if len(s[2]) == 4:
                    year = int(s[2])
                if 1 <= day <= 31 and 1 <= month <= 12 and year >= 2023:
                    date_note1 = date(year, month, day)
                    count, count1 = 0, 0
                    for i in self.__list_notes:
                        count1 += 1
                        if i.date == date_note1:
                            print(i)
                        else:
                            count += 1
                    if count == count1 and count != 0:
                        print(f"{date_note} заметки не создавались!")
                else:
                    print(f"{date_note} - некорректная дата!")
            except ValueError:
                print("Дата введена неверно!")
        else:
            print("Неверный ввод!")
    def save_notes(self):
        with open("f2.json", "a") as f:
            for note in self.__list_notes:
                f.write(json.dumps(note, cls=NoteEncoder))
                f.write("\n")

    def read_json(self):
        self.__list_notes.clear()
        objList = []
        with open("f2.json", "r") as f:
            for str_json in f:
                obj_dict = json.loads(str_json)
                objList.append(obj_dict)

        for obj in objList:
            note = Note(obj["id_note"],
                        obj["dt_create"],
                        obj["title_note"],
                        obj["body_note"])
            self.__list_notes.append(note)


class NoteEncoder(json.JSONEncoder):
    def default(self, n):
        if isinstance(n, Note):
            dict = {
                "id_note": n.id,
                "dt_create": n.date.strftime("%Y-%m-%d"),
                "title_note": n.title,
                "body_note": n.body
            }
            return dict