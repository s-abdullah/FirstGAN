from torch import nn

# leaky relu used to avoid sparse gradients (https://github.com/soumith/ganhacks)
class Discriminator(nn.Module):
    ## three hidden layer network, 
    ## nfeat will be flattened images eg 28x28 = 784
    ## output is 1 since its just learns to distinguish between real and fake
    def __init__(self, n_feat):
        super().__init__()
        # input vector
        n_features = n_feat
        # binary output
        n_out = 1

        self.hidden0 = nn.Sequential( 
            nn.Linear(n_features, 1024),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3)
        )
        self.hidden1 = nn.Sequential(
            nn.Linear(1024, 512),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3)
        )
        self.hidden2 = nn.Sequential(
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3)
        )
        self.out = nn.Sequential(
            nn.Linear(256, n_out),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.hidden0(x)
        x = self.hidden1(x)
        x = self.hidden2(x)
        x = self.out(x)
        return x


class Generator(nn.Module):
    ## output of the generator will be the input of the discriminator ie nfeat ie flattened image
    ## tanh activation will produce normailzed values between -1 an 1
    def __init__(self, batchSize, vecOut):
        super().__init__()
        # number of images to produce
        n_features = batchSize
        # length of vector that will be input to the Discriminator
        n_out = vecOut
        
        self.hidden0 = nn.Sequential(
            nn.Linear(n_features, 256),
            nn.LeakyReLU(0.2)
        )
        self.hidden1 = nn.Sequential(            
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2)
        )
        self.hidden2 = nn.Sequential(
            nn.Linear(512, 1024),
            nn.LeakyReLU(0.2)
        )
        
        self.out = nn.Sequential(
            nn.Linear(1024, n_out),
            nn.Tanh()
        )

    def forward(self, x):
        x = self.hidden0(x)
        x = self.hidden1(x)
        x = self.hidden2(x)
        x = self.out(x)
        return x
    