#1074_z(백준)

N,r,c = map(int, input().split())
count = 0

def zigzag(xi, yi, count, num):  # small z
    if count == (num+1)*2**(N-1)*2**(N-1) and count!=4:  # N=2 인 경우 예외있음
        if num==0 or num==2: 
            yi = 2**(N-1)
            xi = (num//2)*2**(N-1)
        elif num==1:
            xi = 2**(N-1)
            yi = 0
        else:
            return count

        return zigzag(xi, yi, count, num+1)
    
    if (r-xi)==0:
        if (c-yi)==1 or (c-yi)==0:
            count = count + (c-yi)
            return count
    elif (r-xi)==1 and (c-yi)==1:
            count += 3
            return count
    elif (r-xi)==1 and (c-yi)==0:
            count += 2
            return count
    else:
        count += 4
        if yi + 2 < (num%2+1)*2**(N-1):  # num은 0부터 시작
            yi += 2
        else:
            xi += 2
            yi = 0 if num%2==0 else 2**(N-1)
        return zigzag(xi, yi, count, num)
    
answer = zigzag(0,0,count,0)
print(answer)