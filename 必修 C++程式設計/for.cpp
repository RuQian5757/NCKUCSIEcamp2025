#include <iostream>
using namespace std;
int main() {
	
	for(int i=1;i<=10;i++) {
		if( i == 4 ) {
			continue;
		}
		if( i == 8 ) {
			break;
		}
		cout << i << "\n"; // 1 2 3 5 6 7
	}
	
	return 0;
}
