#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        int num = i;
        int clap = 0;
        while (num) {
            int digit = num % 10;
            if (digit % 3 == 0 && digit) clap++;
            num /= 10;
        }
        
        if (clap) {
            for (int j = 0; j < clap; j++) printf("-");
        }
        else printf("%d", i);
        printf(" ");
    }

    return 0;
}