#include "iostream"
#include <set>
#include <vector>

using namespace std;

struct pen {
    long long c;
    long long p;
    long long id;
};

struct penComparePretty {
    bool operator()(const pen& p1, const pen& p2) const {
        return p1.p > p2.p; 
    }
};

long long get_q_score(multiset<pen,penComparePretty> max_score, multiset<pen, penComparePretty> second_score){

    long long score = 0;
    for (auto p : max_score) score += p.p;
    
    long long low = (--max_score.end())->p;
    long long high = second_score.begin()->p;
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
    multiset<pen, penComparePretty> max_score;
    multiset<pen, penComparePretty> second_score;
    
    for (int i = 0; i<N;i++){
        long long C,P;
        cin >> C >> P;
        C-=1;
        pen p = {C,P,i};
        pens.push_back(p);
        sorted_pens[C].insert(p);
    }
    for (auto s : sorted_pens){
        auto it = s.begin();
        max_score.insert(*it);
        ++it;
        if (it == s.end()) continue;
        second_score.insert(*it);
    }
    cout << get_q_score(max_score,second_score) << endl;
    
    for (int i = 0;i<Q;i++){
        int mode, id, val;
        cin >> mode >> id >> val;
        id-=1;
        long long colour = pens[id].c;
        
        if (mode == 1){ // colour

            //// update multiset of colour "colour"
            // erase max, second multiset vals
            auto it = sorted_pens[colour].begin();
            max_score.erase(*it);
            second_score.erase(*(++it));
            // erase pen from colour
            sorted_pens[colour].erase(pens[id]);
            // add to multisets
            it = sorted_pens[colour].begin();
            max_score.insert(*it); 
            second_score.insert(*(++it));
            
            //// update pens
            val-=1;
            pens[id].c = val;

            //// update bbst of colour "val"
            // erase max, second multiset vals
            it = sorted_pens[val].begin();
            max_score.erase(*it);
            ++it;
            second_score.erase(*it);
            // add pen to new colour
            sorted_pens[val].insert(pens[id]);
            // add to new colour multisets
            it = sorted_pens[val].begin();
            max_score.insert(*it);
            ++it;
            second_score.insert(*it);

        } else { // prettiness
            //// remove from multiset
            auto it = sorted_pens[colour].begin();
            max_score.erase(*it);
            ++it;
            second_score.erase(*it);

            //// update the pen prettiness and re-add
            sorted_pens[colour].erase(pens[id]);
            // update pens
            pens[id].p = val;
            sorted_pens[colour].insert(pens[id]);
            
            //// insert to multiset
            it = sorted_pens[colour].begin();
            max_score.insert(*it);
            ++it;
            second_score.insert(*it);

            
        }

        cout << get_q_score(max_score,second_score) << endl;
    }
}




int main(){
    solve();
    return 0;
}
