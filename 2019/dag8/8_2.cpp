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
 
    int cols = 25;
    int rows = 6;
    std::vector<int> resultingImage(cols*rows, 2);
    int i = 0;
    int j = 0;
    while (i < inputString.length()) {
        j = 0;
        std::vector<int> image;

        for (; j < cols * rows; j++) {
            int elem = inputString[i+j] - '0';
            image.push_back(elem);
        }
        imageLayers.push_back(image);
        i += j;
    }

    for (i = imageLayers.size() - 1; i > 0; i--)
    {

        for (j = 0; j < resultingImage.size(); j++)
        {
            if (imageLayers[i][j] != 2) {
                resultingImage[j] = imageLayers[i][j];
            }
        }       
    }
    
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            if (resultingImage[i * cols + j] == 1) {
                std::cout << "#";
            } else if (resultingImage[i * cols + j] == 0) {
                std::cout << " ";
            } else {
                std::cout << "_";

            }
        }
        std::cout << "\n";
    }


    return 0;
}