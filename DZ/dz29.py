class Student:
    def __init__(self, name):
        self.name = name
        self.notebook = self.Notebook()

    def display(self):
        print(
            f'{self.name} '
            '=> '
            f'{self.notebook.manufacture}, '
            f'{self.notebook.CPU}, '
            f'{self.notebook.memory}'
        )

    class Notebook:
        def __init__(self):
            self.manufacture = 'HP'
            self.CPU = 'i7'
            self.memory = '16'


roman = Student('Roman')
roman.display()
vladimir = Student('Vladimir')
vladimir.display()
