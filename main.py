import math
import pyttsx3 as py
from colorama import Fore, Style

engine=py.init()
voices=engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


engine.say("Enter the axial force (P) subjected to rod in newton")
engine.runAndWait()
p=int(input("Enter the axial force(P) subjected to rod (N): "))
#engine.say("")
#engine.runAndWait()

engine.say("Select the option from following")
engine.runAndWait()
print("1.Choose the material:\n")
print("2.Enter yeild tensile strength manually:\n")

n=int(input("Please enter your selected option:"))

if(n==1):
    print("Select material from given below\n")
    print("Materials:")

    print("1.Aluminium(Al6061) syt=276N/mm^2 yeild crushing stress=265\n")
    print("2.Plain carbon steel(30C8) syt=400N/mm^2 yeild crushing stress=390\n")
    print("3.Plain carbon steel(40C8) syt=380N/mm^2 yeild crushing stress=370\n")
    print("4.Plain carbon steel(45C8) syt=410N/mm^2 yeild crushing stress=405\n")
    print("5.Plain carbon steel(50C4) syt=460N/mm^2 yeild crushing stress=450\n")
    print("6.Plain carbon steel(55C8) syt=490N/mm^2 yeild crushing stress=480\n")
    print("7.Stainless steel(40C10S18) syt=600N/mm^2 yeild crushing stress=580\n")
    print("8.Stainless steel(40C15S12) syt=640N/mm^2 yeild crushing stress=620\n")

    engine.say("select the material from given list")
    engine.runAndWait()
    n1=int(input("Please enter your selected option:"))

    if(n1 == 1):
        s=int(276)
        z=int(265)
    elif(n1 == 2):
        s=int(400)
        z=int(390)
    elif (n1 == 3):
        s = int(380)
        z = int(370)
    elif (n1 == 4):
        s = int(410)
        z = int(405)
    elif (n1 == 5):
        s = int(460)
        z = int(450)
    elif (n1 == 6):
        s = int(490)
        z = int(450)
    elif (n1 == 7):
        s = int(600)
        z = int(580)
    elif (n1 == 8):
        s = int(640)
        z = int(620)
    else:
        print("Invalid input")

elif(n==2):

    engine.say("Enter the Yeild tensile strength(syt) in newton per mm square")
    engine.runAndWait()
    s= int(input("Enter the yeild tensile strength(syt): "))
    engine.say("Enter the crushing stress in newton per mm square")
    engine.runAndWait()
    z = int(input("Enter the yeild crushing stress: "))

else:
    print("invalid input")

#engine.say("enter crushing stress of material:")
#engine.runAndWait()
#x=int(input("Enter crushing stress of material:"))
engine.say("Enter the factor of safety")
engine.runAndWait()
f=int(input("Enter the factor of safety:"))

engine.say("Here is your solution\n")
engine.runAndWait()
#calculation of permissible stress

print("Permissible stress\n")

    # tensile stress

t = s / f
print("Tensile stress = ", t, "N/mm^2")

    # compressive stress
c = s / f
print("Compressive stress= ", c, "N/mm^2")
    # shear stress
l = 0.5 * s / f
print("Shear stress= ", l, "N/mm^2")

x = z / f
print("Crushing stress:\n",x)


#calculation of dimensions
#diameter of rod
#formula is square root of  4 * force / pi * tensile stress

D=math.sqrt((4*p)/(math.pi*t))
cD=math.ceil(D)
print("D = ",D)
print("Rounded to = ",cD,"mm","\n")


#Enlarged diameter of rods(D1)
D1=1.1*D
cD1=math.ceil(D1)
print("Enlarged diameter(D1) = ",D1)
print("Rounded to = ",cD1,"mm","\n")

#Dimensions a and b

a=0.75*D
ca=math.ceil(a)
b=1.25*D
cb=math.ceil(b)
print("a & b =",a,"&",b,"mm","resp")
print("Rounded to = ",ca,"mm","&",cb,"mm","\n")

#Diameter of pin

d=(((32)/(math.pi*t))*((p/2)*((cb/4)+(ca/3))))**(1/3)
cd=math.ceil(d)
print("Diameter of pin = ",d,"mm")
print("Rounded to = ",cd,"mm","\n")

#Dimensions of d0 & d1

d0=2*d
cd0=math.ceil(d0)
d1=1.5*d
cd1=math.ceil(d1)
print("d0 & d1 =",d0,"&",d1,"mm","resp")
print("Rounded to = ",cd0,"mm","&",cd1,"mm","\n")

#Check for stresses in eye
engine.say("Stresses acting in eye")
engine.runAndWait()

print(Fore.MAGENTA+Style.BRIGHT+"Stresses acting in eye")

sigma_t=((p)/((cb)*(cd0-cd)))
csigma_t=math.ceil(sigma_t)
print("Tensile stress in eye =",sigma_t,"N/mm^2")
print("Rounded to = ",csigma_t,"N/mm^2")
if (csigma_t<t):
    print("Design is safe for eye\n")
elif(csigma>t):
    print(Fore.RED+Style.BRIGHT+"Design is unsafe for eye\n"+Style.RESET_ALL)

sigma_c=(p/(cb*cd))
csigma_c=math.ceil(sigma_c)
print("Compressive stress in eye =",sigma_c)
print("Rounded to = ",csigma_c,"N/mm^2")
if(csigma_c<c):
    print("Design is safe for eye\n")
elif(csigma_c>c):
    print(Fore.RED+Style.BRIGHT+"Design is unsafe for eye\n"+Style.RESET_ALL)

tau=((p)/((cb)*(cd0-cd)))
ctau=math.ceil(tau)
print("Shear stress in eye =",tau)
print("Rounded to = ",ctau,"N/mm^2")
if (ctau<l):
    print("Design is safe for eye\n")
elif(ctau>l):
    print(Fore.RED+Style.BRIGHT+"Design is unsafe for eye\n"+Style.RESET_ALL)

#Check for stresses in fork

engine.say("Stresses acting in fork")
engine.runAndWait()
print(Fore.BLUE+Style.BRIGHT+"stresses acting in fork")

sigma_2t=((p)/((2*ca)*(cd0-cd)))
csigma_2t=math.ceil(sigma_2t)
print("Tensile stress in fork =",sigma_2t)
print("Rounded to = ",csigma_2t,"N/mm^2")
if (csigma_2t<t):
    print("Design is safe for fork\n")
elif(csigma_2t>t):
    print(Fore.RED+Style.BRIGHT+"Design is unsafe for fork\n"+Style.RESET_ALL)

sigma_2c=((p)/(2*ca*cd))
csigma_2c=math.ceil(sigma_2c)
print("Compressive stress in fork =",sigma_2c)
print("Rounded to = ",csigma_2c,"N/mm^2")
if (csigma_2c<c):
    print("Design is safe for fork\n")
elif(csigma_2c>c):
    print(Fore.RED+Style.BRIGHT+"Design is unsafe for fork\n"+Style.RESET_ALL)

tau_2=((p)/((2*ca)*(cd0-cd)))
ctau_2=math.ceil(tau_2)
print("Shear stress in fork =",tau_2)
print("Rounded to = ",ctau_2,"N/mm^2")
if (ctau_2<l):
    print("Design is safe for fork\n")
elif(ctau_2>l):
    print(Fore.RED+Style.BRIGHT+"Design is unsafe for fork\n"+Style.RESET_ALL)
#for crushing

crush=(p)/(2*(a)*(d))
print("Crushing stress:",crush,"N/mm^2")

if(crush<x):
    print("Design is safe in crushing\n")
elif(crush>x):
    print(Fore.RED+Style.BRIGHT+"Design is unsafe & use material with high crushing stress\n"+Style.RESET_ALL)


print(Fore.GREEN+Style.BRIGHT+"THANK YOU"+Style.RESET_ALL)
