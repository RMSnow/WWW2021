# -*- coding: utf-8 -*-
""" 
@author: RMSnow 
@file: SemanticsModels.py 
@time: 2020/5/27 23:10
@contact: xueyao_98@foxmail.com

# SemanticsModels
"""
from keras.layers import Input
from keras.layers import Bidirectional
from keras.layers import GRU, TimeDistributed
from keras.layers import GlobalAveragePooling1D
from keras.layers import Dense
from keras.layers import Embedding, Concatenate
from keras.models import Model
from keras.regularizers import l2
from keras.optimizers import Adam
from keras.initializers import Constant
from keras import backend as K
from keras.layers.core import Lambda


class EmotionEnhancedBiGRU:
    def __init__(self, max_sequence_length, embedding_matrix, emotion_dim=0, category_num=2, hidden_units=32, l2_param=0.01, lr_param=0.001):
        self.max_sequence_length = max_sequence_length
        self.embedding_matrix = embedding_matrix
        self.emotion_dim = emotion_dim
        self.hidden_units = hidden_units
        self.category_num = category_num
        self.l2_param = l2_param

        self.model = self.build()
        self.model.compile(loss='categorical_crossentropy', optimizer=Adam(
            lr=lr_param, beta_1=0.8), metrics=['accuracy'])

    def build(self):
        semantic_input = Input(
            shape=(self.max_sequence_length,), name='word-embedding-input')

        semantic_emb = Embedding(self.embedding_matrix.shape[0],
                                 self.embedding_matrix.shape[1],
                                 embeddings_initializer=Constant(
                                     self.embedding_matrix),
                                 input_length=self.max_sequence_length,
                                 trainable=False)(semantic_input)

        gru = Bidirectional(
            GRU(self.hidden_units, return_sequences=True))(semantic_emb)
        avg_pool = GlobalAveragePooling1D()(gru)

        if self.emotion_dim != 0:
            emotion_input = Input(
                shape=(self.emotion_dim,), name='emotion-input')
            emotion_enhanced = Concatenate()([avg_pool, emotion_input])

            dense = Dense(32, activation='relu', kernel_regularizer=l2(
                self.l2_param))(emotion_enhanced)
            output = Dense(self.category_num, activation='softmax',
                           kernel_regularizer=l2(self.l2_param))(dense)
            model = Model(
                inputs=[semantic_input, emotion_input], outputs=output)
        else:
            dense = Dense(32, activation='relu',
                          kernel_regularizer=l2(self.l2_param))(avg_pool)
            output = Dense(self.category_num, activation='softmax',
                           kernel_regularizer=l2(self.l2_param))(dense)
            model = Model(inputs=[semantic_input], outputs=output)

        return model
