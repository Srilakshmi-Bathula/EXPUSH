class ComplexNumber:
    def add_complex(self):
        a = complex(input("Enter first complex number: "))
        b = complex(input("Enter second complex number: "))
        return a + b

obj = ComplexNumber()
result = obj.add_complex()
print("The sum of the complex numbers is:", result)
