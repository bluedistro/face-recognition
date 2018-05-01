# FaceRecognition
Webcam face recognition using tensorflow and opencv.
The application tries to find faces in the webcam image and match them against images in an id folder using deep neural networks.

## Dependencies
*   Pillow
*   OpenCv
*   Scipy
*   Tensorflow
*   Flask

## Inspiration
Models, training code and inspriation can be found in the [facenet](https://github.com/davidsandberg/facenet) repository.
[Multi-task Cascaded Convolutional Networks](https://kpzhang93.github.io/MTCNN_face_detection_alignment/index.html) are used for facial and landmark detection while an [Inception Resnet](https://arxiv.org/abs/1602.07261) is used for ID classification.
A direct link to the pretrained Inception Resnet model can be found [here](https://drive.google.com/file/d/0B5MzpY9kBtDVZ2RpVDYwWmxoSUk).

## How to
Get the [model from facenet](https://drive.google.com/file/d/0B5MzpY9kBtDVZ2RpVDYwWmxoSUk) and setup your id folder.
The id folder should contain subfolders, each containing at least one image of one person. The subfolders should be named after the person in the folder since this name is used as output when a match is found.

E.g. id folder named `ids` containing subfolders `Beyonce` and `Will Smith`, each containing images of the respective person.

```bash
├── ids
│   ├── Beyonce
│   │   ├── beyonce_1.jpg
│   │   ├── beyonce_2.jpg
│   ├── Will Smith
│   │   ├── will_smith_1.jpg
        ├── will_smith_2.jpg

```
Download the [model](https://drive.google.com/file/d/0B5MzpY9kBtDVZ2RpVDYwWmxoSUk) to a folder named `model` and run `python __server__.py` to start the program running on port 5030.
