#include <iostream>
using namespace std;

long long int TotalWays(int num) {
  if(num == 1) {
    return 1;
  }
  else {
    return num * TotalWays(num - 1);
  }
}

main() {
  long long int days;
  cin>>days;
  cout<<TotalWays(days);
}
