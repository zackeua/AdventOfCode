#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


int main(int argc, char const *argv[]) {

    std::ifstream inputFile;
    std::string inputString;

    inputFile.open(argv[1], std::ios::in);

    if (inputFile.is_open())
    {
        std::getline(inputFile, inputString);
    }

    std::vector<std::vector<int>> imageLayers;
    std::vector<int> zeroCount;
    std::vector<int> oneCount;
    std::vector<int> twoCount;

 
    int cols = 25;
    int rows = 6;
    int i = 0;
    int j = 0;
    while (i < inputString.length()) {
        j = 0;
        std::vector<int> image;
        int zeros = 0;
        int ones = 0 ;
        int twos = 0;

        for (; j < cols * rows; j++) {
            int elem = inputString[i+j] - '0';

            image.push_back(elem);
            switch (elem)
            {
            case 0:
                zeros += 1;
                break;
            case 1:
                ones += 1;
                break;
            case 2:
                twos += 1;
                break;
            }
        }
        imageLayers.push_back(image);
        zeroCount.push_back(zeros);
        oneCount.push_back(ones);
        twoCount.push_back(twos);
        i += j;
    }

    int minZeroCount = rows * cols;
    int answer = 0;
    for (i = 0; i < zeroCount.size(); i++ ) {
        if (zeroCount[i] < minZeroCount) {
            answer = oneCount[i] * twoCount[i];
            minZeroCount = zeroCount[i];
        }
    }

    std::cout << answer << std::endl;   

    return 0;
}