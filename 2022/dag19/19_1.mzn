int: steps = 24;

enum robot = {ore, clay, obsidian, geode};

array [robot, 1..steps] of var int: robots;

array [robot,0..steps] of var int: state;

include "alldifferent.mzn";

constraint robots[ore, 1] = 1;
constraint robots[clay, 1] = 0;
constraint robots[obsidian, 1] = 0;
constraint robots[geode, 1] = 0;

constraint state[ore, 0] = 0;
constraint state[clay, 0] = 0;
constraint state[obsidian, 0] = 0;
constraint state[geode, 0] = 0;

% the amount of ores at current timestep is the sum of the previous timestep and the gain from the robots
constraint forall (i in 1..steps) (state[ore, i] = state[ore, i-1] + robots[ore, i]);
constraint forall (i in 1..steps) (state[clay, i] = state[clay, i-1] + robots[clay, i]);
constraint forall (i in 1..steps) (state[obsidian, i] = state[obsidian, i-1] + robots[obsidian, i]);
constraint forall (i in 1..steps) (state[geode, i] = state[geode, i-1] + robots[geode, i]);

% cant have lower than 0 of each ore at each timestep.
constraint forall (i in 0..steps) (state[ore, i] >= 0);
constraint forall (i in 0..steps) (state[clay, i] >= 0);
constraint forall (i in 0..steps) (state[obsidian, i] >= 0);
constraint forall (i in 0..steps) (state[geode, i] >= 0);


var int: objective;

constraint objective = state[geode, steps];

solve maximize objective;