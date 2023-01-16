using System;
using System.Net;
using System.Runtime.InteropServices;

// zad 1

int n = int.Parse(Console.ReadLine());

int suma = 0;
while (n > 0)
{
    suma += n % 10;
    n = n / 10;
}
Console.WriteLine(suma);


// zad 2




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
}


// zad 3




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
}



// zad 4





int x = int.Parse(Console.ReadLine());
int y = int.Parse(Console.ReadLine());

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

if (NWD(x, y) == 1)
{
    Console.WriteLine("Liczby są względnie pierwsze");
}
else
{
    Console.WriteLine("Liczby nie są względnie pierwsze");
}


//zad 5



int n = int.Parse(Console.ReadLine());

for (int i = 10; i < 20; i++)
{
    if (NWD(n, i) == 1)
    {
        Console.WriteLine(i);
    }
}


// zad 6

Console.Write("Podaj licznik: ");
int a = int.Parse(Console.ReadLine());
Console.Write("Podaj mianownik: ");
int b = int.Parse(Console.ReadLine());

a = a / NWD(a, b);
b = b / NWD(a, b);

Console.WriteLine($"Skrócony ułamek: {a}/{b}");


// zad 7


Console.Write("Podaj licznik: ");
int a = int.Parse(Console.ReadLine());
Console.Write("Podaj mianownik: ");
int b = int.Parse(Console.ReadLine());

int c = a / b;
Console.WriteLine($"{c}  {(a%b)/NWD(a, b)}/{b/NWD(a, b)}");



//zad 8




for (int i = 2; i < 10000; i++)
{
    int a = 0;
    
    for (int j = 1; j < i; j++)
    {
        if (i%j==0)
        {
            a += j;
        }
    }

    int b = 0;
    
    for (int j = 1; j < a; j++)
    {
        if (a % j == 0)
        {
            b += j;
        }
    }

    if (i == b && i != a)
    {
        Console.WriteLine($"{i} i {a} są liczbami zaprzyjaźnionymi");
    }
}





// zad 9



int pierwsza(int n)
{
    if (n < 2)
    {
        return 0;
    }
    else if (n == 2)
    {
        return 1;
    }

    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

for (int i = 10; i < 100; i++)
{
    if (pierwsza(i) == 1)
    {
        for (int j = 10; j < 100; j++)
        {
            if (pierwsza(j) == 1)
            {
                Console.WriteLine($"{i*j} = {i}*{j}");
            }
        }
    }
}






// zad 10




int n = int.Parse(Console.ReadLine());

if (pierwsza(n) == 1 && pierwsza(n + 2) == 1)
{
    Console.WriteLine($"Tak, liczba {n} ma bliźniaczą liczbę {n+2}");
}
else
{
    Console.WriteLine("Nie, a liczb anie ma bliźniaka lub nie jest pierwsza");
}

