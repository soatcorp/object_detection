#bdd annotation 用
import json
from collections import defaultdict

name_box_id = defaultdict(list)
id_name = dict()

f = open(
    "bdd100k/labels/bdd100k_labels_images_train.json",
    #"bdd100k/labels/bdd100k_labels_images_val.json",
    encoding='utf-8')
labeled_images = json.load(f)

with open('model_data/yolo3/coco/classes.txt') as fp:
    coco_classes = [line.strip() for line in fp]

for image in labeled_images:
    for label in image['labels']:
        if label['category'] in coco_classes:
            name = 'bdd100k/images/100k/train/' + image['name']
            #name = 'bdd100k/images/100k/val/' + image['name']

            cat = coco_classes.index(label['category'])
            if cat >= 1 and cat <= 11:
                cat = cat - 1
            elif cat >= 13 and cat <= 25:
                cat = cat - 2
            elif cat >= 27 and cat <= 28:
                cat = cat - 3
            elif cat >= 31 and cat <= 44:
                cat = cat - 5
            elif cat >= 46 and cat <= 65:
                cat = cat - 6
            elif cat == 67:
                cat = cat - 7
            elif cat == 70:
                cat = cat - 9
            elif cat >= 72 and cat <= 82:
                cat = cat - 10
            elif cat >= 84 and cat <= 90:
                cat = cat - 11

            x_min = int(label['box2d']['x1'])
            y_min = int(label['box2d']['y1'])
            x_max = int(label['box2d']['x2'])
            y_max = int(label['box2d']['y2'])
            name_box_id[name].append([x_min, y_min, x_max, y_max, cat])

f = open('bdd_train.txt', 'w')
#f = open('bdd_val.txt', 'w')
for key in name_box_id.keys():
    f.write(key)
    box_infos = name_box_id[key]
    for info in box_infos:
        box_info = " %d,%d,%d,%d,%d" % (
           info[0], info[1], info[2], info[3], info[4])
        f.write(box_info)
    f.write('\n')
f.close()
