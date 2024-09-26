import numpy as np
import torch
from torch.autograd.variable import Variable

def real_data_target(size):
    '''
    Tensor containing ones, with shape = size
    '''
    data = Variable(torch.ones(size, 1))
    return data

def fake_data_target(size):
    '''
    Tensor containing zeros, with shape = size
    '''
    data = Variable(torch.zeros(size, 1))
    return data
    
def images_to_vectors(images, length):
    # reshapes the input image into a vector of given length
    # just checking that information isnt lost in the covnersion
    if np.prod(images.size()[1:]) > length:
        length = np.prod(images.size()[1:])
    return images.view(images.size(0), length)

def vectors_to_images(vectors, channel, width, height):
    # just error checking
    assert np.prod(vectors.size()[1:]) == channel*width*height
    return vectors.view(vectors.size(0), channel, width, height)

def noise(size, batchSize):
    n = Variable(torch.randn(size, batchSize))
    return n

