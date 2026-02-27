#include "iostream"
#include "vector"
using namespace std;



void solve(){
    int parkingSpots; // cannot be 0
    int lightsNum; // can be 0
    int questions;

    cin >> parkingSpots;
    cin >> lightsNum;
    cin >> questions;
    

    std::vector<int> diff(parkingSpots+2,0);
    
    for (int i =0; i<lightsNum;i++){ // Difference array usage from google
        int spot,spread;
        cin >> spot >> spread;

        int low = max(1,spot-spread);
        int high = min(parkingSpots, spread+spot);

        diff[low] += 1;
        if (high+1 <= parkingSpots){
            diff[high+1] -= 1;
        }
    }

    std::vector<int> cover(parkingSpots+1,0);
    for (int i = 1; i <= parkingSpots;i++){
        cover[i] = cover[i-1] + diff[i];
    }

    

    bool qArr[questions];
    for (int i = 0;i<questions;i++){
        int q;
        cin >> q;
        
        cout << ((cover[q] > 0) ? "Y" : "N") << endl;
    }

    
}


int main(){
    solve();
    return 0;
}
