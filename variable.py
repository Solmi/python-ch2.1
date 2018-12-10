# 변수 이름은 문자, 숫자, _로 구성된다
# friend = 1
# my_name = "ㅊㅅㅁ"
# _yourName = "ㅈㅈㅎ"
# member1 = "gev"
# long_string = """#
# 첫번쨰라인
# 두번째라인#
# 세번쨰라인
# """

# 에러 : 다른 구성의 변수 이름은 사용할 수 없다
# friend$ = 1
# a! = 10
# 1member = 10

# 에러 : 예약어는 변수 이름으로 사용할 수 없다
# def = 1
# 예약어 리스트 보기
import keyword
print(keyword.kwlist)
# [] List 리스트
# {} Dic 딕셔너리
# () Turple 튜플

print(len(keyword.kwlist))

# 한글이름의 변수고 사용 가능
가격1 = 2000
print(가격1)

