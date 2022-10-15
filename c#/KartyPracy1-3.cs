//KARTA PRACY 1







// zad 1


int a = int.Parse(Console.ReadLine());
int b = int.Parse(Console.ReadLine());

Console.WriteLine(Math.Pow(a, 2) + Math.Pow(b, 2));

//zad 2

int a = int.Parse(Console.ReadLine());
int b = int.Parse(Console.ReadLine());

Console.WriteLine(Math.Pow((a+b),2)); 


//zad 3

int a = int.Parse(Console.ReadLine());
int b = int.Parse(Console.ReadLine());

Console.WriteLine(Math.Pow((a - b), 3));


//zad 4 


int a = int.Parse(Console.ReadLine());
int b = int.Parse(Console.ReadLine());
int c = int.Parse(Console.ReadLine());


Console.WriteLine(a * b * c);






//zad 5

int a = int.Parse(Console.ReadLine());
int b = int.Parse(Console.ReadLine());

Console.WriteLine(2*(a + b)/5);




// zad 6


double brutto = double.Parse(Console.ReadLine());

Console.WriteLine(brutto / 1.23);




//zad 7


int a = int.Parse(Console.ReadLine());
int b = int.Parse(Console.ReadLine());  

Console.WriteLine(a%b);








//KARTA PRACY 2









//zad 1

int a = int.Parse(Console.ReadLine());

if (a%3==0)
{
    Console.WriteLine("TAK");
}

else
{
    Console.WriteLine("NIE");
}




//zad 2


int a = int.Parse(Console.ReadLine());

if (a>99 && a<1000 && a%17==0)
{
    Console.WriteLine("TAK");
}


else
{
    Console.WriteLine("NIE");
}





// zad 3 


int wiek = int.Parse(Console.ReadLine());



if (wiek>=18)
{
    Console.WriteLine("Pełnoletni");
}

else
{
    Console.WriteLine("Niepełnoletni");
}






// zad 4

int limit = 20;
int waga = int.Parse(Console.ReadLine());

if (waga>limit)
{
    Console.WriteLine("nie możesz wjechać");
}


else
{
    Console.WriteLine("możesz wjechać");
}


//zad 5


int a = int.Parse(Console.ReadLine());
int b = int.Parse(Console.ReadLine());
int c = int.Parse(Console.ReadLine());

if (c>a && c<b || c>b && c<a)
{
    Console.WriteLine("TAK");
}
else
{
    Console.WriteLine("NIE");
}








// Zad 6

int a = int.Parse(Console.ReadLine());
int p = int.Parse(Console.ReadLine());
if ((Math.Pow(a, p) - a) % p == 0)
{
    Console.WriteLine("TAK, spełnia MTF");
}
else
{
    Console.WriteLine("NIE, nie spełnia MTF");
}












//zad 7


int p = int.Parse(Console.ReadLine());
int k = int.Parse(Console.ReadLine());  
int s = int.Parse(Console.ReadLine());


if (3*s>=k-p)
{
    Console.WriteLine("TAK");
}

else
{
     Console.WriteLine("nie");
}





//////////////////////////////////////KARTA PRACY 2







//zad 1

int n = int.Parse(Console.ReadLine());
for (int i = 0; i < n; i++)
{
    Console.WriteLine(Math.Pow(i, 3)+3);
}


 zad 2


for (int i = 105;i<1000;i=i+15)
{
    Console.WriteLine(i.ToString());    
}


 zad 3 

int n = int.Parse(Console.ReadLine());
for (int i = 1; i < n + 1; i++)
{
    Console.Write(n % i == 0 ? i + " " : "");
}
