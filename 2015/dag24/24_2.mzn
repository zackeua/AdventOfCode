include "alldifferent_except.mzn";
include "decreasing.mzn";


int: number_of_packets;
array[1..number_of_packets] of par int: packet;


array[1..(number_of_packets-2)] of var 1..number_of_packets: bag_first;
array[1..(number_of_packets-2)] of var 1..number_of_packets: bag_second;
array[1..(number_of_packets-2)] of var 1..number_of_packets: bag_third;
array[1..(number_of_packets-2)] of var 1..number_of_packets: bag_fourth;

var 0..max(packet)*(number_of_packets-2): bag_sum_first;
var 0..max(packet)*(number_of_packets-2): bag_sum_second;
var 0..max(packet)*(number_of_packets-2): bag_sum_third;
var 0..max(packet)*(number_of_packets-2): bag_sum_fourth;


var int: bag_quantum_first;
var int: bag_quantum_second;
var int: bag_quantum_third;
var int: bag_quantum_fourth;

var 1..(number_of_packets-2): bag_count_first;
var 1..(number_of_packets-2): bag_count_second;
var 1..(number_of_packets-2): bag_count_third;
var 1..(number_of_packets-2): bag_count_fourth;

constraint alldifferent_except(bag_first ++ bag_second ++ bag_third ++ bag_fourth, {1});

constraint bag_sum_first = sum([packet[i] | i in bag_first]);
constraint bag_sum_second = sum([packet[i] | i in bag_second]);
constraint bag_sum_third = sum([packet[i] | i in bag_third]);
constraint bag_sum_fourth = sum([packet[i] | i in bag_fourth]);

constraint bag_quantum_first = product([packet[i] | i in bag_first where packet[i] != 0]);
constraint bag_quantum_second = product([packet[i] | i in bag_second where packet[i] != 0]);
constraint bag_quantum_third = product([packet[i] | i in bag_third where packet[i] != 0]);
constraint bag_quantum_fourth = product([packet[i] | i in bag_fourth where packet[i] != 0]);

constraint bag_sum_first = bag_sum_second;
constraint bag_sum_second = bag_sum_third;
constraint bag_sum_third = bag_sum_first;
constraint bag_sum_fourth = bag_sum_third;
constraint bag_sum_fourth = bag_sum_second;
constraint bag_sum_fourth = bag_sum_first;

constraint bag_sum_first = sum(packet)/4;
constraint bag_sum_second = sum(packet)/4;
constraint bag_sum_third = sum(packet)/4;
constraint bag_sum_fourth = sum(packet)/4;

constraint bag_count_first = sum([item != 1 | item in bag_first]);
constraint bag_count_second = sum([item != 1 | item in bag_second]);
constraint bag_count_third = sum([item != 1 | item in bag_third]);
constraint bag_count_fourth = sum([item != 1 | item in bag_fourth]);


constraint bag_count_first >= bag_count_second;
constraint bag_count_second >= bag_count_third;
constraint bag_count_third > bag_count_fourth;

% found by running this and optimizing for number of items.
constraint bag_count_fourth = 5;

constraint decreasing(bag_first);
constraint decreasing(bag_second);
constraint decreasing(bag_third);
constraint decreasing(bag_fourth);


constraint bag_sum_first + bag_sum_second + bag_sum_third + bag_sum_fourth = sum(packet);

var int: obj;

%constraint obj = bag_count_fourth;
constraint obj = bag_quantum_fourth;

solve minimize (obj);

output["obj:", show(obj), "\n"];
output["packets: ",show(packet), "\n"];
output["bag_first: ",show(bag_first), ", QE: ", show(bag_quantum_first), ", W: ", show(bag_sum_first), "\n"];
output["bag_second: ",show(bag_second), ", QE: ", show(bag_quantum_second), ", W: ", show(bag_sum_second), "\n"];
output["bag_third: ",show(bag_third), ", QE: ", show(bag_quantum_third), ", W: ", show(bag_sum_third), "\n"];
output["bag_fourth: ",show(bag_fourth), ", QE: ", show(bag_quantum_fourth), ", W: ", show(bag_sum_fourth), "\n"]
