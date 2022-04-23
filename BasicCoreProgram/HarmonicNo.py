print("**********Harmonic No**********")
def HarmonicNo(n):
    harmonic=0
    for i in range(1,n+1):
           harmonic=harmonic+1/i
           print(harmonic)
n=int(input("Enter the Number: ")) 
HarmonicNo(n)
