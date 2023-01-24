import tkinter
import random

def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key
    key = ""
def main_proc():
    if key == "1":
        draw_map(maze)
    if key == "2":
        draw_map(maze2)
    root.after(1, main_proc)
    if key == "space":
        draw_map(random.choice(maps))
    if key == "3":
        draw_map(random_map_maker())
        
def draw_map(map):
    canvas.delete("all")
    for y in range(7):
        for x in range(10):
            if map[y][x] == 1:
                canvas.create_rectangle(x * 80, y * 80, x * 80 + 80, y * 80 + 80, fill="gray")
def random_map_maker():
    freemap = [
    [1,1,1,1,1,1,1,1,1,1], 
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,0,0,1],
    [1,0,1,0,0,0,0,0,0,1],
    [1,0,1,0,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ]

    for y in range(7):
        for x in range(10):
            if y == 0 or y == 6:
                freemap[y][x] = 1
            else:
                if x == 0 or x == 9:
                    freemap[y][x] = 1
                else:
                    freemap[y][x] = random.randint(0, 1)
    return freemap
        
    

key = ""

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ]
maze2 = [
    [1,1,1,1,1,1,1,1,1,1], 
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,0,0,1],
    [1,0,1,0,0,0,0,0,0,1],
    [1,0,1,0,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1]
    ]
maps = [maze, maze2]







root = tkinter.Tk()
root.title("미로 만들기")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()
main_proc()


root.mainloop()

