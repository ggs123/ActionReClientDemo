# coding=utf-8
import pathlib
import sys
sys.path.append(r'D:\Dev\ICARE\Hydra\Code\ActionRecognition')
print(sys.path)
import numpy as np
import collections
import cv2
import TonCV2 as tcv2



_OPENPOSE_POINT_COLORS = [
    (255, 255, 0), (255, 191, 0), 
    (102, 255, 0), (255, 77, 0), (0, 255, 0), 
    (255, 255, 77), (204, 255, 77), (255, 204, 77), 
    (77, 255, 191), (255,191, 77), (77, 255, 91), 
    (255, 77, 204), (204, 255, 77), (255, 77, 191), 
    (191, 255, 77), (255, 77, 127), 
    (127, 255, 77), (255, 255, 0)] 

_OPENPOSE_EDGES = [
    (0, 1), 
    (1, 2), (2, 3), (3, 4),  
    (1, 5), (5, 6), (6, 7), 
    (1, 8), (8, 9), (9, 10), 
    (1, 11), (11, 12), (12, 13), 
    (0, 14), (14, 16),
    (0, 15), (15, 17)
]

_OPENPOSE_EDGE_COLORS = [
    (0, 0, 255), 
    (0, 84, 255), (0, 168, 0), (0, 255, 168), 
    (84, 0, 168), (84, 84, 255), (84, 168, 0), 
    (84, 255, 84), (168, 0, 255), (168, 84, 255), 
    (168, 168, 0), (168, 255, 84), (255, 0, 0), 
    (255, 84, 255), (255, 168, 0), 
    (255, 255, 84), (255, 0, 168)]

RENDER_CONFIG_OPENPOSE = {
    'edges': _OPENPOSE_EDGES,
    'edgeColors': _OPENPOSE_EDGE_COLORS,
    'edgeWidth': 2,
    'pointColors': _OPENPOSE_POINT_COLORS,
    'pointRadius': 4
}


def preparePose(pose, imageSize, invNorm):
    if invNorm == 'auto':
        invNorm = np.bitwise_and(pose >= 0, pose <= 1).all()

    if invNorm:
        w, h = imageSize
        trans = np.array([[w, 0], [0, h]])
        pose = (trans @ pose.T).T

    return pose.astype(np.int32)


def render(image: np.ndarray, poses, config, inplace: bool=True, inverseNormalization='auto') -> np.ndarray:
    '''绘制骨架

    参数

    `image`: 原图

    `poses`: 一组或多组关节点坐标

    `config`: 配置项

    `inplace`: 是否绘制在原图上

    `inverseNormalization`: 是否[True|False]进行逆归一化, 当值为auto时将根据坐标值自动确定

    返回值

    输出图像, `inplace`为True时返回`image`, 为False时返回新的图像

    '''

    if not inplace:
        image = image.copy()

    if len(poses.shape) == 2:
        poses = poses[None, :]

    if inverseNormalization not in ['auto', True, False]:
        raise ValueError('Unknown "inverseNormalization" value {inverseNormalization}')

    _isPointValid = lambda point: point[0] != 0 and point[1] != 0
    _FILL_CIRCLE = -1
    for pose in poses:
        pose = preparePose(pose, (image.shape[1], image.shape[0]), inverseNormalization)
        validPointIndices = set(filter(lambda i: _isPointValid(pose[i]), range(pose.shape[0])))
        for i, (start, end) in enumerate(config['edges']):
            if start in validPointIndices and end in validPointIndices:
                cv2.line(image, tuple(pose[start]), tuple(pose[end]), config['edgeColors'][i], config['edgeWidth'])

        for i in validPointIndices:
            cv2.circle(image, tuple(pose[i]), config['pointRadius'], tuple(config['pointColors'][i]), _FILL_CIRCLE)
        
    return image
    


if __name__ == '__main__':
    srcPath = r"./sample.jpg"
    dstPath = r"./sample2.jpg"
    posePath = r"D:\Dev\ICARE\Hydra\Test\Render\CQh6_8biAzc.json"

    import json
    # rawData = json.load(open(posePath))['data'][0]['skeleton'][0]['pose']
    # pose = np.array(rawData).reshape(-1, 2)
    pose = np.load('./1.npy', allow_pickle=True)[0, :2, 0, :].transpose(1, 0)
    srcImage = tcv2.imreadRGB(srcPath)
    renderedImage = render(srcImage, pose, RENDER_CONFIG_OPENPOSE)
    tcv2.imwriteRGB(dstPath, renderedImage)
    cv2.imshow('', renderedImage)
    cv2.waitKey()
    # import os
    # os.startfile(dstPath)
