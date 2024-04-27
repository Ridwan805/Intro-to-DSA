#include <iostream>
using namespace std;

int Bubblesort(int arr[], int n){
    
    for (int i = 0; i < n - 1; i++){
        for (int j= 0; j < n - i - 1; j++){
            if (arr[j] > arr[j+1]){ 
                swap(arr[j], arr[j+1]);
                
            }
        }
    }
    return 0;
}

int main()
{
    int num;
    cout<<"Enter the Number of elements: ";
    cin >> num;
    int arr[num];
    
    for (int i = 0; i < num; i++){
        int x;
        cout << "Enter the element: ";
        cin >> x; 
        arr[i] = x;
    }
    
    Bubblesort(arr,num);
    
    for (int i = 0; i < num; i++){
        cout << arr[i]<<" ";
    }
    

    return 0;
}

