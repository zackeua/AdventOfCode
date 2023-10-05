#include <iostream>
#include <fstream>
#include <map>
#include <string>


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


int getOrbits(const Object& object) {
    if (object._name == "COM") {
        return 0;
    }
    return 1 + getOrbits(*(object._parent));
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

    int total = 0;

    for (auto &&object : objects)
    {
        total += getOrbits(object.second);
    }
    
    std::cout << total << std::endl;



    return 0;
}

