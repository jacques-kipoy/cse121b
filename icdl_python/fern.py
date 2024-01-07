# Define four affine transformations

f1 = [0,0,0,0.22,0,0]
f2 = [0.85,0.04,-0.04,0.85,0,1.6]
f3 = [0.2,-0.26,0.23,0.22,0,1.6]
f4 = [-0.15,0.28,0.26,0.24,0,0.44]

#The recursive fun=ction that calls itself
# It calls itself four times
# Each of these in turn calls itself four times

def draw_fern (level , p):
    if level < 1:
        plot_point(p)
        return
    draw_fern(level-1, apply_transform(f1, p))
    draw_fern(level-1, apply_transform(f2, p))
    draw_fern(level-1, apply_transform(f3, p))
    draw_fern(level-1, apply_transform(f4, p))

def draw_fen_fern():
    draw_fern(9,(0,0))

draw_once(draw_the_fern)