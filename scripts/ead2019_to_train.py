import argparse
import glob
import os

def ead2019_to_train(ead2019_input_dir_path, output_dir_path):
    ead2019_input_txt_file_names = glob.glob(os.path.join(ead2019_input_dir_path, "*.txt"))
    train_ratio = 0.8

    image_num = len(ead2019_input_txt_file_names)
    train_num = int(image_num * train_ratio)
    output_train_file_name = os.path.join(output_dir_path, "train.txt")
    output_test_file_name = os.path.join(output_dir_path, "test.txt")

    output_rows = []
    for ead2019_input_txt_file_name in ead2019_input_txt_file_names:
        output_row_elements = []
        ead2019_input_jpg_file_name = os.path.splitext(ead2019_input_txt_file_name)[0] + ".jpg"
        output_row_elements.append(ead2019_input_jpg_file_name)

        with open(ead2019_input_txt_file_name) as f:
            ead2019_input_rows = [line.strip() for line in f]

        for ead2019_input_row in ead2019_input_rows:
            ead2019_input_row_split = ead2019_input_row.split()
            ead2019_input_row_comma = ",".join(ead2019_input_row_split[1:] + ead2019_input_row_split[:1])
            output_row_elements.append(ead2019_input_row_comma)

        output_row = " ".join(output_row_elements)
        output_rows.append(output_row)

    output_train_str = "\n".join(output_rows[:train_num])
    output_test_str = "\n".join(output_rows[train_num:])

    with open(output_train_file_name, 'w') as f:
        f.write(output_train_str)

    with open(output_test_file_name, 'w') as f:
        f.write(output_test_str)

def _main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--ead2019_input_dir_path', required=True)
    parser.add_argument('-o', '--output_dir_path', required=True)
    args = vars(parser.parse_args())

    ead2019_to_train(args["ead2019_input_dir_path"], args["output_dir_path"])


if __name__ == '__main__':
    _main()
