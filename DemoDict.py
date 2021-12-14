# DemoDict.py
# = 주석
d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

color = {"apple": "red", "banana": "yellow"}
print (color)
print (type(color))


# 반복구문
# 하나의 반복
for item in color.items():
    print(item)

# 키와 값으로 
# 중단점(Break Point)
for k,v in color.items():
    print(k,v)


# 입력
print("------------입력--------")
color["kiwi"] = "green"
print(color)
print("------------삭제--------")
del color["apple"]
print(color)