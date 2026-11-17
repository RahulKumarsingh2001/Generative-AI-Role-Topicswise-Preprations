## Features and Labels

```
Feature :- The input information a model uses to make a prediction. 
Lable :- The correct answers the model learns to predict during training.

Feature (X) = Message text.
Label (y) = Spam or Not Spam.


Feature are also different types
A. Numerical Features :- these contain numerical value.
        | Age | Salary | Experience |
        |---:|---:|---:|
        | 22 | 25000 | 0 |
        | 25 | 40000 | 2 |
        | 30 | 65000 | 6 |

B. Categorical Features:- These represent categories rather than continuous numerical quantities.
        | City | Education | Purchased |
        |---|---|---|
        | Bengaluru | B.Tech | Yes |
        | Mumbai | MCA | No |
        | Delhi | B.Tech | Yes |

C. Text Features:- These contain written language.
        | Message | Label |
        |---|---|
        | Win a free prize now! | Spam |
        | Let's have lunch tomorrow. | Not Spam |

D. Image Features:- For an image-classification task, the input is an image represented numerically, typically as 
   pixel values or features extracted by a neural network.

        Feature (X): Image of a cat.
        Label (y): Cat.




- A label is the target value you want the model to predict.

| Task | Features (`X`) | Label (`y`) |
|---|---|---|
| House-price prediction | Size, location, bedrooms | House price |
| Spam detection | Message text | Spam or Not Spam |
| Sentiment analysis | Customer review | Positive, Negative, or Neutral |

```



## Train/Validation/Test Splits

```
Training:- train a data from any source like wikipidia or any different place
case 1:- you can directly go training to testing
case 2:- first do traing ---> validation(best data comes) ---> then you can move to a testing
         70%                        10%                         20%
```



## Loss functions

```
A loss function in nural network mesure how far the predicted output if from the actual target output

Types of loss functions:-
(a) Regression Loss functions(For continuous outputs)
    1) Mean square error (MSE)
    2) Mean Absolute Error (MAE)
    3) Huber loss
(b) Classification Loss functions(for discrete outputs)
    1) cross-Entropy loss(Log loss)
    2) Hinge Loss(for SVMs)
```


## Gradient Descent

```
Minimized the Loss Functions. 
```