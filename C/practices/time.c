//Ea 3 period time of day assignment
#include <stdio.h>

int main(){
   int time;
    printf("what is the time in military time?:");
    scanf("%d", &time);

    if (time <= 1759){
        printf("Youre time is %d so good afternoon", time);
    } else if (time <= 2359) {
        printf(" the time is %d so good evening", time);
    } else if (time <= 1159) {
        printf("the time is %d so good morning", time);
    } else {
        printf("Invalid time");
        }

    return 0;
}
