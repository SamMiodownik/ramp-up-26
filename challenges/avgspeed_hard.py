def ave_speed(uphill_time, uphill_speed, downhill_speed):
    hill_in_miles = uphill_time * uphill_speed / 60
    downhill_time = hill_in_miles / downhill_speed * 60
    total_time = uphill_time + downhill_time
    return int(((uphill_speed * uphill_time) + (downhill_speed * downhill_time)) / total_time)

def main():
    print(ave_speed(18, 20, 60), "\tShould be 30")
    print(ave_speed(30, 10, 30), "\tShould be 15")
    print(ave_speed(30, 8, 24), "\tShould be 12")

if __name__ == "__main__":
    main()