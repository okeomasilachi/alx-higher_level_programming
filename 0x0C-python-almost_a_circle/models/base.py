#!/usr/bin/python3

""""""
import json
import os
import csv
import turtle
try:
    from .GenFunc import create_dictionary, myvars
except:
    from GenFunc import create_dictionary, myvars

# The above class is a base class.
class Base:

    # The line `__nb_objects = 0` is creating a class variable called `__nb_objects` and initializing
    # it to 0. This variable is used to keep track of the number of objects that have been created
    # from the `Base` class.
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes an object with an optional ID,
        assigning a unique ID if none is provided.

        Args:
          id: An optional parameter that can be passed to the constructor of the
        class. If a value is provided for "id", it will be assigned to the "id"
        attribute of the object. If no value is provided, the "id" attribute will
        be assigned the value of the __nb_objects
        """
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if not json_string or json_string == None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        class_name = cls.__name__
        with open (f"{class_name}.json", "w", encoding="utf-8") as file:
            ret = []
            for i in list_objs:
                ret.append(i.to_dictionary())
            file.write(cls.to_json_string(ret))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        class_name = cls.__name__
        with open (f"{class_name}.csv", "w", encoding="utf-8") as file:
            ret = []
            col_names = []
            for i in list_objs:
                ret.append(i.to_dictionary())
            writer = csv.writer(file)
            for value in ret:
                l = []
                for k, v in value.items():
                    l.append(v)
                writer.writerow(l)

    @classmethod
    def create(cls, **dictionary):
        dummy = None
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        file_name = f"{cls.__name__}.json"
        if not os.path.exists(file_name):
            ret = []
        with open(file_name, "r", encoding="utf-8") as file:
            data = file.read()
            ret = [cls.create(**item) for item in cls.from_json_string(data)]
            return ret

    @classmethod
    def load_from_file_csv(cls):
        file_name = f"{cls.__name__}.csv"
        if not os.path.exists(file_name):
            return []

        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            name = []
            if cls.__name__ == "Rectangle":
                name = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                name = ["id", "size", "x", "y"]

            data = []
            for row in reader:
                dic = create_dictionary(name, row)
                data.append(dic)

        return [cls.create(**item) for item in data]

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        screen.bgcolor("white")

        pen = turtle.Turtle()

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            for _ in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        screen.mainloop()