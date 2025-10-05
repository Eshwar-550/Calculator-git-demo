def add(num1,num2):
  return num1 + num2

def subtract(num1,num2):
  return num1 - num2

def multiply(num1,num2):
  return num1 * num2

def divide(num1,num2):
  return num1 / num2

def calculator():
  print("Select Option:")
  print("1.Addition")
  print("2.Subtraction")
  print("3.Multiplication")
  print("4.Division")

  choice = input("Enter your choice(1,2,3,4):")

  num1 = int(input("Enter first number:"))
  num2 = int(input("Enter second number:"))

  if choice == "1":
    print("Result:", add(num1,num2))
  elif choice == "2":
    print("Result:", subtract(num1,num2))
  elif choice == "3":
    print("Result:", multiply(num1,num2))
  elif choice == "4":
    print("Result:", divide(num1,num2))

if __name__ == "__main__":
  calculator()
