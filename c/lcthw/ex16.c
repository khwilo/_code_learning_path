#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

/*
 * Define a structure with 4 elements.
 * Similar to a class in OOP or 
 * a record in a database table.
 */
struct Person {
	char *name;
	int age;
	int height;
	int weight;
};

// This function allows us to create the structure
struct Person *Person_create(char *name, int age, int height, int weight)
{
	/*
	 * Use malloc to "memory allocate", 
	 * ask the OS to give a piece of raw memory.
	 * Pass malloc the size of struct
	 * which calculate the total size of struct.
	 */
	struct Person *who = malloc(sizeof(struct Person));
	/*
	 * Use assert to make sure I have 
	 * a valid piece of memory back from malloc.
	 * The special constant NULL means "unset or invalid pointer".
	 * The assert checks if malloc didn't return a NULL invalid pointer."
	 */
	assert(who != NULL);
	
	// Initialize the struct using the x->y syntax
	
	/*
	 * The strdup function is used to duplicate the string for the name,
	 * to make sure that this structure actually owns it.
	 * Similar to malloc and it also copies the original string into
	 * the  memory it creates.
	 */
	who->name = strdup(name);
	who->age = age;
	who->height = height;
	who->weight = weight;

	return who;
}

// This function destroys the Person structs
void Person_destroy(struct Person *who)
{
	assert(who != NULL);
	
	/*
	 * The function free is used to return memory I got with
	 * malloc and strdup. Or else you get a "memory leak".
	 */
	free(who->name);
	free(who);
}

// This function is used to print out people
void Person_print(struct Person *who)
{
	printf("Name: %s\n", who->name);
	printf("\tAge: %d\n", who->age);
	printf("\tHeight: %d\n", who->height);
	printf("\tWeight: %d\n", who->weight);
}

int main(int argc, char *argv[])
{
	// make two people structures
	struct Person *khwilo = Person_create("Khwilo Kabaka", 23, 64, 75);

	struct Person *frank = Person_create("Frank Ochami", 21, 56, 65);

	// print them out when they are in memory
	printf("Khwilo is at memory location %p:\n", khwilo);
	Person_print(khwilo);

	printf("Frank is at memory location %p:\n", frank);
	Person_print(frank);

	// make everyone age 20 years and print them again
	khwilo->age += 20;
	khwilo->height += 2;
	khwilo->weight += 5;
	Person_print(khwilo);

	frank->age += 20;
	frank->weight += 10;
	Person_print(frank);
	
	// destroy them both so we clean up
	Person_destroy(khwilo);
	Person_destroy(frank);
	
	return 0;
}
