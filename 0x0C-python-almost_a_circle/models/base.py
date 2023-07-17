#!/usr/bin/python3

"""
Module for the Base class.
"""
from collections import OrderedDict
import csv
import turtle
import json


class Base:
    """
    Base class for other classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a base object.

        Args:
           id (int): The unique identifier for the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string representation.

        Args:
           list_dictionaries (list): A list of dictionaries.

        Returns:
           str: The JSON string representation.
        """
        if list_dictionaries is None or not bool(list_dictionaries):
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a file in JSON format.

        Args:
            list_objs (list): A list of objects.

        Returns:
            None
        """
        filename = "{}.json".format(cls.__name__)
        list_dictionaries = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                list_dictionaries.append(dictionary)
            json_string = Base.to_json_string(list_dictionaries)
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string representation to a list of dictionaries.

        Args:
           json_string (str): A JSON string.

        Returns:
           list: A list of dictionaries.
        """
        if json_string is None or not bool(json_string):
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of the class with attributes already set.

        Args:
           dictionary (dict): A dictionary with the attributes of the object.

        Returns:
           object: An instance with the attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a file.

        Args:
            None

        Returns:
            list: A list of instances.
        """
        filename = "{}.json".format(cls.__name__)
        instance_list = []
        try:
            with open(filename, 'r') as f:
                json_string = f.read()
                dictionary_list = cls.from_json_string(json_string)
                for item in dictionary_list:
                    instance = cls.create(**item)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of objects to a file in CSV format.

        Args:
            list_objs (list): A list of objects.

        Returns:
            None
        """
        filename = "{}.csv".format(cls.__name__)
        data = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                data.append(dictionary)
        rectangle_header = ['id', 'width', 'height', 'x', 'y']
        square_header = ['id', 'size', 'x', 'y']
        with open(filename, mode='w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == 'Rectangle':
                    result = csv.DictWriter(f, fieldnames=rectangle_header)
                elif cls.__name__ == 'Square':
                    result = csv.DictWriter(f, fieldnames=square_header)
                result.writeheader()
                result.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads a list of instances from a CSV file.

        Args:
            None

        Returns:
            list: A list of instances.
        """
        filename = "{}.csv".format(cls.__name__)
        instance_list = []
        try:
            with open(filename) as f:
                result = csv.DictReader(f)
                for row in result:
                    row = dict(row)
                    for key in row:
                        row[key] = int(row[key])
                    instance = cls.create(**row)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws shapes using the turtle module.

        Args:
           list_squares (list): A list of Square objects.
           list_rectangles (list): A list of Rectangle objects.

        Returns:
           None
        """
        s = turtle.getscreen()
        t = turtle.Turtle()

        turtle.title("My first draw with Python and turtle module")

        t.shape("turtle")
        turtle.bgcolor("black")

        t.pen(pencolor="blue", fillcolor="white", pensize=5, speed=1)

        for instance in list_rectangles:
            t.pen(pencolor="blue", fillcolor="white", pensize=5, speed=1)
            data = instance.to_dictionary()

            t.home()
            t.setpos(data['x'], data['y'])

            t.pd()
            for i in range(2):
                t.forward(data['width'])
                t.left(90)
                t.forward(data['height'])
                t.left(90)
            t.pu()

        t.pen(pencolor="red", fillcolor="white", pensize=5, speed=0.5)

        for instance in list_squares:
            data = instance.to_dictionary()
            t.home()
            t.setpos(data['x'], data['y'])
            t.pd()
            for i in range(4):
                t.forward(data['size'])
                t.left(90)
            t.pu()

        turtle.getscreen()._root.mainloop()
