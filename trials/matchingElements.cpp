#include <iostream>
#include <vector>

using namespace std;

int matchingElements(vector<int> arr, vector<int> arr1);

int main(){
    vector<int> arr = {13, 27, 35, 40, 49, 55, 59, 60};
    vector<int> arr1 = {17, 35, 39, 40, 55, 58, 60};
    int ans = matchingElements(arr, arr1);
    cout << "this is the ans  " << ans << endl;
    return 0;
}

int matchingElements(vector<int> arr, vector<int> arr1){
    // both arrays are sorted
    int ind =0;
    int ind1 = 0;
    int count =0;
    while (ind < arr.size() && ind1 < arr.size()){
        cout << arr[ind] << "  " << arr1[ind1] << endl;
        if(arr[ind] < arr1[ind1]) {
            ind ++;
        } else if (arr[ind]> arr1[ind1]){
            ind1 ++;
        } else {
            count ++;
            ind ++;
            ind1 ++;
        }
    }
    return count;
}