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
        int high = max(N, x+width);
        
        diff[low] += 1;
        if (high+1 > N){
            diff[high] -=1;
        }
    }
    
    for (int x : diff) cout << x;
    cout << endl;

}


int main(){
    solve();
    return 0;
}
