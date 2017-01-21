//
// Created by Drapegnik on 22.09.14.
//
#include <iostream>

using namespace std;

int main()
{
    int n,osn=10,k=1;
    cin>>n;

    for (int i=1;i<n;i++)
    {
        if ((i/osn)!=0)
        {
            osn*=10;
            k++;
        }
        int sum=0;
        int a=i;

        for (int j=0;j<k;j++)
        {
            int b=a%10;
            a/=10;
            int c=1;

            for (int l=0;l<k;l++)
                c*=b;

            sum+=c;

            if (sum>i)
                    break;
        }

        if (sum==i)
            cout<<i<<endl;
    }
    return 0;
}