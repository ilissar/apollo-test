def cloud_function(json_input):
    processed_string = json_input["processedString"]
    # count = json_input["count"]

    # Processing
    encoded_string = "".join(processed_string)
    # count_result = 0 + count
    # return the result
    res = {
        "encodedString": encoded_string,
        # "count": count_result
    }
    return res
