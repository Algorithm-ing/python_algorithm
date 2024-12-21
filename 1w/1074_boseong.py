# 입력받기: N(크기), r(행), c(열)
N, r, c = map(int, input().split())

# 방문 순서를 저장할 변수
cnt = 0

while N > 1:
    size = 2 ** (N - 1)  # Z 배열 한 변 길이
    total_cells = size * size  # 한 사분면에 포함된 셀 수

    # 현재 위치가 어느 사분면에 있는지 확인
    if r < size and c < size:  # 2사분면
        pass  # 아무 작업도 하지 않음
    elif r < size and c >= size:  # 1사분면
        cnt += total_cells  # 1사분면까지의 방문 순서를 더함
        c -= size  # 열 좌표를 1사분면 기준으로 변환
    elif r >= size and c < size:  # 3사분면
        cnt += total_cells * 2  # 3사분면까지의 방문 순서를 더함
        r -= size  # 행 좌표를 3사분면 기준으로 변환
    elif r >= size and c >= size:  # 4사분면
        cnt += total_cells * 3  # 4사분면까지의 방문 순서를 더함
        r -= size  # 행 좌표를 4사분면 기준으로 변환
        c -= size  # 열 좌표를 4사분면 기준으로 변환

    # 배열 크기를 절반으로 줄이고 다음 단계로 진행
    N -= 1

# 마지막 단계의 2x2 배열 처리
# r과 c에 따라 결과값을 출력
cnt += r * 2 + c
print(cnt)
