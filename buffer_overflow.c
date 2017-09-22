#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>

void main() {
	char *ptr;
	char *dptr;
	system("cls");

	ptr = (char *)malloc(5 * sizeof(char));
	dptr = (char *)malloc(5 * sizeof(char));

	printf("Address of ptr: %d\n", ptr);
	printf("Address of dptr: %d\n", dptr);

	printf("Enter a string: ");
	gets(ptr);

	system(dptr);
	getch();
}
