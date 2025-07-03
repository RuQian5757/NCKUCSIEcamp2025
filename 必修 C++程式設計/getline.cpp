#include <iostream>
using namespace std;
int main() {
	
	int a;
	cin >> a;
	string s;
	
	getline(cin, s); // cin.ignore()
	getline(cin, s);
	
	cout << a << "\n";
	cout << s << "\n";
	
	return 0;
}
