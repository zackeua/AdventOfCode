function var int: manhattan(par int: x1, var int: x2, par int: y1, var int: y2) = abs(x1 - x2) + abs(y1 - y2);

par int: number_of_sensors;
par int: max_value = 4000000;
array[1..number_of_sensors] of par int: x_position_of_sensor;
array[1..number_of_sensors] of par int: y_position_of_sensor;
array[1..number_of_sensors] of par int: distance_for_sensor;

var 0..max_value: x_position;
var 0..max_value: y_position;

constraint forall([manhattan(x_position_of_sensor[sensor], x_position, y_position_of_sensor[sensor], y_position) > distance_for_sensor[sensor] | sensor in 1..number_of_sensors]);

solve satisfy;

output["x: ", show(x_position), " y: ", show(y_position), "\n"];
output["result: ", show(x_position * 4000000 + y_position), "\n"];
