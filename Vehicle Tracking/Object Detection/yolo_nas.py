import cv2
from super_gradients.training import models
import torch

device=torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')

model=models.get('yolo_nas_s',pretrained_weights='coco').to(device)

out=model.predict("../Images/image2.jpg")

out.show()