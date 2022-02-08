# Basic Neural Net
# Copied from : https://iamtrask.github.io/2015/07/12/basic-python-network/
# Feb. 3, 2021
# I added more comments onto the code

# IMPORTS
import numpy as np # For ai | linear algebra library
from tqdm import tqdm # for progress bar

# sigmoid function | We use it to convert numbers to probabilities | I HAVE NO CLUE HOW LOL
def nonlin(x,deriv=False): # this function can also generate the derivative of a sigmoid (when deriv=True)
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# input dataset | This initializes our input dataset as a numpy matrix | Each row is a single "training example". Each column corresponds to one of our input nodes.
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])
    
# output dataset | ".T" is the transpose function. After the transpose, this y matrix has 4 rows with one column. Just like our input, each row is a training example, and each column (only one) is an output node            
y = np.array([[0,0,1,1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
# It's good practice to seed your random numbers. Your numbers will still be randomly distributed, but they'll be randomly distributed in exactly the same way each time you train. This makes it easier to see how your changes affect the network.
np.random.seed(1)

# initialize weights randomly with mean 0
# This is our weight matrix for this neural network. It's called "syn0" to imply "synapse zero"
# Since we only have 2 layers (input and output), we only need one matrix of weights to connect them. Its dimension is (3,1) because we have 3 inputs and 1 output
# Also notice that it is initialized randomly with a mean of zero. There is quite a bit of theory that goes into weight initialization. For now, just take it as a best practice that it's a good idea to have a mean of zero in weight initialization.
syn0 = 2*np.random.random((3,1)) - 1

# This begins our actual network training code. This for loop "iterates" multiple times over the training code to optimize our network to the dataset
# I also added tqdm for some flare
for iter in tqdm(range(562_500), bar_format="{percentage:1.0f}%|{bar:50}{r_bar}"):

    # forward propagation
    layer_0 = X # Since our first layer, layer_0, is simply our data. We explicitly describe it as such at this point. Remember that X contains 4 training examples (rows). We're going to process all of them at the same time in this implementation.
    # This is known as "full batch" training. Thus, we have 4 different layer_0 rows, but you can think of it as a single training example if you want. It makes no difference at this point. (We could load in 1000 or 10,000 if we wanted to without changing any of the code).
    
    # This is our prediction step. Basically, we first let the network "try" to predict the output given the input. We will then study how it performs so that we can adjust it to do a bit better for each iteration.
    # The first matrix multiplies l0 by syn0. The second passes our output through the sigmoid function. 
    layer_1 = nonlin(np.dot(layer_0,syn0))
    # Consider the dimensions of each: (4 x 3) dot (3 x 1) = (4 x 1)

    """
    Matrix multiplication is ordered, such the dimensions in the middle of the equation must be the same. 
    The final matrix generated is thus the number of rows of the first matrix and the number of columns of the second matrix.

    Since we loaded in 4 training examples, we ended up with 4 guesses for the correct answer, a (4 x 1) matrix. 
    Each output corresponds with the network's guess for a given input. 
    Perhaps it becomes intuitive why we could have "loaded in" an arbitrary number of training examples. 
    The matrix multiplication would still work out. :)
    """

    # how much did we miss? | So, given that l1 had a "guess" for each input. We can now compare how well it did by subtracting the true answer (y) from the guess (layer_1)
    layer_1_error = y - layer_1 # layer_1_error is just a vector of positive and negative numbers reflecting how much the network missed.

    # multiply how much we missed by the 
    # slope of the sigmoid at the values in layer_1
    """
    Lets break this next line down:

    nonlin(layer_1,True) (The Derivative)
    
    If l1 represents these three dots, the code above generates the slopes of the lines below. 
    Notice that very high values such as x=2.0 (green dot) and very low values such as x=-1.0 (purple dot) have rather shallow slopes. 
    The highest slope you can have is at x=0 (blue dot). This plays an important role. Also notice that all derivatives are between 0 and 1.

    https://iamtrask.github.io/img/sigmoid-deriv-2.png

    layer_1_delta = layer_1_error * nonlin(layer_1,True) (The Error Weighted Derivative)

    l1_error is a (4,1) matrix. nonlin(l1,True) returns a (4,1) matrix. What we're doing is multiplying them "elementwise". 
    This returns a (4,1) matrix l1_delta with the multiplied values.

    When we multiply the "slopes" by the error, we are reducing the error of high confidence predictions. 
    Look at the sigmoid picture again! If the slope was really shallow (close to 0), then the network either had a very high value, or a very low value. 
    This means that the network was quite confident one way or the other. However, if the network guessed something close to (x=0, y=0.5) then it isn't very confident. 
    We update these "wishy-washy" predictions most heavily, and we tend to leave the confident ones alone by multiplying them by a number close to 0.

    """
    layer_1_delta = layer_1_error * nonlin(layer_1,True)

    # update weights
    # So, what does line 39 do? It computes the weight updates for each weight for each training example, sums them, and updates the weights, all in a simple line.
    syn0 += np.dot(layer_0.T,layer_1_delta)

print("Output After Training:")
print(layer_1)
