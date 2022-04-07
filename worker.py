import email_client
import dfk_hero
import time
import argparse
import logging
import json

configuration = {}
logging.getLogger().setLevel(logging.INFO)

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
    logging.info("Starting hero progress track...")
    while True:
        try:
            current_hero_progress = dfk_hero.get_hero_recover_list(configuration)
        except Exception as ex:
            logging.error("There was problem fetching data from bc...")
            current_hero_progress = {}

        recovered_heros = []
        for hero_id, progress_status in current_hero_progress.items():
            if hero_id in hero_progress:
                if (not hero_progress[hero_id]) and (progress_status):
                    recovered_heros.append(hero_id)
                    logging.info("Hero: " + str(hero_id) + ", recovred!")
            hero_progress[hero_id] = progress_status

        if len(recovered_heros) > 0:
            mail_message = "Recovered hero ids: " + " ".join(recovered_heros)
            logging.info("Sending email > " + mail_message)
            email_client.send_email(configuration, "DFK hero progress update", mail_message)

        time.sleep(configuration["sleep_time"])
