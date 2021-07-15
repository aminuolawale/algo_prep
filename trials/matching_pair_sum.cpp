#include <iostream>
#include <vector>

using namespace std;
string matchingPairSum(vector<int>array);

int main(){
    vector<int> array = {1, 3, 7, 9};
    string answer = matchingPairSum(array);
    cout << answer << endl;
    return 0;
}


string matchingPairSum(vector<int>array) {
    int fronti = 0;
    int backi = array.size()-1;
    for (;backi!=fronti;){
        int sum = array[backi] + array[fronti];
        if (sum == 8){
            return "YES";
        }
        else if (sum > 8){
            backi --;
        } 
        else {
            fronti ++;
        }
    }
    return "NO";
}