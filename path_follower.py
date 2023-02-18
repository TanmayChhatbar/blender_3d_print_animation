## made for prusaslicer 2.5.0
# main function
import sys
import numpy as np
from utils import *
from gcodedata import *

def parse_locs(lines):
    printing = 0
    cur = [np.array([0.,0.,0.,0.])]
    for line in lines:
        # get start point
        if "G92 E0\n" == line:
            printing = 1
        if printing == 0:
            continue

        # record points
        if "G1" in line:
            cur.append(find_coord(line, cur[-1]))
            # print("boop\n\n")
            # print(cur)
    return cur


def get_frame_locs(locs, dps):
    locs_frame = [locs[0][0:3]]
    pr_loc = locs[0]
    dslp = 0.0                      # distance since last point

    lenloc = len(locs)
    i = 1
    loc = locs[1]
    pr_loc = locs[0]
    while i <= lenloc:
        cdd = dis(loc[0:3], pr_loc[0:3])      # distance between points
        md = dps-dslp               # distance to go before next frame_loc
        
        if cdd < md:                # if length of line is less than distance to travel
            dslp = dslp + cdd
            if i == lenloc-1:
                break
            else:
                i += 1
            pr_loc = loc
            loc = locs[i]
        else:                       # if somewhere in next line
            nl = pr_loc[0:3] + (loc[0:3]-pr_loc[0:3])*md/cdd
            dslp = 0.0
            pr_loc = nl
            locs_frame.append(nl)
        
    # for loc in locs[1:-1]:
    #     cdd = dis(loc, pr_loc)      # distance between points
    #     md = dps-dslp               # distance to go before next frame_loc
        
    #     if cdd < md:                # if length of line is less than distance to travel
    #         dslp = dslp + cdd
    #     else:                       # if somewhere in next line
    #         nl = pr_loc[0:3] + (loc-pr_loc)[0:3]*md/cdd
    #         dslp = 0.0
    #         locs_frame.append(nl)
            
    #     pr_loc = loc
        # TODO
    return locs_frame

def main():
    if len(sys.argv) == 1:
        # print("usage: python path_follower.py [path.gcode] OPTIONAL- [distance_per_step]")
        fn = 'path.gcode'
    else:
        fn = sys.argv[1]
        # return
    try:
        distance_per_step = float(sys.argv[2])
    except:
        distance_per_step = 100.0
    with open(fn, 'r') as f:
        locs = parse_locs(f.readlines())

        locs_frames = get_frame_locs(locs, distance_per_step)
        
    with open('pathout.csv','w') as f2:
        # f2.write(gcode_header)
        e = 1
        # for loc in locs_frames:
        for loc in locs:
            if e != 1:
                f2.write('\n')
            # f2.write(f"G1 X{loc[0]} Y{loc[1]} Z{loc[2]} E{e}")
            f2.write(f"{loc[0]},{loc[1]},{loc[2]}")
            e += 1
        # f2.write(gcode_footer)

if __name__ == "__main__":
    # args
    main()
