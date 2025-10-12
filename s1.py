from simple_slurm import Slurm

slurm = Slurm(
    array=range(1, 11),
    cpus_per_task=2,
    job_name='demo_name',
    #dependency=dict(after=65541, afterok=34987),
    output=f'{Slurm.JOB_ARRAY_MASTER_ID}_{Slurm.JOB_ARRAY_ID}.out',
)
slurm.sbatch(f'echo task_No_{Slurm.SLURM_ARRAY_TASK_ID}')