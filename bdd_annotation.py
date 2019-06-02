import numpy as np
import json
from collections import defaultdict
name_box_id = defaultdict(list)
id_name = dict()
f = open(
    "bdd100k/labels/bdd100k_labels_images_train.json",
    encoding='utf-8')
labeled_images = json.load(f)

with open('model_data/yolo3/bdd/classes.txt') as f:
    classes = [s.strip() for s in f.readlines()]
    class_dict = {n : i for i, n in enumerate(classes)}

for image in labeled_images:
    name = 'bdd100k/images/100k/train/' + image['name']
    empty_image = True

    for label in image['labels']:
        if label['category'] in class_dict.keys():
            empty_image = False

            if label['category'] == 'lane':
                cat = class_dict[label['attributes']['laneType']]
                poly2d = np.array(label['poly2d'][0]['vertices'])
                x1, y1 = np.min(poly2d, axis = 0)
                x2, y2 = np.max(poly2d, axis = 0)

            else:
                cat = class_dict[label['category']]

                x1 = label['box2d']['x1']
                y1 = label['box2d']['y1']
                x2 = label['box2d']['x2']
                y2 = label['box2d']['y2']

            name_box_id[name].append([[x1, y1, x2, y2], cat])
    if empty_image:
        continue

f = open('train_bdd.txt', 'w')
for key in name_box_id.keys():
    f.write(key)
    box_infos = name_box_id[key]
    for info in box_infos:
        x_min = int(info[0][0])
        y_min = int(info[0][1])
        x_max = int(info[0][2])
        y_max = int(info[0][3])

        box_info = " %d,%d,%d,%d,%d" % (
            x_min, y_min, x_max, y_max, int(info[1]))
        f.write(box_info)
    f.write('\n')
f.close()
