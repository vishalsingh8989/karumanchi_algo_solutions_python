#include<iostream>
using namespace std;
int main(){
	

	string val = "b1";
	string val1 = "b*";
	string val2 = "c*";
	string val3 = "*";
	string val4 = "a1";
	string val5 = "a2";

	cout <<  val1 << " : " << val <<  val1.compare(val) <<endl;
	cout <<  val1 << " : " << val2 <<  val1.compare(val2) <<endl;

	cout <<  val2 << " : " << val3 <<  val2.compare(val3) <<endl;
	cout <<  val3 << " : " << val2 <<  val3.compare(val2) <<endl;
	cout <<  val3 << " : " << val4 <<  val3.compare(val4) <<endl;
	cout <<  val4 << " : " << val5 <<  val4.compare(val5) <<endl;
	cout <<  val5 << " : " << val4 <<  val5.compare(val4) <<endl;

	return 0;

		
}


