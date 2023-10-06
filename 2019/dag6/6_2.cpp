#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>



class Object {

    public:
    Object(): Object("", nullptr) {};
    Object(std::string name, Object* parent)
    : _name(name)
    , _parent(parent)
    {};

    std::string _name;
    Object* _parent;

};


std::vector<std::string> getOrbits(const Object& object, std::vector<std::string> objects) {
    if (object._name == "COM") {
        return objects;
    }
    objects.push_back(object._name);
    return getOrbits(*(object._parent), objects);
}



int main(int argc, char const *argv[])
{
    std::string inputString;
    std::ifstream inputFile;

    std::map<std::string, Object> objects;

    inputFile.open(argv[1], std::ios::in);

    while (!inputFile.eof())
    {
        std::getline(inputFile, inputString);

        int deliminerPos =  inputString.find(')');

        std::string firstObjectName = inputString.substr(0, deliminerPos);
        std::string secondObjectName = inputString.substr(deliminerPos + 1, inputString.length() - deliminerPos);


        auto firstObjectPos = objects.find(firstObjectName);
        auto secondObjectPos = objects.find(secondObjectName);

        if (firstObjectPos == objects.end()) {
            objects[firstObjectName] = Object(firstObjectName, nullptr);
        }

        if (secondObjectPos == objects.end()) {
            objects[secondObjectName] = Object(secondObjectName, &objects[firstObjectName]);
        } else {
            objects[secondObjectName]._parent = &objects[firstObjectName];
        }
    }

    inputFile.close();

    auto you = objects["YOU"];
    auto san = objects["SAN"];

    std::vector<std::string> youPath;
    youPath = getOrbits(you, youPath);

    std::vector<std::string> sanPath;
    sanPath = getOrbits(san, sanPath);
    
    int remove = 0;
    while (youPath[youPath.size() - 1 - remove] == sanPath[sanPath.size() - 1 - remove])
    {
        remove++;
    }
    
    std::cout << youPath.size() - 1 - remove + sanPath.size() - 1 - remove << std::endl;

    return 0;
}

