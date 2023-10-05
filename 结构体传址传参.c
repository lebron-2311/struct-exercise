#define _CRT_SECURE_NO_WARNINGS 1
#include<stdio.h>
#include<string.h>
struct Stu
{
	char name[20];
	int age;
};
void print(struct Stu* ps)
{
	printf("name=%s age=%d\n", (*ps).name, (*ps).age);
	printf("name=%s age=%d\n", ps->name, ps->age);
}

int main()
{
	struct Stu a1 = { "yaochangkun",25 };
	print(&a1);
	return 0;
}