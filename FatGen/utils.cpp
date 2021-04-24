#include "utils.h"

ostream & operator<< (ostream& os,vector <int> &v){

    for(auto x:v) cout<<x<<" ";
    return os;
}


ostream & operator<< (ostream& os,vector <vector <int>> &v){
    for(auto x:v){
        cout<<x<<endl;
    }
    return os;
}




vector <vector<int>> matGen(int tc, int b){
    cout<<tc<<" "<<b<<endl;
    vector <vector<int>> fm(tc,vector<int>(b,0));
    srand(time(NULL));
    uniform_int_distribution<int> distribution(0, 1);
    for(int i=0;i<tc;i++) for(int j=0;j<b;j++) fm[i][j]=distribution(rng);
    for(int i=0;i<b;i++){
        int flag = 0;
        for(int j=0;j<tc;j++){
            if(fm[j][i]==1) flag = 1;
            if(flag) break;
        }
        if(!flag){
            fm[rand()%tc][i] = 1;
        }
    }
    return fm;
}
