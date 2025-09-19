class ComplexNumber:
    def sub_complex(self):
        a = complex(input("Enter first complex number: "))
        b = complex(input("Enter second complex number: "))
        return a - b

obj = ComplexNumber()
result = obj.sub_complex()
print("The diff of the complex numbers is:", result)