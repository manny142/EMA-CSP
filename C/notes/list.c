// datatype of items name[#]={item,item,item};
//                         ^number of items
//                         
//
//

#include <stdio.h>
// array = list
int main() {
    //example one
    int grade[] = {74, 88, 95, 87, 98};
    printf("%d\n", grade[2]);

    //example two
    float sizes[] = {3.57, 24.95, 36.1, 5.99};
    // change a item in the list
    printf("%.2f\n", sizes[0]);
    sizes[0] = 10.45;
    printf("%.2f\n", sizes[0]);

    // example three
    char names[][20] = {"alex", "katie", "andrew", "vienna", "tia", "treyson", "xaveir", "jake"};// first bracket is for the string, second is for the array
    printf("%s\n", names[5]);

    return 0;
}