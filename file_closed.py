try:
    file = open("info.txt","w")

    file.close()
except Exception as e:
    print(e)

print("#파일 제대로 닫혔는지 확인하기")
print("file.closed:",file.closed)