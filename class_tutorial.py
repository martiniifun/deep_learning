# 절차 지향 프로그래밍(근 백년 동안 유지)
a = 1
b = 2
c = a + b
print(c)

# 프로그래머들이 피곤해지기 시작
# 모든 변수, 모든 함수,
# 변수 10만개와 함수 1만개의 관계
# 전적으로 프로그래머가 숙지해야 함.

# 사람 10명에 대한 정보
사람1_이름 = "신명진"
사람2_이름 = "박명진"
사람3_이름 = "최명진"
...
사람10_이름 = "김명진"


# 객체 지향 프로그래밍(Object Oriented Programming, OOP)
# 가장 큰 장점 : 관계를 표시할 수 있다. 읽기 수월
# 코드의 중복이 현저하게 줄어든다.
# 캡슐화, 클래스간 통신 가능, ....
# 객체지향의 유일한 단점 : 복잡하다. -> 설계를 필요로 함.

# 클래스           vs   인스턴스
# 붕어빵틀(설계도) vs 붕어빵(실체)

# 물고기(클래스) vs 광어(인스턴스)
# 물고기(클래스) vs 옥돔(인스턴스)
# 물고기(클래스) vs 고등어(인스턴스)


class 물고기:

    # 클래스 변수
    눈갯수 = 2
    사는곳 = "물"
    지느러미보유 = True
    마릿수 = 0

    # 인스턴스 변수(생성자 메서드 안에 정의)
    def __init__(self, 이름, 비늘여부):
        self.이름 = 이름
        self.비늘여부 = 비늘여부
        물고기.마릿수 += 1

    # 인스턴스 메서드
    def 헤엄(self):
        print("첨벙첨벙")

    def 먹기(self):
        print("냠냠")

    # 클래스 메서드

    @classmethod
    def 한마리죽음(cls):
        cls.마릿수 -= 1
        print("한 마리가 죽었습니다.")
        print("마릿수를 1 줄입니다.")
        print(f"현재 마릿수는 {cls.마릿수}입니다.")




광어 = 물고기("광어", True)
복어 = 물고기("복어", False)

print("광어의 눈 갯수는 ", 광어.눈갯수, "개")
print("복어의 눈 갯수는 ", 복어.눈갯수, "개")

광어.헤엄()
복어.헤엄()
광어.먹기()
복어.먹기()
print(광어.비늘여부)  # True
print(복어.비늘여부)  # False

print(광어.마릿수)
print(복어.마릿수)
print(물고기.마릿수)
넙치 = 물고기("넙치", True)
print(광어.마릿수)
print(복어.마릿수)
print(물고기.마릿수)

광어.마릿수 = 100
print(물고기.마릿수)  # 3? 100?
print(넙치.마릿수)  # 3? 100?
print(광어.마릿수)  # 3? 100?
물고기.한마리죽음()
복어.한마리죽음()
물고기.한마리죽음()

###################################################

# "계좌"라는 클래스를 만들고
# 인스턴스 변수 : 잔액, 예금주
# 인스턴스 메서드 : 입금, 출금, 잔액조회
# 클래스 변수 : 개설계좌수