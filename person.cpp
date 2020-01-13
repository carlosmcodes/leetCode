#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <map>
#include <set>
using namespace std;
class person {
public:
int height = 0;
int weight = 0;
person(int h, int w){
    height = h;
    weight =w;
}
person(){

}

void setHeight(int h){ height = h;}

void setWeight(int w){weight = w;}

int getHeight() {return height;}

int getWeight(){return weight;}

void occupation(){ 
    cout << "no job" << endl;
    }


};