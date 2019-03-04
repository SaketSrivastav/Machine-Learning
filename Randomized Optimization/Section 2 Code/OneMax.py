import mlrose
import numpy as np
import time

# Initialize fitness function object using state
fitness = mlrose.OneMax()

# Define optimization problem object
problem_fit = mlrose.DiscreteOpt(length = 100, fitness_fn = fitness, maximize=True, max_val = 2)

# Set random seed
np.random.seed(2)


## Solve problem using the genetic algorithm
start_time = time.time()
best_state1, best_fitness1 = mlrose.random_hill_climb(problem_fit, max_attempts=100, max_iters= 100)

start_time2 = time.time()
best_state2, best_fitness2 = mlrose.simulated_annealing(problem_fit, schedule= mlrose.GeomDecay(), max_attempts=100, max_iters= 100)

start_time3 = time.time()
best_state3, best_fitness3 = mlrose.genetic_alg(problem_fit, pop_size= 200, mutation_prob=0.1, max_attempts=100, max_iters= 100)

start_time4 = time.time()
best_state4, best_fitness4 = mlrose.mimic(problem_fit, pop_size= 200, keep_pct=0.2, max_attempts=10, max_iters= 100)


print("Random Hill Climb OneMax Fitness Score:", best_fitness1)
print("--- %s RH training seconds ---" % (time.time() - start_time))
print("Simulated Annealing OneMax Fitness Score:", best_fitness2)
print("--- %s SA training seconds ---" % (time.time() - start_time2))
print("Genetic Algorithm OneMax Fitness Score:", best_fitness3)
print("--- %s GA training seconds ---" % (time.time() - start_time3))
print("MIMIC Algorithm OneMax Fitness Score:", best_fitness4)
print("--- %s MIMIC training seconds ---" % (time.time() - start_time4))