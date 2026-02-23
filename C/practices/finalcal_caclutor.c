
#include <stdio.h>

int main(){
   printf("tell me the amount of money you earn:\n");
   float money;
   scanf("%f", &money);
   printf("how much is your rent:\n");
   float rent;
   scanf("%f", &rent);
   printf("your rent is: %4.1f\n", rent / money * 100);
   float utility;
   printf("how much is your utility bill:\n");
   scanf("%f", &utility);
   printf("your utility bill is: %4.1f\n", utility / money * 100);
   float groceries;
   printf("how much is your groceries bill:\n");
   scanf("%f", &groceries);
   printf("your groceries bill is: %4.1f\n", groceries / money * 100);

    return 0;
}