#ifndef ENV_H
#define ENV_H

#include "i_env.h"

class Env : public IEnv
{
public:

    Env(double _norm);

    virtual void s0(std::shared_ptr<Graph>  _g) override;

    virtual double step(int a) override;
    virtual double step_test(int a) override;
    virtual int randomAction() override;

    virtual bool isTerminal() override;

    virtual double getReward() override;

    int numCoveredEdges;
    std::set<int> covered_set;
    std::vector<int> avail_list;
    double influenced_set;//new
};

#endif