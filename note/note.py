import datetime
class Note:
    def __init__(self, id_note, dt_create, title_note, body_note):
        self.verify_title_note(title_note)
        self.verify_body_note(body_note)
        self.__id_note = id_note
        self.__dt_create = dt_create
        self.__title_note = title_note
        self.__body_note = body_note

    @classmethod
    def verify_title_note(cls, title_note):
        if type(title_note) != str:
            raise TypeError("Введена не строка!")
        if len(title_note) >= 256:
            raise TypeError("Название заметки не должно содержать "
                            "более 256 символов")

    @classmethod
    def verify_body_note(cls, body_note):
        if type(body_note) != str:
            raise TypeError("Введена не строка!")

    def __str__(self):
        return f"{self.__id_note}\n" \
               f"{self.__dt_create}\n" \
               f"{self.__title_note}\n" \
               f"{self.__body_note}\n\n"


    @property
    def id(self):
        return self.__id_note

    @id.setter
    def id(self, id_note):
        self.__id_note = id_note

    @property
    def title(self):
        return self.__title_note

    @title.setter
    def title(self, title_note):
        self.verify_title_note(title_note)
        self.__title_note = title_note

    @property
    def date(self):
        return self.__dt_create

    @date.setter
    def date(self, date_note):
        self.__dt_create = date_note

    @property
    def body(self):
        return self.__body_note

    @body.setter
    def body(self, body_note):
        self.verify_body_note(body_note)
        self.__body_note = body_note


