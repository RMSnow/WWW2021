# -*- coding: utf-8 -*-
""" 
@author: RMSnow 
@file: HSA_BLSTM.py 
@time: 2020/6/19 18:40
@contact: xueyao_98@foxmail.com

# CIKM'18 HSA_BLSTM
"""
from keras.layers import Input
from keras.layers import Bidirectional
from keras.layers import GRU, TimeDistributed, LSTM
from keras.layers import GlobalAveragePooling1D
from keras.layers import Dense
from keras.layers import Embedding, Concatenate
from keras.models import Model
from keras.regularizers import l2
from keras.optimizers import Adam
from keras.initializers import Constant
from keras import backend as K
from keras.layers.core import Lambda
from keras.engine.topology import Layer
from keras import initializers
import tensorflow as tf


class SelfAttLayer(Layer):
    def __init__(self, **kwargs):
        self.init = initializers.get('normal')
        # self.init = initializers.get('glorot_uniform')
        super(SelfAttLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        # input_shape: (n, steps, dim)
        dim = input_shape[-1]
        self.W = self.add_weight(shape=(dim,),
                                 initializer=self.init,
                                 name='{}_W'.format(self.name))

    def call(self, x, mask=None):
        # (n, steps, dim) dot (dim,) -> (n, steps)
        e = K.exp(K.tanh(K.sum(x * self.W, axis=-1)))
        # print('e: ', e.shape)

        # (n, steps) / (n, 1) -> (n, steps)
        a = e / K.expand_dims(K.sum(e, axis=1), axis=-1)
        # print(a.shape)

        # (n, steps, dim) * (n, steps, 1) -> (n, steps, dim)
        weighted_input = x * K.expand_dims(a, axis=-1)
        # print(weighted_input.shape)

        # (n, steps, dim) -> (n, dim)
        return K.sum(weighted_input, axis=1)

    def compute_output_shape(self, input_shape):
        # (n, steps, dim) -> (n, dim)
        return (input_shape[0], input_shape[-1])


class HSA_BLSTM:
    def __init__(self, con_steps, con_embedding_matrix, com_steps, com_embedding_matrix,
                 emotion_dim=0, sub_event_num=5, post_num=20,
                 hidden_units=32, l2_param=0.01, lr_param=0.001):
        self.con_steps = con_steps
        self.con_embedding_matrix = con_embedding_matrix
        self.com_steps = com_steps
        self.com_embedding_matrix = com_embedding_matrix

        self.emotion_dim = emotion_dim
        self.sub_event_num = sub_event_num
        self.post_num = post_num

        self.hidden_units = hidden_units
        self.l2_param = l2_param

        self.model = self.build()
        self.model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=lr_param, beta_1=0.8),
                           metrics=['accuracy'])

    def build(self):
        # [n, steps]
        con_input = Input(shape=(self.con_steps,), name='Content')
        # [n, steps, dim]
        con_emb = Embedding(self.con_embedding_matrix.shape[0],
                            self.con_embedding_matrix.shape[1],
                            embeddings_initializer=Constant(
                                self.con_embedding_matrix),
                            input_length=self.con_steps,
                            trainable=False)(con_input)

        # [n, steps, hidden_units*2]
        lstm = Bidirectional(
            LSTM(self.hidden_units, return_sequences=True))(con_emb)
        att_lstm = SelfAttLayer(name='Content_Vec')(lstm)

        # ------------------------------------------------------------------------------ #

        # [n, sub_event, post, steps]
        com_input = Input(
            shape=(self.sub_event_num, self.post_num, self.com_steps), name='Comments')
        # [n, sub_event, post, steps, dim]
        com_emb = TimeDistributed(
            TimeDistributed(Embedding(self.com_embedding_matrix.shape[0],
                                      self.com_embedding_matrix.shape[1],
                                      embeddings_initializer=Constant(
                                          self.com_embedding_matrix),
                                      input_length=self.com_steps,
                                      trainable=False)))(com_input)

        # [n, sub_event, post, hidden_units*2]
        lstm_1 = TimeDistributed(
            TimeDistributed(Bidirectional(
                LSTM(self.hidden_units, return_sequences=True))))(com_emb)
        att_lstm_1 = TimeDistributed(TimeDistributed(SelfAttLayer()))(lstm_1)

        # [n, sub_event, hidden_units*2]
        lstm_2 = TimeDistributed(
            Bidirectional(LSTM(self.hidden_units, return_sequences=True)))(att_lstm_1)
        att_lstm_2 = TimeDistributed(SelfAttLayer())(lstm_2)

        # [n, hidden_units*2]
        lstm_3 = Bidirectional(
            LSTM(self.hidden_units, return_sequences=True))(att_lstm_2)
        att_lstm_3 = SelfAttLayer(name='Comments_Vec')(lstm_3)

        # ------------------------------------------------------------------------------ #

        semantics = Concatenate()([att_lstm, att_lstm_3])

        if self.emotion_dim != 0:
            emotion_input = Input(
                shape=(self.emotion_dim,), name='Emotion-Enhanced')
            emotion_enhanced = Concatenate()([semantics, emotion_input])

            dense = Dense(32, activation='relu', kernel_regularizer=l2(
                self.l2_param))(emotion_enhanced)
            output = Dense(2, activation='softmax',
                           kernel_regularizer=l2(self.l2_param))(dense)
            model = Model(inputs=[con_input, com_input,
                                  emotion_input], outputs=output)
        else:
            dense = Dense(32, activation='relu',
                          kernel_regularizer=l2(self.l2_param))(semantics)
            output = Dense(2, activation='softmax',
                           kernel_regularizer=l2(self.l2_param))(dense)
            model = Model(inputs=[con_input, com_input], outputs=output)

        return model
