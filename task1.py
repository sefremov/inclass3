def read_file(file_name):
    data = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        f.readline()
        for line in f:
            parts = line.split(',')
            date = parts[0]
            row = [file_name, int(parts[1]), float(parts[10])]
            if date not in data:
                data[date] = [row]
            else:
                data[date].append(row)
    return data


data = read_file('data/KCLT.csv')
print(data)
