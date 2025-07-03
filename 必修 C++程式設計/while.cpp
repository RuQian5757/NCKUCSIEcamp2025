#include <iostream>
using namespace std;
int main() {
	
	int q = 10;
	while(q--) {
		cout << q << "\n"; // 9 8 7 6 5 4 3 2 1 0
	}
	
	int a = 10;
	while( a != 0 ) {
		cout << a << "\n"; // 10 9 8 7 6 5 4 3 2 1
		a--;
	}
	
	return 0;
}
