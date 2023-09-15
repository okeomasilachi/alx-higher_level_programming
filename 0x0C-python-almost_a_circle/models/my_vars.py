#!/usr/bin/python3

"""
"""




class person:
    def __init__(self, first_name="", last_name="", age=00):
        self.age = age
        self.last_name =last_name
        self.first_name = first_name
    def __str__(self):
        return f"first name: {self.first_name}\nlast name: {self.last_name}\nage: {self.age}"


p1 = person("Okeomasilachi", "Onyedibia", 67)
print(p1)
print(myvars(p1, ["age", "first_name"]))