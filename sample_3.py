from simple_slurm import Slurm
NT= 10
slurm = Slurm(
    cpus_per_task=1,
    job_name='sample_3',
    #dependency=dict(after=65541, afterok=34987),
    output=f'{Slurm.JOB_ARRAY_MASTER_ID}_{Slurm.JOB_ARRAY_ID}.out',
)

print(slurm)
# Print to a file a message that includes the current $SLURM_ARRAY_TASK_ID and work_dir
for id in range(NT):
    slurm.sbatch(f'./demo.sh {id} task_{id}')

slurm.squeue.update_squeue()  # Fetch latest job data
slurm.squeue.display_jobs()

# Get the jobs as a dictionary
jobs = slurm.squeue.jobs

for job_id, job in jobs.items():
    print(job)