include "globals.mzn";

enum valves = {EG,OR,VO,BV,OF,YZ,EL,EJ,FM,FL,QD,XC,WZ,AT,MZ,WI,YD,QX,AA,VX,VN,RD,QR,CD,VA,RJ,UA,WW,MC,XY,FH,DE,DY,FX,UU,OY,CS,KY,KK,GQ,ZV,QQ,AW,OH,CR,TU,ZP,AR,OZ,GV,PE,ZE,XL,YI,OQ,MG,LS};
%enum valves = {AA,BB,CC,DD,EE,FF,GG,HH,II,JJ};


par int: minutes = 26;

% array of flow for each valve
array[valves] of par int: flow_rate;

% the connections to the current valve
array[valves] of par set of valves: valve_connections;


% array of bool denoting if the valve was opened by the person at that time point.
array[valves, 1..minutes] of var bool: valve_is_opened_at_time_by_person;

% array of bool denoting if the valve was opened by the elephant at that time point.
array[valves, 1..minutes] of var bool: valve_is_opened_at_time_by_elephant;


% array of minutes denoting how many minutes that valve was open
array[valves] of var 0..minutes: time_open;

% array of valves denoting at which valve the person is at during each time step
array[1..minutes] of var valves: current_valve_person;

% array of valves denoting at which valve the elephant is at during each time step
array[1..minutes] of var valves: current_valve_elephant;


% constrain: A valve is only turned on once
constraint forall (valve in valves)(sum(valve_is_opened_at_time_by_person[valve,..] ++ valve_is_opened_at_time_by_elephant[valve,..]) in {0,1});

% constraint: Up to two valves can be opened at one time point
constraint forall (time in 1..minutes) (sum(valve_is_opened_at_time_by_person[..,time] ++ valve_is_opened_at_time_by_elephant[..,time]) in {0,1,2});

% constraint: At least one valve has to be turned on
constraint sum(valve_is_opened_at_time_by_person) + sum(valve_is_opened_at_time_by_elephant) > 0;

% constraint: No valve is open at the start
constraint forall (valve in valves) (valve_is_opened_at_time_by_person[valve,minutes] = 0);
constraint forall (valve in valves) (valve_is_opened_at_time_by_elephant[valve,minutes] = 0);

% Channelling constraint: time_open is the amount of time for which the valve has been opened.
constraint forall ([if valve_is_opened_at_time_by_person[valve, time] \/ valve_is_opened_at_time_by_elephant[valve, time] then time_open[valve] = time else time_open[valve] != time \/ time_open[valve] = 0 endif | valve in valves, time in 1..minutes]);


% constraint: Don't open valves that has 0 flow
constraint forall ([flow_rate[valve] == 0 -> time_open[valve] = 0 | valve in valves]);

% constraint: Two valves can not be opened at the same time point by the same actor.
constraint alldifferent_except_0([if valve_is_opened_at_time_by_person[valve, time] then time_open[valve] else 0 endif | valve in valves, time in 1..minutes]);
constraint alldifferent_except_0([if valve_is_opened_at_time_by_elephant[valve, time] then time_open[valve] else 0 endif | valve in valves, time in 1..minutes]);

% Channelling constraint: current_valve is the valve where we are at the current time point, known for the points where we open a valve.
constraint forall ([valve_is_opened_at_time_by_person[valve, time] -> current_valve_person[time] = valve | valve in valves, time in 1..minutes]);
constraint forall ([valve_is_opened_at_time_by_elephant[valve, time] -> current_valve_elephant[time] = valve | valve in valves, time in 1..minutes]);


% Channeling constraint: The position before a valve is opened is at the same valve.
constraint forall ([valve_is_opened_at_time_by_person[valve, t] -> current_valve_person[t] = current_valve_person[t+1] | valve in valves, t in 1..minutes-1 ]);
constraint forall ([valve_is_opened_at_time_by_elephant[valve, t] -> current_valve_elephant[t] = current_valve_elephant[t+1] | valve in valves, t in 1..minutes-1 ]);

% constraint: The next valve must be the same valve or a valve directly connected to the currentvalve
constraint forall(t in 1..minutes-1) (current_valve_person[t+1] = current_valve_person[t] \/ current_valve_person[t] in valve_connections[current_valve_person[t+1]]);
constraint forall(t in 1..minutes-1) (current_valve_elephant[t+1] = current_valve_elephant[t] \/ current_valve_elephant[t] in valve_connections[current_valve_elephant[t+1]]);

% constraint: Setting the initial valve
constraint current_valve_person[minutes] = AA;
constraint current_valve_elephant[minutes] = AA;

% Objective value
var 0..sum([minutes * flow_rate[valve] | valve in valves]): obj;

% for testing
% constraint obj = 1651;

% constraint to optimize: sum of the total flow out of each valve
constraint obj = sum([flow_rate[valve] * time_open[valve] | valve in valves]);

solve maximize obj;


%output[show2d(valve_is_opened_at_time_by_person), "\n"];
output["valves: ", show(valves), "\n"];
output["time_open: ", show(time_open), "\n"];
output["flow_rate: ", show(flow_rate), "\n"];
output["current_valve_person: ", show(current_valve_person), "\n"];
output["current_valve_elephant: ", show(current_valve_elephant), "\n"];
output[show(obj), "\n"];
output[show(sum(valve_is_opened_at_time_by_person) + sum(valve_is_opened_at_time_by_person)) , "\n"];
