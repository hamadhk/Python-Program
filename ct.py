class Teacher:
    def __init__(self, name):
        self._name = name  # Name is marked as protected (can be accessed by subclasses)
        self.__contact_info = "Not provided"  # Default contact information

    def introduce(self):
        return f"Hello, I am {self._name}, a teacher."

    def get_contact_info(self):
        return self.__contact_info


class Salary(Teacher):
    def __init__(self, name):
        super().__init__(name)
        self._salary = 5000  # Default salary is set to 5000

    def display_salary(self):
        return f"My salary is {self._salary} per month."


class Experience(Teacher):
    def __init__(self, name):
        super().__init__(name)
        self._years_of_experience = 5  # Default experience is set to 5 years

    def display_experience(self):
        return f"I have {self._years_of_experience} years of teaching experience."


class Department(Teacher):
    def __init__(self, name):
        super().__init__(name)
        self._department = "General"  # Default department is set to General

    def display_department(self):
        return f"I belong to the {self._department} department."


def main():
    # Get teacher's name as input
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
