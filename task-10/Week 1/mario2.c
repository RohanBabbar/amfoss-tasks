#include <stdio.h>
#include <cs50.h>

int height;
int direction = 0;

int main(void)
{
    do
    {
        height = get_int("What's is the height?(1-8) ");
    }
    while (height < 1 || height > 8);

    for (int i = 0; i < height; i++)
    {
        for (int j = height - 1; j >= 0; j --)
        {
            if (j <= i)
            {
                printf("#");
            }
            else if (j > i && direction == 0)
            {
                printf(" ");
            }
            if (j <= 0 && direction == 0)
            {
                printf("  ");
                direction = 1;
                j = height;
            }
        }
        direction = 0;
        printf("\n");
    }
}