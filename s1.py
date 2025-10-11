from simple_slurm import Slurm

slurm = Slurm(
    array=range(3, 12),
    cpus_per_task=2,
    job_name='demo_name',
    dependency=dict(after=65541, afterok=34987),
    output=f'{Slurm.JOB_ARRAY_MASTER_ID}_{Slurm.JOB_ARRAY_ID}.out',
)
slurm.sbatch('echo ' + Slurm.SLURM_ARRAY_TASK_ID)