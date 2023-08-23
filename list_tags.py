import numpy as np


tag_list = []

with open("bm_bibliography.bib", "r") as bib_file:
    for line in bib_file:
        if line.startswith("tags:"):
            line_tags = line.split(" ")[1:]
            for tag in line_tags:
                if tag in tag_list:
                    pass
                else:
                    if tag.endswith("\n"):
                        tag = tag[:-1]
                    tag_list.append(tag)

sorted_tags = np.sort(np.unique(tag_list))
tag_array = np.array(tag_list)

with open("tag_file.txt", "w") as tag_file:
    for sort_tag in sorted_tags:
        n_appearances = len(np.where(tag_array == sort_tag)[0])
        print(sort_tag, n_appearances)
        n_spaces = 4 * sort_tag.count(":")
        str_prefix = " " * n_spaces
        str_suffix = ";\n"
        write_str = str_prefix + sort_tag + ": " + str(n_appearances) + str_suffix
        tag_file.write(write_str)

