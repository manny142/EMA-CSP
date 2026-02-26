#include <stdio.h>
#include <string.h>
int main() {
    //if(boolean/conditail statmant){code that happens that above is true};
    // if is true or false stament
    //else if(boolean/conditail statmant){code that happens that esle if is true and if is false};
   //else dosent need a codintion{}
   int grade = -1;

    if (grade >= 90) {
        printf("A\n");
    } else if (grade >= 80) {
        printf("B\n");
    } else if (grade >= 70) {
        printf("C\n");
    } else if (grade >= 60) {
        printf("D\n");
    } else {
        printf("you are a falurie\n");
    }

    int num = 4;

    if(num%2 == 0 && num <10){
        printf("%d is a single digit numder!\n", num);
    }else if(num%2 != 0 && (num <10 || num> -10)){
        printf("%d is a single digit od number\n", num);
    }else{
        printf("%d is not a single digit numder!\n", num);
    }

    char name[] = "cora";
    
    if (strcmp(name, "cora") == 0){
        printf("welcome admin");
    }else{
        printf("hello %s\n", name);
    }
    return 0;
}