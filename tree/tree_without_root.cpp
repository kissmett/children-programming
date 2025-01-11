#include <iostream>

#include "tree_without_root.h"

#define MAXN 100

using namespace std;

namespace without_root{
	
	static int m;
	static int fi[MAXN];
	static int to[MAXN*2];
	static int ne[MAXN*2];
	
	// ÎÞ¸ùÊ÷
	void link(int x, int y){
		to[++m]=y;ne[m]=fi[x];fi[x]=m;
		to[++m]=x;ne[m]=fi[y];fi[y]=m;
	}
	
	void dfs(int x, int fa){
		visit(x,fa);
		for(int i=fi[x];i;i=ne[i]) {
			if(to[i]!=fa) {
					dfs(to[i],x);
					visit(x,fa);
			}
		}
	}
	void visit(int x,int fa){
		cout<<"x="<<x<<";fa="<<fa<<endl;
	}	
		
}

