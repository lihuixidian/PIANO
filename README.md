# DISCO
DISCO: Influence Maximization Meets Graph Embedding and Deep Learning

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

This repository contains the source code for implementing our DISCO framework, which is published in ... Anyone using this source code, please cite our work using the bibtex as follows...
