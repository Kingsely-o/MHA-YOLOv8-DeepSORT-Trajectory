import os

from PIL import Image


def read_image_dimensions(image_folder):
    image_dimensions = {}
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(image_folder, filename)
            with Image.open(image_path) as img:
                width, height = img.size
                image_dimensions[filename] = (width, height)

    return image_dimensions


if __name__ == "__main__":
    # 替换为你的实际情况
    image_folder = "data/dataset/val/images"
    txt_folder = "data/dataset/val/labelTxt"

    # 根据图片尺寸将标签进行修改
    image_dimensions = read_image_dimensions(image_folder)
    for filename, dimensions in image_dimensions.items():  # filename: 图片文件名, dimensions: 图片尺寸
        print(f"Processing {filename} with dimensions {dimensions}")
        txt_path = os.path.join(txt_folder,
                                filename.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt'))
        with open(txt_path, 'r') as file:
            lines = file.readlines()
        with open(txt_path, 'w') as file:
            for line in lines:
                line = line.strip().split(' ')  # 读取标签文件的每一行
                if len(line) > 8:
                    line[0] = str(int(line[0]) / dimensions[0])
                    line[1] = str(int(line[1]) / dimensions[1])
                    line[2] = str(int(line[2]) / dimensions[0])
                    line[3] = str(int(line[3]) / dimensions[1])
                    line[4] = str(int(line[4]) / dimensions[0])
                    line[5] = str(int(line[5]) / dimensions[1])
                    line[6] = str(int(line[6]) / dimensions[0])
                    line[7] = str(int(line[7]) / dimensions[1])
                    file.write(' '.join(line) + '\n')
                print(f"{line}")
