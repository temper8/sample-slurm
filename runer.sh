hostname
tasks_array=task_array.txt
task_dir=$(awk -v ArrayTaskID=$1 '$1==ArrayTaskID {print $2}' $tasks_array)
echo "This is array task $1, the work_dir is $task_dir."
echo "Start date: $(date)"
sleep 30
echo "End date: $(date)"