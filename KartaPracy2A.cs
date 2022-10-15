// KARTA PRACY 2A



// zad 1


int a = int.Parse(Console.ReadLine());  
int b = int.Parse(Console.ReadLine());

if ((a+b)%2==0)
{
    Console.WriteLine("TAK");
}

else
{
    Console.WriteLine("NIE");
}


//zad 2


int a = int.Parse(Console.ReadLine());
int g = int.Parse(Console.ReadLine());

if ((a+g)/2>Math.Sqrt(a*g))
{
    Console.WriteLine("TAK");
}

else
{
    Console.WriteLine("NIE");
}


// zad 3


int k = int.Parse(Console.ReadLine());
int l = int.Parse(Console.ReadLine());  
int m = int.Parse(Console.ReadLine());  


if (k == l && m!=k && m!=l)
{
    Console.WriteLine("Tak, równe są " + k + " i " + l);
}
else
{
    if (k!=l && m==k && m!=l)
    {
        Console.WriteLine("Tak równe są " + m + " i " +k);
    }
    else
    {
        if (k!=l && m!=k && m==l)
        {
            Console.WriteLine("Tak, równe są " + m + " i " + l);
        }
        else
        {
            Console.WriteLine("Żadna z liczb nie jest równa lub wszystkie trzy są równe");
        }
    }
}



//zad 4


int a = int.Parse(Console.ReadLine());
int b = int.Parse(Console.ReadLine());  
int c = int.Parse(Console.ReadLine());
int d = int.Parse(Console.ReadLine());


if (a<b && a<c && a<d)
{
    Console.WriteLine(a);
}
else
{
    if (b < a && b < c && b < d)
    {
        Console.WriteLine(b);
    }
    else 
    {
        if (c < a && c < b && c < d)
        {
            Console.WriteLine(c);
        }
        else
        {
            if (d<a && d<b && d<c)
            {
                Console.WriteLine(d);
            }
        }

    }
}






//zad 5



int a = int.Parse(Console.ReadLine());
int b = int.Parse(Console.ReadLine());
int c = int.Parse(Console.ReadLine());


if ((a<b+c) && (b<a+c) && (c<a+b))
{
    Console.WriteLine("TAK, da się zbudować trójkąt");
}

else
{
    Console.WriteLine("NIE, nie da się zbudowac trójkąta");
}





// zad 6



int a = int.Parse(Console.ReadLine());
int b = int.Parse(Console.ReadLine());  
int c = int.Parse(Console.ReadLine());


if ((a * a + b * b == c * c) && (a * a + b * b == c * c) && (c * c + b * b == a * a))
{
    Console.WriteLine("prostokątny");
}
else
{
    if ((a * a + b * b < c * c) && (a * a + b * b < c * c) && (c * c + b * b < a * a))
    {
        Console.WriteLine("rozwartokątny");
    }
    else
    {
        if ((a * a + b * b > c * c) && (a * a + b * b > c * c) && (c * c + b * b > a * a))
        {
            Console.WriteLine("ostrokątny");
        }
        else
        {

        }
    }
}





