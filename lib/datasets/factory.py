# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""Factory method for easily getting imdbs by name."""

__sets = {}

import datasets
from datasets.caltech import caltech
from datasets.kaist_rgb import kaist_rgb
from datasets.kaist_thermal import kaist_thermal
from datasets.kaist_fusion import kaist_fusion
from datasets.pascal_voc import pascal_voc
from datasets.coco import coco

import numpy as np

# set up caltech
imageset = 'test';
name = 'caltech_{}'.format(imageset)
__sets[name] = (lambda imageset = imageset: caltech('test'))

imageset = 'train04';
name = 'caltech_{}'.format(imageset)
__sets[name] = (lambda imageset = imageset: caltech('train04'))

imageset = 'test-all';
name = 'kaist_{}'.format(imageset)
__sets[name] = (lambda imageset = imageset: kaist_rgb('test-all'))

imageset = 'train-all02';
name = 'kaist_{}'.format(imageset)
__sets[name] = (lambda imageset = imageset: kaist_rgb('train-all02'))

imageset = 'test-all-thermal';
name = 'kaist_{}'.format(imageset)
__sets[name] = (lambda imageset = imageset: kaist_thermal('test-all'))

imageset = 'train-all02-thermal';
name = 'kaist_{}'.format(imageset)
__sets[name] = (lambda imageset = imageset: kaist_thermal('train-all02'))

imageset = 'test-all-fusion';
name = 'kaist_{}'.format(imageset)
__sets[name] = (lambda imageset = imageset: kaist_fusion('test-all'))

imageset = 'train-all02-fusion';
name = 'kaist_{}'.format(imageset)
__sets[name] = (lambda imageset = imageset: kaist_fusion('train-all02'))

# Set up voc_<year>_<split> using selective search "fast" mode
for year in ['2007', '2012']:
    for split in ['train', 'val', 'trainval', 'test']:
        name = 'voc_{}_{}'.format(year, split)
        __sets[name] = (lambda split=split, year=year: pascal_voc(split, year))

# Set up coco_2014_<split>
for year in ['2014']:
    for split in ['train', 'val', 'minival', 'valminusminival']:
        name = 'coco_{}_{}'.format(year, split)
        __sets[name] = (lambda split=split, year=year: coco(split, year))

# Set up coco_2015_<split>
for year in ['2015']:
    for split in ['test', 'test-dev']:
        name = 'coco_{}_{}'.format(year, split)
        __sets[name] = (lambda split=split, year=year: coco(split, year))

def get_imdb(name):
    """Get an imdb (image database) by name."""
    if not __sets.has_key(name):
        raise KeyError('Unknown dataset: {}'.format(name))
    return __sets[name]()

def list_imdbs():
    """List all registered imdbs."""
    return __sets.keys()
