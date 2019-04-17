#include "config.h"

int cfg::max_bp_iter = 1;
int cfg::embed_dim = 64;
unsigned int cfg::seed_k = 50;
int cfg::batch_size = 32;
int cfg::max_iter = 1;
int cfg::reg_hidden = 32;
int cfg::node_dim = 0;
int cfg::aux_dim = 0;
int cfg::max_n = 0;
int cfg::num_env = 0;
int cfg::n_step = -1;
Dtype cfg::learning_rate = 0.0005;
Dtype cfg::l2_penalty = 0;
Dtype cfg::momentum = 0;
const char* cfg::save_dir = "./saved";
