from datetime import datetime
import os
import pathlib
import time
from simple_slurm import Slurm

now = datetime.now()
job_dir = pathlib.Path('results') / now.strftime("%Y-%m-%d_%H-%M-%S")
job_dir.mkdir()
NT= 10
tasks = [ dict(id= id, name= f'task_{id}' ) for id in range(NT)]
with open(job_dir / "task_array.txt", "w") as f:
    for id in range(NT):
        f.write(f'{id}    task_{id}\n')

slurm = Slurm(
    array=range(NT),
    cpus_per_task=1,
    job_name='sample_4',
    #dependency=dict(after=65541, afterok=34987),
    output=(job_dir / f'task_{Slurm.JOB_ARRAY_ID}.out').as_posix(),
)

print(slurm)
# Print to a file a message that includes the current $SLURM_ARRAY_TASK_ID and work_dir
slurm.sbatch("./runer.sh ${SLURM_ARRAY_TASK_ID} " +  job_dir.as_posix())

slurm.squeue.update_squeue()  # Fetch latest job data
slurm.squeue.display_jobs()

# Get the jobs as a dictionary
jobs = slurm.squeue.jobs

for job_id, job in jobs.items():
    print(job_id)

while True:
    slurm.squeue.update_squeue()
    num_jobs= len(slurm.squeue.jobs)
    print(f"Jobs {num_jobs}")
    if num_jobs == 0: break
    time.sleep(10)


for task in tasks:
    id = task['id']
    with open(job_dir / f"time_task_{id}.txt", "r") as f:
        task['time'] = int(f.readline())

with open(job_dir / "time_done_list.txt", "w") as f:
    for task in tasks:
        f.write(f"{task['id']} {task['name']} {task['time']}\n")