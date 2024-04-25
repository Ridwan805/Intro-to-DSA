#include <iostream>
using namespace std;

int insertionsort(int arr[],int n){
    
    for(int i = 0 ; i < n-1; i++){
        int min = i;
        
        for(int j = i+1; j < n ; j++){
            if (arr[j] < arr[min]){
                
                min = j;
            }
        }
        
        arr[i],arr[min] = arr[min],arr[i];
    }
    
}

int main()
{
    int n;
    cout<<"Enter the number of Element: ";
    cin>> n;
    int arr[n];
    
    for(int i = 0;i<n;i++){
        
        int x;
        cout<<"Enter the element: ";
        cin >> x;
        arr[i] = x;
    }
    
    insertionsort(arr,n);
    
    for(int i = 0;i<n;i++){
        cout<<arr[i];
        cout<<" ";
    }

    return 0;
}
