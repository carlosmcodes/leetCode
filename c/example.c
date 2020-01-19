#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
void int_print(int c);
void char_print(char c);

int main(){
    puts("-----------");
    int i = 2;
    int *k = &i;
    char name[5] = "hey";
    int g = 0;
    for (g = 0; g <= strlen(name); g++){
        char_print(name[g]);
    
    }    
}
void int_print(int c){
    printf("%d", c);
}

void char_print(char c){
    printf("%p",(void*) c);
}