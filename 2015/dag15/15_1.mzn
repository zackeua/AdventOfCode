enum Ingredients;

% The capacity of each ingredient:
array[Ingredients] of par int: Capacity;
% The durability of each ingredient:
array[Ingredients] of par int: Durability;
% The flavour of each ingredient:
array[Ingredients] of par int: Flavour;
% The texture of each ingredient:
array[Ingredients] of par int: Texture;
% The caloeries of each ingredient:
array[Ingredients] of par int: Calories;

int: upperBound = 100 * max(Capacity) * 100 * max(Durability) * 100 * max(Flavour) * 100 * max(Texture);


% Var array of the quantity of each ingreadient
array[Ingredients] of var 0..100: Quantity;


%100 units of ingredients must be used:
constraint sum(Quantity)=100;


array[Ingredients] of var min(Capacity)*100..max(Capacity)*100: weightedCapacity;

array[Ingredients] of var min(Durability)*100..max(Durability)*100: weightedDurability;

array[Ingredients] of var min(Flavour)*100..max(Flavour)*100: weightedFlavour;

array[Ingredients] of var min(Texture)*100..max(Texture)*100: weightedTexture;


% the texture score
var int: capacityScore;
% the durability score
var int: durabilityScore;
% the flavour score
var int: flavourScore;
% the texture score
var int: textureScore;


constraint weightedCapacity = [Quantity[i] * Capacity[i] | i in Ingredients];
constraint weightedDurability = [Quantity[i] * Durability[i] | i in Ingredients];
constraint weightedFlavour = [Quantity[i] * Flavour[i] | i in Ingredients];
constraint weightedTexture = [Quantity[i] * Texture[i] | i in Ingredients];




constraint capacityScore = if sum(weightedCapacity) < 0 then 0 else sum(weightedCapacity) endif;

constraint durabilityScore = if sum(weightedDurability) < 0 then 0 else sum(weightedDurability) endif;

constraint flavourScore = if sum(weightedFlavour) < 0 then 0 else sum(weightedFlavour) endif;

constraint textureScore = if sum(weightedTexture) < 0 then 0 else sum(weightedTexture) endif;


var 0..2147483646: obj;


constraint obj = capacityScore * durabilityScore * flavourScore * textureScore;


solve maximize obj;

output["obj: ",show(obj), "\n"];
output["Quantity: ",show(Quantity), "\n"];
