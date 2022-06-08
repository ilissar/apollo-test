def cloud_function(json_input):
    # original - string that have to be broken into array
    original = json_input["stringToProcess"]
    # Processing
    result = list(original)
    # return the result
    res = {
        "charArr": result
    }
    return res
