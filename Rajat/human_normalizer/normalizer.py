import argparse

def getEmptyBoundingBox():
    return {
        "x":{
                "min":None,
            "max":None
        },
        "y":{
            "min":None,
            "max":None
        },
        "z":{
            "min":None,
            "max":None
        },
    }

def getTransformations(boundingBox):
    center ={
        "x": (boundingBox["x"]["min"]+boundingBox["x"]["max"])/2,
        "y": (boundingBox["y"]["min"]+boundingBox["y"]["max"])/2,
        "z": (boundingBox["z"]["min"]+boundingBox["z"]["max"])/2
    }

    dimensions = {
        "x" : boundingBox["x"]["max"]-boundingBox["x"]["min"],
        "y" : boundingBox["y"]["max"]-boundingBox["y"]["min"],
        "z" : boundingBox["z"]["max"]-boundingBox["z"]["min"]
    }
    return [
        lambda x: (x-center["x"]) / dimensions["x"],
        lambda y: (y-center["y"]) / dimensions["y"],
        lambda z: (z-center["z"]) / dimensions["z"]
    ]

def main():
    parser = argparse.ArgumentParser(description="Normalizes the coordinates of human")
    parser.add_argument("-o",dest="outfile",
            default="a.obj",
            help="Specify the outputfile")
    parser.add_argument("filename",help="File to be normalized")

    args = parser.parse_args()

    boundingBox = getEmptyBoundingBox()

    with open(args.filename) as lines:
        for line in lines:
            line = line.strip("\n")
            toks = line.split(" ")
            toks = list(filter( lambda tok: tok , toks))

            if toks and toks[0].lower() == 'v':
                x,y,z = list(map(float,toks[1:4]))


                # Get the minimum pts
                if boundingBox["x"]["min"] is None or boundingBox["x"]["min"] > x:
                    boundingBox["x"]["min"] = x

                if boundingBox["y"]["min"] is None or boundingBox["y"]["min"] > y:
                    boundingBox["y"]["min"] = y

                if boundingBox["z"]["min"] is None or boundingBox["z"]["min"] > z:
                    boundingBox["z"]["min"] = z

                # Get the maximum pts
                if boundingBox["x"]["max"] is None or boundingBox["x"]["max"] < x:
                    boundingBox["x"]["max"] = x

                if boundingBox["y"]["max"] is None or boundingBox["y"]["max"] < y:
                    boundingBox["y"]["max"] = y

                if boundingBox["z"]["max"] is None or boundingBox["z"]["max"] < z:
                    boundingBox["z"]["max"] = z
    
    transformations = getTransformations(boundingBox)
    Tx,Ty,Tz = transformations

    with open(args.filename) as lines:
        f = open(args.outfile,"w+")
        for line in lines:
            line = line.strip("\n")
            toks = line.split(" ")
            toks = list(filter( lambda tok: tok , toks))

            if toks and toks[0].lower() == 'v':
                x,y,z = list(map(float,toks[1:4]))
                x,y,z = [Tx(x) , Ty(y), Tz(z)]
                f.write("v {} {} {}\n".format(x,y,z))
            else:
                f.write(line+"\n")
        f.close()





if __name__ == "__main__":
    main()
