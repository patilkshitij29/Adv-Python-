# Calculate Simple Intrest

def simple_intrest(p:float|int , n:int , r: float|int) -> tuple:

    """
    p : Principal in INR
    n : Number of years
    r : Rate of intrest in percent per annum
    output intrest, amount
    
    """

    i = (p*n*r)/100
    a = p + i
    return i,a

p = float(input("Enter the value of Principal in INR :"))
n = int(input("Enter Number of Years :"))
r = float(input("Enter rate of intrest %p.a :"))

i , a = simple_intrest(p,n,r)

print(f"Simple Intrest : {i:.2f} INR")
print(f"Amount : {a:.2f} INR")

