#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define N (1000)
#define R (1.0)
#define Namt (100)

int main() {
    srand(time(NULL));
    
    double pi = 0;
    
    for (int amt = 0; amt < Namt; amt++) {
        int n_area = 0;
        
        for (int n = 0; n < N; n++) {
            double x = ((float)rand()/RAND_MAX), y = ((float)rand()/RAND_MAX);
            double d = sqrt(pow(x, 2) + pow(y, 2));
            
            if (d <= R) {
                n_area++;
            }
        }
    
        double prob = (double)n_area / (double)N;
    
        pi += prob * 4;
    }
    
    // pi = pi / (double)Namt;
    pi /= (double)Namt;

    printf("π_exp = %f", pi);

    return 0;
}