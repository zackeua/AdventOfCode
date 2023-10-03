#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <tuple>
#include <algorithm>

std::vector<int> parseProgramString(const std::string &programString)
{
    std::vector<int> result;
    std::string tmp = "";

    for (int i = 0; i < programString.size(); i++)
    {
        if (programString[i] != ',')
        {
            tmp += programString[i];
        }
        else
        {
            result.push_back(std::stoi(tmp, nullptr, 10));
            tmp = "";
        }
    }
    result.push_back(std::stoi(tmp));
    return result;
}

void add(const int position, std::vector<int> &program, const int argtype1, const int argtype2)
{
    if (program.size() < program[position + 3])
    {
        program.reserve(program[position + 3]);
    }
    int arg1 = argtype1 != 0 ? position + 1 : program[position + 1];
    int arg2 = argtype2 != 0 ? position + 2 : program[position + 2];
    int arg3 = program[position + 3];

    program[arg3] = program[arg1] + program[arg2];
}

void multiply(const int position, std::vector<int> &program, const int argtype1, const int argtype2)
{
    if (program.size() < program[position + 3])
    {
        program.reserve(program[position + 3]);
    }
    int arg1 = argtype1 != 0 ? position + 1 : program[position + 1];
    int arg2 = argtype2 != 0 ? position + 2 : program[position + 2];
    int arg3 = program[position + 3];    

    program[arg3] = program[arg1] * program[arg2];
}

void input(const int position, std::vector<int>& program) {
    if (program.size() < program[position + 1])
    {
        program.reserve(program[position + 1]);
    }
    const int INPUT = 5;
    program[program[position + 1]] = INPUT;
}

int output(const int position, std::vector<int>& program, const int argtype1) {
    int arg1 = argtype1 != 0 ? position + 1 : program[position + 1];
    return program[arg1];
}

int jumpIfTrue(const int position, std::vector<int>& program, const int argtype1, const int argtype2) {
    int arg1 = argtype1 != 0 ? position + 1 : program[position + 1];
    int arg2 = argtype2 != 0 ? position + 2 : program[position + 2];

    const int INSTRUCTION_LENGTH = 3;
    return program[arg1] != 0 ? program[arg2] : position + INSTRUCTION_LENGTH;
}

int jumpIfFalse(const int position, std::vector<int>& program, const int argtype1, const int argtype2) {
    int arg1 = argtype1 != 0 ? position + 1 : program[position + 1];
    int arg2 = argtype2 != 0 ? position + 2 : program[position + 2];

    const int INSTRUCTION_LENGTH = 3;
    return program[arg1] == 0 ? program[arg2] : position + INSTRUCTION_LENGTH;
}

void lessThan(const int position, std::vector<int>& program, const int argtype1, const int argtype2) {
    int arg1 = argtype1 != 0 ? position + 1 : program[position + 1];
    int arg2 = argtype2 != 0 ? position + 2 : program[position + 2];
    int arg3 = program[position + 3];

    program[arg3] = static_cast<int>(program[arg1] < program[arg2]);
}

void equals(const int position, std::vector<int>& program, const int argtype1, const int argtype2) {
    int arg1 = argtype1 != 0 ? position + 1 : program[position + 1];
    int arg2 = argtype2 != 0 ? position + 2 : program[position + 2];
    int arg3 = program[position + 3];

    program[arg3] = static_cast<int>(program[arg1] == program[arg2]);
}


std::tuple<int, int, int, int> parseOperation(const int opcode)
{
    int op = opcode % 100;
    int argmode1 = (opcode / 100) % 10;
    int argmode2 = (opcode / 1000) % 100;
    int argmode3 = (opcode / 10000) % 1000;

    return {op, argmode1, argmode2, argmode3};
}


std::vector<int> run(std::vector<int> &program)
{
    std::vector<int> outputs;
    int i = 0;
    while (true)
    {
        auto [op, argtype1, argtype2, argtype3] = parseOperation(program[i]);
        switch (op)
        {
        case 1:
            add(i, program, argtype1, argtype2);
            i += 4;
            break;
        case 2:
            multiply(i, program, argtype1, argtype2);
            i += 4;
            break;
        case 3:
            input(i, program);
            i += 2;
            break;
        case 4:
            outputs.push_back(output(i, program, argtype1));
            i += 2;
            break;
        case 5:
            i = jumpIfTrue(i, program, argtype1, argtype2);
            break;
        case 6:
            i = jumpIfFalse(i, program, argtype1, argtype2);
            break;
        case 7:
            lessThan(i, program, argtype1, argtype2);
            i += 4;
            break;
        case 8:
            equals(i, program, argtype1, argtype2);
            i += 4;
            break;
        case 99:
        default:
            return outputs;
            break;
        }
    }
    return outputs;
}

int main(int argc, char const *argv[])
{

    std::string programString;
    std::ifstream inputFile;

    inputFile.open(argv[1], std::ios::in);

    if (inputFile.is_open())
    {
        std::getline(inputFile, programString);
    }

    inputFile.close();
    std::vector<int> originalProgram = parseProgramString(programString);

    std::vector<int> program;

    program.reserve(originalProgram.size());

    program.assign(originalProgram.begin(), originalProgram.end());

    std::vector<int> programOutput = run(program);

    for (auto &&i : programOutput)
    {
        std::cout << i << std::endl;
    }

    return 0;
}
