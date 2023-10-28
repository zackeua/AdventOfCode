#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <tuple>
#include <algorithm>
#include <queue>
#include <optional>

struct parsedOperation {
    int op;
    int argmode1;
    int argmode2;
    int argmode3;
};

struct programOutput
{
    int status;
    int currentInstruction;
    std::optional<int> output;
};

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

void input(const int position, std::vector<int>& program, std::queue<int>& input) {
    if (program.size() < program[position + 1])
    {
        program.reserve(program[position + 1]);
    }
    const int INPUT = input.front();
    input.pop();
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

parsedOperation parseOperation(const int opcode)
{
    int op = opcode % 100;
    int argmode1 = (opcode / 100) % 10;
    int argmode2 = (opcode / 1000) % 100;
    int argmode3 = (opcode / 10000) % 1000;

    return {op, argmode1, argmode2, argmode3};
}

programOutput run(const int startInstruction, std::vector<int> &program, std::queue<int>& inputs)
{
    int i = startInstruction;
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
            input(i, program, inputs);
            i += 2;
            break;
        case 4:
            {
            int currentOutput = output(i, program, argtype1);
            i += 2;
            return {0, i, currentOutput};
            }
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
            return {1, i, std::nullopt};
            break;
        }
    }
    return {1, i, std::nullopt};
;
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

    std::vector<int> amplifierA;
    std::vector<int> amplifierB;
    std::vector<int> amplifierC;
    std::vector<int> amplifierD;
    std::vector<int> amplifierE;

    amplifierA.reserve(originalProgram.size());
    amplifierB.reserve(originalProgram.size());
    amplifierC.reserve(originalProgram.size());
    amplifierD.reserve(originalProgram.size());
    amplifierE.reserve(originalProgram.size());

    amplifierA.assign(originalProgram.begin(), originalProgram.end());
    amplifierB.assign(originalProgram.begin(), originalProgram.end());
    amplifierC.assign(originalProgram.begin(), originalProgram.end());
    amplifierD.assign(originalProgram.begin(), originalProgram.end());
    amplifierE.assign(originalProgram.begin(), originalProgram.end());

    programOutput outputA = {0, 0, std::nullopt};
    programOutput outputB = {0, 0, std::nullopt};
    programOutput outputC = {0, 0, std::nullopt};
    programOutput outputD = {0, 0, std::nullopt};
    programOutput outputE = {0, 0, std::nullopt};


    std::vector<int> phaseSettings = {5, 6, 7, 8, 9};

    int maxSignal = 0;
    std::vector<int> maxSettings = {};

    do {

        std::queue<int> inputA;
        std::queue<int> inputB;
        std::queue<int> inputC;
        std::queue<int> inputD;
        std::queue<int> inputE;

        inputA.push(phaseSettings[0]);
        inputA.push(0);
        inputB.push(phaseSettings[1]);
        inputC.push(phaseSettings[2]);
        inputD.push(phaseSettings[3]);
        inputE.push(phaseSettings[4]);

        outputA.currentInstruction = 0;
        outputB.currentInstruction = 0;
        outputC.currentInstruction = 0;
        outputD.currentInstruction = 0;
        outputE.currentInstruction = 0;


        int lastOutput = 0;

        while (true)
        {
            outputA = run(outputA.currentInstruction, amplifierA, inputA);
            if (outputA.status == 1) {
                break;
            } else {
                //std::cout << outputA.output.value() << std::endl; 
            }
            inputB.push(outputA.output.value());

            outputB = run(outputB.currentInstruction, amplifierB, inputB);
            if (outputB.status == 1) {
                break;
            } else {
                //std::cout << outputB.output.value() << std::endl;
            }
            inputC.push(outputB.output.value());

            outputC = run(outputC.currentInstruction, amplifierC, inputC);
            if (outputC.status == 1) {
                break;
            } else {
                //std::cout << outputC.output.value() << std::endl;
            }
            inputD.push(outputC.output.value());
                    
            outputD = run(outputD.currentInstruction, amplifierD, inputD);
            if (outputD.status == 1) {
                break;
            } else {
                //std::cout << outputD.output.value() << std::endl;
            }
            inputE.push(outputD.output.value());
            
            outputE = run(outputE.currentInstruction, amplifierE, inputE);

            if (outputE.output.has_value()) {
                lastOutput = outputE.output.value();
            }

            if (outputE.status == 1) {
                break;
            } else {
                //std::cout << outputE.output.value() << std::endl;
            }
            inputA.push(outputE.output.value());
            
            

        }
    

        if (lastOutput >= maxSignal) {
            maxSignal = lastOutput;
            maxSettings.assign(phaseSettings.begin(), phaseSettings.end());
        }
        if (lastOutput == 18216) {
            std::cout << "HEJSAN" << std::endl;
        }



    } while ( std::next_permutation(phaseSettings.begin(), phaseSettings.end())  );
        
    std::cout << maxSignal << std::endl;
    //std::cout << maxSettings[0] << maxSettings[1] << maxSettings[2] << maxSettings[3] << maxSettings[4] << std::endl;


    return 0;
}
