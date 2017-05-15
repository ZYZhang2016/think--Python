#coding:utf-8
from World import World

'''利用world中的canvas画一面捷克国旗
'''
world = World()

canvas = world.ca(width=500,height=500,background='white')
bbox = [[-150,-100],[150,100]]
canvas.rectangle(bbox,outline='grey',width=1,fill='white')
abox = [[-150,-100],[150,0]]
canvas.rectangle(abox,outline=None,fill='red')
canvas.polygon([[-150,-100],[-150,100],[-15,0]],outline=None,fill='blue')
world.mainloop()
