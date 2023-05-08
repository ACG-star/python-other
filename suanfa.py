"""
@File    :   suanfa.py    
@Contact :   xwz3568@163.com

@Modify Time          @Author    @Version    @Description
------------          --------   --------    -----------
2023/3/15 0015 10:45  FuGui      1.0         算法设计
"""
# import sys
#
#
# def dijkstra(start_point, graph):
#     # n = len(graph)
#     # MAX = sys.maxsize   #相当于无穷大
#     # 初始化各项数据，把dist[start]初始化为0，其他无穷大
#     dist = [MAX for _ in range(n)]  # 路径长度初始化为无穷大
#     pre = [-1 for _ in range(n)]
#     s = [False for _ in range(n)]
#     dist[start_point] = 0
#     for i in range(n):
#         minLength = MAX
#         minVertex = -1
#         for j in range(n):
#             if not s[j] and dist[j] < minLength:
#                 minLength = dist[j]
#                 minVertex = j
#         s[minVertex] = True
#         for edge in graph[minVertex]:
#             if not s[edge[0]] and minLength + edge[1] < dist[edge[0]]:
#                 dist[edge[0]] = minLength + edge[1]
#                 pre[edge[0]] = minVertex
#     return dist, pre
#
#
# if __name__ == '__main__':
#     data = [[1, 0, 8], [1, 2, 5], [1, 3, 10],
#             [1, 6, 9], [2, 0, 1], [0, 6, 2],
#             [3, 6, 5], [3, 4, 8], [0, 5, 4],
#             [5, 6, 7], [5, 3, 8], [5, 4, 5]]
#     n = 7
#     MAX = sys.maxsize  # 相当于无穷大
#     graph = [[] for _ in range(n)]
#     for edge in data:
#         graph[edge[0]].append([edge[1], edge[2]])
#         graph[edge[1]].append([edge[0], edge[2]])
#     dist, pre = dijkstra(1, graph)
#     print("dist = ", dist)
#     print("pre = ", pre)

'''
import sys
def dijkstra(start_point,graph):
    n = len(graph)
    MAX = sys.maxsize #相当于无穷大
    #初始化各项数据，把dist[start]初始化为0，其他为无穷大
    dist = [MAX for _ in range(n)]
    pre = [-1 for _ in range(n)]
    s = [False for _ in range(n)]
    dist[start_point]=0
    for i in range(n): 
        minLength = MAX
        minVertex = -1
        for j in range(n):  #线性时间找最小
            if not s[j] and dist[j] < minLength:
                minLength = dist[j]
                minVertex = j
        s[minVertex] = True     #定点j加入到S集合中
        #从这个定点出发，遍历与它相邻的顶点的边，计算特殊路径长度，更新dist 和 pre
        for edge in graph[minVertex]:
            if not s[edge[0]] and minLength + edge[1]<dist[edge[0]]: #新的特殊路径长度短
                dist[edge[0]] = minLength+edge[1]
                pre[edge[0]] = minVertex
    return dist,pre
if __name__ == "__main__":
    data = [[1,0,8],[1,2,5],[1,3,10],[1,6,9],[2,0,1],[0,6,2],[3,6,5],[3,4,8],[0,5,4],[5,6,7],[5,3,8],[5,4,5]] #边集合(顶点，顶点，边权)
    n = 7 # 图的顶点数n
    graph = [[] for _ in range(n)] # 图的邻接表
    for edge in data:
        graph[edge[0]].append([edge[1],edge[2]])
        graph[edge[1]].append([edge[0],edge[2]])
    dist,pre = dijkstra(1,graph)
    print("dist=\n",dist)
    print("pre=\n",pre)

'''



# import sys
#
#
# def Prim_mst(graph, vertexs):
#     ulist = []  # 定义一个空集合作为树的顶点集
#     ulist.append(vertexs[0])  # 把顶点A加入集合U
#     tree_list = []  # 最小生成树
#     closest = []  # closest[i]表示生成树集合中与点i最接近的[点的编号]
#     lowcost = []  # lowcost[i]表示生成树中集合中与点i最接近的点构成的边
#
#     lowcost.append(-1)  # 最小权值 -1表示顶点i已经在生成树集合u中
#     closest.append(0)  # 把0号顶点加入集合中
#     n = len(vertexs)  # n为顶点个数6个
#     for i in range(1, n):  # 初始化closest和lowcost数组 从1开始，不考虑0号顶点，已经加入过
#         lowcost.append(graph[0][i])  # 把0号顶点到其他点的权重加进去
#         closest.append(0)  # 最开始，集合中全部是0号点
#     sum = 0  # 记录树的耗费
#     for _ in range(1, n):  # n-1次贪心选择
#         minid = 0  # 记录u中顶点与v-u中顶点最近的 v-u的顶点编号
#         min_ = sys.maxsize  # 系统最大值
#         for j in range(1, n):  # 寻找每次插入如生成树
#             if lowcost[j] != -1 and lowcost[j] < min_:
#                 minid = j
#                 min_ = lowcost[j]
#         ulist.append(vertexs[minid])
#         tree_list.append([vertexs[closest[minid]], vertexs[minid], lowcost[minid]])
#         sum += min_
#         lowcost[minid] = -1
#         for j in range(1, n):
#             if lowcost[j] != -1 and lowcost[j] > graph[minid][j]:
#                 lowcost[j] = graph[minid][j]
#                 closest[j] = minid
#     return sum, tree_list
#
#
# if __name__ == "__main__":
#     graph = [[0, 54, 32, 7, 50, 60], [54, 0, 21, 58, 76, 69], [32, 21, 0, 35, 67, 66],
#              [7, 58, 35, 0, 50, 62], [50, 76, 67, 50, 0, 14], [60, 69, 66, 62, 14, 0]]
#     vertexs = ["A", "B", "C", "D", "E", "F"]
#     sum, tree_list = Prim_mst(graph, vertexs)
#     for edge in tree_list:
#         print(edge[0] + "--" + edge[1] + " 权:" + str(edge[2]))
#     print("树的耗费:", sum)











