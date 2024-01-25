 elif sum(h1) == sum(h2) == max_arr_sum:
        return h1 if h1[0] > h2[0] else h2
    elif sum(h1) == sum(h3) == max_arr_sum:
        return h1 if h1[0] > h3[0] else h3
    elif sum(h2) == sum(h3) == max_arr_sum:
        return h2 if h2[0] > h3[0] else h3
    elif sum(h1) == sum(h2) == sum(h3) == max_arr_sum:
        return h1 if h1[0] > h2[0] and h1[0] > h3[0] else h2 if h2[0] > h1[0] and h2[0] > h3[0] else h3