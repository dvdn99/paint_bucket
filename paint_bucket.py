
#paint bucket simulation

T = [[11, 12, 5, 2], [11, 6,11,11], [11, 11, 12, 5], [12,15,8,6]]


print(T[0])
print(T[1])
print(T[2])
print(T[3])
print("\n")

def paint_bucket(x,y,old_color,new_color,figure):
    fig_width = len(figure)
    fig_height = len(figure[0])
    
    #if color in index is not the selected, stop
    if figure[x][y] != old_color:
        return 
    
    #checking for correct indexes
    if x < 0 or y < 0:
        return
    
    if x > fig_width or y > fig_height:
        return 
    
    #if color is already new one, stop
    if figure[x][y] == new_color:
        return
    
    #if out of figure stop
    if figure[x][y] == -1:
        return
    
    #if color in index is old color, paint it
    elif figure[x][y] == old_color:
        figure[x][y] = new_color
    
    #making a list o tuples with neighbors indexes
    neighbors = [(x-1,y),(x+1,y),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1)]
    
    #looping over all neighbors and calling recursively
    for n in neighbors:
        if 0 <= n[0] <= fig_width-1 and 0 <= n[1] <= fig_height-1:
            paint_bucket(n[0],n[1],old_color,new_color,figure)
            
    return

paint_bucket(0,0,11,0,T)


print(T[0])
print(T[1])
print(T[2])
print(T[3])
       




