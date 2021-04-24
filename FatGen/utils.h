#ifndef FATGEN_
#define FATGEN_
#include <bits/stdc++.h>
#include <random>
using namespace std;
static random_device rd;  
static mt19937_64 rng(rd());
ostream & operator<< (ostream& os,vector <vector <int>> &v);
ostream & operator<< (ostream& os,vector <int> &v);
vector <vector<int>> matGen(int tc,int b);
#endif