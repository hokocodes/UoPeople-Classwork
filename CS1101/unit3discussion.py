

def function(var, tree):
    if var < 100:
        if tree == True:
            print('You liked the song.')
        else:
            print('You need to plant a tree.')
    else:
        print('You disliked the song.')

def bum(var, tree):
    if var < 100 and tree == True:
        print('You liked the song.')
        print('You need to plant a tree.')
    else:
        print('You disliked the song.')
    
function(1, True)
function(111, False)
bum(1, True)
