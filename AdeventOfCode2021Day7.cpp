#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> myVector = { 1101,1,29,67,1102,0,1,65,1008,65,35,66,1005,66,28,1,67,65,20,4,0,1001,65,1,65,1106,0,8,99,35,67,101,99,105,32,110,39,101,115,116,32,112,97,115,32,117,110,101,32,105,110,116,99,111,100,101,32,112,114,111,103,114,97,109,10,478,157,162,1478,323,191,265,102,440,858,1510,962,45,787,1090,499,521,286,332,788,1424,707,420,846,8,942,1040,1473,364,483,427,265,497,287,247,1279,631,382,176,765,919,178,605,959,414,467,806,1111,141,1096,36,830,674,59,722,633,653,778,251,458,24,989,215,16,184,7,919,170,96,1293,223,616,472,116,384,677,878,770,11,2,477,592,1158,446,687,1525,65,468,1160,341,177,575,391,119,151,202,183,860,59,278,841,90,56,29,1407,165,342,1276,239,233,73,693,1299,162,189,202,532,132,1206,522,249,660,394,402,957,1338,290,975,623,935,618,344,1433,436,104,958,7,263,303,728,698,1326,854,21,469,513,319,970,106,529,537,300,1648,431,255,324,154,894,467,627,136,771,250,1046,925,652,257,194,362,37,71,16,1420,827,457,604,188,1349,0,1314,807,138,368,69,236,1332,1169,42,3,351,426,160,516,185,52,224,602,425,87,1615,1439,58,77,252,11,1054,227,80,761,329,1694,626,66,1192,996,65,313,1048,149,10,1024,307,161,20,867,161,1621,723,629,732,915,185,1185,139,953,851,69,238,1366,926,1084,473,298,737,25,357,37,1887,1421,429,1170,49,62,320,855,888,12,281,297,1320,7,215,1192,732,5,711,20,1641,264,389,135,228,1005,858,4,254,90,388,857,481,1340,40,1139,233,1151,57,38,135,381,272,81,226,179,318,539,45,439,780,2,10,33,1094,1259,913,124,1450,731,572,382,718,189,774,1256,854,59,169,365,15,1526,265,333,499,423,96,1645,167,866,828,1217,238,427,419,311,299,35,161,205,431,252,164,206,1651,1014,163,806,552,105,1584,638,909,51,116,1022,810,701,449,918,829,73,624,1017,82,254,1186,54,371,1018,248,1268,53,1194,925,921,354,264,479,1250,554,671,5,1117,62,904,345,824,1312,685,852,59,722,17,138,357,194,1301,605,12,1162,130,1356,1184,375,1082,55,1270,102,90,559,87,1256,216,875,349,1158,75,52,286,1423,116,406,251,108,480,1015,776,8,1170,346,1263,795,1441,276,36,183,1425,38,169,209,120,63,351,41,154,897,142,747,211,439,8,62,429,244,680,73,849,1091,29,149,285,163,873,232,95,299,849,1466,514,401,414,402,527,216,111,462,921,348,119,106,26,147,445,281,1370,1348,360,1695,805,1148,782,422,718,478,745,100,169,453,349,174,278,275,12,247,527,25,166,410,177,743,182,28,669,6,131,777,302,1368,483,386,51,22,30,1143,18,638,713,334,1388,636,1318,1700,175,399,85,509,1155,1388,488,354,6,162,243,164,340,8,827,624,737,86,55,284,6,493,119,575,569,6,599,163,110,1059,9,752,519,84,606,304,923,1183,171,143,282,1159,426,77,250,1323,1632,531,308,706,786,334,72,449,0,779,762,164,994,628,938,181,111,1342,1682,1293,524,821,931,1322,63,417,148,13,8,444,964,220,215,1526,247,714,1043,23,163,174,484,325,29,986,894,1106,4,28,16,184,203,712,24,243,52,426,308,538,49,75,120,42,62,414,224,326,109,1488,1513,58,1312,124,129,316,1216,1109,736,36,605,40,120,1349,158,195,907,32,142,764,240,1031,480,124,931,1803,530,723,230,423,177,53,17,354,549,259,180,1452,676,313,62,941,522,1600,403,292,179,917,888,317,763,345,631,916,730,1654,1650,273,201,488,1088,138,339,661,0,108,814,361,667,5,1019,272,219,904,127,382,15,1294,235,1204,49,305,1084,1723,1315,151,28,142,1781,71,552,1191,239,1278,17,141,29,269,82,136,32,1326,11,972,218,273,1081,469,353,90,99,1183,374,523,993,1355,1128,568,381,800,157,1723,27,983,664,177,381,1300,512,502,291,336,211,12,53,699,95,1136,757,51,339,308,597,1246,21,46,849,114,468,62,871,282,936,108,424,2,210,1261,140,407,901,530,129,1147,230,1149,113,11,210,34,772,96,254,101,278,663,134,767,973,1184,218,1062,13,724,121,13,928,522,424,346,199,1164,282,163,403,1195,12,228,914,7,306,701,124,82,131,1110,1187,577,702,114,605,187,249,19,18,24,9,1108,664,559,1471,174,93,279,1100,18,158,479,106,429,1105,328,126,129,409,523,679,1471,412,1363,1354,221,107,1497,710,346,457,180,247,1048,68,157,791,412,589,215,181,338,879,633,1310,212,1004,299,123,861,980,157,206,734,715,1190,332,542,468,51,39,498,813,1850,275,254,1726,579,239,99,16,80,472,92,800 };
    auto it = max_element(std::begin(myVector), std::end(myVector));
    int max = *it;
    int min_fuel = INT_MAX;
    /*for (int i = 0; i < max; ++i)
    {
        int fuel = 0;

        for (int j = 0; j < myVector.size(); ++j)
        {
            fuel += abs(i - myVector[j]);
        }
        if (fuel < min_fuel)
            min_fuel = fuel;
    }*/
    ////part two
    for (int i = 0; i < max; ++i)
    {
        int fuel = 0;
        int n = 0;
        for (int j = 0; j < myVector.size(); ++j)
        {
            n = abs(i - myVector[j]);
            for (int k = 1; k <= n; ++k)
                fuel += k;
            n = 0;
        }
        if (fuel < min_fuel)
            min_fuel = fuel;
    }
    std::cout << min_fuel;
}

