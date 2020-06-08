# Load in exercises
arr=()
N_tot=0
while IFS= read -r line; do
  arr+=("$line")
  ((N_tot++))
done < ../resources/abs_exercises.txt
echo "Total exercises: $N_tot"

for (( j=0; j<N_tot; j++))
do
  string=`echo ${arr[$j]} | sed 's/ /_/g'`
  say ${arr[$j]} -o ./mp3_bash/${string}
done
