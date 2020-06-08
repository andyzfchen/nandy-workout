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
  local i tmp max rand

  arr1=($(seq 0 $1))

  # $RANDOM % (i+1) is biased because of the limited range of $RANDOM
  # Compensate by using a range which is a multiple of the array size.
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


nSet=$1
type=$2


# Starting sequence
echo "App is starting."
echo "Duration: $nSet sets"

say "Starting strength exercises."
say "$nSet sets."
sleep 2
echo


# Load in exercises
arr=()
nLevel=(0 0 0)
nTot=0
level=0
while IFS= read -r line; do
  if [ -z "$line" ]
  then
    ((level++))
  else
    arr+=("$line")
    ((nLevel[$level]++))
    ((nTot++))
  fi
done < ../resources/${type}_exercises.txt
echo "Easy exercises: ${nLevel[0]}"
echo "Medium exercises: ${nLevel[1]}"
echo "Hard exercises: ${nLevel[2]}"
echo "Total possible exercises: $nTot"

shuffle $nTot

N_exercise=$(($1*4))
echo

exit

# Workout sequence
for (( j=0; j<N_exercise; j++))
do
  if [ $((j % 4)) -eq 0 ]
  then

  elif [ $((j % 4)) -eq 1 ]
  then

  elif [ $((j % 4)) -eq 2 ]
  then
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
  elif [ $((j % 4)) -eq 3 ]
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
  then
  else
    :
  fi
done

echo "Exercise complete."
say "Congratulations! You have finished abdominal exercises."

