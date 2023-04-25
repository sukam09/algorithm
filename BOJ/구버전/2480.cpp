#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    int reward;
    int dice[] = {a, b, c};
    int maxval = 0;
    for (int i = 0; i < 3; i++) {
        if (dice[i] > maxval) maxval = dice[i];
    }

    if (a == b && b == c) reward = 10000 + a * 1000;
    else if (a != b && b != c && a != c) reward = maxval * 100;
    else if (a == b || a == c) reward = 1000 + a * 100;
    else reward = 1000 + b * 100;
    
    printf("%d\n", reward);
    return 0;
}