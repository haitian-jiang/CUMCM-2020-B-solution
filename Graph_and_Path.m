Graph_1=graph(Matrix_1); %由邻接矩阵生成问题1的图
S=sparse(Matrix_1); %由邻接矩阵生成稀疏矩阵S
[d_1,p_1]=graphshortestpath(S,1,12);
%求得从起点到矿山的最短距离与路径
[d_2,p_2]=graphshortestpath(S,12,27);
%求得从矿山到终点的最短距离与路径
plot(Graph_1) %画出图
