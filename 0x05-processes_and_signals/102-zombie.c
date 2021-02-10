#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
#include<stdlib.h>
/**
 *infinite_while - infinit loop
 *Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 *main - fucntion main that creates zombies
 *Return: Always 0
 */
int main(void)
{
	pid_t zombie1, zombie2, zombie3, zombie4, zombie5;

	zombie1 = fork();
	if (zombie1 == 0)
		exit(0);
	else
		printf("Zombie process created, PID: %i\n", zombie1);
	zombie2 = fork();
	if (zombie2 == 0)
		exit(0);
	else
		printf("Zombie process created, PID: %i\n", zombie2);
	zombie3 = fork();
	if (zombie3 == 0)
		exit(0);
	else
		printf("Zombie process created, PID: %i\n", zombie3);
	zombie4 = fork();
	if (zombie4 == 0)
		exit(0);
	else
		printf("Zombie process created, PID: %i\n", zombie4);
	zombie5 = fork();
	if (zombie5 == 0)
		exit(0);
	else
		printf("Zombie process created, PID: %i\n", zombie5);
	infinite_while();
	return (0);
}
