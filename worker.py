import email_client
import dfk_hero
import time
import argparse

configuration = {}

if __name__ == "__main__":
    # Parse and load configuration
    parser = argparse.ArgumentParser(description="DFK-hero-notification scripts")
    parser.add_argument("--config", type=str, required=True)
    args = parser.parse_args()    
    try:
        with open(args.config, "r") as conf_in_file:
            configuration = json.load(conf_in_file)
    except Exception as ex:
        logging.error("There was problem with opening configuration file, exiting...")
        exit(1)

    hero_progress = {}
    while True:
        time.sleep(configuration["sleep_time"])
        current_hero_progress = dfk_hero.get_hero_recover_list(configuration)

        for hero_id, progress_status in current_hero_progress:
            if hero_id in hero_progress:
                if (not hero_progress[hero_id]) and (progress_status):
                    email_client.send_email(configuration, "DFK hero progress update", "hero finished recovering")
                    print("Hero: " + hero_id + ", recovred!")
            hero_progress[hero_id] = progress_status
