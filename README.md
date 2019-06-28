# Generative Adverserial Networks

GAN's basically consist of three main component:
1. Discriminative Network
2. Generative Network
3. Respective Loss and BackProp


## 1. Discriminative Network
The simplest part of GAN is the discriminative network. This is the neural network that tries to learn to differentiate between the True and False inputs. This is the simplest because it is alike any other DL netwrok that one might train. This is also the main motivator of the whole system. This network basically pushes out other network (Generative Network) to learn to "generate" better putputs that can not be differentiated from actual outputs. Hence we want the error of the Discrimnative Network to eventually fall which in the ideal case mean that out Generative Network is getting beeter at produceing fakes which is the whole point of GAN's.


## 2. Generative Network


## Resources
https://medium.com/ai-society/gans-from-scratch-1-a-deep-introduction-with-code-in-pytorch-and-tensorflow-cb03cdcdba0f
https://skymind.ai/wiki/generative-adversarial-network-gan
https://arxiv.org/pdf/1406.2661.pdf

