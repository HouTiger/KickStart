def isEven(s):
    eight = -1
    for i in range(len(s)):
        if s[i] == '8':
        eight = i
        break
    for i in range(len(s)):
        if (int(s[i]) % 2) != 0:
            return False, i, eight
    return True, -1, eight
  
T = int(input())
# innum = [42, 11, 1, 2018]
for i in range(T):
    N = int(input())
    s = str(N)
    even, index, eight = isEven(s)
    if even:
        print('Case #' + str(i + 1) + ': 0')
    else:
        sl = s[0:index] + str(int(s[index]) - 1) + '8' * (len(s) - index - 1)
        nl = int(sl)
        sh = '0'
        nh = -1
        if s[index] != '9':
            sh = s[0:index] + str(int(s[index]) + 1) + '0' * (len(s) - index - 1)
            nh = int(sh)
            print('Case #' + str(i + 1) + ': ' + str(min(N - nl, nh - N)))
        else: 
            # s[index] == '9'
            if index == 0 or eight == 0:
            sh = '2' + '0' * len(s)
            elif s[index - 1] != '8':
            sh = s[0:index - 1] + str(int(s[index - 1]) + 2) + '0' * (len(s) - index)
            else:
            sh = s[0:eight - 1] + str(int(s[eight - 1]) + 2) + '0' * (len(s) - eight)
            nh = int(sh)
            print('Case #' + str(i + 1) + ': ' + str(min(N - nl, nh - N)))