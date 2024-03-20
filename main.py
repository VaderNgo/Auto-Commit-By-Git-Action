from datetime import datetime

filename = 'example.txt'

with open(filename, 'a') as f:
    now = datetime.now()
    f.write(f'Updating: {now.strftime("%Y-%m-%d")}\n')
