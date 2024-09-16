import pandas as pd

df = pd.read_csv("data/italian_gp_2024_fastestlaps.csv")

def get_driver_with_highest_avg_speed(car_name):

    car_df = df[df['Car'].str.lower()  == car_name.lower()]
    if car_df.empty:
        print(f"No fastest lap data available for {car_name}.")
        return None, None, None
    else:
        highest_avg_speed_row = car_df.loc[car_df['avg_speed'].idxmax()]
        driver_name = highest_avg_speed_row['Driver']
        lap_number = highest_avg_speed_row['Lap']
        top_speed =  highest_avg_speed_row['avg_speed']
        return driver_name, lap_number, top_speed


if __name__ == "__main__":
    # team_name = input("""Enter the team name out of the list['McLaren Mercedes', 'Mercedes', 'Red Bull Racing Honda RBPT',
    #    'Aston Martin Aramco Mercedes', 'Ferrari', 'Haas Ferrari',
    #    'Kick Sauber Ferrari', 'Williams Mercedes', 'Alpine Renault',
    #    'RB Honda RBPT']:""")
    team_name = "Mercedes"
    driver, lap, speed = get_driver_with_highest_avg_speed(team_name)
    print(f"The fastest lap for {team_name} was set by {driver} on lap {lap} with speed of {speed}.")
