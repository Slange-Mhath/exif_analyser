import json
from argparse import ArgumentParser


def main(exif_log_path, output_file):
    occurence_of_keys = {}
    with open(exif_log_path, 'r') as exif_log:
        exif_json = json.load(exif_log)
        exif_log.close()
        for f in exif_json:
            for key in f.keys():
                if key not in occurence_of_keys:
                    occurence_of_keys[key] = 1
                else:
                    occurence_of_keys[key] += 1
    sorted_occurence_of_keys = {k: v for k, v in sorted(occurence_of_keys.items(), key=lambda item: item[1], reverse=True)}
    f = open(output_file, 'w')
    print("Start processing exif log")
    for k, v in sorted_occurence_of_keys.items():
        f.write(f"{k} occurs {v} times \n")
    f.close()
    print(f"{output_file} generated")
    return occurence_of_keys


if __name__ == "__main__":
    parser = ArgumentParser(description="...")
    parser.add_argument("-exif_log_path", metavar="exif_log_path",
                        help="Path to the exif log file which should be "
                             "analysed")
    parser.add_argument("-output_file", metavar="output_file",
                        help="Name of the output_file")
    args = parser.parse_args()
    main(args.exif_log_path, args.output_file)

