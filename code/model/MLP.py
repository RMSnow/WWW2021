# -*- coding: utf-8 -*-
""" 
@author: RMSnow 
@file: MLP.py 
@time: 2020/5/20 11:14
@contact: xueyao_98@foxmail.com

# The Simplest Neural Network
"""

from keras.layers import Input, Dense
from keras.regularizers import l2
from keras.optimizers import Adam
from keras.models import Model


class MLP5Layers:
    def __init__(self, input_dim, category_num=2, l2_param=0.01, lr_param=0.001):
        self.input_dim = input_dim
        self.category_num = category_num
        self.l2_param = l2_param

        self.model = self.build()
        self.model.compile(loss='categorical_crossentropy', optimizer=Adam(
            lr=lr_param, beta_1=0.8), metrics=['accuracy'])

    def build(self):
        se_input = Input(shape=(self.input_dim,))

        dense1 = Dense(64, activation='relu',
                       kernel_regularizer=l2(self.l2_param))(se_input)
        dense2 = Dense(48, activation='relu',
                       kernel_regularizer=l2(self.l2_param))(dense1)
        dense3 = Dense(32, activation='relu',
                       kernel_regularizer=l2(self.l2_param))(dense2)
        dense4 = Dense(16, activation='relu',
                       kernel_regularizer=l2(self.l2_param))(dense3)
        output = Dense(self.category_num, activation='softmax',
                       kernel_regularizer=l2(self.l2_param))(dense4)

        model = Model(inputs=[se_input], outputs=output)
        return model
