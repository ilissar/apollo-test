import re


def cloud_function(json_input):
    # original - string that have to be broken into array
    original = json_input["stringToProcess"]
    # pattern_word - word that will be used to count occurrences;
    pattern_word = json_input["pattern"]
    # batch_size - number of words to be processed;
    # maximum number of words in one element of result array
    batch_size = json_input["batchSize"]
    # threshold_size - number of occurrences that have to stay in result;
    # should be more than 0
    threshold_size = json_input["thresholdSize"]

    # Processing
    pattern = "("
    pattern_template = "\w+\s*"
    pattern_result = ""
    for x in range(batch_size):
        pattern_result += pattern_template
    pattern += pattern_result + ")\s"
    result = re.split(pattern, original + " ")
    result = list(filter(None, result))

    if type(threshold_size) == int:
        if threshold_size > 0:
            index = 0
            count_previous = 0
            for elem in result:
                found_in_current = len(re.findall(pattern_word, elem))
                count_current = count_previous + found_in_current
                if count_previous > threshold_size:
                    result[index] = elem + ";d"
                else:

                    if found_in_current + count_previous <= threshold_size:
                        result[index] = str(elem) + ";s"
                    if found_in_current + count_previous > threshold_size:
                        to_save = threshold_size - count_previous
                        to_delete = found_in_current + count_previous - threshold_size
                        if to_save == 0:
                            result[index] = elem + ";d"
                        else:
                            result[index] = str(elem) + ";s=" + str(to_save)

                count_previous = count_current
                index += 1

    for elem in result:
        print(elem)
    # return the result
    res = {
        "stringToProcess": result,
        # "pattern": pattern_word
    }
    return res
