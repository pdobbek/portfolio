import csv
from gpu import GPU


gpus = list()
kwh_price = 0.1437
with open('gpu_input.csv', newline='') as in_file:
    reader = csv.reader(in_file, delimiter=',')
    for row in reader:
        if "model" not in row[0]:
            name = row[0]
            mhs = float(row[1])
            power = int(row[2])
            price = float(row[3])
            gpu = GPU(name=name, mhs=mhs, power=power, price=price, kwh_price_gbp=kwh_price)
            gpus.append(gpu)

columns = ['model', 'mhs', 'power', 'price', 'epp', 'roi']
rows = list()
for gpu in gpus:
    line = [gpu.name, str(gpu.mhs), str(gpu.power), str(gpu.price), str(gpu.epp), str(gpu.roi)]
    rows.append(line)

with open('gpu_output.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(columns)
    writer.writerows(rows)
