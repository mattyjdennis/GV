customerName = input("Customer Name:\n")
mixName = input("Mix Name:\n")
servings = 0 #int(input("Number of Servings:\n"))
L_Citrulline_Mallate = int(input("Amount of L-Citrulline Malate (2:1) per serving(grams):\n"))
Beta_Alanine = int(input("Amount of Beta Alanine per serving(grams):\n"))
Caffeine_Anhydrous = float(input("Amount of Caffeine Anhydrous per serving(milligrams):\n"))/1000
Betaine_Anhydrous = int(input("Amount of Betaine Anhydrous per serving(grams):\n"))
Taurine = int(input("Amount of Taurine per serving(grams):\n"))
Creatine_HCL = int(input("Amount of Creatine_HCL per serving(grams):\n"))
L_Theanine = float(input("Amount of L-Theanine per serving(milligrams):\n"))/1000
L_Tyrosine = int(input("Amount of L-Tyrosine per serving(grams):\n"))
Sodium_Bicarbonate = float(input("Amount of Sodium_Bicarbonate per serving(milligrams):\n"))/1000
#Mix Total
Mix_Total = float(L_Citrulline_Mallate + Beta_Alanine + Caffeine_Anhydrous + Betaine_Anhydrous + Taurine + Creatine_HCL + L_Theanine + L_Tyrosine + Sodium_Bicarbonate)* servings
#Servings Total
Serving_Total = float(L_Citrulline_Mallate + Beta_Alanine + Caffeine_Anhydrous + Betaine_Anhydrous + Taurine + Creatine_HCL + L_Theanine + L_Tyrosine + Sodium_Bicarbonate)
#Flavor
Flavor_Weight = float(Serving_Total)-(Serving_Total*.8)
Flavor_Weight_Total = float(Flavor_Weight * servings)
Grand_Serving_Total_Weight = float(Flavor_Weight + Serving_Total)
Grand_Weight_Mix_Total = float(Grand_Serving_Total_Weight * servings)
#while
while (Grand_Weight_Mix_Total > 400):
        servings = servings - 1

        print('Servings loop value', servings)
#Print 
print (f'Customer: {customerName}')
print (f'Mix Name: {mixName}')
print (f'Servings: {servings}')
print (f'L-Citrulline Malate: {L_Citrulline_Mallate}')
print (f'Beta Alanine: {Beta_Alanine}')
print (f'Caffeine Anhydrous: {Caffeine_Anhydrous}')
print (f'Betaine Anhydrous: {Betaine_Anhydrous}')
print (f'Taurine: {Taurine}')
print (f'Creatine HCL: {Creatine_HCL}')
print (f'L-Theanine: {L_Theanine}')
print (f'L-Tryosine: {L_Tyrosine}')
print (f'Sodium Bicarbonate: {Sodium_Bicarbonate}')
#Calculate total grams needed for each ingredent
Total_L_Citrulline_Mallate = int(L_Citrulline_Mallate * servings)
Total_Beta_Alanine = int(Beta_Alanine * servings)
Total_Caffeine_Anhydrous = float(Caffeine_Anhydrous * servings)
Total_Betaine_Anhydrous = int(Betaine_Anhydrous * servings)
Total_Taurine = int(Taurine * servings)
Total_Creatine_HCL = int(Creatine_HCL * servings)
Total_L_Theanine = float(L_Theanine * servings)
Total_L_Tyrosine = int(L_Tyrosine * servings)
Total_Sodium_Bicarbonate = float(Sodium_Bicarbonate * servings)
#Print total grams of each ingredient
print("L-Citrulline Mallate Total Grams:", Total_L_Citrulline_Mallate)
print("Beta Alanine Total Grams:", Total_Beta_Alanine)
print("Caffeine Anhydrous Total Grams:", Total_Caffeine_Anhydrous)
print("Betaine Anhydrous Total Grams:", Total_Betaine_Anhydrous)
print("Taurine Total Grams:", Total_Taurine)
print("Creatine HCL Total Grams:", Total_Creatine_HCL)
print("L-Theanine Total Grams:", Total_L_Theanine)
print("L-Tyrosine Total Grams:", Total_L_Tyrosine)
print("Sodium Bicarbonate Total Grams:", Total_Sodium_Bicarbonate)
print("Mix serving weight (flavor not included): ", Serving_Total)
print("Mix total wight: ", Mix_Total)
print("Flavor Weight", Flavor_Weight)
print("Flavor Weight Total", Flavor_Weight_Total)
print("Grand Total Serving Weight", Grand_Serving_Total_Weight)
print("Grand Total Mix Weight", Grand_Weight_Mix_Total)

