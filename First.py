#Hammad Khan
#Roll no: S23BSEEN1E02007
class Teacher:
    def __init__(self, name):
        self._name = name  # Name is marked as protected (can be accessed by subclasses)
        self.__contact_info = "Not provided"  # Default contact information.It is set as a Private Attribute.

    def introduce(self):
        return f"{self._name} is an Assistant Professor."

    def get_contact_info(self):
        return self.__contact_info


class Salary(Teacher):
    def __init__(self, name):
        super().__init__(name)
        self._salary = 50000  # Default salary is set to 50000 and is set as a private attribute.

    def display_salary(self):
        return f"Salary = {self._salary} per month."


class Experience(Teacher):
    def __init__(self, name):
        super().__init__(name)
        self._years_of_experience = 5  # Default experience is set to 5 years.It is set as public.

    def display_experience(self):
        return f"{self._years_of_experience} years of teaching experience."


class Department(Teacher):
    def __init__(self, name):
        super().__init__(name)
        self._department = "Software Engineering"  # Default department is set to General.It is a public attribute.

    def display_department(self):
        return f"{self._department} department."


def main():
    # Get the teacher's name as input
    teacher_name = input("Enter the teacher's name: ")

    # Creating instances of the Teacher, Salary, Experience, and Department classes
    teacher = Teacher(teacher_name)

    # Introducing the teacher
    print(teacher.introduce())

    # Displaying default contact information (private attribute)
    print(f"Contact Info: {teacher.get_contact_info()}")

    # Displaying subclass-specific information
    teacher_salary = Salary(teacher_name)
    print(teacher_salary.display_salary())

    teacher_experience = Experience(teacher_name)
    print(teacher_experience.display_experience())

    teacher_department = Department(teacher_name)
    print(teacher_department.display_department())


if __name__ == "__main__":
    main()
