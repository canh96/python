#번호 가중치를 준 로또프로그램   (가중치 = 자주 나오는 값)
import random as rnd

numbers = weights = list(range(1, 46))   # i for i range(1, 46) 을 써도 됌
lotto = []
rnd.shuffle(weights)

lotto = rnd.choices(numbers, weights = weights, k = 6)
lotto.sort()
print(lotto)
