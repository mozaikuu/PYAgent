from pyamaze import maze, agent, COLOR

m = maze(100, 100)
m.CreateMaze(loopPercent=0)
a = agent(m, filled=True, footprints=True, color=color.red)
b = agent(m, filled=True, footprints=True, color=color.blue)
c = agent(m, filled=True, footprints=True, color=color.green)
m.tracePath({a: m.path}, delay=1)
m.tracePath({b: m.path}, delay=1)
m.tracePath({c: m.path}, delay=1)
m.run()
# print(m.maze_map)
