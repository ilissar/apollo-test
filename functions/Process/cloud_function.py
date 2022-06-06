import re


def find_nth(haystack, needle, n):
    parts = haystack.split(needle, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(haystack) - len(parts[-1]) - len(needle)


def cloud_function(json_input):
    string_to_process = json_input["stringToProcess"]
    pattern = json_input["pattern"]

    # Processing
    count = len(re.findall(pattern, string_to_process))

    if ";s=" in string_to_process:
        to_save = re.findall(r";s=\d+", string_to_process)
        to_save = int(str(to_save)[5:-2])
        occurrence_index = find_nth(string_to_process, pattern, to_save)
        system_index = find_nth(string_to_process, ";s=", 0)
        string_to_process = string_to_process[:occurrence_index] + string_to_process[occurrence_index:].replace(pattern,
                                                                                                                "")[
                                                                   :-(len(string_to_process) - system_index)]
    else:
        if ";s" in string_to_process:
            string_to_process = string_to_process[:-2]
        if ";d" in string_to_process:
            string_to_process = string_to_process.replace(pattern, "").strip()[:-2]

    print(string_to_process)
    # return the result
    res = {
        "processedString": string_to_process,
        "count": count
    }
    return res
