#include "iostream"

using namespace std;



void solve(){
    long long padA;
    long long padB;
    long long hopSize;
    int outMode;
    cin >> padA;
    cin >> padB;
    cin >> hopSize;
    cin >> outMode;
    
    long long dist = abs(padA - padB);
    long long maxC = dist/hopSize;
    

    long long hopRemainder = dist%hopSize;
    long long inverseHopRemainder = (maxC+1)*hopSize - dist + 1; // Distance if we hop greater than the endPoint, then minihop negative
    
    maxC += min(hopRemainder, inverseHopRemainder);
    



    if (outMode == 2) {
        long long addFactor = min(
            2LL,
            abs(hopRemainder - inverseHopRemainder)
        );
        if (addFactor == 0) addFactor = 2; // Can't be the same as previous
        
            
        long long backHop = -1LL + hopSize; // Case where going back 1 big hop and replacing with little hops gives second largest
        
        if (dist/hopSize == 0 && hopRemainder <= inverseHopRemainder) backHop = 1000; // Case where you can't backhop due to too little dist

        maxC += min(
            addFactor,
            backHop
        );

    }

    cout << maxC << endl;

}





int main(){
    solve();
    return 0;
}
