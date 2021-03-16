import random as rd


print("# random 모듈")

print(f"- random():{rd.random()} ")

print(f"- uniform(10,20):{rd.uniform(10,20)}")
print(f"- randrange(10):{rd.randrange(10)}")
print(f"- randrange(10,20):{rd.randrange(10,20)}")

print(f"- choice([1,2,3,4,5]):{rd.choice([1,2,3,4,5])}")
print(f"- shuffle([1,2,3,4,5]):{rd.shuffle([1,2,3,4,5])}")
print(f"- sample([1,2,3,4,5],k=2 ):{rd.sample([1,2,3,4,5],k=2)}")

