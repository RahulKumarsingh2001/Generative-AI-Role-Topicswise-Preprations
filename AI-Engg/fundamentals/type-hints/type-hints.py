# Type hints in Python allow you to specify what types of values a function 
# expects and what type of value it should return.


# without type hints
def add(a, b):
    return a + b
print(add(10, 20))



# with type hints
def add(a: int, b: int) -> int:
    return a + b
print(add(10, 20))



# Type hints for variables
name: str = "Rahul"
age: int = 25
salary: float = 45000.50
is_employed: bool = True




# Type hints in functions
def greet(name: str) -> str:
    return f"Hello, {name}"

def is_even(number: int) -> bool:
    return number % 2 == 0


# if function not return anythings
def display_message(message: str) -> None:
    print(message)
    
    
    
    
    
# Type hints for collections
# List
numbers: list[int] = [10, 20, 30]
names: list[str] = ["Rahul", "Amit", "Priya"]


# Dictionaries
student: dict[str, int] = {
    "Rahul": 85,
    "Amit": 90
}


# Tuples
person: tuple[str, int] = ("Rahul", 25)


# Sets    
unique_numbers: set[int] = {10, 20, 30}






# optional value
def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Rahul"

    return None




# Type hints for multiple possible types — Union
def display(value: int | str) -> None:
    print(value)
    
    
    
    
    
    
    
    
# Type hints for dictionaries and real-world data
def create_expense(
    expense_id: int,
    title: str,
    amount: float
) -> dict[str, int | str | float]:
    return {
        "id": expense_id,
        "title": title,
        "amount": amount
    }    