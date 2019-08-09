# coding=utf-8
import requests
import numpy as np
import os

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

URL = 'https://p2-1252380913.cos.ap-shanghai.myqcloud.com/sample.jpg'


def get_data():
    try:
        resp = requests.get(URL, headers=headers)
    except Exception:
        return None
    if resp.status_code == 200:
        pose = np.load('./1.npy', allow_pickle=True)[0, :2, 0, :].transpose(1, 0)
        return {'img_b': resp.content,
                'pose': pose,
                'boundingBox': [39, 917, 336, 886],
                'nameAndAction': ['葛某', '走']}
    else:
        return None


def load_local_data():
    imgs = os.listdir('./data/20_imga/')
    poses = np.load('./data/20.npy', allow_pickle=True)
    i = 0

    def iner():
        nonlocal imgs, i, poses
        if i >= len(imgs):
            return None
        with open('./data/20_imga/'+imgs[i], 'rb') as fr:
            img_b = fr.read()
        pose = poses[0, :2, i, :].transpose(1, 0)
        i += 1
        return {'img_b': img_b,
                'pose': pose,
                'boundingBox': [[39, 917, 336, 886]]*5,
                'nameAndAction': [['葛某', '走']]*5}
    return iner


# for test
get_data = load_local_data()
# get_data = lambda: None


if __name__ == '__main__':
    # import cv2
    #
    # img_b = get_data()['img_b']
    # img_np = np.frombuffer(img_b, dtype=np.uint8)
    # img_cv = cv2.imdecode(img_np, cv2.IMREAD_ANYCOLOR)
    # img_clip = img_cv[39:39+886, 917:917+336]
    b = load_local_data()()
    print(b)
    print('a')