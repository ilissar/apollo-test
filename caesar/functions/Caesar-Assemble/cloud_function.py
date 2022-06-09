def cloud_function(json_input):
    print(str(json_input))
    char_list = json_input["shiftedArr"]

    # Processing
    result = "".join(char_list)

    # return the result
    res = {
        "encodedString": result
    }
    return res
