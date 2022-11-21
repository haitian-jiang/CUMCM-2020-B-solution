Weather = [None, 1, 1, 0, 2, 0, 1, 2, 0, 1, 1,
                 2, 1, 0, 1, 1, 1, 2, 2, 1, 1,
                 0, 0, 1, 0, 2, 1, 0, 0, 1, 1]  # 0：晴朗，1：高温，2：沙暴，索引对应天数
supply_amount = [(5, 7), (8, 6), (10, 10)]  # 索引对应天气
max_mine_day = 7


def get_time_table(binary_code: str, max_mine_day: int) -> dict:
    time_table = {}
    counter = 0
    for day in range(1, 31):
        if binary_code[day] == '1':
            counter += 1
        if counter == 6:
            time_table['village_t_1'] = time_table.get('village_t_1', day)
        elif counter == 8:
            time_table['arrive_mine_t'] = time_table.get('arrive_mine_t', day)
        elif counter == 9:
            time_table['start_mine_t'] = time_table.get('start_mine_t', day)
        elif counter == 8 + max_mine_day:
            time_table['end_mine_t'] = time_table.get('end_mine_t', day)
            time_table['walk_again_t'] = time_table.get('end_mine_t', day) + 1
        elif counter == 10 + max_mine_day:
            time_table['village_t_2'] = time_table.get('village_t_2', day)
        elif counter == 13 + max_mine_day:
            time_table['end_game_t'] = time_table.get('end_game_t', day)
    return time_table


def stay_when_storm(binary_code, time_table) -> bool:
    for date in range(1, time_table['arrive_mine_t'] + 1):
        if Weather[date] == 2 and binary_code[date] == '1':
            return True
    for date in range(time_table['walk_again_t'], time_table['end_game_t'] + 1):
        if Weather[date] == 2 and binary_code[date] == '1':
            return True
    return False


def calc_supply_by_stage(binary_code, time_table, type):  # 箱 type=1:food, type=0:water
    box = {}; cost = 0
    for date in range(1, time_table['village_t_1'] + 1):
        if binary_code[date] == '0':
            cost += supply_amount[Weather[date]][type]
        else:
            cost += supply_amount[Weather[date]][type] * 2
    box['start_to_village'] = cost; cost = 0
    for date in range(time_table['village_t_1'] + 1, time_table['arrive_mine_t'] + 1):
        if binary_code[date] == '0':
            cost += supply_amount[Weather[date]][type]
        else:
            cost += supply_amount[Weather[date]][type] * 2
    box['village_to_mine'] = cost; cost = 0
    for date in range(time_table['arrive_mine_t'] + 1, time_table['end_mine_t'] + 1):
        if binary_code[date] == '0':
            cost += supply_amount[Weather[date]][type]
        else:
            cost += supply_amount[Weather[date]][type] * 3
    box['mine'] = cost; cost = 0
    for date in range(time_table['end_mine_t'] + 1, time_table['village_t_2'] + 1):
        if binary_code[date] == '0':
            cost += supply_amount[Weather[date]][type]
        else:
            cost += supply_amount[Weather[date]][type] * 2
    box['mine_to_village'] = cost; cost = 0
    for date in range(time_table['village_t_2'] + 1, time_table['end_game_t'] + 1):
        if binary_code[date] == '0':
            cost += supply_amount[Weather[date]][type]
        else:
            cost += supply_amount[Weather[date]][type] * 2
    box['village_to_end'] = cost
    return box


def main():
    possible = []
    for i in range(2 ** 30):
        binary_code = '*' + bin(i)[2:].rjust(30, '0')  # 高位填充0
        if binary_code.count('1') != max_mine_day + 13:
            continue
        time_table = get_time_table(binary_code, max_mine_day)
        if stay_when_storm(binary_code, time_table):
            continue
        food_box = calc_supply_by_stage(binary_code, time_table, 1)
        water_box = calc_supply_by_stage(binary_code, time_table, 0)
        initial_food = int(600+food_box['start_to_village']-3*(water_box['village_to_mine']+water_box['mine']+water_box['mine_to_village'])/2)
        initial_water = (1200 - initial_food * 2) // 3
        left_weight = 1200 - initial_food * 2 - initial_water * 3
        if initial_water < water_box['start_to_village']:
            continue  # 不跳出循环说明能走到村庄
        left_weight += (food_box['start_to_village'] * 2 + water_box['start_to_village'] * 3)
        water_in_village_1 = left_weight // 3
        left_weight -= water_in_village_1 * 3
        if water_in_village_1 + initial_water < sum(water_box.values()) - water_box['village_to_end']:
            continue  # 不跳出循环说明能再次走到村庄
        if initial_food < sum(food_box.values()) - food_box['village_to_end']:
            continue
        water_in_village_2 = sum(water_box.values()) - initial_water - water_in_village_1
        food_in_village_2 = sum(food_box.values()) - initial_food
        revenue = 10000 + max_mine_day * 1000 - 10 * (initial_food + water_in_village_1 + water_in_village_2) - 5 * initial_water - 20 * food_in_village_2
        possible.append((binary_code, revenue))
        if revenue > 10000:
            print(revenue)
    possible.sort(key=lambda x: x[1], reverse=True)
    for i in range(5):
        print(possible[i])


if __name__ == '__main__':
    main()
