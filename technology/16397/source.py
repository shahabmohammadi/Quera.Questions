class Grade:
    def __init__(self, student_id, course_code, score):
        self.student_id = int(student_id)
        self.course_code = int(course_code)
        self.score = float(score)


class CourseUtil:
    def __init__(self):
        self.address = str
        self.line_number = int

    def set_file(self, address):
        self.address = address

    def load(self, line_number):
        if self.count() < line_number:
            return None
        else:
            with open(self.address)as my_file:
                row_counter = 1
                for row in my_file:
                    if row_counter == line_number:
                        target = row.split(" ")
                        student_id = target[0]
                        course_id = target[1]
                        if line_number == self.count():
                            grade = target[2]
                        else:
                            grade = list(target[2])
                            grade.pop()
                            grade = "".join(grade)
                        grade = Grade(student_id, course_id, grade)
                        return grade
                    else:
                        row_counter += 1

    def save(self, grade):
        with open(self.address, mode="r+")as my_file:
            for row in my_file:
                target = row.split(" ")
                if int(target[0]) == grade.student_id or int(target[1]) == grade.course_code:
                    return
            if self.count() == 0:
                new_row = f"{grade.student_id} {grade.course_code} {grade.score}"
                my_file.write(new_row)
            else:
                my_file.readline()
                new_row = f"\r{grade.student_id} {grade.course_code} {grade.score}"
                my_file.write(new_row)

    def calc_course_average(self, course_code):
        with open(self.address) as my_file:
            rows = [str(row).split(" ") for row in my_file if row.split(" ")[1] == str(course_code)]
        avg = 0
        for row in rows:
            grade = list(row[2])
            if grade[-1] == "\n":
                grade.pop()
            grade = "".join(grade)
            avg += float(grade)
        if len(rows) == 0:
            return 0
        return avg / len(rows)

    def calc_student_average(self, student_id):
        with open(self.address) as my_file:
            rows = [str(row).split(" ") for row in my_file if row.split(" ")[0] == str(student_id)]
        avg = 0
        for row in rows:
            grade = list(row[2])
            if grade[-1] == "\n":
                grade.pop()
            grade = "".join(grade)
            avg += float(grade)
        if len(rows) == 0:
            return 0
        return avg / len(rows)

    def count(self):
        with open(self.address, mode="r")as my_file:
            counter = 0
            for row in my_file:
                counter += 1
            return counter
