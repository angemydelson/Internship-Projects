# https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.html

# Paper dropout: https://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf

import argparse
import json
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

if __name__ == "__main__":
    # https://docs.python.org/3/howto/argparse.html
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--epochs', type=int, default=2)
    parser.add_argument('--learning-rate', type=float, default=0.001)
    parser.add_argument('--batch-size', type=int, default=32)
    parser.add_argument('--dropout', type=int)
    
    # https://github.com/aws/sagemaker-training-toolkit/blob/master/ENVIRONMENT_VARIABLES.md
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAINING'))
    parser.add_argument('--model-dir', type=str)
    parser.add_argument('--sm-model-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))
    
    args, _ = parser.parse_known_args()
    
    X_treinamento = np.load(os.path.join(args.train, 'train_data.npy'))
    y_treinamento = np.load(os.path.join(args.train, 'train_labels.npy'))
    X_teste = np.load(os.path.join(args.train, 'eval_data.npy'))
    y_teste = np.load(os.path.join(args.train, 'eval_labels.npy'))
    
    #X_treinamento = X_treinamento.astype('float32')
    #X_teste = X_teste.astype('float32')
    #X_treinamento = X_treinamento / 255
    #X_teste = X_teste / 255
    
    rede_neural = Sequential()
    rede_neural.add(Dense(input_shape = (784, ), units = 397, activation = 'relu'))
    if args.dropout == 1:
        rede_neural.add(Dropout(0.2))
    rede_neural.add(Dense(units = 397, activation = 'relu'))
    if args.dropout == 1:
        rede_neural.add(Dropout(0.2))
    rede_neural.add(Dense(units = 10, activation = 'softmax'))
    rede_neural.compile(optimizer = Adam(learning_rate = args.learning_rate),
                        loss = 'sparse_categorical_crossentropy',
                        metrics = ['accuracy'])
    rede_neural.fit(X_treinamento, y_treinamento, batch_size = args.batch_size, 
                    epochs = args.epochs)
    score = rede_neural.evaluate(X_teste, y_teste)
    print('Loss: ', score[0])
    print('Accuracy: ', score[1])
    
    rede_neural.save(os.path.join(args.sm_model_dir, "000000001"))