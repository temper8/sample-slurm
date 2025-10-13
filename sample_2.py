from simple_slurm import Slurm
NT= 10
task_list = [ f'task_{id}' for id in range(NT)]
slurm = Slurm(
    array=range(NT),
    cpus_per_task=1,
    job_name='demo_name',
    #dependency=dict(after=65541, afterok=34987),
    output=f'{Slurm.JOB_ARRAY_MASTER_ID}_{Slurm.JOB_ARRAY_ID}.out',
)
slurm.sbatch(f'echo {task_list[Slurm.SLURM_ARRAY_TASK_ID]}')