# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    # 초기화(생성자) 메서드
    def __init__(self, id, name, balance):
        # 멤버 변수 숨기기 (__앞쪽)에 __(언더바2개)
        self.__id = id
        self.__name = name 
        self.__balance = balance
    # 입금 
    def deposit(self, amount):
        self.__balance += amount 
    # 출금
    def withdraw(self, amount):
        self.__balance -= amount
    # 상태를 문자열로 리턴
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
# 실수한 코드 
account1.balance = 15000000
print(account1)
# 외부에서 접근
# print(account1.__balance)
# 백도어(테스트) 
print(account1._BankAccount__balance)



