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
print(data)

print("Attempt to implement the main app logic")