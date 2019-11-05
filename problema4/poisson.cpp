#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

std::random_device rd;
std::mt19937 rnd_gen(rd());

double simulate_uniform(std::vector<double> &arr_time, double total_time, double lambda)
{
    double sum = 0.;
    int expected_arr = int(total_time*lambda);
    std::uniform_real_distribution<> dis(0., total_time);

    arr_time.push_back(0.);
    for (int i = 0; i <= expected_arr; ++i)
    {
        arr_time.push_back(dis(rnd_gen));
    }
    arr_time[arr_time.size()-1] = 5.;

    std::sort(arr_time.begin(), arr_time.end());
    
    for (int i = 1; i < arr_time.size(); ++i)
        sum += (i-1)*(arr_time[i] - arr_time[i-1]);
    
    return sum;
}

double simulate_exponential(std::vector<double> &arr_time, double total_time, double lambda)
{
    double sum = 0.;
    std::exponential_distribution<> x_t(lambda);

    arr_time.push_back(0.);
    while(arr_time.back() < total_time)
        arr_time.push_back(arr_time.back() + x_t(rnd_gen));
    arr_time[arr_time.size()-1] = 5.;

    for (int i = 1; i < arr_time.size(); ++i)
        sum += (i-1)*(arr_time[i] - arr_time[i-1]);
    
    return sum;
}

int main (int argc, char *argv[])
{
    double const exp_dist_lambda = 1.;
    double const total_time = 5.;

    int const num_sim = 10000; 

    std::vector<double> n_t;

    double sigma = 0;

    std::cout << "n,sigma" << std::endl;

    for (int n = 1; n < num_sim; ++n)
    {
        sigma += simulate_exponential(n_t, total_time, exp_dist_lambda);
        // sigma += simulate_uniform(n_t, total_time, exp_dist_lambda);
        std::cout << n << "," << sigma/n << std::endl;
        
        n_t.clear();
    }
}