# 1이 될 때까지
# 어떠한 수 N이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
# 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다. 2. N을 K로 나눈다.
# 예를 들어 N이 17, K가 4일 때 1번의 과정을 수행하면 16, 2번의 과정을 두번 수행하면 N은 1이 된다.
# 이 경우 전체 과정을 실행한 횟수는 3이 된다. 이는 N을 1로 만드는 최소 횟수이다.
# N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성해라.

n, k = map(int, input().split())
result = 0

## K로 최대한 N을 나누는 것이 최적의 해를 보장한다.
while n >= k :
    if n % k != 0 :
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1 :
    n -= 1
    result += 1

print(result)

while True :
    target = (n // k) * k
    result += (n-target)
    n = target
    if n < k :
        break
    result += 1
    n //= k

result += (n-1)
print(result)
