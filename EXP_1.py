# Read the student details
name = input("Enter the student name: ")
department = input("Enter the student department: ")
academic_year = input("Enter the student academic year: ")
pin_number = input("Enter the student PIN number: ")

# Print the student details
# Using the f-string
print("\nStudent Details:")
print(f"Name: {name}")
print(f"Department: {department}")
print(f"Academic Year: {academic_year}")
print(f"PIN Number: {pin_number}")

#print(f"\nStudent Details:\nName: {name}\nDepartment: {department}\nAcademic Year: {academic_year}\nPIN Number: {pin_number}")

"""
---------------------------------------------------------
#Other ways to print format in Python
---------------------------------------------------------
# Using the format() method
print("Name: {}".format(name))
print("Department: {}".format(department))
print("Academic Year: {}".format(academic_year))
print("PIN Number: {}".format(pin_number))
---------------------------------------------------------
# Using the % formatting
print("Name: %s" % name)
print("Department: %s" % department)
print("Academic Year: %s" % academic_year)
print("PIN Number: %s" % pin_number)
---------------------------------------------------------
# Using the string concatenation
print("Name: " + name)
print("Department: " + department)
print("Academic Year: " + academic_year)
print("PIN Number: " + pin_number)
---------------------------------------------------------
"""