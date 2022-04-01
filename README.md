# PIANO (or DISCO)
PIANO (or DISCO): Influence Maximization Meets Graph Embedding and Deep Learning

Since its introduction in 2003, the influence maximization (im) problem
has drawn significant research attention in the literature. The
aim of im is to select a set of k users who can influence the most individuals
in the social network. The problem is proved to be NP-hard.
A large number of approximate algorithms have been proposed
to address this problem. The state-of-the-art algorithms estimate
the expected influence of nodes based on sampled diffusion paths.
As the number of required samples have been recently proved to
be lower bounded by a particular threshold, which depends on a
presetting tradeoff between the accuracy and efficiency, the result
quality of these traditional solutions is hard to be further improved
without sacrificing efficiency. We present an orthogonal
and novel paradigm to address the im problem by leveraging
deep learning models to estimate the expected influence. Specifically,
we present a novel framework called disco that incorporates
graph embedding and deep reinforcement learning techniques to
address this problem.

This repository contains the source code for implementing our PIANO framework, which is published in IEEE Transactions on Computational Social Systems. Anyone using this source code, please cite our work using the bibtex as follows...

'''@article{piano_tcss_lh,
    author    = {Hui Li and
                 Mengting Xu and
                 Sourav S Bhowmick and
                 Joty Shafiq Rayhan and 
                 Changsheng Sun and 
                 Jiangtao Cui},
    title     = {PIANO: Influence Maximization Meets Deep Reinforcement Learning},
    journal   = {{IEEE} Trans. Comput. Soc. Syst.},
    volume    = {},
    number    = {},
    pages     = {},
    year      = {2022},
  }
'''
===============================================================================

The following instruction describes how to use the code.

## Build and Installation

Get the source code, and install all the dependencies. 

### 1. build the graphnn library
- Download and install [CUDA]( https://developer.nvidia.com/cuda-toolkit).

- Download and install [Intel MKL](https://software.intel.com/en-us/mkl). Add the tool box's to your system path.

  ```
  {path_to_your_intel_root/name_of_parallel_tool_box}/bin/psxevars.sh
  ```

- Build static library

  ```
  cd graphnn/
  cp make_common.example make_common
  # modify configurations in make_common file
  make
  ```

- Build the IM-DQN library:

  ```
   cd code/IM_DQN/IMlib/
      cp Makefile.example Makefile
      make
  ```

  **Now you are all set with the C++ backend.** 


## Training

### 1. Generate training data

Take the DBLP dataset as example, we generated different training data using different sampling algorithms. The training dataset should be stored in `DISCO-KDD/code/data`. If you want to test other data set, you should put the data in the same path.

### 2. Training with n-step Q-learning

Change the parameters int the `IM-train.sh`, and then run the training script. 

```
cd DISCO-KDD/code/IM_DQN
sh IM-train.sh
```

### 3. Test the performance

To run the test, using the `IM-test.sh`, you can change the parameters in the script, make sure the parameters are **same** as those in `IM-train.sh`.

```
cd DISCO-KDD/code/IM_DQN
./IM-test.sh
```

After that, PIANO will gives the solution, as the node selection sequence. And the influence of the nodes selected can be determined by `evaluate.py`. `evaluate.py` in the `DISCO-KDD/code/data`.

## LICENSE
This PIANO framework is partly based on the [graph_comb_opt](https://github.com/Hanjun-Dai/graph_comb_opt) with MIT license.
