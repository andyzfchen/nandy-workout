voice_parallel () {
  say $1 &
}

exercise_start () {
  voice_parallel "$1"
  sleep 5
  voice_parallel "Begin."
}

countdown () {
  sleep $(($1-3))
  for (( i=3; i>0; i--))
  do
    echo "$i"
    voice_parallel "$i"
    sleep 1
  done
}

next_exercise () {
  voice_parallel "Next exercise. $1"
}

exercise () {
  sleep 20
  #sleep 5
}

breaktime () {
  voice_parallel "Take a 30 second break."
  sleep 20
  #sleep 5
}

shuffle() {
  #local i tmp size max rand
  local i tmp max rand

  arr1=($(seq 0 $1))

  # $RANDOM % (i+1) is biased because of the limited range of $RANDOM
  # Compensate by using a range which is a multiple of the array size.
  #size=${#array[*]}
  #max=$(( 32768 / size * size ))
  max=$(( 32768 / $1 * $1 ))

  for ((i=$1-1; i>0; i--))
  do
    while (( (rand=$RANDOM) >= max ))
    do
      :
    done
    rand=$(( rand % (i+1) ))
    tmp=${arr1[i]}
    arr1[i]=${arr1[rand]}
    arr1[rand]=$tmp
  done
}


time=$1
hard=$2


# Starting sequence
echo "App is starting."
echo "Duration: $time mins"
echo "Hardcore: $hard"

say "Starting abdominal exercises."
say "$time minutes."
if $hard
then
  say "Hard mode."
else
  say "Easy mode."
fi
sleep 2
echo


# Load in exercises
arr=()
N_tot=0
while IFS= read -r line; do
  arr+=("$line")
  ((N_tot++))
done < abs_exercises.txt
echo "Total possible exercises: $N_tot"

shuffle $N_tot

N_exercise=$(($1*2))
echo "Total session exercises: $N_exercise"
echo



# Workout sequence
for (( j=0; j<N_exercise; j++))
do
  if [ $((j % 6)) -eq 5 ]
  then
    echo "break time"
    breaktime

    if [ $((j+1)) -eq $N_exercise ]
    then
      :
    else
      echo "Next exercise: ${arr[${arr1[$((j+1))]}]}" 
      next_exercise "${arr[${arr1[$((j+1))]}]}"
    fi

    countdown 10
  else
    echo "Current exercise: ${arr[${arr1[$j]}]}"
    exercise_start "${arr[${arr1[$j]}]}"
    exercise

    if [ $((j+1)) -eq $N_exercise ]
    then
      :
    elif [ $((j % 6 + 1)) -eq 5 ] 
    then
      echo "Next exercise: break time"
      next_exercise "break time"
    else
      echo "Next exercise: ${arr[${arr1[$((j+1))]}]}" 
      next_exercise "${arr[${arr1[$((j+1))]}]}"
    fi

    countdown 10
  fi
done

echo "Exercise complete."
say "Abdominal exercises completed."

