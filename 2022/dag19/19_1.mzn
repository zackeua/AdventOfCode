int: steps = 24;

enum robot = {ore, clay, obsidian, geode};

array[robot, robot] of int: cost = [|4, 0, 0, 0 |
                                     2, 0, 0, 0 |
                                     3, 14, 0, 0|
                                     2, 0, 7, 0 |];

%array[robot, robot] of int: cost = [|2, 0, 0, 0 |
%                                     3, 0, 0, 0 |
%                                     3, 8, 0, 0|
%                                     2, 0, 12, 0 |];

% the amount of robots at each timestep
array [robot, 0..steps] of var 0..steps: robots;

% the total amount of minerals obtained at each timestep
array [robot, 0..steps] of var 0..floor(steps * (steps - 1) / 2): minerals;

% the amount of minerals available for building robots at each timestep
array [robot, 0..steps] of var 0..floor(steps * (steps - 1) / 2): materials;

include "alldifferent.mzn";

% initial conditions
constraint robots[ore, 0] = 1;
constraint robots[clay, 0] = 0;
constraint robots[obsidian, 0] = 0;
constraint robots[geode, 0] = 0;

constraint robots[clay, 3] = 1;
constraint robots[clay, 5] = 2;
constraint robots[clay, 7] = 3;

constraint robots[obsidian, 11] = 1;

constraint robots[clay, 12] = 4;





constraint minerals[ore, 0] = 0;
constraint minerals[clay, 0] = 0;
constraint minerals[obsidian, 0] = 0;
constraint minerals[geode, 0] = 0;

% the amount of ores at current timestep is the sum of the previous timestep and the gain from the robots
constraint forall (i in 1..steps) (minerals[ore, i] = minerals[ore, i-1] + robots[ore, i-1]);
constraint forall (i in 1..steps) (minerals[clay, i] = minerals[clay, i-1] + robots[clay, i-1]);
constraint forall (i in 1..steps) (minerals[obsidian, i] = minerals[obsidian, i-1] + robots[obsidian, i-1]);
constraint forall (i in 1..steps) (minerals[geode, i] = minerals[geode, i-1] + robots[geode, i-1]);

% cant have lower than 0 of each ore at each timestep.
constraint forall (i in 0..steps) (minerals[ore, i] >= 0);
constraint forall (i in 0..steps) (minerals[clay, i] >= 0);
constraint forall (i in 0..steps) (minerals[obsidian, i] >= 0);
constraint forall (i in 0..steps) (minerals[geode, i] >= 0);

% cant have lower than 0 robots at each timestep.
constraint forall (i in 0..steps) (robots[ore, i] >= 0);
constraint forall (i in 0..steps) (robots[clay, i] >= 0);
constraint forall (i in 0..steps) (robots[obsidian, i] >= 0);
constraint forall (i in 0..steps) (robots[geode, i] >= 0);

% cant remove built robots
constraint forall(i in 1..steps) (robots[ore, i] >= robots[ore, i-1]);
constraint forall(i in 1..steps) (robots[clay, i] >= robots[clay, i-1]);
constraint forall(i in 1..steps) (robots[obsidian, i] >= robots[obsidian, i-1]);
constraint forall(i in 1..steps) (robots[geode, i] >= robots[geode, i-1]);

% constraint: the maximum amount of robots you can build at a time is 1
constraint forall (i in 1..steps) ((robots[ore, i] - robots[ore, i-1] + robots[clay, i] - robots[clay, i-1] + robots[obsidian, i] - robots[obsidian, i-1]+ robots[geode, i] - robots[geode, i-1]) in {0, 1});


% constraint: the total abount of ores is greater or equal to the cost of all robots
constraint forall (i in 0..steps) (minerals[ore, i] >= (robots[ore, i] - 1) * cost[ore, ore] + robots[clay, i] * cost[clay, ore] + robots[obsidian, i] * cost[obsidian, ore] + robots[geode, i] * cost[geode, ore]);
constraint forall (i in 0..steps) (minerals[clay, i] >= robots[ore, i] * cost[ore, clay] + robots[clay, i] * cost[clay, clay] + robots[obsidian, i] * cost[obsidian, clay] + robots[geode, i] * cost[geode, clay]);
constraint forall (i in 0..steps) (minerals[obsidian, i] >= robots[ore, i] * cost[ore, obsidian] + robots[clay, i] * cost[clay, obsidian] + robots[obsidian, i] * cost[obsidian, obsidian] + robots[geode, i] * cost[geode, obsidian]);
constraint forall (i in 0..steps) (minerals[geode, i] >= robots[ore, i] * cost[ore, geode] + robots[clay, i] * cost[clay, geode] + robots[obsidian, i] * cost[obsidian, geode] + robots[geode, i] * cost[geode, geode]);


constraint forall (i in 0..steps) (materials[ore, i] = minerals[ore, i] - ((robots[ore, i] - 1) * cost[ore, ore] + robots[clay, i] * cost[clay, ore] + robots[obsidian, i] * cost[obsidian, ore] + robots[geode, i] * cost[geode, ore]));
constraint forall (i in 0..steps) (materials[clay, i] = minerals[clay, i] - (robots[ore, i] * cost[ore, clay] + robots[clay, i] * cost[clay, clay] + robots[obsidian, i] * cost[obsidian, clay] + robots[geode, i] * cost[geode, clay]));
constraint forall (i in 0..steps) (materials[obsidian, i] = minerals[obsidian, i] - (robots[ore, i] * cost[ore, obsidian] + robots[clay, i] * cost[clay, obsidian] + robots[obsidian, i] * cost[obsidian, obsidian] + robots[geode, i] * cost[geode, obsidian]));
constraint forall (i in 0..steps) (materials[geode, i] = minerals[geode, i] - (robots[ore, i] * cost[ore, geode] + robots[clay, i] * cost[clay, geode] + robots[obsidian, i] * cost[obsidian, geode] + robots[geode, i] * cost[geode, geode]));



var 0..steps: objective;
% we want to maximize the amount of geode ores at the end.
constraint objective = minerals[geode, steps];

solve maximize objective;

output ["robots:\n", show2d(robots), "materials:\n", show2d(materials), "\nminerals:\n", show2d(minerals), "\nresult: ", show(objective)]
