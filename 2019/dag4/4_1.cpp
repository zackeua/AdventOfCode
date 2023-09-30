#include <fstream>
#include <iostream>
#include <string>

std::string increment(const std::string input) {
    return std::to_string(std::stoi(input, nullptr, 10) + 1);
}

bool isValid(const std::string input) {
    bool sidebyside = false;
    for (int i = 1; i < input.size(); i++) {
        if (input[i] < input[i-1]) {
            return false;
        }
        if (input[i] == input[i-1]) {
            sidebyside = true;
        }
    }
    return sidebyside;
}


std::string getNextValid(const std::string input) {
    std::string current = input;
    while (true)
    {
        if (isValid(current)) {
            current = increment(current);
            return current;
        }
        current = increment(current);
    }
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

    int total = 0;
    std::string current = part1;
    while (current <= part2) {
        std::cout << part1 << " " << current << " " << part2 << std::endl;
        current = getNextValid(current);
        total += 1;
    }
    std::cout << total - 1 << std::endl;
}