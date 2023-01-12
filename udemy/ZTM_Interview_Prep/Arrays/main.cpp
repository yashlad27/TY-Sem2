#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main(){
    string s1[4] = {"a", "b", "c", "d"};
    cout<<s1<<endl;

    // push
    s1.push_back('e');

    // pop
    s1.pop_back();
    s1.pop_back();

    cout<<s1<<endl;

    return 0;
}