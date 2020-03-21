#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    if length > 1:
        ht = HashTable(16)

        for i in range(length):
            previous_value = hash_table_retrieve(ht, weights[i])
            if previous_value:
                hash_table_insert(ht, weights[i], previous_value + [i])
            else:
                hash_table_insert(ht, weights[i], [i])

        for weight in range(limit):
            lower_weight = weight
            higher_weight = limit - weight
            if lower_weight < higher_weight:
                lower_weight_item_indices = hash_table_retrieve(ht, lower_weight)
                print(lower_weight_item_indices)
                higher_weight_item_indices = hash_table_retrieve(ht, higher_weight)
                print(higher_weight_item_indices)
                if lower_weight_item_indices and higher_weight_item_indices:
                    first_index = lower_weight_item_indices[0]
                    second_index = higher_weight_item_indices[0]
                    if first_index > second_index:
                        return (first_index, second_index)
                    else:
                        return (second_index, first_index)
                else:
                    continue
            elif lower_weight == higher_weight:
                item_indices = hash_table_retrieve(ht, lower_weight)
                if len(item_indices) > 1:
                    first_index = item_indices[0]
                    second_index = item_indices[1]
                    if first_index > second_index:
                        return (first_index, second_index)
                    else:
                        return (second_index, first_index)
                else:
                    return None
            else:
                return None

    else:
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
