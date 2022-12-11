# who wins ?
# what's the amount of points given ?
# calculate the points for each round, sum them at the end
# score for shape, score for outcome
# get elements, calculate score for shape, see who won, calculate score for outcome and sum

# three dimensions: my shape, opponent shape, outcome (rock beats scissors, paper beats rock, scissors beats paper, same shape = draw)
rock_paper_scissors_list_opponent=['A','B','C'] # [r,p,s]
rock_paper_scissors_list_mine=['X','Y','Z'] # [r,p,s]

# (opponent, mine); index_opponent-index_mine:
# 0 : same, draw
# -1 : (r,p) - win; (p,s) - win;
# -2 : (r,s) - loss;
# 1 : (p,r) - loss; (s,p) - loss
# 2 : (s,r) - win

# (opponent, mine); index_opponent-index_mine+3:
# 3 : same, draw
# 1 : (r,s) - loss;
# 4 : (p,r) - loss; (s,p) - loss
# 2 : (r,p) - win; (p,s) - win;
# 5 : (s,r) - win

# (opponent, mine); (index_opponent-index_mine)%3:
# 0 : same, draw
# 2 : (r,p) - win; (p,s) - win;
# 1 : (r,s) - loss;
# 1 : (p,r) - loss; (s,p) - loss
# 2 : (s,r) - win

# index_opponent-index_mine=r <-> index_mine=index_opponent-r; BUT INDEX_MIN < 3, so there's only possible solution

def get_score_from_shape(my_shape):
    if my_shape=='X': # rock
        return 1
    elif my_shape=='Y': # paper
        return 2
    elif my_shape=='Z': # scissors
        return 3
    else:
        print('I dont know whats this weird shape ',my_shape)

def get_score_from_shape_index(my_shape):
    return rock_paper_scissors_list_mine.index(my_shape)+1

def get_score_from_outcome(opponent_shape,my_shape):
    if opponent_shape=='A' and my_shape=='X':
        return 3
    elif opponent_shape=='B' and my_shape=='Y':
        return 3
    elif opponent_shape=='C' and my_shape=='Z':
        return 3            
    elif opponent_shape=='A' and my_shape=='Y': # rock vs. paper - I win
        return 6
    elif opponent_shape=='B' and my_shape=='Z': # paper vs. scissors - I win
        return 6
    elif opponent_shape=='C' and my_shape=='X': # scissors vs. rock - I win
        return 6
    else:
        return 0

def get_score_from_outcome_index(opponent_shape,my_shape):
    val=(rock_paper_scissors_list_opponent.index(opponent_shape)-rock_paper_scissors_list_mine.index(my_shape))%3
    if val==0:
        return 3
    elif val==1:
        return 0
    elif val==2:
        return 6

def get_shape_from_opponent_and_outcome(opponent_shape,outcome): # this function is damn wrong
    if opponent_shape=='A' and outcome=='X': # if opponent plays rock and I need to lose
        return 'Y'
    elif opponent_shape=='B' and outcome=='Y': # if opponent plays paper and I need to draw
        return 'Y'
    elif opponent_shape=='C' and outcome=='Z': # if opponent plays scissors and I need to win
        return 'Y'            
    elif opponent_shape=='A' and outcome=='Y': # if opponent plays rock and I need to draw
        return 'X'
    elif opponent_shape=='B' and outcome=='Z': # if opponent plays paper and I need to lose
        return 'X'
    elif opponent_shape=='C' and outcome=='X': # if opponent plays scissors and I need to win
        return 'X'
    else:
        return 'Z'

def get_shape_from_opponent_and_outcome_index(opponent_shape,outcome):
    if outcome=='X': # loss (val: -2, 1, for index_mine=index_opponent-val, index_mine < 3)
        if rock_paper_scissors_list_opponent.index(opponent_shape)+2 < 3:
            index=rock_paper_scissors_list_opponent.index(opponent_shape)+2
        else:
            index=rock_paper_scissors_list_opponent.index(opponent_shape)-1
    elif outcome=='Y':
        index=rock_paper_scissors_list_opponent.index(opponent_shape)
    elif outcome=='Z': # win (val: -1,2 for index_min=index_opponent-val, index_mine < 3)
        if rock_paper_scissors_list_opponent.index(opponent_shape)+1 < 3:
            index=rock_paper_scissors_list_opponent.index(opponent_shape)+1
        else:
            index=rock_paper_scissors_list_opponent.index(opponent_shape)-2        
    
    return rock_paper_scissors_list_mine[index]
    

# part 1 - my shape defined, opponent shape defined, get score from shape, get score from outcome
f=open('input_2_12')
list_lines=f.readlines()
list_scores_part1=[]
list_scores_part1_index=[]
list_scores_part2=[]
list_scores_part2_index=[]

for line in list_lines:
    opponent_shape,my_shape=line.strip("\n").split(" ")
    list_scores_part1.append(get_score_from_shape(my_shape)+get_score_from_outcome(opponent_shape,my_shape))
    list_scores_part1_index.append(get_score_from_shape_index(my_shape)+get_score_from_outcome_index(opponent_shape,my_shape))
    outcome=my_shape

    my_shape_from_outcome=get_shape_from_opponent_and_outcome(opponent_shape,outcome)
    my_shape_from_outcome_index=get_shape_from_opponent_and_outcome_index(opponent_shape,outcome) # the problem comes from the difference in these two functions

    print(opponent_shape,outcome,my_shape_from_outcome,my_shape_from_outcome_index)
    list_scores_part2.append(get_score_from_shape(my_shape_from_outcome)+get_score_from_outcome(opponent_shape,my_shape_from_outcome))
    list_scores_part2_index.append(get_score_from_shape_index(my_shape_from_outcome_index)+get_score_from_outcome_index(opponent_shape,my_shape_from_outcome_index))

print(sum(list_scores_part1))
print(sum(list_scores_part1_index))
print(sum(list_scores_part2))
print(sum(list_scores_part2_index))

# part 2 - opponent shape defined, outcome (and outcome score) defined, get shape from opponent shape and outcome -> get score from that shape and sum