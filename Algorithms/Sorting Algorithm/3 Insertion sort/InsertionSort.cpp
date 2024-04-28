
#include <iostream>
using namespace std;

int insertionSort(int arr[],int n){
    
    for (int i = 1; i < n; i++){
        
        int temp = arr[i];
        int  j = i - 1 ;
        
        while (j >= 0 and temp < arr[j]){
            arr[j + 1] = arr[j];
            j -= 1;
        arr[j + 1] = temp;
            
        }
        
    }
    return 0;
}

int main()
{
    int n;
    cout << "Enter the number of elements: ";
    cin>>n ;
    int arr[n];
    for (int i = 0; i < n; i++){
        int x;
        cout<< "Enter the element: ";
        cin >> x;
        arr[i] = x;
    }
    
    insertionSort(arr,n);
    
    for (int i = 0; i < n; i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}
