'''
8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot
'''

a=int(input("Enter temperature :"))

if a<0 :
   print("Weather Condition : Freezing")
elif 0<=a<21 :
   print("Weather Condition : Cold")
elif 20<a<36 :
   print("Weather Condition : Warm")
else :
   print("Weather Condition : Hot")