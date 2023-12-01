class utils:
    def __init__(self):
        pass

    def parse_specs(self, specs):
        h = w = d = -1
        for dimension in specs:
            #find the max dimension value
            if("Height" in dimension['key'] or "height" in dimension['key']):
                new_h = dimension["value"]
                try:
                    new_h = float(new_h)
                except:
                    continue
                if(new_h > h):
                    h = new_h
            if ("Width" in dimension['key'] or "width" in dimension['key']):
                new_w = dimension["value"]
                try:
                    new_w = float(new_w)
                except:
                    continue
                if (new_w > w):
                    w = new_w
            if ("Depth" in dimension['key'] or "depth" in dimension['key'] or "length" in dimension['key'] or "Length" in dimension['key'] ):
                new_d = dimension["value"]
                try:
                    new_d = float(new_d)
                except:
                    continue
                if (new_d > d):
                    d = new_d

        return (h,w,d)