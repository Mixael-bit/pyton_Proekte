print (" Hallo beim Temparatur converter!")

fahrenheit = input("Bitte gib die Temperatur in Fahrenheit an:")
print ("Du hast " +fahrenheit + "° Fahrenheit angegeben.")

fahrenheitFloat = float(fahrenheit)
celsius = (fahrenheitFloat -32) * 5/9
print ("%s° Fahrenheit sind %0,2f° Celsius" %(fahrenheit, celsius))