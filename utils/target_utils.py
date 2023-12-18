def target_encoding(row):
    if row['hotel_id'] == 1 or row['hotel_id'] == 2 or row['hotel_id'] == 3 or row['hotel_id'] == 4:
        val = 1 #Economy
    elif row['hotel_id'] == 5 or row['hotel_id'] == 6 or row['hotel_id'] == 7 or row['hotel_id'] == 8:
        val = 2 # Standart
    else:
        val = 3 # Luxury
    return val
