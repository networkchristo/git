# # # echo "File Name : $0"
# # # echo "First Parameter : $1"
# # # echo "Second Parameter : $2"
# # # echo "Quoted Values : $@"
# # # echo "Quoted Values : $*"
# # # echo "Total number of Parameters : $#"

# # for token in $*
# # do
# #     echo $token
# # done

# NAME[0]="Zara"
# NAME[1]="Qadir"
# NAME[2]="Mahnaz"
# NAME[3]="Ayan"
# NAME[4]="Daisy"
# echo "First Index: ${NAME[0]}"
# echo "Second Index: ${NAME[1]}"

NAME[0]="Zara"
NAME[1]="Qadir"
NAME[2]="Mahnaz"
NAME[3]="Ayan"
NAME[4]="Daisy"

# echo ${NAME[@]}

val = 'expr 2 + 2'
echo "Total value : $val"