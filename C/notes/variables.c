// comment
#include <stdio.h> // lets put inputs and outputs

int main(){
    int number = 12; // every time i end a stament i need ;
    float pi = 3.14;
    char name[] = "Xavier";
    char person[50];
    int age;
   
    printf("tell me youre name\n");
    scanf("%d", &age);

    printf("tell me how old you are\n");
    scanf("%d", &age);

    printf("%d\n" , number);
    printf("%f\n" , pi);// \n tells computer that its a new line
    printf("%s is %d years old\n", name , age);
    return 0; // always the last line of main
}
