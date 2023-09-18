#!/usr/bin/python3

"""Holds the model for the base class"""


import json
import os
import csv
import turtle
try:
    from .GenFunc import create_dictionary, myvars
except Exception:
    from GenFunc import create_dictionary, myvars


class Base:
    """
    The above class is a base class that provides methods for
    serializing and deserializing objects, saving objects to files,
    and drawing rectangles and squares using the turtle module.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes an object with an optional ID,
        assigning a unique ID if none is provided.

        Args:
          id: An optional parameter that can be passed to the constructor
            of the class. If a value is provided for "id", it will be
            assigned to the "id" attribute of the object. If no value is
            provided, the "id" attribute will be assigned the value of
            the __nb_objects
        """
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        converts a list of dictionaries into a JSON string.

        Args:
          list_dictionaries: A list of dictionaries that you want to
          convert to a JSON string.

        Returns:
          a JSON string representation of the input list of dictionaries.
          If the input list is empty, it returns "[]". Otherwise, it uses
          the json.dumps() function to convert the list of dictionaries
          into a JSON string.
        """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        converts a JSON string into a Python object.

        Args:
          json_string: The `json_string` parameter is a string that
          represents a JSON object or array.

        Returns:
          a list.
        """
        if not json_string or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        The function saves a list of objects to a JSON file.

        Args:
          cls: The parameter `cls` refers to the class object
            itself. It is used to access class-level attributes
            and methods.
          list_objs: The parameter `list_objs` is a list of objects
            that you want to save to a file. The objects in the list
            should be instances of the class `cls`.
        """
        class_name = cls.__name__
        with open(f"{class_name}.json", "w", encoding="utf-8") as file:
            ret = []
            for i in list_objs:
                ret.append(i.to_dictionary())
            file.write(cls.to_json_string(ret))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        saves a list of objects to a CSV file by converting each object
        to a dictionary and writing the dictionary values to the file.

        Args:
          cls: The parameter `cls` is a reference to the class object.
            It is used to determine the name of the class for the filename.
          list_objs: The parameter `list_objs` is a list of objects that
            you want to save to a CSV file. Each object in the list
            should have a method `to_dictionary()` that returns a dictionary
            representation of the object's attributes.
        """
        class_name = cls.__name__
        with open(f"{class_name}.csv", "w", encoding="utf-8") as file:
            ret = []
            col_names = []
            for i in list_objs:
                ret.append(i.to_dictionary())
            writer = csv.writer(file)
            for value in ret:
                lent = []
                for k, v in value.items():
                    lent.append(v)
                writer.writerow(lent)

    @classmethod
    def create(cls, **dictionary):
        """
        creates an instance of a class (either Rectangle or Square) and
          updates its attributes using a dictionary.

        Args:
          cls: The parameter `cls` is a reference to the class that is
            being instantiated. It is used to determine which class to
            create an instance of (either `Rectangle` or `Square`).

        Returns:
          an instance of either the Rectangle or Square class, depending
          on the value of `cls.__name__`.
        """
        dummy = None
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        loads data from a JSON file and returns a list of objects
          created from the loaded data.

        Args:
          cls: The parameter `cls` is a reference to the class itself.
            It is used to access class attributes and methods within
            the method.

        Returns:
          The method is returning a list of objects created from the
          data read from the file.
        """
        file_name = f"{cls.__name__}.json"
        if not os.path.exists(file_name):
            ret = []
        with open(file_name, "r", encoding="utf-8") as file:
            data = file.read()
            ret = [cls.create(**item) for item in cls.from_json_string(data)]
            return ret

    @classmethod
    def load_from_file_csv(cls):
        """
        loads data from a CSV file and creates instances of a
          class based on the data.

        Args:
          cls: The parameter `cls` is a reference to the class
            that the method is being called on. It is used to
            determine the name of the file to load data from and
            to create instances of the class using the loaded data.

        Returns:
          a list of objects created from the data read from
          the CSV file.
        """
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
        """
        takes in a list of rectangles and a list of squares,
        and uses the turtle module to draw each shape on
        the screen.

        Args:
          list_rectangles: A list of rectangle objects. Each
            rectangle object should have the following attributes:
          list_squares: A list of square objects. Each square object
            should have the following attributes:
        """
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
