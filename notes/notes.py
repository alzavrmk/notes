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
        # dt_note = datetime.strftime(date.today(), )
        note = Note(id_note, dt_note,  title_note, body_note)
        # note = Note(id_note, title_note, body_note)
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
        with open("data_file.json", "w") as write_file:
            json.dump(self, write_file)

    # def save_json(self):
    #     with open("data.json", "a") as fh:
    #         # for i in self.__list_notes:
    #         json.dump([i.__dict__ for i in self.__list_notes], fh,
    #                   cls=NoteEncoder, indent=2)
    # def read_json(self):
    #     with open("data.json", "r") as fh:
    #         for i in self.__list_notes:
    #             i = json.load(fh, object_hook=noteDecoder)

# def noteDecoder(obj):
#     return Note(obj['id'], obj['title_note'], obj['body_note'])







# d = datetime(2012, 1, 14)
#
# print(type(d.year))  # 2012
# print(d.day)  # 14
# print(d.month)  # 12
# s = ["15", 2, 1945]
# if len(s[0]) == 2 and s[0][0] == "0":
#     day = int(s[0][1])
# else:
#     day = int(s[0])
# print(day)
# month = int(s[1])
# year = int(s[2])
# d = datetime(year, month, day)
# print(d)
# l = Notes()
# l.add_note()
# print()
# print(date.today())
# print(date(2023, 8, 15))