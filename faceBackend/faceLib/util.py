def box2location(box):
        return box[1:4]+box[0]

def boxes2locations(boxes):
        locations=[0]*len(boxes)
        for i in range(len(boxes)):
                locations[i]=boxes[i][1:4]+boxes[i][0]
        return locations
