from note.note import *
from notes.notes import *
# from notes.datatable import *
import json

#
# class ComplexEncoderClass(json.JSONEncoder):
#     def default(self, obj):
#         objDict = obj.__dict__
#         typeDict = {"__type__": type(obj).__name__}
#         return {**objDict, **typeDict}
#
# def ComplexDecoderFunction(jsonDict):
#     if '__type__' in jsonDict and jsonDict['__type__'] == 'Note':
#         return Note(jsonDict['id_note'], jsonDict['dt_create'],
#                     jsonDict['title_note'], jsonDict['body_note'])
#     # if '__type__' in jsonDict and jsonDict['__type__'] == 'Details':
#     #     return Details(jsonDict['Height'], jsonDict['Weight'])

l1 = Notes()
while True:
    print("Выберите действие")
    print("1. Создать заметку")
    print("2. Вывеси все заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Поиск по дате")
    # print("6. Сохранить заметки в файл")
    # print("7. Загрузить заметки из файла")
    print("8. Выход")
    choice = input('Ваш выбор (введите число от 1-5): ')
    if choice == "1":
        l1.add_note()
        print("Заметка добавлена\n")
    elif choice == "2":
        print(l1)
    elif choice == "3":
        id_note = input("Введите id заметки, которую хотите изменить: ")
        l1.edit_note(id_note)
    elif choice == "4":
        id_note = input("Введите id заметки, которую хотите удалить: ")
        l1.del_note(id_note)
    elif choice == "5":
        l1.search_date()
    elif choice == "8":
        print("Работа приложения завершена")
        break
    else:
        print("Неверный выбор")

#
# l1.add_note("Заголовок 2", "Тело2")
#
# print(l1)
# print(l1.del_note(1))
# print(l1.edit_note(2))
# print(l1)
# n1 = Note("Моя заметка", "Тело заметки")
# print(n1)
