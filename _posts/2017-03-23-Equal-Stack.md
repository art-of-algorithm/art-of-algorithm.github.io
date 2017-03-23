---
layout: post
title:  "Equal Stack"
categories: implementation stack
author: "Rahul"
---

C++ program for printing the maximum height at which all stacks will be of equal height.

```C++
#include <bits/stdc++.h>

using namespace std;

int arr1[100005];
int arr2[100005];
int arr3[100005];

void solution() {

    int n1, n2, n3, h, sum1=0, sum2=0, sum3=0, d1, d2, d3;
    cin >> n1 >> n2 >> n3;

    for(int i=0; i<n1; i++) {
        cin>>arr1[i];
        sum1+=arr1[i];
    }
    d1 = 0;

    for(int i=0; i<n2; i++) {
        cin>>arr2[i];
        sum2+=arr2[i];
    }
    d2 = 0;

    for(int i=0; i<n3; i++) {
        cin>>arr3[i];
        sum3+=arr3[i];
    }
    d3 = 0;

    while(1) {
        if(d1 == n1 || d2 == n2 || d3 == n3) {
            h = 0;
            break;
        }

        if(sum1 == sum2 && sum2 == sum3) {
            h = sum1;
            break;
        }

        // If height op pile one is highest
        if(sum1 >= sum2 && sum1 >= sum3) {
            sum1 -= arr1[d1];
            d1++;
        }
        // If height op pile two is highest
        else if(sum2 >= sum1 && sum2>=sum3) {
           sum2 -= arr2[d2];
           d2++;
        }
        // If height op pile three is highest
        else if(sum3 >= sum2 && sum3 >= sum1) {
            sum3 -= arr3[d3];
            d3++;
        }
    }
    cout << h << endl;
}

int main () {
    solution();
    return 0;
}

```
