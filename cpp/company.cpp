#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <map>
#include <set>
#include "person.cpp"
using namespace std;

class abstract{
    public:
        virtual void show() = 0;

};

class job : public person, public abstract{
    public:
    void occupation(){cout << "has a job" << endl;}
    void show(){ cout << "virtual works" << endl;}

};

int main(){
    person p = person();
    person p2 = person(32, 32);
    p.setHeight(99);
    cout << p.getHeight() << endl;
    job j = job();
    j.occupation();
    p.occupation();
    j.show();
    
}
