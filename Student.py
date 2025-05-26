"""Module for managing student information and grades."""
class Student:
    """
    Student module for managing grades and information.
    """
    def __init__(self, student_id, name):
        """
        Initialize a Student object.

        Args:
            student_id (str): Unique ID of the student.
            name (str): Name of the student.
        """
        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.letter = "F"
        self.honor = False
    def add_grades(self, g):
        """
        Add a grade to the student's record.

        Args:
            g (int or float): Grade to add.

        Returns:
            None
        """
        if not isinstance(g, (int, float)):
            print("Invalid grade type")
            return
        self.grades.append(g)

    def calc_average(self):
        """
        Calculate the average of the student's grades.

        Returns:
            float: Average grade. Returns 0 if there are no grades.
        """
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def check_honor(self):
        """
        Check if the student qualifies for honor roll.

        Returns:
            None
        """
        average = self.calc_average()
        if average > 90:
            self.honor = True
        self.update_letter(average)

    def update_letter(self, avg):
        """
        Update the student's letter grade based on the average.

        Args:
            avg (float): The average grade.

        Returns:
            None
        """
        if avg >= 90:
            self.letter = "A"
        elif avg >= 80:
            self.letter = "B"
        elif avg >= 70:
            self.letter = "C"
        elif avg >= 60:
            self.letter = "D"
        else:
            self.letter = "F"

    def remove_grade_at_index(self, index: int):
        """
        Remove a grade at the specified index.

        Args:
            index (int): The index of the grade to remove.

        Returns:
            None
        """
        if not isinstance(index, int): # Le agrege error handling
            print("Index must be an integer")
            return

        if not self.grades:
            print("No grades to delete")
            return

        if index < 0 or index >= len(self.grades):
            print("Index out of range")
            return

        print(f"Removing grade at index: {index}")
        del self.grades[index]

    def report(self):
        """
        Print a report of the student's information and grades.

        Returns:
            None
        """
        print("ID: " + str(self.id))
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Final Grade = " + self.letter)
        print("Honor Student:", "Yes" if self.honor else "No")

def startrun():
    """
    Run a sample test of the Student class.
    """
    a = Student("x", "Jeremy Poveda")
    a.add_grades(100)
    a.add_grades("Fifty")
    a.calc_average()
    a.check_honor()
    a.remove_grade_at_index(5)
    a.report()

startrun()
