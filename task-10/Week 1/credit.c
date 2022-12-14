#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    long card_number;
    int get_digit;
    int count_digits = 0;
    int other_digit;
    int other_sum = 0;
    long start_number = 0;
    int checksum = 0;
    bool visa_digits;
    bool amex_start;
    bool mastercard_start;

    card_number = get_long("What's is you credit card card_number? ");
    while (card_number != 0)
    {
        get_digit = card_number % 10;

        if (count_digits % 2 != 0)
        {
            other_digit = get_digit * 2;

            other_sum += (other_digit % 100 == 0) ? other_digit :
                         other_digit % 10 + other_digit / 10;
        }
        else
        {
            checksum += get_digit;
        }
        if (card_number / 100 == 0 && start_number == 0)
        {
            start_number = card_number;
        }

        card_number = card_number / 10;
        count_digits++;
    }
    checksum = (checksum + other_sum) % 10;

    visa_digits = count_digits == 13 || count_digits == 16;

    amex_start = start_number == 34 || start_number == 37;

    mastercard_start = start_number == 51 || start_number == 52 || start_number == 53 ||
                       start_number == 54 || start_number == 55;

    if (checksum == 0 && count_digits == 15 && amex_start)
    {
        printf("AMEX\n");
    }
    else if (checksum == 0 && start_number / 10 == 4 && visa_digits)
    {
        printf("VISA\n");
    }
    else if (checksum == 0 && count_digits == 16 && mastercard_start)
    {
        printf("MASTERCARD\n");
    }
    else
    {
        printf("INVALID\n");
    }
}