#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int distance(const std::pair<int, int>& position) {
    return abs(position.first) + abs(position.second); 
}

std::vector<std::pair<int, int>> parseString(const std::string& programString) {
    std::vector<std::pair<int, int>> positions;
    std::string tmp = "";
    
    std::pair<int, int> position = {0, 0};


    for (int i = 0; i < programString.size(); i++) {
        if (programString[i] != ',') {
             tmp += programString[i];
        } else {
            int steps = std::stoi(tmp.substr(1, 1000));

            switch (tmp[0])
            {
            case 'R':
                for (int i = 1; i <= steps; i++)
                {
                    positions.push_back({position.first + i, position.second});
                }
                position = {position.first + steps, position.second};
                break;
            case 'L':
                for (int i = 1; i <= steps; i++)
                {
                    positions.push_back({position.first - i, position.second});
                }
                position = {position.first - steps, position.second};
                break;
            case 'U':
                for (int i = 1; i <= steps; i++)
                {
                    positions.push_back({position.first, position.second + i});
                }
                position = {position.first, position.second + steps};
                break;
            case 'D':
                for (int i = 1; i <= steps; i++)
                {
                    positions.push_back({position.first, position.second - i});
                }
                position = {position.first, position.second - steps};
                break;
            }
            tmp = "";
        }
    }

    int steps = std::stoi(tmp.substr(1, 1000));

    switch (tmp[0])
    {
    case 'R':
        for (int i = 1; i <= steps; i++)
        {
            positions.push_back({position.first + i, position.second});
        }
        position = {position.first + steps, position.second};
        break;
    case 'L':
        for (int i = 1; i <= steps; i++)
        {
            positions.push_back({position.first - i, position.second});
        }
        position = {position.first - steps, position.second};
        break;
    case 'U':
        for (int i = 1; i <= steps; i++)
        {
            positions.push_back({position.first, position.second + i});
        }
        position = {position.first, position.second + steps};
        break;
    case 'D':
        for (int i = 1; i <= steps; i++)
        {
            positions.push_back({position.first, position.second - i});
        }
        position = {position.first, position.second - steps};
        break;
    }

    return positions;
}


int main(int argc, char const *argv[])
{
    
    std::string parth1String;
    std::string parth2String;

    std::ifstream inputFile;

    inputFile.open(argv[1], std::ios::in);
    
    if (inputFile.is_open()) {
        std::getline(inputFile, parth1String);
        std::getline(inputFile, parth2String);

    }

    inputFile.close();
    std::vector<std::pair<int, int>> path1Positions = parseString(parth1String);
    std::vector<std::pair<int, int>> path2Positions = parseString(parth2String);

    std::vector<int> overlapingPositionDistance;


    for (int i = 0; i < path1Positions.size(); i++)
    {
        for (int j = 0; j < path2Positions.size(); j++) {
            if (path1Positions[i] == path2Positions[j])
                overlapingPositionDistance.push_back(i+j + 2);
        }
    }
    
    int minDistance = overlapingPositionDistance[0];

    for (auto distance : overlapingPositionDistance)
    {
        if (minDistance > distance) {
            minDistance = distance;
        }
    }
    


    std::cout << std::to_string(minDistance) << std::endl;

    return 0;
}
