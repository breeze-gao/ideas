
#include <iostream>
#include <cstdio>
using namespace std;

void float2str(string& str, float value) {
  //case 0
  if (value == 0) {
    str.push_back('0');
    return;
  }
  //take care of negative number
  float v = value > 0 ? value : -value;
  int body = int(v);
  float tail = v - body;
  //convert integer part into string
  while (body > 0) {
    str.insert(0, 1, (char)(body%10 + '0'));
    body /=10;
  }
  //convert fraction part into string
  if (tail > 0.0) {
    str.append(".");
    while(tail > 0) {
      tail *= 10;
      str.push_back((char)((int)(tail) + '0'));
      tail = tail - int(tail);
    }
  }
  //negative number
  if (value < 0) {
    str.insert(0, 1, '-');
  }
}

/**
*caution of decimal overflow
*/
int str2float(float& value, string str) {
  value = 0;
  int i = 0;
  int flag = 1;
  if (str[i] == '-') {
    flag = -1;
    i++;
  } else if (str[i] == '+') {
    i++;
  }

  for(; i < str.length() && str[i] != '.'; i++) {
    if ( str[i] >= '0' && str[i] <= '9') {
      value = value * 10 + (str[i] - '0');
    } else {
      return -1;
    }
  }
  
  if (str[i] == '.') {
    float factor = 0.1;
    for (i = i + 1; i < str.length(); i++) {
      if (str[i] >= '0' && str[i] <= '9') {
        value += (str[i] - '0') * factor;
        factor *= 0.1;
      } else { 
        return -1;
      }
    }
  }
  value *= flag;
  return 0;
}

int main() {
  string s;
  float v = 0;
  float2str(s, -10.234);
  cout<<s<<endl;
  cout<<str2float(v, "12.s")<<endl;
  cout<<v<<endl;
  return 0;
}
