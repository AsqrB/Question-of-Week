#include <iostream>
#include<vector>
using namespace std;

int main() {
    
    int dec;
    cout<<"Enter Decimal number: ";
    cin>>dec;
    vector<int> result;
    while(dec!=1){
        int bin = dec%2;
        result.push_back(bin);
        dec=dec/2;
        }
    result.push_back(1);
    for(int i =result.size()-1;i>=0;i--)
    {
        cout<<result[i];
    }
    return 0;
}
