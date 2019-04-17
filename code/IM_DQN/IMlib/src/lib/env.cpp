#include "env.h"
#include "graph.h"
#include <cassert>
#include <random>
#include <iostream>
#include <vector>
#include <set>
#include <deque>
#include <time.h>
#include <sys/time.h>
#include "config.h"

using namespace std;
Env::Env(double _norm) : IEnv(_norm)
{

}

void Env::s0(std::shared_ptr<Graph> _g)
{
    graph = _g;
    covered_set.clear();
    influenced_set=0;//
    action_list.clear();
    numCoveredEdges = 0;
    state_seq.clear();
    act_seq.clear();
    reward_seq.clear();
    sum_rewards.clear();
}

double Env::step(int a)
{
    assert(graph);
    assert(covered_set.count(a) == 0); 

    state_seq.push_back(action_list);
    act_seq.push_back(a);

    covered_set.insert(a);
    action_list.push_back(a);

    vector<bool> active;
    vector<bool>().swap(active);
    double r_t=0;

    for(int fz=0;fz<1000;fz++)
    {
        active.clear();
        for(int i=0;i<graph->num_nodes;i++)
            active.push_back(false);
        double r_t_once = 0;
        deque<int> q1;
        q1.clear();
        q1.push_back(a); 
        active[a]=true;
        r_t_once+=1; 
        while (!q1.empty())
        {
            int expand = q1.front();
            q1.pop_front();
            int i = expand;
            for (auto& neigh : graph->adj_list[i])
            { 
                srand(time(NULL));
                double randDouble = rand() % (99 + 1) / (double)(99 + 1);
                if (randDouble > 0.1) 
                {
                    continue;
                }
                if(active[neigh])
                    continue;
                if(!active[neigh])
                {
                    active[neigh]=true;
                }
                q1.push_back(neigh);
                r_t_once+=1;
            }
        }
        r_t = r_t + r_t_once;
    }
    numCoveredEdges=numCoveredEdges+r_t/1000;
    r_t = r_t/1000.0/norm;
    influenced_set=r_t/1000+influenced_set;
    reward_seq.push_back(r_t);
    sum_rewards.push_back(r_t); 
    return r_t;
}
double Env::step_test(int a)
{
    assert(graph);
    assert(covered_set.count(a) == 0); 

    state_seq.push_back(action_list);
    act_seq.push_back(a);

    covered_set.insert(a);
    action_list.push_back(a);

    return 1;
}
int Env::randomAction()
{
    assert(graph);
    avail_list.clear();
    for (int i = 0; i < graph->num_nodes; ++i)
        if (covered_set.count(i) == 0)
        {
            bool useful = false;
            for (auto& neigh : graph->adj_list[i])
                if (covered_set.count(neigh) == 0)
                {
                    useful = true;
                    break;
                }
            if (useful)
            avail_list.push_back(i);
        }
    assert(avail_list.size());
    //int idx = rand() % graph->num_nodes;
    int idx = rand() % avail_list.size();
    return avail_list[idx];
}

bool Env::isTerminal()
{
    assert(graph);
    return covered_set.size() == cfg::seed_k;
}

double Env::getReward()
{
    return -1.0 / norm;
}
