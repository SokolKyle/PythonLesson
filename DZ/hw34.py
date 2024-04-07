import json


# from pprint import pprint


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        a = ", ".join(map(str, self.marks))
        return f"Студент: {self.name}: {a}"

    def add_mark(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    def dump_to_json(self):
        data = {"name": self.name, "marks": self.marks}
        with open(self.get_file_name(), "w") as f:
            json.dump(data, f)

    def load_from_file(self):
        with open(self.get_file_name(), "r") as f:
            print(json.load(f))

    def get_file_name(self):
        return self.name + ".json"


class Group:
    def __init__(self, students, group: str):
        self.students = students
        self.group: str = group

    def __str__(self):
        a = "\n".join(map(str, self.students))
        return f"\nГруппа: {self.group}\n{a}"

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @staticmethod
    def change_group(group_1, group_2, index):
        group_2.add_student(group_1.remove_student(index))

    def dump_to_json(self):
        data = [
            {'name': student.name, 'marks': student.marks} for student in self.students
        ]
        with open(self.get_file_name(), 'w') as file:
            json.dump(data, file, indent=2)

    def get_file_name(self):
        return self.group.lower().replace(" ", "-") + ".json"

    def get_from_file(self):
        with open(self.get_file_name(), "r") as f:
            print(json.load(f))

    @staticmethod
    def dump_groups(file, group):
        try:
            data = json.load(open(file))
        except FileNotFoundError:
            data = {}

        with open(file, 'w') as f:
            stud_list = {}
            for i in group.students:
                stud_list[i.name] = i.marks

            data[group.group] = stud_list
            json.dump(data, f, indent=2)

    @staticmethod
    def load_groups(file):
        with open(file, "r") as f:
            print(json.load(f))


st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
sts1 = [st1, st2]
group1 = Group(sts1, "ГК Python")
# # print(group1)
group1.add_student(st3)
# # print(group1)
group1.remove_student(1)
# print(group1)
sts2 = [st2]
group2 = Group(sts2, "ГК Web")
# print(group2)
Group.change_group(group1, group2, 0)
# group2.dump_to_json()
# print(group1)
# print(group2)
# print(st1)
# st1.add_mark(4)
# print(st1)
# st1.delete_mark(2)
# print(st1)
# st1.edit_mark(4, 5)
# print(st1)
# print(st1.average_mark())

# st1.dump_to_json()
# st1.load_from_file()

print(group1)
print(group2)
Group.dump_groups("groups.json", group1)
Group.dump_groups("groups.json", group2)
Group.load_groups("groups.json")