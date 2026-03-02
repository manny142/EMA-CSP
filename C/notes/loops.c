#include <stdio.h>
// icludes to get random
#include <stdlib.h>
#include <time.h>
// LIST AND LOOPS
//loops are structures
//syntax breakdown
// thimgs needed for loop 1. end point/ 2. start point/3. incrementor(count)
//varidle with start point while(boolean statement(endpoint)){
// what happens while loop is running
//adjust the icementor }
int main() {
    // example one
    int i = 1;
    while(i <=1){
        printf("%d\n", i);
        i++;// increase i by one
    }
    // genrate random namuder
    srand(time(NULL));

    printf("%d\n", rand()% 10);// random betwwen the numder there
    printf("%d\n", (rand()% 5)+1);//random between 1 and 5
    printf("%d\n", rand()% 20);

   // example 2
   int goose = (rand()%9)+1;
   int count = 1;

   while(count < goose){
    printf("duck\n");
    count++;
   }
   printf("goose");

    //example 3
    int time = 30;
    while (time > 0){
        printf("%d\n", time);
        time= time - 2;
    }
    printf("times uuuuuuuuuuuuuuuuuuuuuuuuuuuuuupppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp");
   
    return 0;
}