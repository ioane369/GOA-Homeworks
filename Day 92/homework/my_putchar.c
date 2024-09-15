// Write a function my_putchar to distinguish between two types of errors if EOF is returned: use ferror to check for error indicators and feof to check for end-of-file indicators.

#include <stdio.h>
#include <stdlib.h>

int my_putchar(){
    int c;  
    if ((c = getchar()) == EOF){
        if (ferror(stdin)){
            perror("error indicator is set");
            exit(1);
        } 
        if (feof(stdin)){
            perror("end-of-file indicator is set");
            exit(2);
        }
        perror("getchar returned EOF when error indicator and end-of-file indicator ARE NOT SET");
        exit(3);
    }   

    if (putchar(c) == EOF){
        if (ferror(stdout)){
            perror("error indicator is set");
            exit(4);    
        }     
        if (feof(stdout)){      
            perror("end-of-file indicator is set");
            exit(5);
        }
        perror("putchar returned EOF when error indicator and end-of-file indicator ARE NOT SET");
        exit(6);
    }
    return c;
}

int main(){
    my_putchar();
    return 0;
}