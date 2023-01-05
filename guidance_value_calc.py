import pandas as pd

def hobli_guidance_value(hobli_name, year):
    df = pd.read_csv("hoblis.csv")

    df = df[df['hobli'].str.contains(hobli_name)]

    built_up = df['a'] + df['b']*year
    guidance_value_pandas = df['x'] + df['y']*year + df['z']*built_up
    guidance_value = round(guidance_value_pandas.values[0])
    guidance_value_sqft = round(guidance_value/10.764)

    print(f"{guidance_value} is the value per sq mt")
    print(f"{guidance_value_sqft} is the value per sq ft")
    return

def ward_guidance_value(ward_name, year):
    df = pd.read_csv("wards.csv")

    df = df[df['ward'].str.contains(ward_name)]

    built_up = df['a'] + df['b']*year
    guidance_value_pandas = df['x'] + df['y']*year + df['z']*built_up
    guidance_value = round(guidance_value_pandas.values[0])
    guidance_value_sqft = round(guidance_value/10.764)

    print(f"{guidance_value} is the value per sq mt")
    print(f"{guidance_value_sqft} is the value per sq ft")
    return

def main():

    val = input("Enter : hobli or ward?: ")
    if val == "hobli":
        hobli_name = input("Enter hobli name: ")
        year = int(input("Enter year: "))
        hobli_guidance_value(hobli_name, year)
    else :
        ward_name = input("Enter ward name: ")
        year = int(input("Enter year: "))
        ward_guidance_value(ward_name, year)
    return

if __name__=="__main__":
    main()