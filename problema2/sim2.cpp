#include <iostream>
#include <fstream>
#include <random>

typedef std::discrete_distribution<int> discrete;

int main(int argc, char const *argv[])
{
    const int nrolls = 1000000; // number of experiments

    std::default_random_engine generator;

    discrete *trans_prob = new discrete[4];

    trans_prob[0] = {1, 0, 0, 2};
    trans_prob[1] = {1, 2, 1, 0};
    trans_prob[2] = {1, 0, 1, 0};
    trans_prob[3] = {0, 1, 0, 2};

    int dist[4] = {0};

    int curr_state = 0;
    double sigma = 0.;

    std::ofstream chain_file, plot_file;

    chain_file.open("chain.txt");
    plot_file.open("plot.csv");

    plot_file << "n, s" << std::endl;

    for (int i=1; i < nrolls; ++i)
    {
        int next_state = trans_prob[curr_state](generator);
        dist[next_state] = dist[next_state] + 1;
        sigma += (curr_state+1)*(curr_state+1);
        curr_state = next_state;
        plot_file << i << "," << double(sigma)/i << std::endl;
    }

    chain_file << "Simulando Cadeia de Markov em tempo discreto." << std::endl;
    chain_file << "Numero de iteracoes: " << nrolls << std::endl;

    chain_file << "Distribuicao Limite: " << std::endl;
    chain_file << "TT = [";
    for (int i = 0; i < 4; ++i)
    {
        double pi_i = double(dist[i]) / double(nrolls);
        chain_file << " " << pi_i;
    }
    chain_file << " ]" << std::endl;

    chain_file << "Aproximacao para o limite ~ " << double(sigma) / nrolls << std::endl;

    plot_file.close();
    chain_file.close();

    return 0;
}