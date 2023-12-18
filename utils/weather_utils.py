def weather_encoding(row):
    if row['country'] == 'Finland':
        val = 1
    elif row['country'] == 'Norway':
        val = 2
    else:
        val = 3
    return val
