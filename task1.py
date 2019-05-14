def read_file(file_name, abbr, data):
    with open(file_name, 'r', encoding='utf-8') as f:
        f.readline()
        for line in f:
            parts = line.split(',')
            date = parts[0]
            row = [abbr, int(parts[1]), float(parts[10])]
            if date not in data:
                data[date] = [row]
            else:
                data[date].append(row)


def read_all_data():
    import os
    data = {}
    for file in os.scandir('data'):
        if file.name.startswith('K'):
            abbr = os.path.splitext(file.name)[0]
            read_file(file.path, abbr, data)
    return data


data = read_all_data()
while True:
    date = input("Enter date: ")
    if not date:
        break
    if date in data:
        for entry in data[date]:
            print(f'{entry[0]} - {entry[1]}')
    else:
        print("No information found for the given date")
print(data)

print("Attempt to implement the main app logic")