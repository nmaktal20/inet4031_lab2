#include <stdio.h>

int main() {
    int a = 2;
    int b = 2;
    int c = a + b;
    printf("C says: Hello, World!\n");
    printf("%d + %d = %d\n",a,b,c);
    
    // Add array of strings and for loop
    char *users[] = {"User1", "User2", "User3"};
    for(int i = 0; i < 3; i++) {
        printf("%s\n", users[i]);
    }
    return 0;
}
