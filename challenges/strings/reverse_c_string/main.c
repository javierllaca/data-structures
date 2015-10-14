/*
 * Implement a function void reverse(char *str) in C or C++
 * which reverses a null-terminated string.
 */

#include <stdio.h>
#include <string.h>
#include <assert.h>

void swap(char *s, int i, int j)
{
    char temp = s[i];
    s[i] = s[j];
    s[j] = temp;
}

void reverse(char *s)
{
    int len = strlen(s);
    int mid = len / 2;
    int i;
    for (i = 0; i < mid; i++) {
        swap(s, i, len - 1 - i);
    }
}

int main()
{
    char a[24], b[24];

    strcpy(a, "hello world");
    strcpy(b, "dlrow olleh");

    reverse(a);

    assert(strcmp(a, b) == 0);

    return 0;
}
