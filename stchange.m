%% Define Function to Depict Status_Changing 
function [money,food,water]=stchange(money,food,water,strategy,date)
food_cost=[4,9,10];
water_cost=[3,9,10];
weather=[1,2,1,1,1,1,2,2,2,2];
if strategy==2
    money=money+200;
    food=food-3*food_cost(weather(date));
    water=water-3*water_cost(weather(date));
elseif strategy==1
    money=money;
    food=food-2*food_cost(weather(date));
    water=water-2*water_cost(weather(date));
else money=money;
    food=food-food_cost(weather(date));
    water=water-water_cost(weather(date));
end
end



