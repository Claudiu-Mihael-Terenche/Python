import sys

set1 = {"A", 1, "B", 2, "C", 3}
set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}

# Using getsizeof() function:
print("Size of Set1: " + str(sys.getsizeof(set1)) + " bytes")
print("Size of Set2: " + str(sys.getsizeof(set2)) + " bytes")
print("Size of Set3: " + str(sys.getsizeof(set3)) + " bytes")

# Using inbuilt __sizeof__() method:
print("Size of Set1: " + str(set1.__sizeof__()) + " bytes")
print("Size of Set2: " + str(set2.__sizeof__()) + " bytes")
print("Size of Set3: " + str(set3.__sizeof__()) + " bytes")
