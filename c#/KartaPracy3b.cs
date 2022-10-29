//zad 1

/*
for (int i = 1; i<32;i++)
{
    Console.WriteLine(i);
}
*/

// zad 2

/*
int n = int.Parse(Console.ReadLine());
for (int i = 1; i < n+1; i = i + 2)
{
    Console.WriteLine(i*i + " ");
}
*/


// zad 3

/*
for (int i = 1137;i<10000; i++)
{
    if (i % 379 == 0)
    {
        Console.WriteLine(i);
    }
    else
    {

    }
}
*/


//zad 4
/*
for (int i = 100; i < 1000;i++)
{
    if (i%5==0 || i%6==0 || i%11==0)
    {
        Console.WriteLine(i);
    }
}
*/


//zad 5

/*
int suma = 0;
int n = int.Parse(Console.ReadLine());
for (int i = 0; i < n;i++)
{
    int a = int.Parse(Console.ReadLine());
    suma = suma + a;
}
Console.WriteLine(suma);
*/

// zad 6

/*
int k = int.Parse(Console.ReadLine());
for (int i = 2; i < (k * 2) + 2; i = i + 2) 
{
    Console.WriteLine(i);
}
*/


// zad 7

/*
int l = int.Parse(Console.ReadLine());
for (int i = 11; i < (l * 2) + 11; i = i + 2) 
{
    Console.WriteLine(i);
}
*/


// zad 8                NIE DZIAŁA

/* 
int kwej = int.Parse(Console.ReadLine());
int lata = int.Parse(Console.ReadLine());
double suma = 0;
suma = kwej;

for (int i = 1; i < lata * 12 ; i++)
{
    double kkon = suma * 0.06 * 1 / 12;
    suma = suma + kkon;
}
Console.WriteLine(suma);

*/


// zad 9

/*
int suma = 0;
int n = int.Parse(Console.ReadLine());
for (int i = 21; i < n * 100; i = i + 100)
{
    suma = suma + i;
    
}
Console.WriteLine(suma);
*/




// zad 10

for (int i = 1; i< 1000; i++)
{
    if (i % 10 == Math.Sqrt(i))
    {
        Console.WriteLine(i);
    }
    if (i%100 == Math.Sqrt(i))
    {
        Console.WriteLine(i);
    }
}
