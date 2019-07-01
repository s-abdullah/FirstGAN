# Generative Adverserial Networks

GAN's basically consist of three main component:
1. Discriminative Network
2. Generative Network
3. Respective Loss


## 1. Discriminative Network
The simplest part of GAN is the discriminative network. This is the neural network that tries to learn to differentiate between the True and False inputs. This is the simplest because it is alike any other DL netwrok that one might train. This is also the main motivator of the whole system. This network basically pushes out other network (Generative Network) to learn to "generate" better putputs that can not be differentiated from actual outputs. Hence we want the error of the Discrimnative Network to eventually fall which in the ideal case mean that out Generative Network is getting beeter at produceing fakes which is the whole point of GAN's.
The only difference in the Discriminator is that instead of predicting the class, it will be binary classification i.e. whether its a "True" example or "False".

## 2. Generative Network
The generator network is more interesting. The input to the generator is a latent variale vector which the network will learn to transform into a good "fake". So the ouput od the network should be example the same size and value range as the input to the discriminator.

## 3. Loss
From the Original paper we see that the we need to do stachastic gradient ascent on the following fro the discrminator 
since its a binary predictor:

![alt text][gloss]

And for the generator the loss would be a descent of the following: 

![alt text][dloss]

And as the Paper states, the overall mathematical equation comes out to this minimax game:

![alt text][game]

So finally we can get the following pseudo-code for the simple GAN:

![alt text][pseudo]

We will use binary cross entropy loss for both. This is very simply explained in Tutorial#1. 

![alt text][bce]

Replace Y = 1 for real-data and Y = 0 for fake-data. (Mx = min of negative, BCE has negative attached hence gradient is decent in discrimniator loss)

## Resources
[Original Paper on GAN by Ian GoodFellow](https://arxiv.org/pdf/1406.2661.pdf)

[Tutoial#1 from Medium that was Majorly followed](https://medium.com/ai-society/gans-from-scratch-1-a-deep-introduction-with-code-in-pytorch-and-tensorflow-cb03cdcdba0f)

[Turoial#2 from Skymind that was refernce](https://skymind.ai/wiki/generative-adversarial-network-gan)

Notes on the loss being used:
![alt text][note]

[gloss]: https://github.com/s-abdullah/FirstGAN/blob/master/images/gen.png 
[pseudo]: https://github.com/s-abdullah/FirstGAN/blob/master/images/pseudo.png 
[dloss]: https://github.com/s-abdullah/FirstGAN/blob/master/images/disc.png 
[game]: https://github.com/s-abdullah/FirstGAN/blob/master/images/minimax.png 
[bce]: https://github.com/s-abdullah/FirstGAN/blob/master/images/bce.png 
[note]: https://github.com/s-abdullah/FirstGAN/blob/master/images/forloss.jpg 

