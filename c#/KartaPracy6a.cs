using System;
using System.Runtime.InteropServices;

// zad 1

/*int n = int.Parse(Console.ReadLine());

int suma = 0;
while (n > 0)
{
    suma += n % 10;
    n = n / 10;
}
Console.WriteLine(suma);*/


// zad 2


/*

int n = int.Parse(Console.ReadLine());

if (n < 2)
{
    Console.WriteLine("Liczba nie jest pierwsza");
}
else if (n == 2) 
{
    Console.WriteLine("Liczba jest pierwsza");
    
}

for (int i = 2; i < n; i++)
{
    if (n % i == 0)
    {
        Console.WriteLine("Liczba nie jest pierwsza");
        break;
    }
    else
    {
        Console.WriteLine("Liczba jest pierwsza");
        break;
    }
}*/


// zad 3


/*

int n = int.Parse(Console.ReadLine());
int suma = 0;
for (int i = 1; i < n; i++)
{
    if (n % i == 0)
    {
        suma += i;
    }
}

if (suma == n)
{
    Console.WriteLine("Liczba jest doskonała");
}
else
{
    Console.WriteLine("Liczba nie jest doskonała");
}*/



// zad 4




/*
int x = int.Parse(Console.ReadLine());
int y = int.Parse(Console.ReadLine());
*/
int NWD(int a, int b)
{
    while (b != 0)
    {
        int temp = a % b;
        a = b;
        b = temp;
    }

    return a;
}
/*
if (NWD(x, y) == 1)
{
    Console.WriteLine("Liczby są względnie pierwsze");
}
else
{
    Console.WriteLine("Liczby nie są względnie pierwsze");
}*/


//zad 5



/*int n = int.Parse(Console.ReadLine());

for (int i = 10; i < 20; i++)
{
    if (NWD(n, i) == 1)
    {
        Console.WriteLine(i);
    }
}*/


// zad 6

Console.Write("Podaj licznik: ");
int a = int.Parse(Console.ReadLine());
Console.Write("Podaj mianownik: ");
int b = int.Parse(Console.ReadLine());

a = a / NWD(a, b);
b = b / NWD(a, b);

Console.WriteLine($"Skrócony ułamek: {a}/{b}");
