def calculation(a,b):

    return a+b, a-b, a*b, a/b



x,y = map(int, input().split())

a,b,c,d =calculation(x,y)

print('더하기 : {0}, 빼기 : {1}, 곱하기:{2}, 나누기{3}'.format(a,b,c,d))