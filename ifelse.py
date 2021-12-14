# ifelse.py
score = int(input("점수를입력 :"))

if 90 <= score <= 100:
    grade = "a"
elif 80 <= score < 90:
    grade = "b"
elif 70 <= score < 80:
    grade = "c"
else :
    grade = "d"

print("등급은", grade)
