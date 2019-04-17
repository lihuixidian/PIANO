#ifndef cfg_H
#define cfg_H

#include <iostream>
#include <cstring>
#include <fstream>
#include <set>
#include <map>
#include "util/gnn_macros.h"

typedef float Dtype;

#ifdef GPU_MODE
    typedef gnn::GPU mode;
#else
    typedef gnn::CPU mode;
#endif

struct cfg
{
    static int max_bp_iter;
    static int embed_dim;
    static int batch_size;
    static int max_iter;
    static unsigned int seed_k;
    static int max_n;
    static int n_step;
    static int num_env;
    static int reg_hidden;
    static int node_dim;
    static int aux_dim;
    static Dtype learning_rate;
    static Dtype l2_penalty;
    static Dtype momentum;    
    static const char *save_dir; 

    static void LoadParams(const int argc, const char** argv)
    {
        for (int i = 1; i < argc; i += 2)
        {
		    if (strcmp(argv[i], "-learning_rate") == 0)
		        learning_rate = atof(argv[i + 1]);
            if (strcmp(argv[i], "-max_bp_iter") == 0)
                max_bp_iter = atoi(argv[i + 1]);        
            if (strcmp(argv[i], "-seed_k") == 0)
                seed_k = atoi(argv[i + 1]);
		    if (strcmp(argv[i], "-embed_dim") == 0)
			    embed_dim = atoi(argv[i + 1]); 
		    if (strcmp(argv[i], "-reg_hidden") == 0)
			    reg_hidden = atoi(argv[i + 1]);
            if (strcmp(argv[i], "-max_n") == 0)
			    max_n = atoi(argv[i + 1]);
            if (strcmp(argv[i], "-num_env") == 0)
			    num_env = atoi(argv[i + 1]);                
            if (strcmp(argv[i], "-n_step") == 0)
			    n_step = atoi(argv[i + 1]);                
    		if (strcmp(argv[i], "-batch_size") == 0)
	       		batch_size = atoi(argv[i + 1]);
            if (strcmp(argv[i], "-max_iter") == 0)
	       		max_iter = atoi(argv[i + 1]);                   
    		if (strcmp(argv[i], "-l2") == 0)
    			l2_penalty = atof(argv[i + 1]);            
      		if (strcmp(argv[i], "-momentum") == 0)
    			momentum = atof(argv[i + 1]);
    		if (strcmp(argv[i], "-save_dir") == 0)
    			save_dir = argv[i + 1];
        }

        if (n_step <= 0)
            n_step = max_n;
        std::cerr << "seed_k = " << seed_k << std::endl;    
        std::cerr << "n_step = " << n_step << std::endl;      
        std::cerr << "batch_size = " << batch_size << std::endl;        
        std::cerr << "embed_dim = " << embed_dim << std::endl;        
    	std::cerr << "learning_rate = " << learning_rate << std::endl;
    }
};

#endif
