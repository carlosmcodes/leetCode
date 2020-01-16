#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <set>
#include <mutex>
#include <thread>
#include <map>
using namespace std;

typedef struct command_t
{
   string type;
   string name;
   bool active;
} Command;

  typedef struct device_t
{
   string id;
   vector<string> capabilities;
} Device;

int main(){
    int j = 0;
    map<string, int> mmap;
    mmap["id"] = 1;
    cout << mmap["id"] << endl;
    
map<string, string> statemap;
  statemap.insert({"0", "off"});
  statemap.insert({"1", "low"});
  statemap.insert({"2", "medium"});
  statemap.insert({"3", "high"});
  if (statemap["3"] == "high"){
      cout << "hey"<< endl;
  }
  
    
}
vector<string> list_commands(string device_id)
{

vector<Command> commands = {
  { .type = "audio", .name = "turn down volume", .active = true },
  { .type = "audio", .name = "turn up volume", .active = true },
  { .type = "music", .name = "next song", .active = true },
  { .type = "music", .name = "previous song", .active = true },
  { .type = "music", .name = "purchase song", .active = false }, // payment integration still in beta
  { .type = "channel", .name = "channel up", .active = true },
  { .type = "channel", .name = "channel down", .active = true },
  { .type = "temperature", .name = "raise temperature", .active = true },
  { .type = "temperature", .name = "lower temperature", .active = true }
};

vector<Device> devices = {
  { .id = "Television", .capabilities = { "audio", "channel" } },
  { .id = "Smart thermostat", .capabilities = { "temperature" } },
  { .id = "Stereo system", .capabilities = { "audio", "music" } },
  { .id = "Kitchen sink", .capabilities = { } },
  { .id = "Paper shredder", .capabilities = { "shredding" } }
};

vector<string> to_return;
string idFound = "";
vector<string> cap;


for ( auto i : devices){
    if (i.id == device_id){
        idFound = device_id;
        cap = i.capabilities;
    }
}
if (idFound == "") return to_return;


for (auto i : commands){
    if (i.active == true){
        for (int j = 0; j < cap.size();j++){
            if (cap[j] == i.name){
                to_return.push_back(i.name);
            }
        }
        if (cap.size() == 1){

        }
    }
}

  return to_return;
}
bool check_valid(string command_name, string device_id) {

vector<Command> commands = {
  { .type = "audio", .name = "turn down volume", .active = true },
  { .type = "audio", .name = "turn up volume", .active = true },
  { .type = "music", .name = "next song", .active = true },
  { .type = "music", .name = "previous song", .active = true },
  { .type = "music", .name = "purchase song", .active = false }, // payment integration still in beta
  { .type = "channel", .name = "channel up", .active = true },
  { .type = "channel", .name = "channel down", .active = true },
  { .type = "temperature", .name = "raise temperature", .active = true },
  { .type = "temperature", .name = "lower temperature", .active = true }
};

vector<Device> devices = {
  { .id = "Television", .capabilities = { "audio", "channel" } },
  { .id = "Smart thermostat", .capabilities = { "temperature" } },
  { .id = "Stereo system", .capabilities = { "audio", "music" } },
  { .id = "Kitchen sink", .capabilities = { } },
  { .id = "Paper shredder", .capabilities = { "shredding" } }
};

string deviceFound;
  map<string, int> namedCommands;
  for (auto i : commands){
      namedCommands.insert({i.name,0});
  }
  // TODO: fill this out!
  for ( auto i : devices){
      if (i.id == device_id){
          for (int k = 0; k < devices.size(); k++){
              if(namedCommands.count(i.capabilities[k])){
                  return true;
              }
          }
      }

  }

  return false;
}
