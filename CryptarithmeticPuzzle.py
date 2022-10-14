# second solution, much easier

from simpleai.search import CspProblem, backtrack

factor1 = input("Factor1: ").upper() #input vragen aan gebruiker voor factor1
factor2 = input("Factor2: ").upper() #input vragen aan gebruiker voor factor2
result = input("result: ").upper()  #input vragen aan gebruiker voor result

variables = [] #input initializeren

for letter in factor1: #loop over alle leters van factor1
    variables.append(letter) #voeg de letter toe aan variables
for letter in factor2: #loop over alle leters van factor2
    variables.append(letter) #voeg de letter toe aan variables
for letter in result: #loop over alle leters van result
    variables.append(letter) #voeg de letter toe aan variables

variables = set(variables) #we gaan ervoor zorgen dat elke waarde in de lijst variables uniek word met de set functie
variables = tuple(variables) #we maken van variables een tuple

domains = {} # we initialiseren de dictionary domains voor onze domains in toe te voegen voor de ranges van al de letters in te zetten (de eerste letters range(1,10) de rest range(0,10))
for letter in variables: #voor elke waarde/letter in de tuple variables loopen
    if letter in (variables[variables.index(factor1[0])],variables[variables.index(factor2[0])],variables[variables.index(result[0])]): # als de letter de eerste letter is van factor1, factor2 of result
        domains[letter] = list(range(1,10)) #dan geven we deze leter(key) de waarde list(range(1,10)) voor geen leading zeros te hebben in onze som
    else: #anders
        domains[letter] = list(range(0,10)) #geven we deze leter(key) de waarde list(range(0,10))

indexFactor1 = [] #we initialiseren hier indexFactor1 lijst voor alle indexen bij te houden van factor1 string in de variables tuple
indexFactor2 = [] #we initialiseren hier indexFactor2 lijst voor alle indexen bij te houden van factor2 string in de variables tuple
indexResult = [] #we initialiseren hier indexResult lijst voor alle indexen bij te houden van result string in de variables tuple
for index in range(len(factor1)): #voor elke index tussen 0 tot lengte van factor1
    indexFactor1.append(variables.index(factor1[index])) #voeg de index van variables toe van de letter op meegegeven index van factor1
for index in range(len(factor2)): #voor elke index tussen 0 tot lengte van factor2
    indexFactor2.append(variables.index(factor2[index])) #voeg de index van variables toe van de letter op meegegeven index van factor2
for index in range(len(result)): #voor elke index tussen 0 tot lengte van result
    indexResult.append(variables.index(result[index])) #voeg de index van variables toe van de letter op meegegeven index van result


def constraint_unique(variables, values):   #define functie constraint_unique met parameters: variables, values
    return len(values) == len(set(values))  #verwijder dubble waardes in values

def constraint_add(variables, values): #define functie constraint add met parameters: variables, values. De constraint om ervoor te zorgen dat de som van factor1 en factor gelijk is aan result
    factor = "" # initialiseer factor variable
    Sfactor ="" # initialiseer Sfactor variable
    result = "" # initialiseer result variable
    for index in indexFactor1: #loop voor elke waard(index) in indexFactor1
        factor += str(values[index]) #voeg elke letter van factor1 toe aan factor
    for index in indexFactor2: #loop voor elke waard(index) in indexFactor2
        Sfactor += str(values[index]) #voeg elke letter van factor2 toe aan Sfactor
    for index in indexResult: #loop voor elke waard(index) in indexResult
        result += str(values[index]) #voeg elke letter van result toe aan result
    return (int(factor) + int(Sfactor)) == int(result) #maak van factor, Sfactor en result een integer en tel factor en Sfactor op zodat dit gelijk is aan result. dit word gereturned

constraints = [ #zet beide aangemaakte functies in constrainsts
    (variables, constraint_unique), #gebruik variables als waarde in functie constraint_unique
    (variables, constraint_add), #gebruik variables als waarde in functie constraint_add
]

problem = CspProblem(variables, domains, constraints) #zet de variables , domains en constraints in de CsProblem clas zodat de AI het probleem kan oplossen

output = backtrack(problem) #zorgt ervoor dat backtracking werkt


#Hier weergeef ik de output
print("  {}\n +{}\n{}\n {}".format(factor1,factor2,(len(result)+1)*"-",result)) #print factor1 factor2 en result in som vorm

#hier maak ik variables aan om makkelijk te kunnen printen
cijfer1 = ""
cijfer2 = ""
cijfer3 = ""

for letter in factor1: #loop voor elke letter in factor1
    cijfer1 += str(output[variables[variables.index(letter)]]) #zet het cijfer dat overeenkomt met de letter van factor1 om naar string zodat dit geconcateneerd kan worden
for letter in factor2: #loop voor elke letter in factor2
    cijfer2 += str(output[variables[variables.index(letter)]]) #zet het cijfer dat overeenkomt met de letter van factor2 om naar string zodat dit geconcateneerd kan worden
for letter in result: #loop voor elke letter in result
    cijfer3 += str(output[variables[variables.index(letter)]])#zet het cijfer dat overeenkomt met de letter van result om naar string zodat dit geconcateneerd kan worden

print("  {}\n +{}\n{}\n {}".format(cijfer1,cijfer2,(len(cijfer3)+1)*"-",cijfer3)) #print de cijfers in som vorm

for variable in variables: #loop voor elke variable in variables
    print(variable, end=" ") #print elke variable met 1 spatie
print() #enter
for variable in variables: #loop voor elke variable in variables
    print(output[variable], end=" ") #print elke overeenkomende waarde van de variable af