
class Person:
    pass
class Bird:
    pass
# 상속
class Student(Person):
    pass

# 인스턴스 생성 
p, s = Person(), Student()

# isinstance = true 인지 false 인지 판별 
print("p is instance of Person: ", isinstance(p, Person))
print("s is instance of Person: ", isinstance(s, Person))
print("p is instance of Object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("int is instance of Object: ", isinstance(int, object))