# Cloud masking with convolutional neural networks (CNNs)

This repository contains code related to the study analyzed in the paper cited below:

Kristollari, Viktoria, and Vassilia Karathanassi. "Convolutional neural networks for detecting challenging cases in cloud masking using Sentinel-2 imagery." In Eighth International Conference on Remote Sensing and Geoinformation of the Environment (RSCy2020), vol. 11524, p. 115240K. International Society for Optics and Photonics, 2020.

It can be accessed in: https://doi.org/10.1117/12.2571111

![CNN architecture](/images/CNN_architecture.png)

## Steps to implement the code

Run:
>1. the commands in the "gdal_commands" file to convert the Sentinel-2 images to .tiff files and merge bands.
>
>2. "data_downloading.py" to download the Sentinel-2 images.
>
>3. "data_preprocessing.py" to create training and test data for the CNN. 
>
>4. "generator.py" to generate training and test patches.
>
>5. "CNN_training.py" to train the CNN and save the weights.
>
>6. "CNN_predictions.py" to create and save the predicted cloud masks.
>
>7. "evaluation_metrics.py" to evaluate the cloud masks.

*Detailed guidelines are included inside each script.*

### Optionally:
Run:
- "add_padding.py" to add zero padding to the Sentinel-2 images.

If you use this code, please cite the below paper.

```
@inproceedings{10.1117/12.2571111,
author = {Viktoria Kristollari and Vassilia Karathanassi},
title = {{Convolutional neural networks for detecting challenging cases in cloud masking using Sentinel-2 imagery}},
volume = {11524},
booktitle = {Eighth International Conference on Remote Sensing and Geoinformation of the Environment (RSCy2020)},
editor = {Kyriacos Themistocleous and Giorgos Papadavid and Silas Michaelides and Vincent Ambrosia and Diofantos G. Hadjimitsis},
organization = {International Society for Optics and Photonics},
publisher = {SPIE},
pages = {188 -- 201},
keywords = {Convolutional neural networks, Cloud masking, Sentinel satellite imagery, Thin cloud detection, Bright surfaces detection, Feature maps},
year = {2020},
doi = {10.1117/12.2571111},
URL = {https://doi.org/10.1117/12.2571111}
}
```
