# 숫자 카드게임
# 숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
# 게임의 룰이다.
# N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
# 카드의 행을 선택한다. 가장 숫자가 낮은 카드를 뽑아야한다. 따라서 처음에 카드를 골라낼 행을 선택할 때,
# 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 고려한다.

N, M = map(int, input().split())

# 행 한줄마다 가장 작은 답을 찾고 그 결과를 그다음 행과 비교해서 출력한다.
for i in range(N) :
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)

# 파이썬 문법 !
# max(result, min_value)
# if min_value > result :
#     result = min_value
# result가 가장 큰 값


# 다른 방법!
n, m = map(int, input().split())

for i in range(n) :
    data = list(map(int,input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
        # if min_value < a :
        #     a = min_value
        # 파이썬 문법 결과값이 가장 작은 값을 찾을 때 쓴다.
    # 행마다 가장 작은 수를 찾고 그 수들 중 가장 큰 값을 출력한다.
    result = max(result, min_value)