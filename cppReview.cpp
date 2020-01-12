#include <iostream>
#include <vector>
using namespace std;

void print(int val);
void printVec(vector<int> v);
int main(){

cout << "run" << endl;
int i = 0;
vector<int> v;
v.push_back(12);
v.push_back(23);
printVec(v);


int values[10];
}

void print(int val){
    cout << val << endl;
}

void swap(int &a, int &b){
    int temp = a;

}

void printVec(vector<int> v){
    int i;
    for (i = 0; i < v.size(); i++){
        print(v.at(i));
    }
}
