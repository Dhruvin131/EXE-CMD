import argparse
import json

if __name__ == "__main__":

    with open("polling_cmd_config.json") as config:
        cfg_data = json.load(config)

    default_exe_path = cfg_data['pooling_exe_path']
    parser = argparse.ArgumentParser("This command is for Polling files")
    parser.add_argument("--p", default=default_exe_path, help='To specify path for pooling')
    args = parser.parse_args()
    
     
    print(args.p)