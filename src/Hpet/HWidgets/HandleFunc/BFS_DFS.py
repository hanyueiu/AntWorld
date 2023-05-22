graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def BFS(graph, s):  # s是起始点
    queue = []  # 数组可以动态的添加或者删除 append、pop
    queue.append(s)
    seen = []  # 来保存放过的节点
    seen.append(s)
    while (len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.append(node)
        print(vertex)  # 把当前拿出去的节点打印出来


def DFS(graph, start):  # 参数 graph是邻接节点的一个字典   参数start是起始点
    stack = []  # 当栈用
    seen = set()  # 创建一个集合，查重用(判断这条路是否已经走过)+记录路径的作用
    print("一笔画路径为:", end="")
    stack.append(start)
    seen.add(start)
    while (len(stack) > 0):
        vertx = stack.pop()  # 默认是从栈顶取出
        node = graph[vertx]
        for i in node:
            if i not in seen:  # 确保之前没有走过该节点
                stack.append(i)
                seen.add(i)
        print(vertx + "->", end="")
    print("\b\b")


BFS(graph, "B")
