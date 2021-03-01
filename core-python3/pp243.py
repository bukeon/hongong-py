def flatten(data):
    result = []
    for item in data:
        # 만약 data에서 뽑은 요소의 타입이 list라면
        if isinstance(item, list):
            flatten(item)
            # 요소(item)를 인자로 보내서 재귀 호출 실행
            result.extend(flatten(item))
        else:
            # 리스트 타입이 아닌 정수 타입은 바로 뒤에 붙이기
            result.append(item)

    return result


example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print(f'원본: {example}')
print(f'변환: {flatten(example)}')