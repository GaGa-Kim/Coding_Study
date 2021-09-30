S, K, H = map(int, input().split())
if S+K+H >= 100:
    print('OK')
else:
    a = min(S, K, H)
    if a == S:
        print('Soongsil')
    elif a == K:
        print('Korea')
    else:
        print('Hanyang')