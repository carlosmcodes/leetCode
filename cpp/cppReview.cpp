#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <map>
#include <set>
using namespace std;

struct employee
{
    string name;
    int id;
    int dob;
};

// decleration
template< typename T>
void print(T val);
void printVec(vector<int> v);
void sideEffect(string &b);
vector<int> retVec(const int j);
inline void swap(int &a, int &b);
int recursion(int k);
void hashmap();
void printmap(map<int,string>  Map);
void uniqueVec(vector<int> &v);
employee makeEmployee(int dob, int id, string name);
void struct_withDS();
vector<int> twosum(vector<int> nums , int target);
vector<int> intersectTwo(vector<int> &a, vector<int> b);


int main(){

print("run");
int i = 0;
vector<int> v;
v.push_back(12);
v.push_back(23);
string x = to_string(v.at(0));

// print("x is:    " +x);
// printVec(v);
// string c = "hey";
// print(c.length());
// getline(cin, c);
// print("you printed" + c + "man");
// string s = "kfdshkfsjfljls";
// for ( i = 0; i < s.length();i++){
//     print(s.at(i));
// }
// string &k = s;
// k = "yp";
// print("s:" + s);
// print(&k);
// print(&s);
// print("k:" +k);
// sideEffect(k);
// print("s:" + s);
// print("k:" +k);
// string *l = &s;
// l;
// print(s[0]);
// int g = 3;
// int f = 4;
// swap(g,f);
// int values[10];
// vector<int> ret = retVec(5);
// printVec(ret);
// print(recursion(6));
// hashmap();
// struct_withDS();
vector<int> c = {4,9,5};
vector<int> c2 = {9,4,9,8,4};
// twosum(c, 9);
intersectTwo(c, c2);
}


//definition

string hi(string s){
    string str;
    if (s.length() == 0)
        return "Hello there!";
    else 
        return "Hello" + s;
}
bool containsDuplicate(vector<int>& nums) {
    map<int, int> nap;
    for (auto i : nums){
        if (nap.count(i)){
            return true;
        }
        nap.insert({i,0});
    }
    return false;

    //method two
    vector<int> self;
    for ( auto i : nums){
        if (find(self.begin(), self.end(), i) != self.end()){
            return true;
        }
        self.push_back(i);
    }
    return false;
    }

int singleNumber(vector<int>& nums) {
    int val = 0;
    for (auto i : nums)
    val ^=i;
    return val;
}

vector<int> intersectTwo(vector<int> &a, vector<int> b){
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    a.erase(set_intersection(a.begin(), a.end(), b.begin(), b.end(), a.begin()), a.end());
    return a;
}
void struct_withDS(){
    employee e1 = makeEmployee(202091, 30, "saraj");
    employee e2 = makeEmployee(2, 5, "ahd");


    vector<employee> vec_of_employees;
    vec_of_employees.push_back(e1);
    if (vec_of_employees[0].id == 3){
        print(vec_of_employees[0].name);
    }
    map<int, employee> mmap;
    for ( int i = 0; i < 4; i++){
        employee e = makeEmployee(i,i, "kdj");
        mmap[i] = e;
    }
    employee *ePtr;
    ePtr = &mmap[0];
    // ePtr++;
    print(ePtr->id);
    // print(&mmap[1]);
    if (mmap.count(2)){
        print(mmap[2].name);
    }

}

vector<int> twosum(vector<int> nums , int target){
    map<int,int> lap;
    for (int i = 0; i < nums.size(); i++){
        if (lap.count(nums[i])){
            nums.clear();
            nums.push_back(lap[nums[i]]);
            nums.push_back(i);
        }
        else
        lap[target - nums[i]] = i;
    }
    return nums;
}


employee makeEmployee(int dob, int id, string name){
    employee e;
    e.name = name;
    e.dob = dob;
    e.id = id;
    return e;
}
int recursion(int k){
    if( k < 1)
        return 1;
    else{
        print(k);
        return recursion(k-1)+ k;
    }
}
void uniqueVec(vector<int> &v){
    set<int> s;
    for (int i : v)
    s.insert(i);
    v.assign(s.begin(), s.end());

}

void hashmap(){
    map<int, string> map;
    map[43] = "fourtythre";
    for (int i = 0; i < 8; i++){
        map[i] = "i is:  " + to_string(i);
        
    }
    map.insert({10, "ten"});
    printmap(map);
    int val = 10;
    if (map.count(val))
    print("key found");
    print(map[val]);

    map.erase(10);
    printmap(map);
    
}

void printmap(map<int,string>  Map){
    for (auto x: Map){
        print(x.first);
        print(x.second);
    }

}

vector<int> retVec(const int j){
    vector<int> r;
    for (int i =0; i < j; i++){
        r.push_back(i);   
    }
    reverse(r.begin(), r.end());
    
    return r;
}

void sideEffect(string &b){
    b = "this is the side effect";
    print(&b);
    print(b);
}


template< typename T>
void print(T val){
    cout << val << endl;
}

void swap(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
    print(a);
    print(b);



}

void printVec(vector<int> v){
    int i;
    for (i = 0; i < v.size(); i++){
        print(v.at(i));
    }
}
