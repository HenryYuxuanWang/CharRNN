import tensorflow as tf
from data_preprocessing import Tokenizer, batch_generator
from model import CharRNN
import os
import codecs

FLAGS = tf.flags.FLAGS

tf.flags.DEFINE_string('name', 'default', 'name of the model')
tf.flags.DEFINE_integer('batch_size', 100, 'number of seqs in one batch')
tf.flags.DEFINE_integer('num_steps', 100, 'length of one seq')
tf.flags.DEFINE_integer('n_neurons', 128, 'size of hidden state(neurons) of lstm')
tf.flags.DEFINE_integer('n_layers', 2, 'number of lstm layers')
tf.flags.DEFINE_boolean('embedding', False, 'whether to use embedding')
tf.flags.DEFINE_integer('embedding_size', 128, 'size of embedding')
tf.flags.DEFINE_float('learning_rate', 0.001, 'learning_rate')
tf.flags.DEFINE_float('train_keep_prob', 0.5, 'dropout rate during training')
tf.flags.DEFINE_string('input_file', '', 'utf8 encoded text file')
tf.flags.DEFINE_integer('n_iterations', 10000, 'number of iterations to train')
tf.flags.DEFINE_integer('save_every_n', 1000, 'save the model every n steps')
tf.flags.DEFINE_integer('log_every_n', 10, 'log to the screen every n steps')
tf.flags.DEFINE_integer('num_words', 3500, 'number of words in the vocabulary')

FLAGS.input_file = 'data/poetry.txt'

def main(_):
    model_path = os.path.join('model', FLAGS.name)
    if os.path.exists(model_path) is False:
        os.makedirs(model_path)
    with codecs.open(FLAGS.input_file, encoding='utf-8') as f:
        text = f.read()
    tokenizer = Tokenizer(text, FLAGS.num_words)
    tokenizer.save_to_file(os.path.join(model_path, 'tokenizer.pkl'))

    arr = tokenizer.texts_to_sequences(text)
    batch = batch_generator(arr, FLAGS.batch_size, FLAGS.num_steps)
    print(tokenizer.vocab_size)
    model = CharRNN(tokenizer.vocab_size,
                    batch_size=FLAGS.batch_size,
                    num_steps=FLAGS.num_steps,
                    n_neurons=FLAGS.n_neurons,
                    n_layers=FLAGS.n_layers,
                    learning_rate=FLAGS.learning_rate,
                    train_keep_prob=FLAGS.train_keep_prob,
                    embedding=FLAGS.embedding,
                    embedding_size=FLAGS.embedding_size
                    )
    model.train(batch,
                FLAGS.n_iterations,
                model_path,
                FLAGS.save_every_n,
                FLAGS.log_every_n,
                )


if __name__ == '__main__':
    tf.app.run()
'''
python train.py --embedding True --input_file data/poetry.txt --name Chinese_poetry --learning_rate 0.005 --num_steps 26 --batch_size 32 --n_iterations 10000

python train.py  --input_file data/jay.txt --num_steps 20 --batch_size 32 --name jay --n_iterations 5000 --learning_rate 0.01 --n_layers 3 --embedding True


'''