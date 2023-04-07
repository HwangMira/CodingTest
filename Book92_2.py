# 큰 수의 법칙
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더해서 가장 큰 수를 만드는 법칙
# 단 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
# 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오.
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
# data 숫자를 크기 순서로 정렬했기 때문에 마지막이 가장 큰 숫자
first = data[n-1]
second = data[n-2]

result = 0

while True :
    for i in range(k) :
        if m == 0 :
            break
        result += first
        m -= 1
    if m == 0 :
        break
    result += second
    m -= 1

print(result)

# 위 방법은 M의 크기가 100억 이상처럼 커진다면 시간 초과 판정을 받을 것이다.
# 6, 5 ==> 6665 6665 같은 수가 반복적으로 주어진다.
# 수열이 K+1번 만큼 반복 m이 k+1로 나누어 떨어지지 않는 경우도 생각해야함.
# x
count = int(m / (k+1)) * k
count += m % (k+1)

result2 = 0
result2 += (count) * first
result2 += (m-count) * second

print(result2)