#include "iostream"
#include <set>
#include <vector>

using namespace std;

struct pen {
    long long c;
    long long p;
    int id;
};

struct penComparePretty {
    bool operator()(const pen& p1, const pen& p2) const {
        return p1.p > p2.p; 
    }
};

long long get_q_score(vector<multiset<pen,penComparePretty>> sorted_pens, int N, int M){

    long long score = 0;
    for (auto s : sorted_pens) score += s.begin()->p;
    

    long long low = 1e10;
    long long high = 0;
    for (auto s : sorted_pens){
        auto it = s.begin();
        if (it->p < low) low = it->p;
        it++;
        if (it==s.end()) continue;
        if (it->p > high) high = it->p;
        
    }
    if (high > low){
        score = score - low + high;
    }
    return score;    
}


void solve(){
    int N,M,Q;
    cin >> N >> M >> Q;
    
    vector<multiset<pen,penComparePretty>> sorted_pens(M);
    vector<pen> pens;
    
    for (int i = 0; i<N;i++){
        long long C,P;
        cin >> C >> P;
        C-=1;
        pen p = {C,P,i+1};
        pens.push_back(p);
        sorted_pens[C].insert(p);
    }
    cout << get_q_score(sorted_pens,N,M) << endl;
    
    for (int i = 0;i<Q;i++){
        int mode, id, val;
        cin >> mode >> id >> val;
        
        long long colour = pens[id-1].c;
        sorted_pens[colour].erase(pens[id-1]);
        if (mode == 1){ // colour
            val-=1;
            pens[id-1].c = val;
            sorted_pens[val].insert(pens[id-1]);

        } else { // prettiness
            pens[id-1].p = val;
            sorted_pens[colour].insert(pens[id-1]); 
        }

        cout << get_q_score(sorted_pens,N,M) << endl;
    }
}




int main(){
    solve();
    return 0;
}
