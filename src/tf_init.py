# src/tf_init.py
import tensorflow as tf

def initialize_tf():
    if not tf.config.experimental.list_physical_devices('GPU'):
        tf.config.threading.set_inter_op_parallelism_threads(2)
        tf.config.threading.set_intra_op_parallelism_threads(4)

initialize_tf()