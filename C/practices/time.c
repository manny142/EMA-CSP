//Ea 3 period time of day assignment
#include <stdio.h>

int main(){
   int time;
    printf("what is the time in military time?:");
    scanf("%d", &time);

    if (time >= 1759){
        printf("Youre time is %d so good afternoon", time);
    } else if (time >= 2359) {
        printf(" the time is %d so good evening", time);
    }
    


    return 0;
}
