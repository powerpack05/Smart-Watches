# Importing the required Libraries
import subprocess
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import os

print("\n\n*****************SMART WATCH ANALYSIS************************\n\n")

base_dir = os.path.abspath(os.path.dirname(__name__))
print("base dir directory",base_dir)
joining_path = os.path.join(base_dir,'static','excel_files')
print("joining path",joining_path)

# reading the brands sheet
brands_data = pd.read_excel(os.path.join(joining_path,'brands.xlsx'))
print("--------------------Smart Watch Brands in India-----------------------\n")
print(brands_data.to_string(index=False))

def refresh_screen():
    # clear the screen
    subprocess.run('cls',shell=True)


while True:
    print("\n")
    choice = int(input("Enter the brand :-"))
    print("\n----------------------------------------------------------------------\n")
    if choice == 1:

        apple_data = pd.read_excel(os.path.join(joining_path,'apple.xlsx'))
        print("\nApple Smart Watch--->\n")
        print(apple_data.to_string(index=False))

        print("\n1.Scatter Plot\n2.Bar Plot")
        analysis = int(input("\nEnter the value:-"))

        if analysis == 1:
            apple_data.plot(kind='scatter',x='Total Steps',y='Calories',title='Relation between Calories and Total Steps',color='blue')
            plt.show()
            break

        elif analysis == 2:
            apple_data.plot(kind='bar',x='Total Steps',y='Calories',title='Relation between Calories and Total Steps',color='red')
            plt.show()
            break
        else:
            print("No Plot")
            refresh_screen()

    elif choice == 2:

        boat_data = pd.read_excel(os.path.join(joining_path,'boat.xlsx'))
        print("\nBoat Smart Watch--->\n")
        print(boat_data.to_string(index=False))

        print("\n1.Scatter Plot\n2.Bar Plot")
        analysis = int(input("\nEnter the value:-"))

        if analysis == 1:
            boat_data.plot(kind='scatter',x='Total Steps',y='Calories',title='Relation between Calories and Total Steps',color='green')
            plt.show()
            break

        elif analysis == 2:
            boat_data.plot(kind='bar',x='Total Steps',y='Calories',title='Relation between Calories and Total Steps',color='red')
            plt.show()
            break
        else:
            print("No plot")
            refresh_screen()

    elif choice == 3:

        samsung_data = pd.read_excel(os.path.join(joining_path,'samsung.xlsx'))
        print("\nSamsung GalaSmart Watch--->\n")
        print(samsung_data.to_string(index=False))

        print("\n1.Scatter Plot\n2.Bar Plot")
        analysis = int(input("\nEnter the value:-"))

        if analysis == 1:
            samsung_data.plot(kind='scatter',x='Total Steps',y='Calories',title='Relation between Calories and Total Steps',color='red')
            plt.show()
            break
        elif analysis == 2:
            samsung_data.plot(kind='bar',x='Total Steps',y='Calories',title='Relation between Calories and Total Steps',color='green')
            plt.show()
            break
        else:
            print("No plot")
            refresh_screen()

    elif choice == 4:

        oneplus_data = pd.read_excel(os.path.join(joining_path,'oneplus.xlsx'))
        print("\nHonor Brand Smart Watch--->\n")
        print(oneplus_data.to_string(index=False))

        print("\n1.Scatter Plot\n2.Bar Plot")
        analysis = int(input("\nEnter the value:-"))

        if analysis == 1:
            oneplus_data.plot(kind='scatter',x='Total Steps',y='Calories',title='Relation between Calories and Total Steps',color='orange')
            plt.show()
            break
        elif analysis == 2:
            oneplus_data.plot(kind='bar',x='Total Steps',y='Calories',title='Relation between Calories and Total Steps',color='red')
            plt.show()
            break
        else:
            print("No plot")
            refresh_screen()

    elif choice == 5:

        noise_data = pd.read_excel(os.path.join(joining_path,'noise.xlsx'))
        print("\nNoise Colorfit Smart Watch--->\n")
        print(noise_data.to_string(index=False))

        print("\n1.Scatter Plot\n2.Bar Plot")
        analysis = int(input("\nEnter the value:-"))

        if analysis == 1:
            noise_data.plot(kind='scatter',x='Total Steps',y='Calories',title='Relation between Calories and Total Steps',color='red')
            plt.show()
            break
        elif analysis == 2:
            noise_data.plot(kind='bar',x='Total Steps',y='Calories',title='Relation between Calories and Total Steps',color='pink')
            plt.show()
            break
        else:
            print("No plot")
            refresh_screen()

    elif choice == 0:
        exit()

