import numpy as np


class Dense(object):
    def __init__(
        self,
        m_inputs,
        n_outputs,
        activate,
    ):
        self.m_inputs = int(m_inputs)
        self.n_outputs = int(n_outputs)
        self.activate = activate
        self.learning_rate = .001

        # Choose random weights.
        # Inputs match to rows. Outputs match to columns.
        self.weights = (np.random.sample(
            size=(self.m_inputs + 1, self.n_outputs)) * 2  - 1)
        self.x = np.zeros((1, self.m_inputs + 1))
        self.y = np.zeros((1, self.n_outputs))
        
        self.v = np.zeros((1, self.n_outputs))  #same dimension as y

    def forward_prop(self, inputs):
        """
        Propagate the inputs forward through the network.

        inputs: 2D array
            One column array of input values.
        """
        bias = np.ones((1, 1))
        self.x = np.concatenate((inputs, bias), axis=1)
        
        #v = self.x @ self.weights
        self.v = self.x @ self.weights
        
        #self.y = self.activate.calc(v)
        self.y = self.activate.calc(self.v)
        return self.y

    def back_prop(self, de_dy):
        """
        Propagate the outputs back through the layer.
        """
        #dy_dv = self.activate.calc_d(self.y)
        dy_dv = self.activate.calc_d(self.v)
        
        # v = self.x @ self.weights
        # dv_dw = self.x
        # dv_dx = self.weights
        dy_dw = self.x.transpose() @ dy_dv
        de_dw = de_dy * dy_dw
        
        de_dx = (de_dy * dy_dv) @ self.weights.transpose()
        
        #self.weights -= de_dw * self.learning_rate
        change = de_dw * self.learning_rate
        self.weights = np.subtract(self.weights, change)
        
        return de_dx[:, :-1]
