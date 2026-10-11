// First 5 marks
#include "iostream"
#include <algorithm>
#include <map>
#include <numeric>
#include <vector>

using namespace std;

struct pen {
    int colour;
    int prettiness;
};

void solve(){
    int N,M,Q;
    cin >> N >> M >> Q;
    // key colour, item an array of prettiness vlaues
    map<int,vector<long long>> pens;
    vector<long long> prettiest(M);
    vector<long long> sub_prettiest(M);

    for (int i = 0; i<N;i++){
        long long C,P;
        cin >> C >> P;
        C -= 1; // Always gotta remove 1 from C index so overflow err doesnt happen
        if (prettiest[C] < P){
            sub_prettiest[C] = prettiest[C];
            prettiest[C] = P;
        } else if (sub_prettiest[C] < P) {
            sub_prettiest[C] = P;
        }
    }
    long long score = 0;
    for (int p : prettiest) score += p;
    

    long long low = 1e10;
    long long high = 0;
    for (int i = 0; i < M ; i++){
        if (prettiest[i] < low) low = prettiest[i];
        if (sub_prettiest[i] > high) high = sub_prettiest[i];
    }
    if (high > low){
        score = score - low + high;
    }
    cout << score << endl;
    
    

}




int main(){
    solve();
    return 0;
}
