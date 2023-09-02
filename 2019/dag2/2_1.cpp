#include <fstream>
#include <iostream>
#include <string>
#include <vector>

std::vector<int> parseProgramString(const std::string& programString) {
    std::vector<int> result;
    std::string tmp = "";
    

    for (int i = 0; i < programString.size(); i++) {
        if (programString[i] != ',') {
             tmp += programString[i];
        } else {
             result.push_back(std::stoi(tmp, nullptr, 10));
            tmp = "";
        }
    }
    result.push_back(std::stoi(tmp));
    return result;
}


void add(const int position, std::vector<int>& program) {
    if (program.size() < program[position + 2]) {
        program.reserve(program[position + 2]);
    }
    program[program[position + 2]] = program[program[position]] + program[program[position + 1]];
}

void multiply(const int position, std::vector<int>& program) {
    if (program.size() < program[position + 2]) {
        program.reserve(program[position + 2]);
    }
    program[program[position + 2]] = program[program[position]] * program[program[position + 1]];
}

void run(std::vector<int>& program) {
    int i = 0;
    while (true)
    {
        switch (program[i])
        {
        case 1:
            add(i+1, program);
            break;
        case 2:
            multiply(i+1, program);
            break;
        case 99:
        default:
            return;
            break;
        }
        i += 4;
    }
}

int main(int argc, char const *argv[])
{
    
    std::string programString;
    std::ifstream inputFile;

    inputFile.open(argv[1], std::ios::in);
    
    if (inputFile.is_open()) {
        std::getline(inputFile, programString);
    }

    inputFile.close();
    std::vector<int> program = parseProgramString(programString);


    program[1] = 12;
    program[2] = 2;
    run(program);

    std::cout << std::to_string(program[0]) << std::endl;

    return 0;
}
