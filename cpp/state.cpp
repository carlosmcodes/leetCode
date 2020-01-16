#include <stdlib.h>
#include <map>
#include <vector>
using std::string;
using std::pair;
using namespace std;
string tick(string id);
vector<pair<string, string>> current_states();


class Lights
{
  public:
 string state;
  map<string, string> statemap;
  string currentState;
  
 
  
    Lights()
    {
  statemap.insert({"0", "off"});
  statemap.insert({"1", "low"});
  statemap.insert({"2", "medium"});
  statemap.insert({"3", "high"});
  
    }
  
    string tick(string id)
    {
      currentState = id;
      if (currentState == "3"){
        return statemap["0"];
      }
      return statemap[id];
    }

    vector<pair<string, string>> current_states()
    {
      vector<pair<string, string>> to_return;
      return to_return;
    }  
};