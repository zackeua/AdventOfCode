include "globals.mzn";

%enum valves = {EG,OR,VO,BV,OF,YZ,EL,EJ,FM,FL,QD,XC,WZ,AT,MZ,WI,YD,QX,AA,VX,VN,RD,QR,CD,VA,RJ,UA,WW,MC,XY,FH,DE,DY,FX,UU,OY,CS,KY,KK,GQ,ZV,QQ,AW,OH,CR,TU,ZP,AR,OZ,GV,PE,ZE,XL,YI,OQ,MG,LS};
enum valves = {AA,BB,CC,DD,EE,FF,GG,HH,II,JJ};


par int: minutes = 30;

% array of flow for each valve
array[valves] of par int: flow_rate;

% the connections to the current valve
array[valves] of par set of valves: valve_connections;


% array of bool denoting if the valve was opened at that time point.
array[valves, 1..minutes] of var bool: valve_is_opened_at_time;

% array of minutes denoting how many minutes that valve was open
array[valves] of var 0..minutes: time_open;

% array of valves denoting at which valve the person is at during each time step
array[1..minutes] of var valves: current_valve;


% constrain: A valve is only turned on once
constraint forall (valve in valves)(sum(valve_is_opened_at_time[valve,..]) in {0,1});

% constraint: Only a single valve can opened at one time point
constraint forall (time in 1..minutes) (sum(valve_is_opened_at_time[..,time]) in {0,1});

% constraint: At least one valve has to be turned on
constraint sum(valve_is_opened_at_time) > 0;

% constraint: No valve is open at the start
constraint forall (valve in valves) (valve_is_opened_at_time[valve,minutes] = 0);

% Channelling constraint: time_open is the amount of time for which the valve has been opened.
constraint forall ([if valve_is_opened_at_time[valve, time] then time_open[valve] = time else time_open[valve] != time \/ time_open[valve] = 0 endif | valve in valves, time in 1..minutes]);


% constraint: Don't open valves that has 0 flow
constraint forall ([flow_rate[valve] == 0 -> time_open[valve] = 0 | valve in valves]);

% constraint: Two valves can not be opened at the same time point.
constraint alldifferent_except_0(time_open);

% Channelling constraint: current_valve is the valve where we are at the current time point, known for the points where we open a valve.
constraint forall ([valve_is_opened_at_time[valve, time] -> current_valve[time] = valve | valve in valves, time in 1..minutes]);

% Channeling constraint: The position before a valve is opened is at the same valve.
constraint forall ([valve_is_opened_at_time[valve, t] -> current_valve[t] = current_valve[t+1] | valve in valves, t in 1..minutes-1 ]);

% constraint: The next valve must be the same valve or a valve directly connected to the currentvalve
constraint forall(t in 1..minutes-1) (current_valve[t+1] = current_valve[t] \/ current_valve[t] in valve_connections[current_valve[t+1]]);

% constraint: Setting the initial valve
constraint current_valve[minutes] = AA;

% Objective value
var 0..sum([minutes * flow_rate[valve] | valve in valves]): obj;

% for testing
% constraint obj = 1651;

% constraint to optimize: sum of the total flow out of each valve
constraint obj = sum([flow_rate[valve] * time_open[valve] | valve in valves]);

solve maximize obj;


%output[show2d(valve_is_opened_at_time), "\n"];
output["valves: ", show(valves), "\n"];
output["time_open: ", show(time_open), "\n"];
output["flow_rate: ", show(flow_rate), "\n"];
output["current_valve: ", show(current_valve), "\n"];
output[show(obj), "\n"];
output[show(sum(valve_is_opened_at_time)), "\n"];
