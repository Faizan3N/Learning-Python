Immutable Objects in Python

Immutable = Cannot be changed after creation

✅ Common Immutable Types:

int

float

bool

str

tuple

frozenset

bytes

🧪 Examples:
int (Immutable)
a = 5
print(id(a))  # Memory address of 'a'

a += 1        # Creates a new int object
print(id(a))  # Different address — new object

str (Immutable)
s = "hello"
print(id(s))

s += " world"  # Creates a new string object
print(id(s))

tuple (Immutable)
t = (1, 2, 3)
# t[0] = 10     # ❌ Error: tuples are immutable

# You can create a new tuple, but not modify existing one
t = t + (4,)
print(t)

🔁 Mutable Objects in Python

Mutable = Can be changed after creation

✅ Common Mutable Types:

list

dict

set

bytearray

🧪 Examples:
list (Mutable)
lst = [1, 2, 3]
print(id(lst))

lst.append(4)     # Modifies the list in-place
print(lst)
print(id(lst))    # Same ID — object modified, not replaced

dict (Mutable)
person = {"name": "Alice", "age": 25}
person["age"] = 26     # Updates existing key
person["city"] = "NY"  # Adds a new key

print(person)

set (Mutable)
colors = {"red", "blue"}
colors.add("green")  # Adds an element
colors.discard("red")  # Removes an element

print(colors)