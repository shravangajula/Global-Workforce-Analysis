import os
import matplotlib.pyplot as plt
import datetime

logs_dir = 'daily_logs'
dates = []
wpms = []
accuracies = []

for log_file in os.listdir(logs_dir):
    if log_file.endswith('.md'):
        with open(os.path.join(logs_dir, log_file), 'r') as file:
            lines = file.readlines()
            date_str = lines[0].split(': ')[1].strip()
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            dates.append(date)
            wpms.append(int(lines[2].split(': ')[1].strip()))
            accuracies.append(float(lines[3].split(': ')[1].strip().strip('%')))

plt.figure(figsize=(10, 5))
plt.plot(dates, wpms, label='WPM')
plt.plot(dates, accuracies, label='Accuracy')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.title('Typing Progress')
plt.savefig('charts/typing_progress.png')
