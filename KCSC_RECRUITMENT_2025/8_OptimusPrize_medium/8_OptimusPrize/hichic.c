#include <iostream>
#include <algorithm> 
using namespace std;

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
    int n = sizeof(arr) / sizeof(arr[0]);

    int i = 2, j = 5;

    cout << "mang ban dau";
    printArray(arr, n);

    
    sort(arr + i, arr + j + 1);

    cout << "amng sau khi sap xep vi tri " << i << " den " << j << ": ";
    printArray(arr, n);

    return 0;

}