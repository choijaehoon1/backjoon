answer = 0
def solution(begin, target, words):
    global answer
    visit = [0 for _ in range(len(words))]
    if target not in words:
        return 0
    dfs(begin,target,words,visit)
    return answer

def dfs(begin,target,words,visit):
    global answer
    stacks = [begin]
    while stacks:
        current_node = stacks.pop()
        if current_node == target:
            return answer
        for w in range(len(words)):
            if len([i for i in range(len(words[w])) if words[w][i] != current_node[i]]) == 1 and visit[w] == 0:
                visit[w] = 1
                stacks.append(words[w])
        answer+=1
