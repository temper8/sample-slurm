import time
from simple_slurm import Slurm
NT= 10
task_list = [ f'task_{id}' for id in range(NT)]
with open("task_array.txt", "w") as f:
    for id in range(NT):
        f.write(f'{id}    task_{id}\n')

slurm = Slurm(
    array=range(NT),
    cpus_per_task=1,
    job_name='sample_2',
    #dependency=dict(after=65541, afterok=34987),
    output=f'{Slurm.JOB_ARRAY_MASTER_ID}_{Slurm.JOB_ARRAY_ID}.out',
)

# Specify the path to the config file
slurm.add_cmd("tasks_array=task_array.txt")
# Extract the sample name for the current $SLURM_ARRAY_TASK_ID
slurm.add_cmd("work_dir=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $2}' $tasks_array)")
slurm.add_cmd('echo "Environment setup complete"')
print(slurm)
# Print to a file a message that includes the current $SLURM_ARRAY_TASK_ID and work_dir
slurm.sbatch('./demo.sh ${SLURM_ARRAY_TASK_ID} ${work_dir}')

slurm.squeue.update_squeue()  # Fetch latest job data
slurm.squeue.display_jobs()

# Get the jobs as a dictionary
jobs = slurm.squeue.jobs

for job_id, job in jobs.items():
    print(job_id)

while True:
    time.sleep(10)
    slurm.squeue.update_squeue()
    num_jobs= len(slurm.squeue.jobs)
    print(f"Jobs {num_jobs}")
    if num_jobs == 0: break