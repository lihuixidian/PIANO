#!/bin/bash

result_root=model_results

# max belief propagation iteration
max_bp_iter=1

# embedding size
embed_dim=64

#seedset number
seed_k=50

# max batch size for training/testing
batch_size=64

net_type=QNet

# set reg_hidden=0 to make a linear regression
reg_hidden=64

# learning rate
learning_rate=0.0001

# nstep
n_step=4

min_n=1000
max_n=100000

num_env=10
#mem_size=500000
prob_q=4
max_iter=1000000

# folder to save the trained model
save_dir=$result_root/embed-$embed_dim-nbp-$max_bp_iter-rh-$reg_hidden-prob_q-$prob_q

if [ ! -e $save_dir ];
then
    mkdir -p $save_dir
fi

python2 IM-test.py \
    -prob_q $prob_q \
    -n_step $n_step \
    -data_root /home/xmt/DISCO-KDD/code/data \
    -max_n $max_n \
    -num_env $num_env \
    -seed_k $seed_k \
    -max_iter $max_iter \
    -learning_rate $learning_rate \
    -max_bp_iter $max_bp_iter \
    -net_type $net_type \
    -max_iter $max_iter \
    -save_dir $save_dir \
    -embed_dim $embed_dim \
    -batch_size $batch_size \
    -reg_hidden $reg_hidden \
    -momentum 0.9 \
    -l2 0.00 \
#    -load_model $save_dir/iter_5.model \
