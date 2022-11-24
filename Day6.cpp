#include <iostream>
#include <vector>
#include<fstream>

int main()
{
    std::ifstream s("input.txt");
    char c;
    std::vector<int> myVector;
    std::vector<long long> partTwo = { 0,0,0,0,0,0,0,0,0 };
    while (s.get(c))
    {
        if (c != ',') 
        {
            int i = c - '0';
            myVector.push_back(i);
        }
    }
    for (auto i : myVector)
    {
        partTwo[i]++;
    }
    long long zeroes = 0;
    for (int i = 0; i < 256; ++i)
    {   
        zeroes = partTwo[0];
        for (int j = 1; j < 9; ++j)
        {
            partTwo[j-1] = partTwo[j];
        }
        partTwo[6] += zeroes;
        partTwo[8] = zeroes;
    }
    
    long long sum = 0;
    for (int i = 0; i < partTwo.size(); ++i )
        sum += partTwo[i];
    std::cout << sum;
}

