#include <iostream>
#include <vector>

void dfs(vector<int>graph[],int node,vector<bool> &visit){
    if(!visit[node]){
        visit[node]=1;
        for(auto child : graph[node]){
            if(!visit[child]){
                dfs(graph,child,visit)
            }
        }
    }
}

int main(){

    return 0;
}