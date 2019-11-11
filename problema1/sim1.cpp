#include <iostream>
#include <random>

typedef std::discrete_distribution<int> discrete;

std::default_random_engine generator;

void simulate(int *d, discrete *p, int curr_state, int n)
{
    int i, next_state;
    for (i = 0; i < n; ++i)
    {
        next_state = p[curr_state](generator);
        d[next_state]++;
        curr_state = next_state;
    }
}

int main(int argc, char const *argv[])
{
    const int nrolls = 10000000;

    discrete *trans_prob = new discrete[5];

    trans_prob[0] = {1, 0, 2, 0, 0};
    trans_prob[1] = {1, 2, 1, 0, 0};
    trans_prob[2] = {1, 0, 1, 0, 0};
    trans_prob[3] = {0, 0, 0, 0, 1};
    trans_prob[4] = {0, 0, 0, 2, 1};

    std::cout << "Simulando Cadeia de Markov em tempo discreto." << std::endl;
    std::cout << "Numero de iteracoes: " << nrolls << std::endl;

    int num_states = 5;

    for (int i = 0; i < num_states; ++i)
    {
        int curr_state = i;
        int distribution[5] = {0};

        simulate(distribution, trans_prob, curr_state, nrolls);

        std::cout << "Estado inicial: " << (curr_state + 1) << " . Distribucao limite : " << std::endl;
        for (int i = 0; i < num_states; ++i)
        {
            double pi_i = double(distribution[i]) / double(nrolls);
            std::cout << "PI_" << (i+1) << " = " << pi_i << std::endl;
        }
        std::cout << std::endl;
    }

    return 0;
}