# sets have same operation that are performed on set in maths
#  including :
#        intersection            (&)
#        symmetric difference    (disjoint)
#        union                   (|)



math = ({"mathew", "helen", "prashant", "james", "aparna"})
biology = ({"jane", "mathew", "charlotte", "masut", "oliver", "james"})

print(f"math : {math}")
print(f"biology : {biology}")
print("union : ")
print(math | biology)      # union
print("intersection : ")
print(math & biology)     # instersection
print("disjoint : ")
print((math | biology) - (math & biology))    # disjoint
