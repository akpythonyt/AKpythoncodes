from imageai.Classification import ImageClassification
import os
executionpath=os.getcwd()
print(executionpath)
detection=ImageClassification()
detection.setModelTypeAsResNet50()
detection.setModelPath(executionpath + "/resnet50_imagenet_tf.2.0.h5")
detection.loadModel()
detections,percentageprobabilites=detection.classifyImage("Testimage.jpg",result_count=5)
for Index in range(len(detections)):
    print(detections[Index],":",percentageprobabilites[Index])