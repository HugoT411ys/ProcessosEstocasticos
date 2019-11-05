#include <iostream>
#include <random>

typedef std::discrete_distribution<int> discrete;

int main(int argc, char const *argv[])
{
    const int nrolls = 10000000; // number of experiments

    std::default_random_engine generator;

    discrete *trans_prob = new discrete[4];

    trans_prob[0] = {1, 0, 0, 2};
    trans_prob[1] = {1, 2, 1, 0};
    trans_prob[2] = {1, 0, 1, 0};
    trans_prob[3] = {0, 1, 0, 2};

    int dist[4] = {0};

    int curr_state = 0;
    double sigma = 0.;
    for (int i=0; i < nrolls; ++i)
    {
        int next_state = trans_prob[curr_state](generator);
        dist[next_state] = dist[next_state] + 1;
        sigma += (curr_state+1)*(curr_state+1);
        curr_state = next_state;
    }

    std::cout << "Simulando Cadeia de Markov em tempo discreto." << std::endl;
    std::cout << "Numero de iteracoes: " << nrolls << std::endl;

    std::cout << "Distribuicao Limite: " << std::endl;
    for (int i = 0; i < 4; ++i)
    {
        double pi_i = double(dist[i]) / double(nrolls);
        std::cout << "PI_" << (i+1) << " = " << pi_i << std::endl;
    }
    std::cout << "Aproximacao para o limite: " << double(sigma) / nrolls << std::endl;

    return 0;
}