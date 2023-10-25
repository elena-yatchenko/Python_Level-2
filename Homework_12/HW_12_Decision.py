import csv

# class Check:
    
#     def __init__(self, name):
#         self.name = name
        
#     def ___set__(self, instance, value):
#         self.validate(value)
#         setattr(instance, self.name, value)
        
#     def validate(self, value):
#         if not value.replace(' ', '').isalpha() or not value.istitle():
#             raise ValueError(f'ФИО должно состоять только из букв и начинаться с заглавной буквы')


class Student:
     
    
    """Конструктор класса. Принимает имя студента и файл с предметами и их результатами"""
    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)
    
    """проверяет ФИО на первую заглавную букву и наличие только букв"""
    def __setattr__(self, item, value):
        if item == 'name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                raise ValueError(f'ФИО должно состоять только из букв и начинаться с заглавной буквы')
        return object.__setattr__(self, item, value)
      

    """Возвращает строковое представление студента, включая имя и список предметов"""
    def __str__(self):
        return f'Студент: {self.name}\n Предметы: {", ".join(self.subjects.keys())}'
    
    """Загружает предметы из файла CSV. Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут subjects"""   
    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', newline='', encoding='utf-8') as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                subject = line[0]
                self.subjects[subject] = {'grade': [], 'test_score': []}
            return self.subjects
            
            
    """Добавляет оценку по заданному предмету. Убеждается, что оценка является целым числом от 2 до 5"""
    def add_grade(self, subject, grade):
        grade_min = 2
        grade_max = 5
        if subject not in self.subjects:
            raise ValueError(f'Предмет {subject} не найден')
        if not isinstance(grade, int) or grade < grade_min or grade > grade_max:
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        else:
            for key, value in self.subjects.items():
                if key == subject:
                    value['grade'].append(grade)
        return self.subjects

    
    """ Добавляет результат теста по заданному предмету. Убеждается, что результат теста является целым числом от 0 до 100."""
    def add_test_score(self, subject, test_score):   
        test_score_min = 0
        test_score_max = 100
        if subject not in self.subjects:
            raise ValueError(f'Предмет {subject} не найден')
        if not isinstance(test_score, int) or test_score < test_score_min or test_score_max > test_score_max:
            raise ValueError('Результат теста должен быть целым числом от 0 до 100')
        else:
            for key, value in self.subjects.items():
                if key == subject:
                    value['test_score'].append(test_score)
        return self.subjects
    
        
    """Возвращает средний балл по тестам для заданного предмета."""
    def get_average_test_score(self, subject):
        for key, value in self.subjects.items():
            if key == subject:
                average_test_score = sum(value['test_score']) / len(value['test_score'])
        print(f"Средний результат по тестам по предмету {subject}: {average_test_score}")
        return average_test_score
    
    """Возвращает средний балл по всем предметам"""
    def get_average_grade(self):
        sum_grade = 0
        mean_grade = 0
        sum_subjects = 0
        for value in self.subjects.values():
            if value['grade']: # условие, что не пустой список баллов по этому предмету
                mean_grade = sum(value['grade']) / len(value['grade'])
                sum_grade += mean_grade
                sum_subjects += 1
        average_grade = sum_grade / sum_subjects
        print(f"Средний балл: {average_grade: .2f}")
        return average_grade
    
student = Student("Иван Иванов Gtnz", "subjects.csv")
#print(student.subjects)
student.add_grade("Химия", 4)
# student.add_test_score("Математика", 85)


# student.add_grade("История", 5)
# student.add_test_score("История", 92)
# student.add_grade("История", 4)
# student.add_grade("История", 5)
# student.add_grade("Математика", 5)
# student.add_test_score("Математика", 10)
# student.add_test_score("Математика", 58)
# print(student.subjects)

# average_grade = student.get_average_grade()
# # print(f"Средний балл: {average_grade}")

# average_test_score = student.get_average_test_score("Математика")


# print(student)
        
    
        