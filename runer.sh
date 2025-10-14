hostname
echo "Task $1, job_dir $2."
tasks_array=$2 'task_array.txt'
task_dir=$2 '/' $(awk -v ArrayTaskID=$1 '$1==ArrayTaskID {print $2}' $tasks_array)
echo "This is array task $1, the work_dir is $task_dir."
START=$(date +%s)
echo "Start : $START"
sleep 30
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "End : $END"
echo "It took $DIFF seconds"