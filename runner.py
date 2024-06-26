import subprocess
import csv
import time

postfix = '_moved_disk'

def run_and_time(program_name):
    p = subprocess.run(["python", program_name + ".py", postfix], capture_output=True, text=True)
    if p.stderr:
        print(p.stderr)
    return float(p.stdout)

num_trials = 30

programs = ['unnested', 'unnested_with_transform', 'nested']

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(programs)
    
    for trial in range(num_trials):
        print("Running trial", trial)
        row = []    
        for program in programs:
            count = run_and_time(program)
            print("Running program", program, "took", count)
            row.append(count)
        writer.writerow([str(a) for a in row])
