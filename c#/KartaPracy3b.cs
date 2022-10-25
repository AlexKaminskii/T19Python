
//zad 1

/*
for (int i = 0; i<32; i++)
{
    Console.Write(i + " ");
}
*/


//zad 2

/*
int n = int.Parse(Console.ReadLine());
for (int i = 1; i < n + 1; i = i + 2)
{
    Console.Write(i*i + " ");
}
*/


//zad 3

/*
for 
    (int i = 1137; i < 10000; i = i + 379)
{
    Console.Write(i + " ");
}
*/


//zad 4

/*
for (int i = 100; i < 1000; i++)
{
    if (i%5==0 || i%6==0 || i%11==0)
    {
        Console.Write(i + " ");
    }
    else
    {

    }
}
*/


//zad 5

/*
int suma = 0;
int n = int.Parse(Console.ReadLine());
for (int i = 0; i < n; i++)
{
    int a = int.Parse(Console.ReadLine());
    suma = suma + a;
}
Console.WriteLine(suma);
*/


//zad 6

/*
int suma = 0;
int k = int.Parse(Console.ReadLine());
for (int i = 2; i < (k * 2) + 2; i += 2)
{
    suma = i;
}
Console.WriteLine(suma);
*/


//zad 7


/*
int m = int.Parse(Console.ReadLine());
suma = 0;
for (int i = 11; i < (m * 2) + 2; i += 11)
{
    suma =+ i;
}
Console.WriteLine(suma);
Console.WriteLine();

*/


// zad 8




// zad 9




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
