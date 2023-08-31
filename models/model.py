from torch.nn import CrossEntropyLoss
from torch.optim import Adam

class Model():

    def __init__(self, model, optimizer=Adam, loss=CrossEntropyLoss()) -> None:
        self.model = model
        self.optimizer = optimizer
        self.loss = loss
        self.optimizer = optimizer(self.model.parameters())
