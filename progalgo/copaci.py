max_area=0
max_rectangle = tuple()
cnt = 0
def is_inside_area(bottom_left, top_right, c):
    if bottom_left[0] < c[0] < top_right[0] and bottom_left[1] < c[1] < top_right[1]:
        return True
    return False

def find_area(bottom_left, top_right):
        global cnt
        cnt+=1
        global max_area,max_rectangle
        for c in copaci:
            if is_inside_area(bottom_left,top_right,c) == True:
                #split #verticala
                find_area(bottom_left,tuple([c[0],top_right[1]]))
                find_area(tuple([c[0],bottom_left[1]]), top_right)
                #orizontala
                find_area(bottom_left,tuple([top_right[0],c[1]]))
                find_area(tuple([bottom_left[0],c[1]]),top_right)
                break
        else:
            #aria
            area = (bottom_left[0]-top_right[0])*(bottom_left[1]-top_right[1])
            if area > max_area:
                max_area = area
                max_rectangle = [bottom_left,top_right]



with open("tis.txt","r") as f:
    text = [t.strip().split(' ') for t in f.readlines()]
    print(text)
    dreptunghi = [ tuple([int(x) for x in text[0]]), tuple(int(x) for x in text[1])]
    copaci = [ tuple([int(x) for x in t]) for t in text[2:]]
    find_area(dreptunghi[0], dreptunghi[1])
   # print (dreptunghi,copaci)
    print(max_rectangle,max_area,cnt)
