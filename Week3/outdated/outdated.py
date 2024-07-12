def main():
    months = {
        "January"   : "1"  ,
        "February"  : "2"  ,
        "March"     : "3"  ,
        "April"     : "4"  ,
        "May"       : "5"  ,
        "June"      : "6"  ,
        "July"      : "7"  ,
        "August"    : "8"  ,
        "September" : "9"  ,
        "October"   : "10" ,
        "November"  : "11" ,
        "December"  : "12"
    }

    adj_date = None

    while adj_date == None:
        date = input("Date: ")

        slash_split = date.strip().split("/")
        space_split = date.strip().replace(",", "").split()

        if len(slash_split) == 3:
            adj_date = validate_date(slash_split)
        elif len(space_split) == 3:
            adj_date = validate_date(space_split)
    
    print(f"{adj_date[0]}-{adj_date[1]}-{adj_date[2]}")
        

def validate_date(date):
    try:
        year = date[2]
        month = date[0]
        day = date[1]

        if int(day) > 31 or int(month) > 12:
            raise ValueError

    except ValueError:
        print("Date out of range.")
    else:
        adj_date = [year.zfill(4), month.zfill(2), day.zfill(2)]
        return adj_date

if __name__ == "__main__":
    main()
