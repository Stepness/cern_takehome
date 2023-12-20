      if index > 0:
            sign = pow(-1, index)
            n_mountains_combinations = _summation_of_intersections_of_n_size(mountains, index+1)
            current_row = sign * n_mountains_combinations
            total_area += current_row