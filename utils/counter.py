def count_reps(angle, flag, count, up_thresh, down_thresh):
    if angle > up_thresh and flag != "down":
        count += 1
        flag = "down"
    elif angle < down_thresh and flag == "down":
        flag = "up"
    return flag, count