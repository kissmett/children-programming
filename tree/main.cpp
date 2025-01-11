#include <cstdlib>
#include <iostream>

#include "tree_without_root.h"
#include "tree_with_root.h"

using namespace std;

int main(int argc, char *argv[])
{
//    cout << "hello world" << endl; 
    
    int n;
    scanf("%d",&n);
    for(int i=1,x,y;i<n;++i){
    	scanf("%d%d",&x,&y);
    	without_root::link(x,y);//link(y,x);	
		with_root::link(x,y);			
	}
    
    without_root::dfs(1,0);
    with_root::dfs(1,0);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
