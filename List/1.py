justice_league = ["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]
print("list of superheros",justice_league,sep='\n')
print("\nNumber of members in justice league",len(justice_league))
batman=["Batgirl","Nightwing"]
justice_league.extend(batman)
print("\nAfter add new members for Batman",justice_league,sep='\n')
x=justice_league.index("Wonder Woman")
leader=justice_league.pop(x)
justice_league.insert(0,leader)
print("\nLeague after wonder woman became leader",justice_league,sep='\n')
x=justice_league.index("Superman")
y=justice_league.pop(x)
for i in range(len(justice_league)):
    if(justice_league[i]=="Flash" or justice_league[i]=="Aquaman"):
        justice_league.insert(i+1,y)
        break
print("\nLeague after seperated Flash and Aquaman",justice_league,sep='\n')
justice_league.remove("Batgirl")
justice_league.remove("Nightwing")
new=["Shazam","Cyborg","Hawkgirl","Martian Manhunter","Green Arrow"]
j=0
for i in range(len(justice_league)):
    if justice_league[i]!="Superman":
        justice_league[i]=new[j]
        j+=1
print("\nLeague after replacement",justice_league,sep='\n')
justice_league.sort()
print("\nLeague sorted alphabetically",justice_league,sep='\n')
print("\nPresent leader of the justice league is",justice_league[0])
        
        
