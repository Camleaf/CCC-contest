
#include "iostream"
#include <algorithm>
#include <iterator>
#include <map>
#include <numeric>
#include <set>
#include <vector>
#include <array>

using namespace std;



set<long long> factorize(long long a){
    set<long long> factors; // set instead of list as items only need to share one prime factor
    while (a % 2 == 0){ // could be a way to do less divisions.
        a >>= 1; // rshift is fast
        factors.insert(2); // could be a way to insert less, as it is a redundant operation after first one
    }
    
    // is odd now
    
    
    for (long long i = 3; i*i<=a; i+=2){ 
        while (a % i == 0){ // No way to shorten this to just one operation, as we need to find the last prime below.
            factors.insert(i);
            a /= i;
        }
    }

    if (a > 2) factors.insert(a); // if a is a prime
    return factors;
}


set<long long> is_even_factor(long long a){
    if (a % 2 == 0){
        return {2};
    }
    return {};
}

void solve(){
    int N;
    cin >> N;
    
    vector<long long> cards(N);
    
    for (long long i = 0; i<N; i++){
        cin >> cards[i];
    }




    int even_card=0;
    map<long long, vector<int>> f_map;
    for (int i = 0; i<N; i++){
        int c = cards[i];
        set<long long> factors;

        if (N < 4){ // If N < 4, we need to check for even AND odd common factors for all nums.
            factors = factorize(c);
        } else { // If N >= 4, all we need to verify is for even common factors
            factors = is_even_factor(c);
        }

        for (long long f : factors) {
            if (f == 1) continue;

            // we keep index of the even card for later. If the condition below doesn't trigger, there will only be one
            if (f == 2) even_card=i+1; 

            f_map[f].push_back(i+1); // push_back index, not stored number, we don't need it.
            if (std::size(f_map[f]) == 2){ // case where there is a common factor in first row
                cout << "YES" << endl << "1 1" << endl;
                cout << f_map[f][0] << endl << f_map[f][1] << endl;
                return;
            }
        }
    } 
    // now that no common factors in first row, we verify for no additions.
    // Most remaining cards are odd, although one card may be even.
    if (N == 2) {
        cout << "NO" << endl; // if 2 cards, then impossible, as no factors as observed above.
        return;
    }

    if (N >= 3 && even_card){
        cout << "YES\n2 1" << endl;
        
        std::vector<int> tmp(N); // funky stuff to not have to hardcode
        std::iota(tmp.begin(),tmp.end(),1);
        tmp.erase(tmp.begin()+even_card-1);
        cout << tmp[0] << " " << tmp[1] << endl;
        cout << even_card << endl;
        return;
    }

    if (N>=4 && !even_card){ // If there are at least 4 cards and no even, then 1+2 and 3+4 will both be even, with a common factor of 2.
        cout << "YES" << endl;
        cout << "2 2" << endl;
        cout << "1 2" << endl << "3 4" << endl;
        return;
    } 

    // Includes properties above, as well as: no even cards, no common factors, and there are N = 3
    for (auto [x,y,z] : vector<array<int,3>>{{0,1,2},{1,2,0},{2,1,0}}){
        long long single = cards[x];
        long long sum = cards[y] + cards[z];
        
        set<long long> single_factors = factorize(single);
        set<long long> sum_factors = factorize(sum);
        set<long long> intersect;

        set_intersection(
            single_factors.begin(),single_factors.end(),
            sum_factors.begin(), sum_factors.end(),
            std::inserter(intersect, intersect.begin())
        );

        if (std::size(intersect) > 0){
            cout << "YES\n1 2"<< endl;
            cout << x+1 << endl;
            cout << y+1 << " " << z+1 << endl;
            return;
        }
    } 


    // end case for when it is not possible
    
    cout << "NO" << endl;
    
}



int main(){
    solve();
    return 0;
}
