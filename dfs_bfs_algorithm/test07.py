answer = 0
def solution(numbers, target):
    global answer
    dfs(numbers, target, 0)
    print('aa')
    return answer

def dfs(numbers, target, i):
    global answer
    if i == len(numbers):
        if sum(numbers) == target:
            answer += 1
        return
    else:
        dfs(numbers,target,i+1)
        print('ss')
        numbers[i] *= -1
        dfs(numbers,target,i+1)
