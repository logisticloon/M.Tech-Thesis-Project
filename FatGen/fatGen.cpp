#include "utils.h"
using namespace std;

int main(int argc, char* argv[]){
    
    int tc,b;
    cin>>tc>>b;
    vector <vector<int>> fm = matGen(tc,b); 
    cout<<fm<<endl;
    
    
    return 0;

}