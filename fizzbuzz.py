# linux 환경에서 코드
## vi fizzbuzz.py
### i -> print('hello') -> esc -> :wq + enter

# branch 이동 시에는 무조건 commit 을 하고 넘어갈 것 !

for i in range(1,16+1):
    if i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(i)
