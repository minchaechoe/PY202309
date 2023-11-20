class Student:
    def __init__(self, name, korean, math, english):
        self.name = name
        self.korean = float(korean)
        self.math = float(math)
        self.english = float(english)
    
    def get_average(self):
        total = self.korean + self.math + self.english
        return total / 3