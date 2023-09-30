#include <fstream>
#include <iostream>
#include <string>

std::string increment(const std::string input)
{
    return std::to_string(std::stoi(input, nullptr, 10) + 1);
}

bool isValid(const std::string input, const std::string maxVal)
{
    bool sidebyside = false;
    for (int i = 1; i < input.size(); i++)
    {
        if (input[i] < input[i - 1])
        {
            return false;
        }
    }
    sidebyside = input[0] == input[1] && input[1] != input[2];
    for (int i = 3; i < input.size(); i++) {
        sidebyside = sidebyside || (input[i-3] != input[i-2] && input[i-2] == input[i-1] && input[i-1] != input[i]);
    }
    sidebyside = sidebyside || (input[3] != input[4] && input[4] == input[5]);

    return sidebyside && input < maxVal;
}

int getTotalValid(const std::string input, const std::string maxVal)
{
    std::string current = input;
    int total = 0;
    while (current < maxVal)
    {
        if (isValid(current, maxVal))
        {
            total += 1;
        }
        current = increment(current);
    }
    return total;
}

int main(int argc, char const *argv[])
{
    std::string data;
    std::ifstream inputFile;
    inputFile.open(argv[1], std::ios::in);
    if (inputFile.is_open())
    {
        std::getline(inputFile, data);
    }
    std::string part1 = data.substr(0, 6);
    std::string part2 = data.substr(7, 7);

    int total = getTotalValid(part1, part2);
    std::cout << total << std::endl;
}