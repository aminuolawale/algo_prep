#include <iostream>
#include <sstream>

using namespace std;

int main(){
    string a = "11";
    stringstream conv(a);
    int b;
    conv >> b;
    cout << "now a number" << b << endl;
    
    return 0;
}
this is me coding now and there is nothing you can do about it 