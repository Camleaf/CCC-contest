#include "iostream"
#include <vector>

using namespace std;



void solve(){
    int N, L, Q; // parking spots, lights, questions
    cin >> N >> L >> Q;
    
    vector<int> diff(N+2); 
    
    for (int i = 0; i<L;i++){
        int x, width; // x position,         
        cin >> x >> width;
    
        int low = max(1, x-width); // bounds so that the 
        int high = min(N, x+width);
        
        diff[low] += 1;
        if (high+1 <= N){
            diff[high+1] -=1;
        }
    }
    

    vector<int> lit_spots(N+1);
    lit_spots[0] = diff[0];
    for (int i = 1; i<N; i++){
        lit_spots[i] = lit_spots[i-1] + diff[i];
    }
    

    for (int i = 0;i<Q;i++){
        int query;
        cin >> query;
        
        if (lit_spots[query] > 0) cout << "Y" << endl;
        else cout << "N" << endl;

    }
}


int main(){
    solve();
    return 0;
}
