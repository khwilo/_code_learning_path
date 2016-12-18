#include <stdio.h>

int main(int argc, char *argv[])
{
	int i = 0;

	/*
	 * go through each string in argv
	 * note why argv[0] is skipped
	 */
	for(i = 1; i < argc; i++)
	{
		printf("arg %d: %s\n", i, argv[i]);
	}

	// make an array of strings
	char *states[] = 
	{
		"Nairobi", "Kisumu", "Mombasa", "Kakamega"
	};

	int num_states = 4;

	for(i = 0; i < num_states; i++)
	{
		printf("state %d: %s\n", i, states[i]);
	}

	return 0;
}
