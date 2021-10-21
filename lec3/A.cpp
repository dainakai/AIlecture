#include<iostream>
#include<vector>
#include<string>
#include<sstream>
using namespace std;
void adjMat(vector <vector<int>> inputMat, vector<int> vec);

int main(){
    //Item num
    int n;
    cin >> n;
    cin.ignore();

    vector <vector<int>> adjMatrix(n, vector<int>(n));

    string tmp_string;   
    int s;
    vector<int> vec;
    for (int idx = 0; idx < n; idx++)
    {
        getline(cin,tmp_string);
        stringstream ss(tmp_string);
        while(ss >> s){
            vec.push_back(s);
        }
        adjMat(adjMatrix,vec);
    }


    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < adjMatrix.at(i).size(); j++)
        {
            if(j != 0)
                cout << " ";

            cout << adjMatrix.at(i).at(j);
        }
        cout << endl;
    }
    
    return 0;
    
}

void adjMat(vector <vector<int>> inputMat, vector<int> vec){
    int x = vec.at(0);
    int y;
    for (int n = 0; n < vec.at(1); n++)
    {
        y = vec.at(n+2);
        inputMat.at(x).at(y) = 1;
    }   
}