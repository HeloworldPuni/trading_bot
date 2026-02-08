
import os

input_path = 'data/BTC_USDT_2020_2026.csv'
output_path = 'data/BTC_RECENT.csv'

if not os.path.exists(input_path):
    print(f"Input file {input_path} not found.")
    exit(1)

with open(input_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

if len(lines) < 2:
    print("Not enough data.")
    exit(1)

header = lines[0]
data_lines = lines[1:]

# Get last 10,000 lines
recent_lines = data_lines[-10000:]

with open(output_path, 'w', encoding='utf-8', newline='') as f:
    f.write(header)
    for line in recent_lines:
        if line.strip():
            f.write(line.strip() + '\n')

print(f"Successfully wrote {len(recent_lines)} lines (+header) to {output_path}")
