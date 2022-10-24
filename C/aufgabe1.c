#!/usr/bin/env -S tcc -run
#include <stdio.h>

int isEven(int num) {
	return num % 2 == 0;
}

int isOdd(int num) {
	return !isEven(num);
}

int main() {
	// print from 1 to 10
	for(int i = 1; i <= 10; i++) {
		printf("%d, ", i);
	}
	putchar('\n');

	// print odd numbers from 1 to 100
	for(int i = 1; i <= 100; i++) {
		if(isOdd(i)) {
			printf("%d, ", i);
		}
	}
	putchar('\n');

	int i = 0;
	while(i <= 99) {
		if(isEven(i)) {
			printf("%d, ", i);
		}
		i++;
	}
	putchar('\n');

	char foo = 'a';
	do {
		printf("%c, ", foo);
		foo++;
	} while(foo <= 'z');
	putchar('\n');

	/*
		Multi
		Zeilen
		Kommentar
	*/

	return 0;
}
