def box2location(box):
        return box[1:4]+box[0]

def boxes2locations(boxes):
        locations=[0]*len(boxes)
        for i in range(len(boxes)):
                locations[i]=boxes[i][1:4]+boxes[i][0]
        return locations

def checkIntersect(box1,box2):
	#box[left,top,right,bottom[
	return not(box1[2]<box2[0] or box2[2]<box1[0] or box1[3]<box2[1] or box2[3]<box1[1])


def Overlap(self, rect1, rect2):
	x01, y01, x02, y02 = rect1
	x11, y11, x12, y12 = rect2
	col = min(x02, x12) - max(x01, x11)
	row = min(y02, y12) - max(y01, y11)
	intersection = col * row
	area1 = (x02 - x01) * (y02 - y01)
	area2 = (x12 - x11) * (y12 - y11)
	coincide = intersection / (area1 + area2 - intersection)
	return coincide